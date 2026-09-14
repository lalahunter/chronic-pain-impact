"""Operational definition of chronic pain and high-impact chronic pain (NHIS 2025).

Source: Lucas, J. W., & Sohi, I. (2024). Chronic pain and high-impact chronic pain in U.S. adults, 2023. NCHS Data Brief No. 518.
"""

CHRONIC_PAIN_CODES = [3, 4]     # 3 = most days, 4 = every day
LIMITATION_CODES = [3, 4]       # 3 = most days, 4 = every day
PAIN_INVALID_CODES = [7, 8, 9]  # refused / not ascertained / don't know


def flag_chronic_pain(df):
    """Pain on most days or every day in the past 3 months."""
    return df["PAIFRQ3M_A"].isin(CHRONIC_PAIN_CODES)


def flag_hicp(df):
    """Chronic pain that also limits life or work activities on most days or every day."""
    return flag_chronic_pain(df) & df["PAIWKLM3M_A"].isin(LIMITATION_CODES)


def flag_cohort(df):
    """Analytical cohort: chronic pain, with the limitation question answered."""
    return flag_chronic_pain(df) & ~df["PAIWKLM3M_A"].isin(PAIN_INVALID_CODES)


def recode_invalid_to_nan(df, invalid_codes):
    """Replace survey non-response codes with NaN.

    invalid_codes maps each column to its own non-response codes, because these
    differ across variables (7/8/9 for most, 97/98/99 for EDUCP_A and RATCAT_A).
    """
    out = df.copy()
    for column, codes in invalid_codes.items():
        out[column] = out[column].mask(out[column].isin(codes))
    return out