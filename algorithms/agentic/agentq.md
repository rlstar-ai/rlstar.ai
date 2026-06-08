---
id: agentq
name: Agent-Q
full: Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents
category: agentic
year: 2024
affiliation: MultiOn / Stanford
paper: https://arxiv.org/abs/2408.07199
venue: arXiv
stars: 1100
connects: [agent_rl, dpo]
improves:
  agent_rl: "引入 MCTS 在训练时探索高质量轨迹，解决 agentic RL 中稀疏奖励下探索困难的问题，WebShop 任务提升至 57%"
  dpo: "将 DPO 从单轮文本偏好扩展到多步轨迹级偏好，用 MCTS 成功/失败路径对构造训练数据"
---

## Core Idea

Combines **MCTS-guided search** at training time with **DPO** for policy optimization. MCTS explores the action space to find high-quality trajectories; DPO then trains the policy from preference pairs (successful vs failed paths) without requiring explicit reward modeling.

## Training Pipeline

1. **MCTS Rollout** — Monte Carlo Tree Search explores web navigation action sequences
2. **Trajectory Scoring** — final task success/failure scores each path
3. **Preference Construction** — pair successful and failed paths sharing a common prefix
4. **DPO Update** — fine-tune policy to prefer successful paths over failed ones

## Key Formula

$$\mathcal{L}^{\text{AgentQ}} = -\log \sigma\!\left(\beta \log \frac{\pi_\theta(\tau_w)}{\pi_\text{ref}(\tau_w)} - \beta \log \frac{\pi_\theta(\tau_l)}{\pi_\text{ref}(\tau_l)}\right)$$

Applied at the **trajectory level** $\tau$ rather than single-response level, using MCTS-discovered pairs.

## Results

| Benchmark | Zero-shot GPT-4o | Agent-Q (1-day data) |
|---|---|---|
| WebShop | 24.7% | 57.2% |
| Mind2Web | 28.4% | 50.5% |

## Impact

- Demonstrated MCTS + offline RL (DPO) as viable for web agents
- Showed that trajectory-level preference learning generalizes from text to action sequences
- Influenced multi-turn DPO and agent training pipelines
