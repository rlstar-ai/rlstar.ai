---
id: agent_rl
name: AgentRL
full: Scaling LLM Test-Time Compute for Agentic Tasks (Survey)
category: agentic
year: 2024
affiliation: Various
paper: https://arxiv.org/abs/2410.02707
venue: arXiv
stars: ~
connects: [ppo, grpo, ragen, agentq]
improves:
  ppo: "将 PPO 扩展到多步工具调用轨迹，处理稀疏奖励和长程信用分配，使 PPO 可用于复杂 agentic 任务"
  grpo: "将 GRPO 的 group-relative 思想引入多步 agent 轨迹级奖励，为 RAGEN 等工作奠定基础"
  ragen: "RAGEN 直接继承 AgentRL 的多步 RL 框架，加入 think-tool 交替轨迹和推理 mask 精细化信用分配"
  agentq: "Agent-Q 在 AgentRL 框架下引入 MCTS 搜索生成高质量轨迹对，再用 DPO 而非在线 RL 优化策略"
---

## Core Idea

Applies RL to LLM agents operating in multi-step environments with tool use. Unlike single-turn reasoning RL, agentic RL deals with long trajectories, sparse rewards, and environments that include web browsers, code interpreters, databases, and APIs.

## Problem Setting

- **State**: conversation history + tool observations
- **Action**: text generation (may include tool calls like `search("query")`)
- **Reward**: task completion signal at the end of trajectory (sparse)
- **Challenge**: credit assignment over many steps; reward may be delayed by 10–50 turns

## Key Techniques Surveyed

| Technique | Purpose |
|---|---|
| Trajectory-level REINFORCE | Assign reward to full multi-step rollout |
| Process Reward Models (PRM) | Dense per-step reward to reduce sparsity |
| MCTS rollouts | Explore action space at inference time |
| Hindsight relabeling | Turn failed trajectories into useful training data |

## Representative Results

- WebArena (web navigation): RL-trained agents achieve 35%+ success vs <20% for SFT
- SWE-Bench (software engineering): RL improves patch generation by 15+ points
- Tool-use benchmarks: significant gains with multi-turn RL vs single-turn prompting

## Impact

- Unified framework for understanding agent RL across diverse environments
- Motivated RAGEN, AgentQ, and subsequent work on multi-turn RL
- Established that tool-use diversity and trajectory length are key challenges
