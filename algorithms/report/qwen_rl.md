---
id: qwen_rl
name: Qwen-GRPO
full: Qwen3 Technical Report
category: report
year: 2025
affiliation: Alibaba / Qwen Team
paper: https://arxiv.org/abs/2505.09388
code: https://github.com/QwenLM/Qwen3
venue: arXiv
stars: 18000
connects: [grpo, deepseek_r1]
improves:
  grpo: "在 Qwen3 系列上大规模应用 GRPO，补充了 curriculum 难度调度、reward shaping 细节和 thinking budget 等工程最佳实践"
  deepseek_r1: "复现并超越 DeepSeek-R1，开源了完整权重和训练细节，将 RL 推理训练推广到 0.6B-235B 全系列规模"
---

## Core Idea

The Qwen series (QwQ, Qwen3) adopts GRPO-style training for math and code reasoning, with detailed ablations on reward shaping, curriculum design, and multi-stage training. Reports both "thinking" (long-CoT) and "non-thinking" (standard chat) modes in a single model.

## Training Pipeline

1. **Stage 1: SFT** — diverse high-quality instruction data including long-CoT reasoning traces
2. **Stage 2: Reasoning RL** — GRPO with rule-based rewards on math/code/logic tasks
3. **Stage 3: Fusion SFT** — mix reasoning and non-reasoning data to maintain chat capability
4. **Stage 4: General RL** — preference optimization for helpfulness, safety, format

## Key Design Choices

- **Curriculum by difficulty** — start RL with easy problems, gradually increase difficulty
- **Reward shaping** — separate rewards for format compliance, step-level correctness, final answer
- **Thinking budget** — soft constraint on CoT length via reward penalty after threshold
- **Dual-mode inference** — same model switches between thinking and non-thinking via system prompt

## Benchmark Results (Qwen3-235B-A22B)

| Benchmark | Score | Comparison |
|---|---|---|
| AIME 2025 | 85.7% | > o3 mini |
| LiveCodeBench | 70.7% | State-of-art (open) |
| MATH-500 | 97.4% | Matches best |

## Impact

- Largest-scale public reproduction of DeepSeek-R1's RL approach
- Detailed ablation studies clarified best practices for GRPO training
- Model weights fully open; Qwen3 family includes 0.6B → 235B sizes
