# The Fleishman Equation

An estimate of the chance that AI wipes out humanity, split into a rogue-AI path and a human-misuse path. Single-file, no-build web calculator.

**Live:** https://leofle.github.io/fleishman-equation/

**[Read the white paper (PDF)](https://leofle.github.io/fleishman-equation/fleishman-equation-whitepaper.pdf)**

```
P(doom) = f_T · [1 − (1 − R) · (1 − S)] + (f_C − f_T) · S,   f_C ≥ f_T
R       = f_M · f_P · f_U · f_H · f_X   (rogue path, given transformative AI)
S       = f_A · f_W · f_F               (misuse path, given weapons-capable AI)

Path contributions shown: P(rogue) = f_T · R, P(misuse) = f_C · S.

P(doom) = probability that AI causes human extinction within a stated time frame.

f_T Transformative capability · f_C misuse Capability · f_M Misalignment · f_P Power · f_U Uncaught · f_H Harmful pursuit · f_X eXtinction · f_A Actor · f_W Weapon · f_F deFenses fail
```

f_C is the chance of AI capable enough to give serious uplift toward mass-casualty weapons. Transformative AI implies it, so f_C ≥ f_T (the calculator enforces this). Worlds with transformative AI face both paths; worlds with only weapons-capable AI face misuse alone. f_H covers extinction deliberately or as a side effect of the AI pursuing its goals. Old share links without `C` still work: f_C defaults to f_T, which gives the same result as before.

Like the Drake equation, the structure is the useful part; the inputs are guesses. The Optimist/Middle/Pessimist presets are illustrative, not real estimates; research presets are listed below. Slider state is shareable via the query string.

## Assumptions

f_T is counted once (an earlier version multiplied it into both paths, double-counting it). The two paths are treated as independent once transformative AI exists, and S is assumed the same in worlds with and without transformative AI. In reality they can interact (e.g. a misused AI could also escape control), so this is a simplification. Path factors are implicitly averaged over the arrival time of the relevant capability within the time frame. Inputs are point values: the product of medians is in general not the median of the product.

License: MIT

## Research presets and sources

The calculator has research presets that reproduce published estimates. When a source gives only a total, the per-factor split is ours, not the authors'. We put the whole total on the rogue-AI path (misuse factors = 0, f_C = f_T). Where the same source reports a probability of general/human-level AI for the same time frame, f_T is anchored on it and the other five rogue factors are set equal; otherwise all six are equal. XPT: f_T = 0.7475 (superforecasters) and 0.87 (domain experts, N = 5), the Stage-4 medians for "Nick Bostrom will affirm the existence of AGI" by 2100 (FRI Working Paper #1, Table 17, p. 55; a proxy question), other five factors 0.3477 and 0.5099. Grace et al. (2025) reports HLMI forecasts only for 2027 (10%) and 2047 (50%), not for its 100-year horizon, so it keeps the even split (0.607). Grace et al. (2018) is conditional on HLMI, so f_T = 1. The page's Sources panel shows the citation, the quoted estimate, the time frame and the mapping for the selected preset.

| Preset | Source | Peer reviewed | Source estimate | Calculator P(doom) |
|---|---|---|---|---|
| AI researchers 2023 | Grace et al. (2025), *Thousands of AI Authors on the Future of AI*, JAIR 84, Art. 9. [doi:10.1613/jair.1.19087](https://doi.org/10.1613/jair.1.19087) | Yes | Median 5%: AI causes human extinction or similarly permanent and severe disempowerment within the next 100 years | 5.0% |
| ML researchers 2016 | Grace et al. (2018), *When Will AI Exceed Human Performance? Evidence from AI Experts*, JAIR 62, 729–754. [doi:10.1613/jair.1.11222](https://doi.org/10.1613/jair.1.11222) | Yes | Median 5%: "Extremely bad (e.g., human extinction)" long-run outcome, assuming HLMI exists (so f_T = 1) | 5.0% |
| Superforecasters (XPT) | Karger et al. (2025), *Subjective-probability forecasts of existential risk*, Int. J. Forecasting 41(2), 499–516. [doi:10.1016/j.ijforecast.2024.11.008](https://doi.org/10.1016/j.ijforecast.2024.11.008); figure from [FRI Working Paper #1 (2023)](https://forecastingresearch.org/pdf/existential-risk-persuasion-tournament.pdf) | Tournament yes; figure from working paper | Median 0.38% [95% CI on the median 0.10–0.75%]: AI causes extinction (population < 5,000) by 2100 | 0.38% |
| AI domain experts (XPT) | Same as above | Same as above | Median 3% [95% CI on the median 0.49–10.00%] by 2100 | 3.0% |
| Carlsmith 2022 | Carlsmith, *Is Power-Seeking AI an Existential Risk?* [arXiv:2206.13353](https://arxiv.org/abs/2206.13353) | No (included for its premise-by-premise breakdown) | 65%·80%·40%·65%·40%·95% ≈ 5% by 2070 (>10% per the May 2022 update note) | 5.1% |

Apart from the XPT f_T anchors, per-factor values in total-only presets are artifacts of the equal-split mapping, not the respondents' forecasts. The Grace 2018 preset is conditional on HLMI, so it is not on the same scale as the unconditional presets.

Carlsmith mapping (approximate; the deploy-incentive premise is folded into f_T, and APS systems are not the same threshold as "beats humans at most tasks"): f_T = f_C = 0.65 × 0.80, f_M = 0.40, f_P = 0.65, f_U = 0.40, f_H = 1, f_X = 0.95, misuse = 0.

Checked but not used: Müller & Bostrom (2016, *Fundamental Issues of AI*, Springer Synthese Library) reports a mean of 18% for "extremely bad (existential catastrophe)", assuming HLMI exists, but we could not confirm it was peer reviewed and it adds no factor breakdown. Sandberg & Bostrom (2008), the FHI Global Catastrophic Risks survey, is a technical report with no factor breakdown. We found no peer-reviewed estimate of extinction from AI-assisted bioterrorism. The FRI LLM-biorisk study (2025) and the GovAI bioterrorism report forecast epidemics, not extinction.
