---
id: simpo
name: SimPO
full: Simple Preference Optimization with a Reference-Free Reward
category: alignment
year: 2024
affiliation: UIUC
paper: https://arxiv.org/abs/2405.14734
code: https://github.com/princeton-nlp/SimPO
venue: NeurIPS 2024
stars: 1900
connects: [dpo, orpo]
improves:
  dpo: "去掉 reference model，引入长度归一化（1/|y|）防止冗长偏好，加入 reward margin γ 避免 winning/losing 奖励趋近，AlpacaEval 2.0 提升 11 点"
  orpo: "与 ORPO 同样无需 reference model，但用平均 log-likelihood 替代 odds ratio，并显式引入 margin 约束"
---

## Core Idea

Uses **average log-likelihood** as an implicit reward (instead of DPO's log-ratio with a reference model) and adds a target reward margin $\gamma$ to ensure a minimum gap between winning and losing responses. Simpler, faster, and often stronger than DPO.

## Key Formula

$$\mathcal{L}^{\text{SimPO}} = -\log \sigma\!\left(\textcolor{#f472b6}{\frac{\beta}{|y_w|}} \log \pi_\theta(y_w|x) - \frac{\beta}{|y_l|} \log \pi_\theta(y_l|x) - \gamma\right)$$

The $\textcolor{#f472b6}{1/|y|}$ length normalization prevents the model from preferring longer responses due to higher cumulative log-likelihood. The margin $\gamma > 0$ enforces a minimum reward gap between preferred and rejected responses.

## Two Key Design Choices

### 1. Length-Normalized Reward
$$r_\text{SimPO}(y|x) = \frac{\beta}{|y|} \log \pi_\theta(y|x)$$
Uses the policy itself as the reward (no reference model needed), normalized by length.

### 2. Target Margin $\gamma$
Adds a constant margin to the Bradley-Terry objective: $r_w - r_l > \gamma$. Prevents the model from converging to near-trivial solutions where $r_w \approx r_l$.

## Comparison with DPO

| Property | DPO | SimPO |
|---|---|---|
| Reference model | Required | Not needed |
| Length normalization | No | Yes ($1/|y|$) |
| Reward margin | No | Yes ($\gamma$) |
| AlpacaEval 2.0 (Llama-3-8B) | 33.8% | 44.7% |

## Impact

- Consistently outperforms DPO on instruction-following benchmarks
- Reference-free and single-stage: simpler deployment than DPO
- Length normalization technique widely adopted for preventing verbosity bias
