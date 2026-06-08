---
id: orpo
name: ORPO
full: Odds Ratio Preference Optimization
category: alignment
year: 2024
affiliation: KAIST
paper: https://arxiv.org/abs/2403.07691
code: https://github.com/xfactlab/orpo
venue: ACL 2024
stars: 1600
connects: [dpo]
improves:
  dpo: "去掉 reference model（节省一倍显存），将 SFT 目标内嵌为正则项，单阶段完成对齐，训练速度提升且无需分阶段"
---

## Core Idea

Unifies supervised fine-tuning (SFT) and preference alignment into a **single training loss** using an odds-ratio penalty. Eliminates the need for a separate reference model — the SFT objective itself acts as a regularizer.

## Key Formula

$$\mathcal{L}^{\text{ORPO}} = \mathcal{L}_{\text{SFT}} - \lambda \cdot \log \sigma\!\left(\log \textcolor{#f472b6}{\frac{\text{odds}_\theta(y_w|x)}{\text{odds}_\theta(y_l|x)}}\right)$$

Where $\textcolor{#f472b6}{\text{odds}_\theta(y|x) = \frac{\pi_\theta(y|x)}{1 - \pi_\theta(y|x)}}$ is the odds of the response being generated.

## Why Odds Ratio?

The odds ratio $\frac{\text{odds}(y_w)}{\text{odds}(y_l)}$ measures the relative preference strength in a scale-invariant way. Unlike DPO's log-ratio, the odds ratio penalizes weakly-preferred responses even when absolute probabilities are low.

## Comparison with DPO

| Property | DPO | ORPO |
|---|---|---|
| Reference model | Required | Not needed |
| SFT step | Separate | Unified in loss |
| Training stages | 2 (SFT → DPO) | 1 |
| Memory | 2× (policy + ref) | 1× |

## Results

- LLaMA-3-8B fine-tuned with ORPO matches DPO quality on AlpacaEval 2.0
- Trains faster (single-stage) with lower memory
- Achieves better calibration on safety benchmarks

## Impact

- Reference-free formulation inspired SimPO and subsequent single-stage methods
- Integrated into Hugging Face TRL
- Demonstrated that SFT regularization can replace explicit KL constraints
