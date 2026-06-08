---
id: grpo
name: GRPO
full: Group Relative Policy Optimization
category: reasoning
year: 2024
affiliation: DeepSeek AI
paper: https://arxiv.org/abs/2402.03300
code: https://github.com/deepseek-ai/DeepSeek-Math
venue: arXiv
stars: 9100
connects: [ppo, dapo, gspo, deepseek_r1]
improves:
  ppo: "用 group-relative baseline 替代 value network，节省约 50% 显存，天然适配 pass@k 风格的规则奖励，无需 critic 网络"
---

## Core Idea

For each question, sample a group of $G$ responses and use their relative rewards as the advantage estimate — eliminating the need for a separate value network.

## Key Formula

$$\mathcal{L}^{\text{GRPO}} = -\mathbb{E}\left[\sum_i \textcolor{#a78bfa}{\hat{A}_i} \cdot \min\!\left(\rho_i,\, \text{clip}(\rho_i, 1\pm\varepsilon)\right) - \beta\, \mathbb{D}_\text{KL}[\pi_\theta \| \pi_\text{ref}]\right]$$

$$\textcolor{#a78bfa}{\hat{A}_i = \frac{R_i - \text{mean}(R)}{\text{std}(R)}}$$

The $\textcolor{#a78bfa}{\text{group normalization}}$ replaces the critic network entirely.

## Key Improvements over PPO

- **No value network** — saves ~50% GPU memory during training
- **Group-relative baseline** — naturally suited for pass@k style rewards
- **Simple reward signal** — rule-based (correctness) or ORM score

## Limitations (addressed by later work)

- Token-level IS ratio can cause instability → fixed by GSPO
- Difficulty bias and length bias → fixed by Dr. GRPO
- KL penalty hurts exploration → removed by DAPO

## Impact

- Core algorithm of DeepSeek-Math, DeepSeek-R1
- Adopted by Qwen, Kimi, and dozens of open-source projects
