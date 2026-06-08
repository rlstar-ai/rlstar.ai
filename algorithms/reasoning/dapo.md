---
id: dapo
name: DAPO
full: Decoupled Clip and Dynamic sAmpling Policy Optimization
category: reasoning
year: 2025
affiliation: ByteDance / Tsinghua University
paper: https://arxiv.org/abs/2503.14476
code: https://github.com/BytedTsinghua-SIA/DAPO
venue: arXiv
stars: 2800
connects: [grpo, gspo, ppo, reinforce_plus]
improves:
  grpo: "引入解耦 clip（ε_low ≠ ε_high）、去除 KL 惩罚、动态采样过滤无梯度信号、token 级归一化，解决 GRPO 在长 CoT 场景的四大失效模式，AIME 提升 50 分"
  ppo: "移除对称 clip 和 KL 惩罚，改为单侧解耦 clip，策略在正更新方向可迈更大步，更适合长链推理"
---

## Core Idea

Identifies four key failure modes in GRPO for long-chain-of-thought reasoning and introduces four targeted fixes: decoupled clipping, removal of KL penalty, dynamic sampling, and token-level policy gradient loss.

## Key Formula

$$L^{\text{DAPO}} = -\frac{1}{|\mathcal{G}|} \sum_i \min\!\left(\rho_i A_i,\; \textcolor{#a78bfa}{\text{clip}(\rho_i, 1\!-\!\varepsilon_l, 1\!+\!\varepsilon_h)} A_i\right)$$

The $\textcolor{#a78bfa}{\text{decoupled clipping}}$ uses $\varepsilon_h > \varepsilon_l$ (e.g., 0.2 vs 0.28): a tighter lower bound prevents reward hacking while a looser upper bound allows larger positive updates to encourage exploration.

## Four Key Innovations

1. **Decoupled Clip** — separate $\varepsilon_\text{low}$ and $\varepsilon_\text{high}$ for lower/upper importance ratio bounds
2. **No KL Penalty** — removes $\beta \mathbb{D}_\text{KL}$ term entirely, enabling longer exploration
3. **Dynamic Sampling** — filters out prompts where all $G$ responses are correct or all wrong (no gradient signal), re-samples to maintain batch diversity
4. **Token-level Loss** — normalizes gradient by total token count rather than per-response, balancing long vs. short responses

## Results

- +50 points on AIME 2024 over baseline GRPO
- Achieves 50% on AIME with Qwen2.5-32B backbone
- Released full training codebase for reproducibility

## Impact

- Widely adopted as a stronger drop-in replacement for GRPO
- Dynamic sampling trick adopted by many subsequent works
- Decoupled clip became standard in GSPO, REINFORCE++
