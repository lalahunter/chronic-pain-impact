"""Operational definition of chronic pain and high-impact chronic pain (NHIS 2025).

Source: Lucas, J. W., & Sohi, I. (2024). Chronic pain and high-impact chronic
pain in U.S. adults, 2023. NCHS Data Brief No. 518.
"""

CHRONIC_PAIN_CODES = [3, 4]   # 3 = most days, 4 = every day
LIMITATION_CODES = [3, 4]     # 3 = most days, 4 = every day
INVALID_CODES = [7, 8, 9]     # refused / not ascertained / don't know


def flag_chronic_pain(df):
    """Pain on most days or every day in the past 3 months."""
    return df["PAIFRQ3M_A"].isin(CHRONIC_PAIN_CODES)


def flag_hicp(df):
    """Chronic pain that also limits life or work activities on most days or every day."""
    return flag_chronic_pain(df) & df["PAIWKLM3M_A"].isin(LIMITATION_CODES)


def recode_invalid_to_nan(df, columns):
    """Replace survey non-response codes (7/8/9) with NaN in the given columns."""
    out = df.copy()
    out[columns] = out[columns].mask(out[columns].isin(INVALID_CODES))
    return out