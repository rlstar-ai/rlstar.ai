---
id: deepseek_r1
name: DeepSeek-R1
full: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
category: report
year: 2025
affiliation: DeepSeek AI
paper: https://arxiv.org/abs/2501.12948
code: https://github.com/deepseek-ai/DeepSeek-R1
venue: arXiv
stars: 32000
connects: [grpo, dapo, qwen_rl]
improves:
  grpo: "首次在大规模 base model 上纯用 GRPO 激发涌现 CoT，验证了 GRPO 不需要 SFT 冷启动即可产生自我反思行为"
  dapo: "DeepSeek-R1 的训练经验直接催生了 DAPO 对 GRPO 失效模式的系统性修复"
  qwen_rl: "Qwen3 复现并扩展了 DeepSeek-R1 的 GRPO 训练方案，在更大规模上验证并补充了其训练技巧"
---

## Core Idea

Shows that pure RL on a base model (without SFT cold-start) produces emergent chain-of-thought reasoning. The model spontaneously develops self-verification, reflection, and multi-step planning behaviors — never explicitly trained on such demonstrations.

## Training Pipeline

1. **DeepSeek-R1-Zero** — GRPO directly on base model with rule-based rewards (format + correctness)
2. **DeepSeek-R1** — cold-start SFT on small high-quality CoT data, then GRPO, then rejection-sampling SFT distillation

## Key Result: Emergent Reasoning

DeepSeek-R1-Zero (no SFT) naturally learned to:
- Re-examine its own work ("Wait, let me reconsider...")
- Explore multiple solution paths before committing
- Self-correct mid-reasoning when detecting inconsistencies

This emergence was not engineered — it arose from the RL optimization pressure alone.

## Benchmark Results

| Benchmark | DeepSeek-R1 | OpenAI o1 |
|---|---|---|
| AIME 2024 | 79.8% | 79.2% |
| MATH-500 | 97.3% | 96.4% |
| Codeforces | 96.3rd %ile | 96.6th %ile |

## Impact

- First open-source model matching OpenAI o1 on reasoning benchmarks
- Validated GRPO as the core algorithm for long-CoT RL
- Released model weights + training recipe; triggered global reproduction efforts
- Distilled versions (1.5B–70B) outperform larger non-reasoning models
