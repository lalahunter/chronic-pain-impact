# Chronic pain impact

Among US adults living with chronic pain, what distinguishes those whose pain disables them from those whose pain does not, and what do they report doing to manage it?

Individual final project, Ironhack Data Analytics bootcamp, September 2026.

## The questions

1. Among adults with chronic pain, what distinguishes those with high-impact chronic pain, and is pain intensity alone enough to distinguish them?
2. What pain-management strategies are reported by adults with HICP?
3. Among adults with HICP, does reported use of those strategies vary across socioeconomic and healthcare-access characteristics?

The full framing, hypotheses and analysis plan are in:
[`docs/business-case.md`](docs/business-case.md).

## Data

NHIS 2025 Sample Adult public-use file (24215 respondents, 577 variables), included in `data/raw/`. Analytical cohort: 5592 adults with chronic pain, of whom 1956 have high-impact chronic pain.

Documentation PDFs are in `references/`; full references in:
[`references/sources.md`](references/sources.md).

## Repository

- `notebooks/01-data-audit.ipynb` — what is in the file, missing data, variable selection
- `notebooks/02-data-preparation.ipynb` — building the cohort and the HICP outcome
- `src/` — the operational definitions and reusable functions
- `docs/` — project framing
- `references/` — source documentation


## Running it

    pip install -r requirements.txt

Then run the notebooks in order.

## Disclaimer

The analyses, interpretations and conclusions in this project are the author's own.
The National Center for Health Statistics is responsible only for the initial data.