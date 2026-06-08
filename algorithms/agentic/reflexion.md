---
id: reflexion
name: Reflexion
full: Reflexion: Language Agents with Verbal Reinforcement Learning
category: agentic
year: 2023
affiliation: Northeastern University / MIT
paper: https://arxiv.org/abs/2303.11366
code: https://github.com/noahshinn/reflexion
venue: NeurIPS 2023
stars: 4100
connects: [agent_rl]
improves:
  agent_rl: "用语言反思替代梯度更新，无需参数修改即可在多次尝试间学习，开创了 verbal RL 范式，为 agentic RL 提供了无梯度的轻量替代路径"
---

## Core Idea

Agents improve through **verbal reinforcement**: after failing a task, the agent reflects on the failure in natural language, stores the reflection in a memory buffer, and uses it to guide the next attempt. No gradient updates — learning happens through prompting and memory.

## Key Formula (verbal RL loop)

$$\text{Reflect}_t = \text{LLM}(\text{task}, \text{trajectory}_t, \text{outcome}_t)$$
$$\text{Memory}_{t+1} = \text{Memory}_t + \{\text{Reflect}_t\}$$
$$\text{Action}_{t+1} = \text{LLM}(\text{task}, \textcolor{#f59e0b}{\text{Memory}_{t+1}})$$

The $\textcolor{#f59e0b}{\text{accumulated memory}}$ of past reflections guides future attempts, approximating a policy improvement step without backpropagation.

## Three Components

1. **Actor** — generates task-solving trajectories via LLM
2. **Evaluator** — scores trajectory outcome (correct/incorrect, reward signal)
3. **Self-Reflection** — synthesizes natural language critique stored in episodic memory

## Results

- Sequential Decision Making (AlfWorld): 91% success vs 67% baseline
- Programming (HumanEval): 91% pass@1 after 4 iterations
- Web Navigation (WebShop): 12-point improvement over ReAct

## Impact

- Popularized "verbal RL" as a lightweight alternative to gradient-based fine-tuning
- Episodic memory + reflection pattern widely adopted in agent frameworks
- Influenced LangChain, AutoGPT, and other agent architectures
