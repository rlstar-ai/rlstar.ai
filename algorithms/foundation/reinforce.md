---
id: reinforce
name: REINFORCE
full: REINFORCE / Policy Gradient
category: foundation
year: 1992
affiliation: University of Massachusetts
paper: https://link.springer.com/article/10.1007/BF00992696
venue: Machine Learning
stars: ~
connects: [ppo, grpo]
improves:
  ppo: "PPO 在 REINFORCE 基础上引入 clip 约束和 value network，解决了其高方差和步长难以控制的问题"
  grpo: "GRPO 以 REINFORCE 为基础，用组内相对奖励替代累积回报，去掉 value network 同时降低方差"
---

## Core Idea

Monte Carlo policy gradient: collect full episode trajectories, then update the policy in the direction that increases the log-probability of actions weighted by their cumulative return.

## Key Formula

$$\nabla J(\theta) = \mathbb{E}\left[\sum_t \nabla \log \pi_\theta(a_t|s_t)\, R_t\right]$$

## Limitations

- High variance without a baseline
- Requires complete episodes (not suited for online LLM training as-is)
- Revisited in RLOO and REINFORCE++ with variance reduction tricks

## Impact

- Foundation of all modern policy gradient methods
- REINFORCE++ (2025) shows it can match GRPO with simple modifications
