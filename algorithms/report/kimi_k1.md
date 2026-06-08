---
id: kimi_k1
name: Kimi k1.5
full: Kimi k1.5: Scaling Reinforcement Learning with LLMs
category: report
year: 2025
affiliation: Moonshot AI
paper: https://arxiv.org/abs/2501.12599
venue: arXiv
stars: 4200
connects: [ppo, grpo, deepseek_r1]
improves:
  ppo: "用 online mirror descent 替代 PPO clip，在长 horizon rollout 下更新更稳定，并引入 length penalty 防止奖励 hack"
  grpo: "在 GRPO 基础上引入上下文窗口渐进扩展（4K→128K）和长度惩罚，解决长 CoT 训练的扩展性问题"
  deepseek_r1: "与 DeepSeek-R1 同期，Kimi k1.5 独立验证了长 CoT RL 路线，并补充了上下文扩展和 long-to-short 蒸馏技术"
---

## Core Idea

Scales long-CoT RL training with a context-window expansion strategy and an online mirror descent variant. Introduces a length penalty to prevent reward hacking through verbosity, and proposes a "long-to-short" distillation to compress reasoning chains.

## Key Innovations

- **Context window scaling** — progressively increases training context from 4K → 128K tokens during RL, matching inference-time compute needs
- **Online mirror descent** — more stable policy update rule than PPO clipping under long-horizon rollouts
- **Length penalty** — subtracts a term proportional to response length from reward to discourage padding/verbosity
- **Long-to-short distillation** — uses long-CoT model to generate training data for a shorter, more efficient student model

## Reward Design

$$r = r_\text{correct} - \textcolor{#f59e0b}{\lambda \cdot \frac{|y|}{|y_\text{max}|}}$$

The $\textcolor{#f59e0b}{\text{length penalty}}$ with coefficient $\lambda$ prevents the model from achieving higher reward purely by generating longer responses.

## Benchmark Results

| Benchmark | Kimi k1.5 (long-CoT) | o1 |
|---|---|---|
| AIME 2025 | 77.5% | 79.2% |
| MATH-500 | 96.2% | 96.4% |

## Impact

- Demonstrated context scaling as a key axis for long-CoT RL
- Length penalty approach widely adopted to combat reward hacking
- Long-to-short distillation influenced subsequent efficiency research
