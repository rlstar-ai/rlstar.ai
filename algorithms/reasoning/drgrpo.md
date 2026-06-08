---
id: drgrpo
name: Dr. GRPO
full: Bias-Eliminated GRPO
category: reasoning
year: 2025
affiliation: University of Waterloo / Alibaba
paper: https://arxiv.org/abs/2503.20783
code: https://github.com/sail-sg/Dr-GRPO
venue: arXiv
stars: 510
connects: [grpo]
improves:
  grpo: "消除两个系统性偏差：用 1/T_i 长度归一化消除长回复梯度虚高，跨问题归一化消除难题梯度主导，使训练更公平稳定"
---

## Core Idea

Identifies two systematic biases in GRPO's advantage estimator: **question difficulty bias** (easy questions have higher mean reward, inflating their gradients) and **response length bias** (longer responses receive larger gradient updates regardless of quality). Eliminates both with a simple normalization fix.

## Key Formula

$$\hat{A}_i = \frac{R_i - \mu_q}{\sigma_q} \cdot \textcolor{#a78bfa}{\frac{1}{T_i}}$$

The $\textcolor{#a78bfa}{1/T_i}$ term normalizes by response length $T_i$, so each token contributes equally regardless of sequence length. $\mu_q, \sigma_q$ are the per-question mean and std computed from the group.

## Two Biases in GRPO

### 1. Question Difficulty Bias
GRPO normalizes across a group of responses to a **single question**. If that question is easy (all rewards ≈ 1), the normalized advantage is near zero, providing minimal learning signal. Hard questions dominate training.

### 2. Response Length Bias
The PPO-style summed gradient over tokens means long responses receive larger total gradient updates. A correct long response is rewarded more than a correct short one — incentivizing verbosity over quality.

## Fix

- Divide advantage by token length $T_i$ for length normalization
- Optionally normalize across questions (not just within group) for difficulty normalization

## Impact

- Adopted in several downstream GRPO implementations
- Highlights that "unbiased" gradient estimates matter for stable convergence
- Code released for easy integration into existing GRPO pipelines
