#!/usr/bin/env python3
"""Generate README.md from info.yaml files in Talks/, Lectures/, Posters/.

To add a new talk:
  1. Create a folder: Talks/YYYY-MM_short-name/
  2. Drop in your slides and an info.yaml (copy from any existing folder)
  3. Commit — the pre-commit hook will regenerate README.md automatically.
"""

from pathlib import Path
from urllib.parse import quote
from datetime import datetime
import yaml

REPO = Path(__file__).parent
GITHUB_RAW = "https://github.com/htjb/Talks/raw/master"
GITHUB_TREE = "https://github.com/htjb/Talks/tree/master"


def raw_url(section: str, folder: str, filename: str) -> str:
    return f"{GITHUB_RAW}/{section}/{folder}/{quote(filename)}"


def tree_url(section: str, folder: str, subpath: str = "") -> str:
    path = f"{GITHUB_TREE}/{section}/{folder}"
    if subpath:
        path += f"/{subpath}"
    return path


def format_date(date_str: str) -> str:
    """Convert YYYY-MM or YYYY to a human-readable string."""
    if not date_str:
        return ""
    try:
        if len(str(date_str)) == 7:  # YYYY-MM
            return datetime.strptime(str(date_str), "%Y-%m").strftime("%B %Y")
        return str(date_str)
    except ValueError:
        return str(date_str)


def load_section(section_dir: str) -> list[dict]:
    """Load all info.yaml files from a section, sorted newest-first."""
    section_path = REPO / section_dir
    if not section_path.exists():
        return []
    items = []
    for folder in section_path.iterdir():
        if not folder.is_dir():
            continue
        info_file = folder / "info.yaml"
        if not info_file.exists():
            continue
        with open(info_file) as f:
            data = yaml.safe_load(f)
        data["_folder"] = folder.name
        data["_section"] = section_dir
        items.append(data)
    # Sort by date descending; items without dates go last
    items.sort(key=lambda x: str(x.get("date", "0000")), reverse=True)
    return items


def render_talk(item: dict, talk: dict) -> str:
    folder = item["_folder"]
    section = item["_section"]
    lines = []

    lines.append(f"1. {talk.get('title', '')}")

    event = item.get("event", "")
    event_url = item.get("event_url", "")
    if event:
        lines.append(f"    - [{event}]({event_url})" if event_url else f"    - {event}")

    location = item.get("location", "")
    if location:
        lines.append(f"    - {location}")

    item_notes = item.get("notes", "")
    if item_notes:
        lines.append(f"    - {item_notes}")

    if talk.get("invited"):
        lines.append("    - Invited")

    pdf = talk.get("pdf", "")
    if pdf:
        lines.append(f"    - [PDF]({raw_url(section, folder, pdf)})")

    for link in talk.get("links", []) or []:
        lines.append(f"    - [{link['label']}]({link['url']})")

    date_str = format_date(item.get("date", ""))
    if date_str:
        lines.append(f"    - {date_str}")

    talk_notes = talk.get("notes", "")
    if talk_notes:
        lines.append(f"    - {talk_notes}")

    return "\n".join(lines)


def render_lecture(item: dict, talk: dict) -> str:
    folder = item["_folder"]
    section = item["_section"]
    lines = []

    lines.append(f"1. {talk.get('title', '')}")

    notes = talk.get("notes", "")
    if notes:
        lines.append(f"    - {notes}")

    event = item.get("event", "")
    event_url = item.get("event_url", "")
    if event:
        lines.append(f"    - [{event}]({event_url})" if event_url else f"    - {event}")

    location = item.get("location", "")
    if location:
        lines.append(f"    - {location}")

    pdf = talk.get("pdf", "")
    if pdf:
        lines.append(f"    - [Lecture]({raw_url(section, folder, pdf)})")

    sub_files = talk.get("sub_files", []) or []
    if sub_files:
        lines.append("    - Lectures:")
        for sf in sub_files:
            lines.append(f"        - [{sf['label']}]({raw_url(section, folder, sf['file'])})")

    code_dir = talk.get("code_dir", "")
    if code_dir:
        lines.append(f"    - [Code Examples]({tree_url(section, folder, code_dir)})")

    if talk.get("additional_material"):
        lines.append(f"    - [Additional Material]({tree_url(section, folder)})")

    return "\n".join(lines)


def generate_readme() -> str:
    parts = []

    # Lectures
    lectures = load_section("Lectures")
    if lectures:
        parts.append("# Lectures\n")
        for item in lectures:
            for talk in item.get("talks", []):
                parts.append(render_lecture(item, talk))
                parts.append("")

    # Talks
    talks = load_section("Talks")
    if talks:
        parts.append("# Talks\n")
        for item in talks:
            for talk in item.get("talks", []):
                parts.append(render_talk(item, talk))
                parts.append("")

    # Posters
    posters = load_section("Posters")
    if posters:
        parts.append("# Posters\n")
        for item in posters:
            for talk in item.get("talks", []):
                parts.append(render_talk(item, talk))
                parts.append("")

    return "\n".join(parts).rstrip() + "\n"


if __name__ == "__main__":
    readme = generate_readme()
    readme_path = REPO / "README.md"
    with open(readme_path, "w") as f:
        f.write(readme)
    print(f"README.md written ({readme.count(chr(10))} lines)")
