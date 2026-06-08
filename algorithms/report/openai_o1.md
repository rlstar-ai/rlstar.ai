---
id: openai_o1
name: OpenAI o1
full: OpenAI o1 System Card
category: report
year: 2024
affiliation: OpenAI
paper: https://openai.com/index/openai-o1-system-card/
venue: System Card
stars: ~
connects: [ppo, deepseek_r1]
improves:
  ppo: "将 PPO 大规模应用于 LLM 长链推理训练，引入 hidden reasoning tokens，首次展示 test-time compute scaling 的巨大潜力"
  deepseek_r1: "DeepSeek-R1 以开源方式复现了 o1 的核心能力，用 GRPO 替代 PPO 在 AIME 等 benchmark 上达到同等水平"
---

## Core Idea

The first publicly demonstrated system to achieve strong reasoning via large-scale RL producing extended chain-of-thought (CoT). The model learns to "think before answering" by generating long internal reasoning traces before producing a final response.

## Key Innovations (inferred from system card)

- **Long chain-of-thought RL** — model is rewarded for final answer correctness; intermediate reasoning steps emerge from RL pressure
- **Reasoning tokens** — hidden `<think>` tokens allow the model to explore solution paths without being constrained to produce user-visible text
- **Test-time compute scaling** — more RL steps at inference (longer thinking) yields better accuracy, reversing the "scale training" paradigm

## Benchmark Results

| Benchmark | GPT-4o | o1 |
|---|---|---|
| AIME 2024 | ~13% | ~74% |
| MATH-500 | ~74% | ~97% |
| Codeforces | ~11th %ile | ~89th %ile |

## Impact

- Demonstrated that RL (not just SFT) can produce qualitatively different reasoning capabilities
- Inspired DeepSeek-R1 to reproduce via open methods (GRPO on base model)
- Sparked the "reasoning model" wave: Kimi k1.5, QwQ, DeepSeek-R1, Gemini Thinking
- Established "test-time compute" as a new scaling axis
