# White paper source

Source for *The Rogue–Misuse Decomposition* white paper (the PDF in the repo root).

## Build

Requires Node.js 18+ (and Python 3 with matplotlib for the figure).

```sh
cd paper
npm install
npx playwright install chromium
python3 make_chart.py   # optional: regenerates fig1_sensitivity.svg/.png
node build.js           # writes paper.html and rogue_misuse_decomposition_whitepaper.pdf
python3 check.py        # recomputes the scenario and preset numbers quoted in the paper
python3 check_arith.py  # extra arithmetic checks
```

`build.js` renders the `$...$` / `$$...$$` math with KaTeX, prints the page to PDF with Playwright/Chromium, and sets the PDF Author with pdf-lib. To publish, copy the PDF to `../rogue-misuse-decomposition-whitepaper.pdf` and `../fleishman-equation-whitepaper.pdf` (the old filename is kept so existing links work).
