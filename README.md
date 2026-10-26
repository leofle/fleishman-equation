# The Fleishman Equation

An estimate of the chance that AI wipes out humanity, split into a rogue-AI path and a human-misuse path. Single-file, no-build web calculator.

**Live:** https://leofle.github.io/fleishman-equation/

**[Read the white paper (PDF)](https://leofle.github.io/fleishman-equation/fleishman-equation-whitepaper.pdf)**

```
P(doom) = f_T · [1 − (1 − R) · (1 − S)]
R       = f_M · f_P · f_U · f_H · f_X   (rogue path, given powerful AI exists)
S       = f_A · f_W · f_F               (misuse path, given powerful AI exists)

Path contributions shown: P(rogue) = f_T · R, P(misuse) = f_T · S.

P(doom) = probability that AI causes human extinction within a stated time frame.

f_T Transformative capability · f_M Misalignment · f_P Power · f_U Uncaught · f_H Hostile plan · f_X eXtinction · f_A Actor · f_W Weapon · f_F deFenses fail
```

Like the Drake equation, the structure is the useful part; the inputs are guesses. The Optimist/Middle/Pessimist presets are illustrative, not real estimates; research presets are listed below. Slider state is shareable via the query string.

## Assumptions

f_T is counted once (an earlier version multiplied it into both paths, double-counting it). The two paths are treated as independent once powerful AI exists. In reality they can interact (e.g. a misused AI could also escape control), so this is a simplification. Path factors are implicitly averaged over the arrival time of powerful AI within the time frame. Inputs are point values: the product of medians is in general not the median of the product.

License: MIT

## Research presets and sources

The calculator has research presets that reproduce published estimates. When a source gives only a total, the per-factor split is ours, not the authors'. We put the whole total on the rogue-AI path (misuse factors = 0) and set the rogue factors equal so their product matches the source. The page's Sources panel shows the citation, the quoted estimate, the time frame and the mapping for the selected preset.

| Preset | Source | Peer reviewed | Source estimate | Calculator P(doom) |
|---|---|---|---|---|
| AI researchers 2023 | Grace et al. (2025), *Thousands of AI Authors on the Future of AI*, JAIR 84, Art. 9. [doi:10.1613/jair.1.19087](https://doi.org/10.1613/jair.1.19087) | Yes | Median 5%: AI causes human extinction or similarly permanent and severe disempowerment within the next 100 years | 5.0% |
| ML researchers 2016 | Grace et al. (2018), *When Will AI Exceed Human Performance? Evidence from AI Experts*, JAIR 62, 729–754. [doi:10.1613/jair.1.11222](https://doi.org/10.1613/jair.1.11222) | Yes | Median 5%: "Extremely bad (e.g., human extinction)" long-run outcome, assuming HLMI exists (so f_T = 1) | 5.0% |
| Superforecasters (XPT) | Karger et al. (2025), *Subjective-probability forecasts of existential risk*, Int. J. Forecasting 41(2), 499–516. [doi:10.1016/j.ijforecast.2024.11.008](https://doi.org/10.1016/j.ijforecast.2024.11.008); figure from [FRI Working Paper #1 (2023)](https://forecastingresearch.org/pdf/existential-risk-persuasion-tournament.pdf) | Tournament yes; figure from working paper | Median 0.38% [95% CI on the median 0.10–0.75%]: AI causes extinction (population < 5,000) by 2100 | 0.38% |
| AI domain experts (XPT) | Same as above | Same as above | Median 3% [95% CI on the median 0.49–10.00%] by 2100 | 3.0% |
| Carlsmith 2022 | Carlsmith, *Is Power-Seeking AI an Existential Risk?* [arXiv:2206.13353](https://arxiv.org/abs/2206.13353) | No (included for its premise-by-premise breakdown) | 65%·80%·40%·65%·40%·95% ≈ 5% by 2070 (>10% per the May 2022 update note) | 5.1% |

Per-factor values in total-only presets are artifacts of the equal-split mapping, not the respondents' forecasts. The Grace 2018 preset is conditional on HLMI, so it is not on the same scale as the unconditional presets.

Carlsmith mapping (approximate; the deploy-incentive premise is folded into f_T, and APS systems are not the same threshold as "beats humans at most tasks"): f_T = 0.65 × 0.80, f_M = 0.40, f_P = 0.65, f_U = 0.40, f_H = 1, f_X = 0.95, misuse = 0.

Checked but not used: Müller & Bostrom (2016, *Fundamental Issues of AI*, Springer Synthese Library) reports a mean of 18% for "extremely bad (existential catastrophe)", assuming HLMI exists, but we could not confirm it was peer reviewed and it adds no factor breakdown. Sandberg & Bostrom (2008), the FHI Global Catastrophic Risks survey, is a technical report with no factor breakdown. We found no peer-reviewed estimate of extinction from AI-assisted bioterrorism. The FRI LLM-biorisk study (2025) and the GovAI bioterrorism report forecast epidemics, not extinction.
