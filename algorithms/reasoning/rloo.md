---
id: rloo
name: RLOO
full: REINFORCE Leave-One-Out
category: reasoning
year: 2024
affiliation: Hugging Face
paper: https://arxiv.org/abs/2402.14740
code: https://github.com/huggingface/trl
venue: arXiv
stars: 1200
connects: [reinforce, grpo]
improves:
  reinforce: "用 leave-one-out 估计量作为 baseline，相比原始 REINFORCE 的零 baseline 大幅降低方差，且估计无偏"
  grpo: "LOO baseline 在理论上无偏（GRPO 将自身包含在 mean 里有小偏差），适合作为轻量对比基线"
---

## Core Idea

Applies the leave-one-out (LOO) estimator as a variance-reduction baseline for REINFORCE. For a group of $k$ sampled responses, each response's baseline is the mean reward of the **other** $k-1$ responses — providing a low-variance, unbiased advantage estimate without a learned critic.

## Key Formula

$$\hat{A}_i = R_i - \textcolor{#a78bfa}{\frac{1}{k-1}\sum_{j \neq i} R_j}$$

The $\textcolor{#a78bfa}{\text{LOO baseline}}$ excludes response $i$ itself, making the estimate unbiased (unlike GRPO which includes all $k$ responses in the mean, introducing a small bias for finite $k$).

## Comparison with GRPO

| Property | GRPO | RLOO |
|---|---|---|
| Baseline | Mean of all $k$ | Mean of other $k-1$ |
| Bias | Slightly biased | Unbiased |
| Normalization | z-score | No std division |
| Critic | None | None |

## Key Advantage

RLOO's estimator is theoretically unbiased — the LOO trick is a classic statistics result. GRPO's z-score normalization introduces a bias because the sample used to compute mean/std includes the response being evaluated.

## Impact

- Integrated into Hugging Face TRL library
- Often used as a lightweight baseline to compare against GRPO
- Demonstrates that classical statistics (LOO) transfers well to LLM RL
