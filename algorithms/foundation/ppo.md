---
id: ppo
name: PPO
full: Proximal Policy Optimization
category: foundation
year: 2017
affiliation: OpenAI
paper: https://arxiv.org/abs/1707.06347
code: https://github.com/openai/baselines
venue: arXiv
stars: 8200
connects: [grpo, dapo, reinforce_plus]
improves:
  grpo: "PPO 的 clip 机制和 importance sampling 框架被 GRPO 直接继承，GRPO 在此基础上去掉了 value network"
  dapo: "DAPO 将 PPO 的对称 clip 拆分为解耦 clip，是对 PPO clip 设计的直接扩展"
  reinforce_plus: "REINFORCE++ 借用了 PPO 的 reward clip、mini-batch 等工程技巧，将其移植到无 value network 的 REINFORCE 框架"
---

## Core Idea

Constrains the policy update by clipping the importance sampling ratio, preventing destructively large gradient steps that destabilize training.

## Key Formula

$$L^{\text{CLIP}}(\theta) = \mathbb{E}\left[\min\!\left(r_t(\theta)\hat{A}_t,\; \textcolor{#f59e0b}{\text{clip}(r_t, 1\!-\!\varepsilon, 1\!+\!\varepsilon)}\hat{A}_t\right)\right]$$

Where $\textcolor{#f59e0b}{r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_\text{old}}(a_t|s_t)}}$ is the probability ratio and $\varepsilon$ (typically 0.2) controls the trust region.

## Improvements over Previous Work

- Removes the complex second-order optimization of TRPO
- Clip trick is simpler and faster than KL-penalty methods
- Supports parallel rollout collection

## Impact

- Became the de facto RL algorithm for LLM RLHF (InstructGPT, ChatGPT)
- Directly inspired GRPO (removes value network) and DAPO (decoupled clipping)
