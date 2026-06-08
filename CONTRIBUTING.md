# Contributing a New Algorithm

## Quick start

1. Fork this repo and create a branch: `git checkout -b add-<id>`
2. Create `algorithms/<category>/<id>.md` (see format below)
3. Run locally: `python build.py` — fix any errors it reports
4. Open a Pull Request — CI will validate and build automatically

---

## File format

Each algorithm lives in its own `.md` file. The file **must** start with a YAML frontmatter block.

```markdown
---
id: grpo
name: GRPO
full: Group Relative Policy Optimization
category: reasoning
year: 2024
affiliation: DeepSeek AI
paper: https://arxiv.org/abs/2402.03300
code: https://github.com/deepseek-ai/DeepSeek-Math   # optional
venue: arXiv                                           # optional
stars: 9100                                            # optional, GitHub stars
connects: [ppo, dapo]
improves:                                              # optional
  ppo: "Replaces value network with group-relative baseline"
---

## Core Idea

One paragraph describing the core contribution. The first sentence is used
as the hover description in the visualization, so make it self-contained.

## Key Formula

$$\mathcal{L} = ...$$

## Key Improvements over Previous Work

- Point 1
- Point 2
```

---

## Fields reference

| Field | Required | Description |
|-------|----------|-------------|
| `id` | ✅ | Unique snake_case identifier, matches the filename |
| `name` | ✅ | Short display name (e.g. `GRPO`) |
| `full` | ✅ | Full algorithm name |
| `category` | ✅ | See categories below |
| `year` | ✅ | Publication year (integer) |
| `affiliation` | ✅ | Lab / company name |
| `paper` | ✅ | URL to the paper (arXiv or official) |
| `connects` | ✅ | List of related algorithm ids, e.g. `[ppo, dapo]` |
| `code` | optional | URL to official code repository |
| `venue` | optional | Conference or journal name |
| `stars` | optional | GitHub stars count (integer) |
| `improves` | optional | Map of `id: "one-line explanation"` for algorithms this work directly improves upon |
| `desc` | optional | Short description override — auto-extracted from `## Core Idea` if omitted |
| `formula` | optional | Key formula in LaTeX (single line, no `$$` delimiters) |

---

## Categories

| Category | When to use |
|----------|-------------|
| `foundation` | Classic RL algorithms that underpin LLM training (PPO, REINFORCE, RLHF) |
| `reasoning` | RL methods specifically targeting LLM reasoning (GRPO, DAPO, GSPO…) |
| `report` | Full model tech reports with novel RL recipes (DeepSeek-R1, Kimi k1.5…) |
| `agentic` | RL for agent / tool-use settings |
| `alignment` | Alignment and preference optimization methods (DPO, ORPO, SimPO…) |

---

## Connections (`connects`)

- List the ids of algorithms this one is most closely related to
- Aim for 2–4 connections; too many dilutes the graph
- Both sides don't need to be symmetric — the graph handles directionality
- Use `improves` to annotate *how* this work builds on another

---

## Local testing

```bash
python build.py          # validate all .md files and regenerate algorithms.js
python -m http.server 8080
# open http://localhost:8080/rl-star.html
```

`build.py` will print a clear error if any required field is missing or a category is invalid. Fix all errors before opening a PR.
