---
id: ragen
name: RAGEN
full: RAGEN: Training Agents by Reinforcing Reasoning
category: agentic
year: 2025
affiliation: UIUC / Tsinghua
paper: https://arxiv.org/abs/2504.20073
code: https://github.com/RAGEN-AI/RAGEN
venue: arXiv
stars: 890
connects: [agent_rl, dapo]
improves:
  agent_rl: "在多步 agentic RL 框架上引入 think-tool 交替轨迹格式，并用 reasoning mask 只对思考 token 施加梯度，WebArena 提升 18 点"
  dapo: "将 DAPO 的 token 级归一化和动态采样扩展到多轮 agent 场景，解决长轨迹中梯度失衡问题"
---

## Core Idea

Trains reasoning agents with **multi-turn rollout** by interleaving thinking steps and tool-calling steps in a single trajectory. Uses GRPO/DAPO-style group rewards applied to entire multi-turn sequences, teaching the model to plan, call tools, interpret results, and revise — all within one RL optimization.

## Training Setup

- **Environment**: tool-augmented sandbox (web search, calculator, code interpreter)
- **Trajectory format**: `<think>...</think> → <tool_call> → <observation> → <think>...` repeated
- **Reward**: final task outcome assigned to entire trajectory; intermediate steps receive no direct reward
- **Policy**: GRPO with group normalization across $G$ multi-turn rollouts per query

## Key Innovation: Turn-Level Credit Assignment

$$\hat{A}_\text{turn} = \frac{R_\text{final} - \mu_\text{group}}{\sigma_\text{group}} \cdot \textcolor{#a78bfa}{\mathbb{1}[\text{turn is reasoning}]}$$

The $\textcolor{#a78bfa}{\text{reasoning-only mask}}$ applies the gradient only to `<think>` tokens and tool call tokens, not to verbatim tool output observations.

## Results

- Outperforms ReAct + GPT-4 on ALFWorld, WebArena, and MiniWoB
- Multi-turn RL significantly outperforms single-turn RL baseline (+18 pts on WebArena)
- Reasoning quality improves with more RL steps even when final accuracy plateaus

## Impact

- Extended GRPO-style RL to multi-turn agentic settings
- Showed that thinking + tool-use can be jointly optimized with RL
- Open codebase enabling reproduction of multi-turn agent RL
