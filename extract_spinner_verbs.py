#!/usr/bin/env python3
"""Extract spinner verbs from the Claude Code CLI binary.

Uses a seed-based bootstrapping strategy: known rare spinner verbs locate
the array inside the binary, then all verbs are parsed out. Results are
saved as versioned markdown files for history tracking.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

# --- Configuration -----------------------------------------------------------

VERSIONS_DIR = Path.home() / ".local/share/claude/versions"
WORDS_DIR = Path(__file__).parent / "words"

BOOTSTRAP_SEEDS = [
    "Flibbertigibbeting",
    "Combobulating",
    "Recombobulating",
    "Whatchamacalliting",
    "Prestidigitating",
    "Hullaballooing",
    "Discombobulating",
    "Razzmatazzing",
    "Honking",
    "Cogitating",
    "Lollygagging",
    "Boondoggling",
]

GERUND_RE = re.compile(
    r"^[A-Z][a-zA-Z\u00e0-\u00ff'\\-]+(ing|in')$"
)

SEED_MATCH_THRESHOLD = 3


# --- Helpers -----------------------------------------------------------------

def find_binary() -> Path:
    """Locate the newest Claude Code binary."""
    try:
        result = subprocess.run(
            ["which", "claude"], capture_output=True, text=True, check=True
        )
        resolved = Path(result.stdout.strip()).resolve()
        if resolved.is_file():
            return resolved
    except (subprocess.CalledProcessError, OSError):
        pass

    if VERSIONS_DIR.is_dir():
        versions = sorted(VERSIONS_DIR.iterdir(), key=lambda p: p.name, reverse=True)
        for v in versions:
            if v.is_file():
                return v

    sys.exit("Error: Could not find the Claude Code binary.")


def get_version(binary: Path) -> str:
    """Extract version string from binary path."""
    return binary.name


def run_strings(binary: Path) -> list[str]:
    result = subprocess.run(
        ["strings", str(binary)], capture_output=True, text=True, check=True
    )
    return result.stdout.splitlines()


def load_seeds() -> list[str]:
    """Load seeds from the latest existing MD file, plus built-in seeds."""
    seeds = list(BOOTSTRAP_SEEDS)
    if WORDS_DIR.is_dir():
        md_files = sorted(
            [f for f in WORDS_DIR.glob("*.md") if "_kr" not in f.name],
            reverse=True,
        )
        if md_files:
            words = parse_md(md_files[0])
            seeds = words + [s for s in seeds if s not in set(words)]
    return seeds


def parse_md(path: Path) -> list[str]:
    """Parse word list from a previously saved MD file."""
    words = []
    for line in path.read_text().splitlines():
        stripped = line.strip()
        if stripped:
            words.append(stripped)
    return words


def find_spinner_line(lines: list[str], seeds: list[str]) -> str | None:
    best_line = None
    best_count = 0
    for line in lines:
        if len(line) < 500:
            continue
        count = sum(1 for s in seeds if s in line)
        if count > best_count:
            best_count = count
            best_line = line
    if best_count >= SEED_MATCH_THRESHOLD:
        return best_line
    return None


def extract_words(line: str) -> list[str]:
    raw_words = re.findall(r'"([A-Z][^"]*)"', line)
    spinner_verbs = []
    seen = set()
    for word in raw_words:
        decoded = re.sub(
            r"\\x([0-9A-Fa-f]{2})",
            lambda m: chr(int(m.group(1), 16)),
            word,
        )
        if GERUND_RE.match(decoded) and decoded not in seen:
            seen.add(decoded)
            spinner_verbs.append(decoded)
    spinner_verbs.sort()
    return spinner_verbs


def diff_words(old: list[str], new: list[str]) -> tuple[list[str], list[str]]:
    old_set, new_set = set(old), set(new)
    return sorted(new_set - old_set), sorted(old_set - new_set)


def save_md(version: str, words: list[str]):
    """Save results as words/<version>.md."""
    WORDS_DIR.mkdir(exist_ok=True)
    path = WORDS_DIR / f"{version}.md"
    path.write_text("\n".join(words) + "\n")
    return path


# --- Main --------------------------------------------------------------------

def main() -> tuple[str, list[str]]:
    """Extract spinner verbs and return (version, words)."""
    binary = find_binary()
    version = get_version(binary)
    print(f"Binary:  {binary}")
    print(f"Version: {version}")

    # Load previous words for diff
    prev_md = WORDS_DIR / f"{version}.md" if WORDS_DIR.is_dir() else None
    old_words = parse_md(prev_md) if prev_md and prev_md.exists() else []

    seeds = load_seeds()
    print(f"Seeds:   {len(seeds)} words ({len(BOOTSTRAP_SEEDS)} built-in)")

    print("Running strings...")
    lines = run_strings(binary)

    spinner_line = find_spinner_line(lines, seeds)
    if spinner_line is None:
        sys.exit("Error: Could not locate the spinner array in the binary.")

    words = extract_words(spinner_line)
    print(f"\nExtracted {len(words)} spinner verbs:\n")
    for i, w in enumerate(words, 1):
        print(f"  {i:3d}. {w}")

    if old_words:
        added, removed = diff_words(old_words, words)
        if added or removed:
            print(f"\nDiff vs previous ({len(old_words)} words):")
            for w in added:
                print(f"  + {w}")
            for w in removed:
                print(f"  - {w}")
        else:
            print(f"\nNo changes vs previous ({len(old_words)} words).")

    path = save_md(version, words)
    print(f"\nSaved to {path}")

    return version, words


if __name__ == "__main__":
    main()
