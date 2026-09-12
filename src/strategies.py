"""Pain management strategies reported in the past 3 months (NHIS 2025, PAI module)."""

import pandas as pd

STRATEGY_LABELS = {
    "PAIOTCMEDS_A": "OTC medication",
    "PAIPRSMEDS_A": "Prescribed pain reliever",
    "PAIOPIOID_A": "Opioids",
    "PAIPHYSTPY_A": "Physical therapy",
    "PAICHIRO_A": "Chiropractic care",
    "PAITALKTPY_A": "Talk therapy",
    "PAIYOGA_A": "Yoga",
    "PAIEXRCISE_A": "Exercise",
    "PAIMASSAGE_A": "Massage",
    "PAIMEDITAT_A": "Meditation",
    "PAIMOTHER_A": "Other methods",
}

YES, NO = 1, 2


def strategy_uptake(df, mask):
    """Share of respondents using each pain management strategy, within a subgroup.

    Parameters
    ----------
    df : pandas.DataFrame
        NHIS Sample Adult file.
    mask : pandas.Series of bool
        Subgroup selector, e.g. df["hicp"].

    Returns
    -------
    pandas.DataFrame
        One row per strategy, sorted by uptake, with valid responses as denominator.
    """
    rows = []
    for column, label in STRATEGY_LABELS.items():
        answers = df.loc[mask, column]
        n_valid = answers.isin([YES, NO]).sum()
        n_yes = (answers == YES).sum()
        rows.append({
            "strategy": label,
            "n_yes": n_yes,
            "n_valid": n_valid,
            "pct": round(n_yes / n_valid * 100, 1),
        })
    return pd.DataFrame(rows).sort_values("pct", ascending=False, ignore_index=True)