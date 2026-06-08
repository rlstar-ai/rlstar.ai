---
id: rlhf
name: RLHF
full: Reinforcement Learning from Human Feedback
category: foundation
year: 2022
affiliation: OpenAI
paper: https://arxiv.org/abs/2203.02155
venue: NeurIPS 2022
stars: 12000
connects: [ppo, dpo, rlaif]
improves:
  ppo: "RLHF 将 PPO 应用于语言模型对齐，引入 KL 惩罚防止奖励 hack，开创了 LLM 后训练范式"
  dpo: "DPO 将 RLHF 的两阶段流程（训练 RM + PPO）简化为单一分类损失，无需显式 reward model"
  rlaif: "RLAIF 保留 RLHF 框架，将人工标注替换为 AI judge，大幅降低标注成本并提升可扩展性"
---

## Core Idea

Train a reward model from human pairwise preferences, then fine-tune an LLM with PPO to maximize that reward while staying close to the original policy via a KL penalty.

## Key Formula

$$r_\phi(x, y) = \log \frac{p_\phi(y_w \succ y_l \mid x)}{p_\phi(y_l \succ y_w \mid x)}, \quad \text{PPO objective: } \mathbb{E}\left[r_\phi(x,y) - \textcolor{#f59e0b}{\beta \log \frac{\pi_\theta(y|x)}{\pi_\text{ref}(y|x)}}\right]$$

The $\textcolor{#f59e0b}{\beta}$ term is the KL penalty preventing reward hacking.

## Pipeline

1. **SFT** — supervised fine-tune on demonstration data
2. **Reward Model** — train $r_\phi$ on human preference pairs
3. **RL Fine-tuning** — optimize policy with PPO + KL constraint

## Impact

- Powers InstructGPT, ChatGPT, Claude 1/2
- DPO (2023) replaces step 2+3 with a single loss
- RLAIF replaces human labelers with an AI judge
