#!/usr/bin/env python3
"""
Skill Graph Validator - Validates skill graph structure, links, and metadata

Performs all standard skill validations (frontmatter, naming, description) plus
graph-specific checks (link integrity, orphan detection, index size, interlinking).

Usage:
    python validate_graph.py <skill_directory>
"""

import sys
import os
import re
import yaml
from pathlib import Path


def validate_frontmatter(skill_path):
    """Validate SKILL.md frontmatter (preserved from quick_validate.py)."""
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text()
    if not content.startswith('---'):
        return False, "No YAML frontmatter found"

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as e:
        return False, f"Invalid YAML in frontmatter: {e}"

    ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility'}
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return False, (
            f"Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}. "
            f"Allowed properties are: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )

    if 'name' not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if 'description' not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    name = frontmatter.get('name', '')
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"Name '{name}' should be kebab-case (lowercase letters, digits, and hyphens only)"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
        if len(name) > 64:
            return False, f"Name is too long ({len(name)} characters). Maximum is 64 characters."

    description = frontmatter.get('description', '')
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        if '<' in description or '>' in description:
            return False, "Description cannot contain angle brackets (< or >)"
        if len(description) > 1024:
            return False, f"Description is too long ({len(description)} characters). Maximum is 1024 characters."

    compatibility = frontmatter.get('compatibility', '')
    if compatibility:
        if not isinstance(compatibility, str):
            return False, f"Compatibility must be a string, got {type(compatibility).__name__}"
        if len(compatibility) > 500:
            return False, f"Compatibility is too long ({len(compatibility)} characters). Maximum is 500 characters."

    return True, "Frontmatter valid"


def extract_markdown_links(filepath):
    """Extract all relative markdown links from a file, skipping fenced code blocks."""
    content = filepath.read_text()

    # Remove fenced code blocks before extracting links
    # This prevents false positives from example links in code samples
    content_no_code = re.sub(r'```.*?```', '', content, flags=re.DOTALL)

    # Match [text](relative/path) but not [text](http...) or [text](#anchor)
    links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', content_no_code)
    relative_links = []
    for link in links:
        # Skip external URLs and anchors
        if link.startswith(('http://', 'https://', '#', 'mailto:')):
            continue
        # Strip anchor from link (e.g., file.md#section -> file.md)
        link = link.split('#')[0]
        if link:
            relative_links.append(link)
    return relative_links


def resolve_link(source_file, link, skill_path):
    """Resolve a relative link from a source file to an absolute path."""
    source_dir = source_file.parent
    resolved = (source_dir / link).resolve()
    return resolved


def validate_links(skill_path):
    """Check that all markdown links in all files resolve to existing files."""
    errors = []
    all_md_files = list(skill_path.rglob('*.md'))

    for md_file in all_md_files:
        links = extract_markdown_links(md_file)
        for link in links:
            resolved = resolve_link(md_file, link, skill_path)
            if not resolved.exists():
                rel_source = md_file.relative_to(skill_path)
                errors.append(f"Broken link in {rel_source}: '{link}' -> file not found")

    return errors


def validate_no_orphans(skill_path):
    """Check that every file in references/ and scripts/ is linked from somewhere."""
    errors = []

    # Collect all files in the skill
    all_files = set()
    for f in skill_path.rglob('*'):
        if f.is_file() and f.name != 'LICENSE.txt':
            all_files.add(f.resolve())

    # Collect all linked files
    linked_files = set()
    all_md_files = list(skill_path.rglob('*.md'))
    for md_file in all_md_files:
        links = extract_markdown_links(md_file)
        for link in links:
            resolved = resolve_link(md_file, link, skill_path)
            linked_files.add(resolved)

    # SKILL.md itself is always reachable (it's the root)
    linked_files.add((skill_path / 'SKILL.md').resolve())

    # Check for orphans in references/ and scripts/
    refs_dir = skill_path / 'references'
    scripts_dir = skill_path / 'scripts'

    for f in all_files:
        if f.resolve() not in linked_files:
            # Only flag orphans in references/ and scripts/
            try:
                f.relative_to(refs_dir.resolve())
                rel = f.relative_to(skill_path)
                errors.append(f"Orphan file (not linked from anywhere): {rel}")
            except ValueError:
                pass
            try:
                f.relative_to(scripts_dir.resolve())
                rel = f.relative_to(skill_path)
                errors.append(f"Orphan file (not linked from anywhere): {rel}")
            except ValueError:
                pass

    return errors


def validate_index_size(skill_path):
    """Check that SKILL.md is under 100 lines."""
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return []  # Already caught by frontmatter validation

    lines = skill_md.read_text().splitlines()
    if len(lines) > 100:
        return [f"SKILL.md is {len(lines)} lines (max 100 for graph-structured skills)"]

    return []


def validate_skill(skill_path):
    """
    Full validation of a skill graph. Returns (bool, str) for compatibility
    with package_skill.py.
    """
    skill_path = Path(skill_path)
    all_errors = []

    # 1. Frontmatter validation (preserved from quick_validate.py)
    valid, message = validate_frontmatter(skill_path)
    if not valid:
        return False, message

    # 2. Link integrity
    link_errors = validate_links(skill_path)
    all_errors.extend(link_errors)

    # 3. Orphan detection
    orphan_errors = validate_no_orphans(skill_path)
    all_errors.extend(orphan_errors)

    # 4. Index size
    size_errors = validate_index_size(skill_path)
    all_errors.extend(size_errors)

    if all_errors:
        error_report = "Graph validation errors:\n" + "\n".join(f"  - {e}" for e in all_errors)
        return False, error_report

    return True, "Skill graph is valid!"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_graph.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
