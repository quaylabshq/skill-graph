#!/usr/bin/env python3
"""Validate a DESIGN.md file for structural completeness and quality.

Usage:
    python3 scripts/validate_design_md.py <path_to_design_md>

Checks:
    - Required sections present (1-5)
    - Color entries have descriptive names + hex codes + functional roles
    - No raw CSS class names without translation
    - Typography describes font character
    - Atmosphere uses descriptive adjectives
"""

import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    r"##\s+1\.\s+Visual Theme",
    r"##\s+2\.\s+Color Palette",
    r"##\s+3\.\s+Typography",
    r"##\s+4\.\s+Component Styl",
    r"##\s+5\.\s+Layout Principles",
]

# Raw CSS class patterns that should be translated
RAW_CSS_PATTERNS = [
    r"\brounded-(sm|md|lg|xl|2xl|3xl|full|none)\b",
    r"\bshadow-(sm|md|lg|xl|2xl)\b",
    r"\btext-(sm|base|lg|xl|2xl|3xl)\b",
    r"\bfont-(thin|light|normal|medium|semibold|bold|extrabold)\b",
    r"\btracking-(tight|normal|wide|wider|widest)\b",
    r"\bleading-(tight|snug|normal|relaxed|loose)\b",
    r"\bgap-\d+\b",
    r"\bp[xytblr]?-\d+\b",
    r"\bm[xytblr]?-\d+\b",
]

HEX_COLOR_PATTERN = r"#[0-9A-Fa-f]{6}\b"


def validate(filepath: str) -> list[str]:
    """Validate a DESIGN.md file. Returns list of issues found."""
    path = Path(filepath)
    if not path.exists():
        return [f"File not found: {filepath}"]

    content = path.read_text()
    lines = content.split("\n")
    issues = []

    # Check: File has a title
    if not re.search(r"^#\s+Design System:", content, re.MULTILINE):
        issues.append("Missing title: Expected '# Design System: [Project Title]'")

    # Check: Project ID present
    if not re.search(r"\*\*Project ID:\*\*", content):
        issues.append("Missing Project ID field")

    # Check: Required sections
    for i, pattern in enumerate(REQUIRED_SECTIONS, 1):
        if not re.search(pattern, content):
            issues.append(f"Missing required section {i}: {pattern}")

    # Check: Hex colors present (at least 3)
    hex_colors = re.findall(HEX_COLOR_PATTERN, content)
    if len(hex_colors) < 3:
        issues.append(
            f"Only {len(hex_colors)} hex colors found. "
            "Expected at least 3 (foundation, accent, text)."
        )

    # Check: Raw CSS class names
    for pattern in RAW_CSS_PATTERNS:
        for full_match in re.finditer(pattern, content):
            pos = full_match.start()
            before = content[:pos]
            # Skip if inside a code block (fenced ```)
            open_blocks = before.count("```")
            if open_blocks % 2 == 1:
                continue
            # Skip if inside inline code backticks
            line_start = content.rfind("\n", 0, pos) + 1
            line = content[line_start : content.find("\n", pos)]
            col = pos - line_start
            backticks_before = line[:col].count("`")
            if backticks_before % 2 == 1:
                continue
            # Skip if inside quotes (anti-pattern examples like 'not "rounded-md"')
            surrounding = content[max(0, pos - 30) : pos + 30]
            if re.search(r'(not\s+"|"[^"]*$)', content[max(0, pos - 30) : pos]):
                continue
            issues.append(
                f"Raw CSS class found outside code block: "
                f"'{full_match.group()}' — translate to descriptive language"
            )
            break  # One warning per pattern is enough

    # Check: Color entries have functional roles (only in section 2)
    color_section = re.search(
        r"##\s+2\.\s+Color Palette.*?(?=##\s+3\.)", content, re.DOTALL
    )
    if color_section:
        color_text = color_section.group()
        color_lines = [
            l for l in color_text.split("\n")
            if re.search(HEX_COLOR_PATTERN, l) and l.strip().startswith("- **")
        ]
        for line in color_lines:
            if "—" not in line and "–" not in line:
                issues.append(
                    f"Color entry missing functional role: {line.strip()[:60]}..."
                )

    # Check: Typography section mentions font character
    typo_section = re.search(
        r"##\s+3\.\s+Typography.*?(?=##\s+4\.)", content, re.DOTALL
    )
    if typo_section:
        typo_text = typo_section.group()
        if not re.search(r"(family|character|personality|humanist|geometric|serif|sans)", typo_text, re.IGNORECASE):
            issues.append(
                "Typography section should describe the font's visual character, "
                "not just its name"
            )

    # Check: Atmosphere uses descriptive adjectives
    atmo_section = re.search(
        r"##\s+1\.\s+Visual Theme.*?(?=##\s+2\.)", content, re.DOTALL
    )
    if atmo_section:
        atmo_text = atmo_section.group()
        descriptive_words = len(re.findall(
            r"\b(airy|dense|minimalist|sophisticated|warm|cool|elegant|playful|"
            r"serene|bold|refined|modern|classic|utilitarian|luxurious|spacious|"
            r"tranquil|dramatic|editorial|gallery)\b",
            atmo_text, re.IGNORECASE
        ))
        if descriptive_words < 2:
            issues.append(
                "Atmosphere section lacks descriptive adjectives. "
                "Use evocative language to capture the design mood."
            )

    # Summary
    line_count = len(lines)
    word_count = len(content.split())

    return issues, line_count, word_count, len(hex_colors)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_design_md.py <path_to_design_md>")
        sys.exit(1)

    filepath = sys.argv[1]
    result = validate(filepath)

    if isinstance(result, tuple):
        issues, lines, words, colors = result
    else:
        issues = result
        lines = words = colors = 0

    print(f"Validating: {filepath}")
    print(f"Stats: {lines} lines, {words} words, {colors} hex colors")
    print()

    if not issues:
        print("PASS: All checks passed.")
    else:
        print(f"ISSUES FOUND: {len(issues)}")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")

    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
