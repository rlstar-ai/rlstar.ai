---
id: reinforce_plus
name: REINFORCE++
full: REINFORCE with Baseline and PPO-style Tricks
category: reasoning
year: 2025
affiliation: Jülich Supercomputing Centre
paper: https://arxiv.org/abs/2501.03262
venue: arXiv
stars: 680
connects: [ppo, grpo, dapo]
improves:
  ppo: "去掉 value network，加入 token 级 running baseline + reward clip + mini-batch SGD，在保留 PPO 稳定性的同时大幅降低显存"
  grpo: "无需 group sampling（每 prompt 只采 1 条）即可达到 GRPO 相当的性能，显存占用约为 GRPO 的 1/G"
  dapo: "与 DAPO 的 token 级归一化思路相同，但从 REINFORCE 角度出发，提供更简洁的理论解释"
---

## Core Idea

Shows that vanilla REINFORCE, augmented with a small set of engineering tricks borrowed from PPO, can match or exceed GRPO's performance — without the group-sampling overhead. Key tricks: per-token baseline, reward clipping, mini-batch updates, and token-level normalization.

## Key Formula

$$\nabla J = \mathbb{E}\left[\sum_t \nabla \log \pi_\theta(a_t) \cdot \textcolor{#a78bfa}{\text{clip}\!\left(R_t - b_t,\, -c,\, c\right)}\right]$$

The $\textcolor{#a78bfa}{\text{clipped advantage}}$ uses a running token-level baseline $b_t$ and clips to $[-c, c]$ to bound gradient magnitude, replacing the need for a group normalization step.

## Key Tricks Added

1. **Token-level baseline** — moving average reward per position replaces group mean
2. **Reward clipping** — clips $R_t - b_t$ to $[-c, c]$ (analogous to PPO clip)
3. **Mini-batch SGD** — reuses collected trajectories for multiple gradient steps
4. **Entropy regularization** — lightweight entropy bonus to maintain exploration

## Comparison with GRPO

| Property | GRPO | REINFORCE++ |
|---|---|---|
| Baseline | Group mean | Running per-token |
| Group sampling | G responses/prompt | 1 response/prompt |
| Memory overhead | ~G× | ~1× |
| Performance | Strong | Comparable |

## Impact

- Challenges the necessity of group sampling in LLM RL
- Widely used in memory-constrained training setups
- Adopted by several open-source RLVR frameworks
