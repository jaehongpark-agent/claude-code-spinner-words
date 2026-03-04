#!/usr/bin/env python3
"""Build pipeline: extract spinner verbs and generate llms.txt."""

from __future__ import annotations

from pathlib import Path

from extract_spinner_verbs import WORDS_DIR, main as extract

ROOT_DIR = Path(__file__).parent


def generate_llms_txt(version: str, words: list[str]):
    """Generate llms.txt with latest words and Korean translations if available."""
    kr_path = WORDS_DIR / f"{version}_kr.md"
    kr_section = ""
    if kr_path.exists():
        kr_section = (
            "\n## Korean Translations (v{version})\n\n{content}"
            .format(version=version, content=kr_path.read_text().strip())
        )

    content = f"""# Claude Code Spinner Verbs

> Extracted spinner (loading) verbs from the Claude Code CLI binary, with Korean translations.

## Overview

Claude Code displays playful gerund-form verbs (e.g. "Cogitating", "Flibbertigibbeting", "Lollygagging") in its spinner while processing. This project extracts all of them from the binary and tracks changes across versions.

## Repository Structure

- `extract_spinner_verbs.py` — Extractor: finds and parses spinner verbs from the binary
- `build.py` — Build pipeline: extract + generate llms.txt
- `words/<version>.md` — English word list, one word per line
- `words/<version>_kr.md` — Korean translation, one `English: 한국어` pair per line
- `README.md` — English documentation
- `README_KR.md` — Korean documentation

## How Extraction Works

1. Locate the Claude Code binary via `which claude` or `~/.local/share/claude/versions/`
2. Run `strings` on the binary to dump printable text
3. Use seed-based bootstrapping — rare known words (Flibbertigibbeting, Razzmatazzing, etc.) pinpoint the spinner array
4. Parse all gerund-form (`-ing` / `-in'`) words with regex
5. Save as plain line-separated markdown

## Latest Version: {version} ({len(words)} words)

{chr(10).join(words)}
{kr_section}

## Usage

```bash
# Extract only
python3 extract_spinner_verbs.py

# Extract + generate llms.txt
python3 build.py
```

Requirements: Python 3.10+, Claude Code CLI installed, `strings` command (pre-installed on macOS/Linux).

## File Formats

**English** (`words/<version>.md`): one word per line
```
Accomplishing
Actioning
Actualizing
```

**Korean** (`words/<version>_kr.md`): `English: 한국어` per line
```
Accomplishing: 완수하는 중
Actioning: 실행하는 중
Actualizing: 실현하는 중
```

## Source

https://github.com/jaehongpark-agent/claude-code-spinner-verbs
"""
    path = ROOT_DIR / "llms.txt"
    path.write_text(content)
    return path


def main():
    version, words = extract()
    llms_path = generate_llms_txt(version, words)
    print(f"Saved to {llms_path}")


if __name__ == "__main__":
    main()
