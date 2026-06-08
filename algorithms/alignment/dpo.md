---
id: dpo
name: DPO
full: Direct Preference Optimization
category: alignment
year: 2023
affiliation: Stanford University
paper: https://arxiv.org/abs/2305.18290
code: https://github.com/eric-mitchell/direct-preference-optimization
venue: NeurIPS 2023
stars: 7800
connects: [rlhf, orpo, simpo]
improves:
  rlhf: "将 RLHF 的三步流程（SFT→RM→PPO）压缩为单一 BCE 损失，通过闭式解推导出等价目标，训练稳定性大幅提升"
  orpo: "ORPO 在 DPO 基础上去掉 reference model，将 SFT 与对齐合并为一个 loss，进一步简化流程"
  simpo: "SimPO 在 DPO 基础上去掉 reference model 并引入长度归一化与 reward margin，缓解了 DPO 的冗长偏好问题"
---

## Core Idea

Bypasses reward model training entirely by reparameterizing the RLHF objective. Shows that the optimal policy under the KL-constrained reward maximization problem can be expressed in closed form, yielding a simple binary cross-entropy loss on preference pairs.

## Key Formula

$$\mathcal{L}^{\text{DPO}} = -\log \sigma\!\left(\beta \log \frac{\textcolor{#f472b6}{\pi_\theta(y_w|x)}}{\pi_{\text{ref}}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)}\right)$$

The $\textcolor{#f472b6}{\text{implicit reward}}$ $\beta \log \frac{\pi_\theta(y|x)}{\pi_\text{ref}(y|x)}$ replaces the explicit reward model $r_\phi$, derived by solving the RLHF optimization in closed form.

## Derivation Insight

Under the KL-penalized reward objective:
$$\max_\pi \mathbb{E}_{y \sim \pi}[r(x,y)] - \beta \mathbb{D}_\text{KL}[\pi \| \pi_\text{ref}]$$

The optimal policy is $\pi^*(y|x) \propto \pi_\text{ref}(y|x) \exp(r(x,y)/\beta)$. Substituting this and the Bradley-Terry preference model, the reward model drops out, leaving only $\pi_\theta$ and $\pi_\text{ref}$.

## Advantages over RLHF

- No separate reward model training (Step 2 of RLHF pipeline eliminated)
- No PPO training loop (Step 3 eliminated)
- Single supervised-style loss; stable training
- 2–3× faster to train than PPO-based RLHF

## Impact

- Most widely adopted alignment method in open-source LLMs
- Used in LLaMA-2-Chat, Mistral-Instruct, Zephyr, and hundreds of fine-tuned models
- Spawned SimPO, ORPO, IPO, KTO as variants addressing different limitations
