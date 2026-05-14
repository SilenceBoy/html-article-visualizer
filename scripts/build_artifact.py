#!/usr/bin/env python3
"""Build a self-contained HTML artifact from a content fragment and shared assets."""

from __future__ import annotations

import argparse
import html
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STYLE_PATH = ROOT / "assets" / "styles" / "warm-neutral-artifact.css"
TEMPLATE_PATH = ROOT / "assets" / "templates" / "artifact-template.html"
EXAMPLES_DIR = ROOT / "assets" / "examples"


DEFAULT_SCRIPT = """
document.querySelectorAll('[data-copy]').forEach((button) => {
  button.addEventListener('click', async () => {
    const target = document.querySelector(button.getAttribute('data-copy'));
    if (!target) return;
    await navigator.clipboard.writeText(target.innerText || target.textContent || '');
    const old = button.textContent;
    button.textContent = 'Copied';
    setTimeout(() => { button.textContent = old; }, 1200);
  });
});
document.querySelector('[data-back-top]')?.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
""".strip()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def replace(template: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    return template


def build(args: argparse.Namespace) -> str:
    content = read(Path(args.content_file))
    if args.example:
        example_path = EXAMPLES_DIR / args.example
        if not example_path.exists():
            choices = ", ".join(sorted(p.name for p in EXAMPLES_DIR.glob("*.svg")))
            raise SystemExit(f"Unknown example SVG: {args.example}. Choices: {choices}")
        content = read(example_path) + "\n" + content

    template = read(TEMPLATE_PATH)
    return replace(
        template,
        {
            "LANG": html.escape(args.lang),
            "TITLE": html.escape(args.title),
            "DESCRIPTION": html.escape(args.description or args.subtitle or args.title),
            "KICKER": html.escape(args.kicker),
            "SUBTITLE": html.escape(args.subtitle),
            "STYLE": read(STYLE_PATH),
            "CONTENT": content,
            "SCRIPT": DEFAULT_SCRIPT,
        },
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a self-contained warm-neutral HTML artifact.")
    parser.add_argument("--content-file", required=True, help="HTML fragment file for the main content.")
    parser.add_argument("--output", required=True, help="Output .html path.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--description", default="")
    parser.add_argument("--kicker", default="HTML Artifact")
    parser.add_argument("--lang", default="zh-CN")
    parser.add_argument("--example", default="", help="Optional SVG filename from assets/examples to inline before content.")
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build(args), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
