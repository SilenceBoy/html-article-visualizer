<div align="center">

# html-article-visualizer

**Make AI output worth reading to the end.**

Turn articles, long-form text, research material, PR/code write-ups, product specs, reports, or any structured content into a complete, self-contained, single-file HTML5 visualization you can open in a browser.

English · [简体中文](./README.md)

<img src="./images/exp.png" alt="Example: turning an article into a visualized HTML page" width="720" />

</div>

---

## Origin

This skill is inspired by a post from Thariq ([@trq212](https://x.com/trq212/status/2052809885763747935?s=20)) of the Anthropic Claude Code team — *The Unreasonable Effectiveness of HTML*.

The core idea: **in the age of AI agents, Markdown is no longer the best format for human-AI communication. HTML is.**

The reason is simple —

> Once an AI's output exceeds ~100 lines, almost no one reads it carefully.

HTML can organize the same information into charts, tabs, interactive controls, and shareable pages — content people actually read, and can hand back to the agent with feedback, closing the loop.

This skill is an engineering practice of that idea.

## What problems it solves

- **Long output goes unread.** Agents emit 5,000 words; readers skim the first two paragraphs. HTML brings hierarchy, table of contents, collapsibles, and tabs to raise information density.
- **Markdown can't express structure.** Flows, comparisons, relationships, timelines — Markdown only stacks text. HTML + SVG can draw them.
- **No feedback loop.** Markdown is one-way. HTML can carry copy buttons, checklists, parameter sliders — humans edit, then hand the page back to the agent.
- **Sharing is painful.** Notion / Lark create platform lock-in. A single-file HTML opens in any browser, exports to PDF, attaches to email, drops into any knowledge base.

## Use cases

| Type | Output form |
| --- | --- |
| Article / paper digest | Claim → argument → counter-example → action items |
| Product specs / RFCs | Goals, constraints, decision matrices, flow diagrams, open questions |
| PR / code write-ups | Diffs, call graphs, risk annotations, review conclusions |
| Research reports | TL;DR, evidence tables, timelines, charts, conclusions |
| Prompt / tool kits | Copyable code blocks, parameter editors, live previews |

## Quick start

### 1. Claude Code

Clone this repo into the Claude Code skills directory:

```bash
git clone https://github.com/SilenceBoy/html-article-visualizer.git \
  ~/.claude/skills/html-article-visualizer
```

Then in Claude Code:

> Turn this article into an HTML visualization: <paste content or file path>

### 2. Codex / OpenClaw / OpenAI-style agents

The repo ships [`agents/openai.yaml`](./agents/openai.yaml) as agent metadata. At minimum, inject [`SKILL.md`](./SKILL.md) as the system prompt and expose `references/`, `assets/`, and `scripts/` as readable resources.

### 3. Any LLM / manual use

You don't need an agent framework. Concatenate [`SKILL.md`](./SKILL.md) and [`references/article-to-html-prompt.md`](./references/article-to-html-prompt.md) as a system prompt, and put the content to visualize in the user message.

## Repository layout

```
.
├── SKILL.md                          # Entry point: workflow, design rules, output constraints
├── agents/
│   └── openai.yaml                   # OpenAI-style agent registration metadata
├── assets/
│   ├── styles/
│   │   └── warm-neutral-artifact.css # Default visual style (warm neutral)
│   ├── templates/
│   │   └── artifact-template.html    # Single-file HTML shell template
│   └── examples/                     # Example SVGs, ready to inline
├── references/
│   ├── article-to-html-prompt.md     # Customizable prompt template
│   ├── default-style-system.md       # Default style system reference
│   └── token-efficiency.md           # Token-saving assembly strategy
├── scripts/
│   └── build_artifact.py             # Assemble a content fragment into single-file HTML
└── images/
    └── exp.png                       # README banner
```

## Customization

- **Change the style.** Hand the model your brand palette, fonts, or reference screenshots, or replace `assets/styles/warm-neutral-artifact.css`.
- **Change the example SVGs.** Edit `assets/examples/` and update the reference list in `SKILL.md`.
- **Change the prompt.** Fork `references/article-to-html-prompt.md` for your own scenario.
- **Save tokens.** Use `scripts/build_artifact.py` so the model only outputs the body fragment — fixed CSS and shell aren't regenerated each time.

## Design principles

- **Reading efficiency first.** Visuals serve comprehension, not decoration.
- **Structural editing.** Don't wrap the source in a webpage — restructure information, then choose the right visual form.
- **Single-file, shareable.** Default output is a browser-openable `.html` with no external dependencies.
- **Accessibility baseline.** Semantic tags, sufficient contrast, keyboard reachable, core content readable without JS.

## Credits

- [Thariq (@trq212)](https://x.com/trq212/status/2052809885763747935?s=20) — the core thesis comes from his post on the unreasonable effectiveness of HTML.
- The Anthropic Claude Code team — for the skill mechanism itself.

## License

[MIT](./LICENSE) © Robin Liang
