# The Fleishman equation

A Drake-style estimate of the chance that AI wipes out humanity, split into a rogue-AI path and a human-misuse path. Single-file, no-build web calculator.

**Live:** https://leofle.github.io/fleishman-equation/

```
P(doom)   = 1 − (1 − P(rogue)) · (1 − P(misuse))
P(rogue)  = f_T · f_M · f_P · f_U · f_H · f_X
P(misuse) = f_T · f_A · f_W · f_F
```

Like the Drake equation, the structure is the useful part; the inputs are guesses. Presets are illustrative, not real estimates. Slider state is shareable via the query string.

License: MIT
