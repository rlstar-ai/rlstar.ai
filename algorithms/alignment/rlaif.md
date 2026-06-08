---
id: rlaif
name: RLAIF
full: RLHF from AI Feedback (Constitutional AI)
category: alignment
year: 2023
affiliation: Google DeepMind / Anthropic
paper: https://arxiv.org/abs/2309.00267
venue: arXiv
stars: 2900
connects: [rlhf, dpo]
improves:
  rlhf: "将人工标注替换为 AI judge，标注成本降低 10-100×，可扩展至海量数据，且 AI 标注一致性优于人工"
  dpo: "RLAIF 提供高质量 AI 标注偏好对，可作为 DPO 的数据来源，实现全自动对齐流水线"
---

## Core Idea

Replaces human preference labelers with an AI judge (a frontier LLM) to generate preference labels at scale. The AI is guided by a **constitution** — a list of principles — to evaluate responses for helpfulness and harmlessness, matching human-feedback quality at a fraction of the cost.

## Pipeline

1. **Generate candidates** — sample two responses $y_1, y_2$ from the policy
2. **AI labeling** — prompt a strong LLM with the constitution: *"Which response is more helpful and less harmful?"*
3. **Reward model** — train $r_\phi$ on AI-labeled preference pairs
4. **RL fine-tuning** — PPO or DPO with the learned reward model

## Constitutional AI Principle Example

> "Choose the response that is most helpful while avoiding content that is dangerous, harmful, or dishonest. If both are similar, prefer the more concise response."

## Key Finding

AI-labeled preferences achieve **comparable or better** alignment quality vs human labels on:
- Helpfulness: human evaluators prefer RLAIF output in 68% of comparisons
- Safety: RLAIF reduces harmful outputs comparably to human RLHF

## Advantages over Human RLHF

- **10–100× cheaper** — API calls vs human annotator hours
- **Scalable** — no bottleneck from human labeler availability
- **Consistent** — AI applies principles uniformly; humans show annotator disagreement

## Impact

- Core technique behind Claude's Constitutional AI training
- Demonstrated AI self-improvement loop: stronger model → better labels → better student
- Widely adopted in fine-tuning pipelines where human labels are expensive
