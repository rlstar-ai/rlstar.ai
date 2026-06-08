---
id: minillm
name: MiniLLM
full: On-Policy Distillation of Large Language Models
category: OPD
year: 2023
affiliation: Tsinghua University / Microsoft Research
paper: https://arxiv.org/abs/2306.08543
venue: arXiv
connects: [grpo, reinforce]
---

## Core Idea

Replaces forward KL divergence with reverse KL divergence for knowledge distillation in LLMs, preventing the student from overestimating low-probability regions of the teacher distribution, and derives an on-policy optimization algorithm to train the student.

## Key Formula

$$\min_\theta \mathbb{KL}(p_\theta \| p_T) = \mathbb{E}_{y \sim p_\theta}\left[\log \frac{p_\theta(y|x)}{p_T(y|x)}\right]$$

Reverse KL (student generates, teacher scores) vs. standard forward KL (teacher generates, student imitates).

## Key Improvements over Standard KD

- Forward KL causes mode-averaging and overestimation of low-prob regions
- Reverse KL + on-policy sampling keeps student in high-probability teacher regions
- Derives REINFORCE-style gradient for end-to-end sequence-level optimization

## Impact

- Established "on-policy distillation" as a distinct paradigm from SFT-based imitation
- Directly inspired SDPO, SDAR, and MOPD in MiMo-V2
