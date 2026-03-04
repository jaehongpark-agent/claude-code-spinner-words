# Claude Code Spinner Verbs

Ever wondered what those quirky loading messages in [Claude Code](https://docs.anthropic.com/en/docs/claude-code) are?

This tool extracts all spinner verbs from the Claude Code CLI binary and saves them as versioned markdown files for history tracking.

> [Korean (한국어)](README_KR.md)

## How It Works

1. Locates the Claude Code binary on your system
2. Runs `strings` to dump printable text from the binary
3. Uses seed-based bootstrapping to find the spinner verb array — known rare verbs (e.g. *Flibbertigibbeting*, *Razzmatazzing*) pinpoint the right location
4. Parses out all gerund-form words and saves them to `words/<version>.md`
5. Shows a diff against the previous extraction, so you can spot additions and removals across versions

## Usage

```bash
# Extract spinner verbs only
python3 extract_spinner_verbs.py

# Extract + generate llms.txt (for AI agents)
python3 build.py
```

Output example:

```
Binary:  /Users/you/.local/share/claude/versions/2.1.63
Version: 2.1.63
Seeds:   192 words (12 built-in)
Running strings...

Extracted 192 spinner verbs:

    1. Accomplishing
    2. Actioning
    3. Actualizing
  ...
  192. Zigzagging

Saved to words/2.1.63.md
Saved to llms.txt
```

## Requirements

- Python 3.10+
- Claude Code CLI installed
- `strings` command available (pre-installed on macOS/Linux)

## Project Structure

```
.
├── extract_spinner_verbs.py   # Extractor (standalone)
├── build.py                   # Build pipeline (extract + llms.txt)
├── llms.txt                   # Auto-generated context for AI agents
└── words/
    ├── 2.1.63.md              # English words by version
    └── 2.1.63_kr.md           # Korean translations by version
```

## Customizing Your Spinner

Want to use your own spinner verbs? See the **[Customization Guide](CUSTOMIZE.md)** to learn how to configure `spinnerVerbs` in `settings.json`.

## Sample Words

Some highlights from the 192 spinner verbs found in v2.1.63:

| | | | |
|---|---|---|---|
| Beboppin' | Flibbertigibbeting | Razzmatazzing | Discombobulating |
| Canoodling | Lollygagging | Shenaniganing | Tomfoolering |
| Clauding | Flambéing | Sautéing | Prestidigitating |
| Moonwalking | Spelunking | Hullaballooing | Whatchamacalliting |

## License

MIT
