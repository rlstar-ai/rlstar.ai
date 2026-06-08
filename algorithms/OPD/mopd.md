---
id: mopd
name: MOPD
full: Multi-Teacher On-Policy Distillation
category: OPD
year: 2026
affiliation: Xiaomi
paper: https://arxiv.org/abs/2601.02780
venue: arXiv
connects: [minillm, sdpo, grpo, deepseek_r1]
improves:
  minillm: "MOPD scales MiniLLM's on-policy distillation to multiple domain-specialized teachers trained via large-scale RL, providing token-level dense rewards instead of sequence-level KL"
---

## Core Idea

Uses multiple domain-specialized teacher models (each trained via large-scale RL) to provide dense token-level reward signals to a student model, enabling the student to simultaneously master expertise across domains without requiring a single generalist teacher.

## Key Formula

$$\mathcal{L}^{\text{MOPD}} = \sum_{k} \mathbb{E}_{y \sim \pi_\theta}\left[\mathbb{KL}(\pi_{T_k}(\cdot | x) \| \pi_\theta(\cdot | x))\right] \cdot \mathbf{1}[x \in \mathcal{D}_k]$$

Each teacher $\pi_{T_k}$ is a domain expert; the student learns from the most relevant teacher per input.

## Key Improvements over Single-Teacher Distillation

- Multi-teacher setup covers diverse domains (math, code, reasoning, tool use)
- Token-level dense rewards vs. sequence-level KL in MiniLLM
- Teachers are RL-trained, not just SFT-trained — higher quality ceiling
- Applied at scale in MiMo-V2-Flash (309B MoE, 15B active)

## Impact

- Core training recipe of Xiaomi MiMo-V2-Flash
- Demonstrates on-policy distillation scales to production MoE models
