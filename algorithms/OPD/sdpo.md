---
id: sdpo
name: SDPO
full: Self-Distillation Policy Optimization
category: OPD
year: 2026
affiliation: ETH Zurich / Stanford University
paper: https://arxiv.org/abs/2601.20802
venue: arXiv
connects: [minillm, grpo, reinforce_plus]
---

## Core Idea

Converts rich tokenized feedback (verifier outputs, test results) into dense learning signals by treating the model conditioned on that feedback as an internal teacher, enabling on-policy self-distillation without any external teacher or explicit reward model.

## Key Formula

$$\mathcal{L}^{\text{SDPO}} = \mathbb{E}_{y \sim \pi_\theta}\left[\mathbb{KL}(\pi_\theta(\cdot | x, f) \| \pi_\theta(\cdot | x))\right]$$

The same model conditioned on feedback $f$ serves as the teacher, extracting dense token-level supervision from sparse verifiable rewards.

## Key Improvements over Prior Work

- No external teacher model required — self-contained distillation
- Converts sparse verifiable rewards into dense token-level signals
- Outperforms GRPO and PPO on scientific reasoning, tool use, competitive programming

## Impact

- Demonstrates self-distillation as a viable alternative to RL with reward models
- Applicable to any setting with verifiable feedback (code, math, tool use)
