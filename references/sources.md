# References

## Data

- National Center for Health Statistics. National Health Interview Survey, 2025.
Public-use data file and documentation.
https://www.cdc.gov/nchs/nhis/documentation/index.html. 2026.

Suggested data source line for tables and figures:
> Data Source: National Center for Health Statistics, National Health Interview Survey, 2025.

**Disclaimer required by NCHS:** the analyses, interpretations, and conclusions in this project are the author's own. NCHS is responsible only for the initial data.



## Documentation

- National Center for Health Statistics. *2025 National Health Interview Survey: Sample Adult Codebook*. 2026.
https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2025/Adult-codebook.pdf

Used to understand the variables, their response codes, and how the survey questions were applied.Pages used: `WTFA_A` (p. 4), `PSTRAT` (p. 7), `PPSU`  (p. 8).

---

- National Center for Health Statistics. *2025 National Health Interview Survey: Sample Adult Summary*. 2026.
https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2025/Adult-summary.pdf

Used to locate the chronic pain module and its variables (p. 54).

---

- National Center for Health Statistics. National Health Interview Survey, 2025 survey description. 2026.
https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2025/srvydesc-508.pdf

Used for the sample design and the survey design variables.
Sections: Sample Design (p. 14), Weighting (p. 33), Weights (p. 34),
Variance Estimation (p. 35), Variance Estimation for Subsetted Data Analysis (p. 72).



## Definitions

- Lucas JW, Sohi I. Chronic pain and high-impact chronic pain in U.S. adults, 2023. NCHS Data Brief, no 518. Hyattsville, MD: National Center for Health Statistics. 2024. DOI: https://dx.doi.org/10.15620/cdc/169630

Used for the operational definitions of chronic pain and high-impact chronic pain.
The definitions are consistent across NHIS years; this project applies them to the 2025 data. The published prevalence figures in this brief (2023 data) are used only as a sanity check.



## Context and burden

- Guy GP Jr, Miller GF, Legha JK, Rikard SM, Strahan AE, Mikosz C, Florence CS.
Economic Costs of Chronic Pain—United States, 2021. *Medical Care*.
2025 Sep 1;63(9):679-685. doi:10.1097/MLR.0000000000002181

Used to support the statement on the economic burden of chronic pain ($722.8 billion in 2021: $530.6 billion in medical care costs and $192.2 billion in lost work productivity).



## Clinical background

- Butler DS, Moseley GL. *Explain Pain*. 2nd ed. Adelaide: Noigroup Publications; 2013.

Used for the pain neuroscience framework underlying the section on why pain intensity may not be enough: central sensitisation, the role of perceived threat in pain output, and the effect of pain education on pain itself.

--- 

- Dunn M, Rushton AB, Mistry J, Soundy A, Heneghan NR. The biopsychosocial factors associated with development of chronic musculoskeletal pain. An umbrella review and meta-analysis of observational systematic reviews. PLOS ONE. 2024;19(1):e0294830. doi:10.1371/journal.pone.0294830

Umbrella review of 13 systematic reviews (185 studies, 489,644 participants). Used here to justify the biopsychosocial domains from which the candidate variables were drawn. Note that its outcome is the development of chronic pain, not high impact within chronic pain.



## Biopsychosocial framework and variable selection

- Eccleston C, et al. The establishment, maintenance, and adaptation of high- and low-impact chronic pain: a framework for biopsychosocial pain research. PAIN. 2023;164(10):2143–2147. doi:10.1097/j.pain.0000000000002951

Used as the conceptual framework for distinguishing pain impact from pain characteristics
and for guiding the biopsychosocial structure of the candidate-variable selection.

---

- Falasinnu T, Hossain MB, Weber KA II, Helmick CG, Karim ME, Mackey S.
*The Problem of Pain in the United States: A Population-Based Characterization
of Biopsychosocial Correlates of High Impact Chronic Pain using the National
Health Interview Survey.* The Journal of Pain. 2023;24(6):1094–1103.
doi:10.1016/j.jpain.2023.03.008

Used as prior empirical evidence for the selection of candidate biopsychosocial
domains. The study used NHIS data and examined sociodemographic, psychosocial comorbidity, healthcare-utilisation and behavioural factors associated with HICP.

The study also informed the interpretation of these variables as correlates rather
than causal risk factors because of the cross-sectional survey design.



### Population-level chronic pain and HICP

- Von Korff, M., Scher, A. I., Helmick, C., Carter-Pokras, O., Dodick, D. W.,
  Goulet, J., Hamill-Ruth, R., LeResche, L., Porter, L., Tait, R., Terman, G.,
  Veasley, C., & Mackey, S. (2016). United States National Pain Strategy for
  Population Research: Concepts, definitions, and pilot data.
  *The Journal of Pain, 17*(10), 1068–1080.
  https://doi.org/10.1016/j.jpain.2016.06.009

- Dahlhamer, J., Lucas, J., Zelaya, C., Nahin, R., Mackey, S., DeBar, L.,
  Kerns, R., Von Korff, M., Porter, L., & Helmick, C. (2018). Prevalence of chronic pain and high-impact chronic pain among adults — United States, 2016.
  *Morbidity and Mortality Weekly Report, 67*(36), 1001–1006.
  https://doi.org/10.15585/mmwr.mm6736a2

- Lucas, J. W., & Sohi, I. (2024). Chronic pain and high-impact chronic pain in U.S. adults, 2023. *NCHS Data Brief*, No. 518. National Center for Health Statistics.
https://doi.org/10.15620/cdc/169630



### Model transportability and external validation

- Riley, R. D., Archer, L., Snell, K. I. E., Ensor, J., Dhiman, P., Martin, G. P., Bonnett, L. J., & Collins, G. S. (2024). Evaluation of clinical prediction models (part 2): how to undertake an external validation study. *BMJ, 384*, e074820. https://doi.org/10.1136/bmj-2023-074820

- Collins, G. S., Dhiman, P., Ma, J., Schlussel, M. M., Archer, L., Van Calster, B., Harrell, F. E. Jr., Martin, G. P., Moons, K. G. M., van Smeden, M., Sperrin, M., & Bullock, G. S. (2024). Evaluation of clinical prediction models (part 1): from development to external validation. *BMJ, 384*, e074819. https://doi.org/10.1136/bmj-2023-074819



### Classification thresholds and decision usefulness

- Vickers, A. J., & Elkin, E. B. (2006). Decision curve analysis:
  A novel method for evaluating prediction models. *Medical Decision Making, 26*(6), 565–574.
  https://doi.org/10.1177/0272989X06295361

- Efthimiou, O., Seo, M., Chalkou, K., Debray, T., Egger, M.,
  Salanti, G., et al. (2024). Developing clinical prediction models: A step-by-step guide. *BMJ, 386*, e078276.
  https://doi.org/10.1136/bmj-2023-078276