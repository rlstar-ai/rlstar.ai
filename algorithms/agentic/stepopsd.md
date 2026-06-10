---
id: stepopsd
name: StepOPSD
full: Step-Aware Online Preference Distillation for Agent RL
category: agentic
year: 2026
affiliation: Unknown
paper: https://arxiv.org/abs/2605.27140
venue: arXiv
connects: [minillm]
---

## Core Idea

Decomposes agent trajectories into action-centered segments, re-scores each step online, and applies preference distillation with advantage shaping to solve the credit assignment problem in multi-turn agent RL.

## Key Innovation

Rather than assigning a single terminal reward to the entire trajectory, StepOPSD segments the rollout at each action boundary and scores each segment independently using an online preference model. The per-step advantage estimates are then used to weight a distillation loss, propagating dense learning signals through all turns.

## Impact

- Addresses sparse reward / credit assignment in long-horizon agentic tasks
- Combines online preference distillation with step-level advantage shaping
- Bridges on-policy distillation (MiniLLM) with multi-turn agent RL
