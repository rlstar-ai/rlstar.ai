---
id: sdar
name: SDAR
full: Self-Distilled Agentic Reinforcement Learning
category: OPD
year: 2026
affiliation: Zhejiang University / Meituan
paper: https://arxiv.org/abs/2605.15155
venue: arXiv
connects: [sdpo, minillm, grpo]
improves:
  sdpo: "SDAR 将 SDPO 的单轮自蒸馏扩展到多轮 agentic 任务，引入 sigmoid 门控机制过滤低质量 teacher 信号，并与 GRPO 联合优化"
  grpo: "用 GRPO 作为 RL 基础，在其损失上叠加 OPSD 自蒸馏项，sigmoid 门控确保蒸馏只在 teacher 轨迹高质量时才生效"
---

## Core Idea

Extends on-policy self-distillation to multi-turn agentic tasks by combining OPSD (On-Policy Self-Distillation) with GRPO-based RL, using a sigmoid gate to amplify positive teacher signals while softly suppressing negative ones.

## Key Formula

$$\mathcal{L}^{\text{SDAR}} = \mathcal{L}^{\text{GRPO}} + \lambda \cdot \sigma(r) \cdot \mathcal{L}^{\text{OPSD}}$$

The sigmoid gate $\sigma(r)$ weights distillation by reward, ensuring teacher guidance is only trusted when the teacher trajectory is high-quality.

## Key Improvements over SDPO / OPSD

- Adapts self-distillation to multi-turn agent trajectories (not just single-response)
- Sigmoid gating prevents propagating bad teacher signals
- Tested on ALFWorld, WebShop, Search-QA agent benchmarks

## Impact

- First to apply on-policy self-distillation in multi-turn agentic RL settings
- Shows distillation + RL can be combined without reward model collapse
