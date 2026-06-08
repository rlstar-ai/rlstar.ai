---
id: gspo
name: GSPO
full: Group Sequence Policy Optimization
category: reasoning
year: 2025
affiliation: Tencent AI Lab
paper: https://arxiv.org/abs/2507.18071
venue: arXiv
stars: 420
connects: [grpo, dapo]
improves:
  grpo: "将 token 级 IS ratio 改为 sequence 级，避免长序列中 IS 乘积爆炸，训练更稳定，梯度方差显著降低"
  dapo: "从 IS 粒度角度与 DAPO 的解耦 clip 互补，两者结合可同时解决 clip 不对称和 IS 爆炸问题"
---

## Core Idea

Replaces token-level importance sampling (IS) in GRPO with sequence-level IS within groups. Token-level IS ratios compound multiplicatively across long sequences, causing extreme values that destabilize training; sequence-level IS is more stable.

## Key Formula

$$\rho^{\text{seq}}_i = \textcolor{#a78bfa}{\prod_{t=1}^{T_i}} \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\text{old}}}(a_t|s_t)}$$

The $\textcolor{#a78bfa}{\text{sequence-level product}}$ is clipped as a single unit, preventing any individual response from having an outsized gradient contribution regardless of token count.

## Key Improvements over GRPO

- **Sequence-level clipping** — IS ratio computed per-response, not per-token
- **Reduced gradient variance** — eliminates compounding instability from long CoT sequences
- **Compatible with group normalization** — retains GRPO's critic-free advantage estimation

## Limitations

- Sequence-level IS can still be large for very long responses
- Does not address difficulty bias (see Dr. GRPO)

## Impact

- Validates that IS granularity is a critical hyperparameter for long-CoT RL
- Complements DAPO's decoupled-clip approach from a different angle
