#!/usr/bin/env python3
"""Generate Korean translations for spinner verbs.

Reuses existing translations from the most recent _kr.md file.
New words are translated via Claude Code CLI (claude -p).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

WORDS_DIR = Path(__file__).parent / "words"


def load_existing_translations() -> dict[str, str]:
    """Load all existing Korean translations as {English: Korean} dict."""
    translations: dict[str, str] = {}
    kr_files = sorted(WORDS_DIR.glob("*_kr.md"), reverse=True)
    for kr_file in kr_files:
        for line in kr_file.read_text().splitlines():
            line = line.strip()
            if ": " in line:
                eng, kor = line.split(": ", 1)
                if eng not in translations:
                    translations[eng] = kor
    return translations


def load_words(version: str) -> list[str]:
    """Load English word list for a version."""
    path = WORDS_DIR / f"{version}.md"
    if not path.exists():
        sys.exit(f"Error: {path} not found")
    return [w.strip() for w in path.read_text().splitlines() if w.strip()]


def translate_with_claude(words: list[str], reference: dict[str, str]) -> dict[str, str]:
    """Translate new words using Claude Code CLI (claude -p)."""
    # Build reference examples from existing translations
    examples = []
    for eng, kor in sorted(reference.items())[:30]:
        examples.append(f"{eng}: {kor}")
    examples_text = "\n".join(examples)

    words_text = "\n".join(words)

    prompt = f"""아래는 Claude Code CLI의 스피너(로딩) 동사들의 한국어 번역 예시입니다:

{examples_text}

위 번역 스타일을 참고하여, 아래 단어들을 한국어로 번역해주세요.
규칙:
- 형식: "English: 한국어번역" (한 줄에 하나씩)
- 모든 번역은 "~하는 중" 형태로 끝나야 합니다
- 재미있고 자연스러운 한국어 표현을 사용하세요
- 추가 설명 없이 번역만 출력하세요

{words_text}"""

    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if result.returncode != 0:
        print(f"  claude -p failed: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    results = {}
    for line in result.stdout.strip().splitlines():
        line = line.strip()
        if ": " in line:
            eng, kor = line.split(": ", 1)
            eng = eng.strip()
            if eng in words:
                results[eng] = kor.strip()
    return results


def generate(version: str) -> Path:
    """Generate Korean translation file for a version."""
    words = load_words(version)
    existing = load_existing_translations()

    # Split into already-translated and new
    translated = {}
    new_words = []
    for w in words:
        if w in existing:
            translated[w] = existing[w]
        else:
            new_words.append(w)

    print(f"Version {version}: {len(words)} words total")
    print(f"  Existing translations: {len(translated)}")
    print(f"  New words to translate: {len(new_words)}")

    if new_words:
        new_translations = translate_with_claude(new_words, existing)
        translated.update(new_translations)

        missing = [w for w in new_words if w not in new_translations]
        if missing:
            print(f"  Warning: {len(missing)} words not translated: {missing}")

    # Write output in same order as English word list
    lines = []
    for w in words:
        if w in translated:
            lines.append(f"{w}: {translated[w]}")
        else:
            lines.append(f"{w}: (미번역)")
    lines.append("")  # trailing newline

    out_path = WORDS_DIR / f"{version}_kr.md"
    out_path.write_text("\n".join(lines))
    print(f"  Saved to {out_path}")
    return out_path


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="Version to translate (e.g. 2.1.74)")
    parser.add_argument(
        "--all-missing",
        action="store_true",
        help="Generate for all versions missing _kr.md",
    )
    args = parser.parse_args()

    if args.all_missing:
        en_files = sorted(WORDS_DIR.glob("*.md"))
        for f in en_files:
            if "_kr" in f.name:
                continue
            ver = f.stem
            kr_path = WORDS_DIR / f"{ver}_kr.md"
            if not kr_path.exists():
                generate(ver)
    else:
        generate(args.version)


if __name__ == "__main__":
    main()
