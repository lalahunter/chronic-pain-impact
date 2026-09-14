# Business case

## 1. Business problem

Chronic pain is common and its consequences go well beyond the symptom itself. In 2023, using data from the National Health Interview Survey, the National Center for Health Statistics reported that 24.3% of US adults had chronic pain and 8.5% had high-impact chronic pain in the past 3 months (Lucas & Sohi, 2024).

These definitions are operational and specific. Chronic pain means pain experienced on most days or every day during the previous 3 months. High-impact chronic pain (HICP) adds a second condition: the pain limited life or work activities on most days or every day. Both increase with age (Lucas & Sohi, 2024).

The distinction matters, because the two groups are not the same problem. Chronic pain has multifactorial biopsychosocial causes and affects every domain of a person's life: personal, professional, social, family and financial. But it is the high-impact group that carries the disruption. These are the people for whom pain is not only present, but disabling.

The burden is also economic. A recent analysis estimated the annual cost of chronic pain in the United States in 2021 at $722.8 billion, including $530.6 billion in medical care costs and $192.2 billion in lost work productivity (Guy et al., 2025).

In clinical practice, though, pain is usually quantified by intensity, a single number on a scale. Intensity describes the sensation. It does not describe what the pain does to a life, and the two do not always move together.

The 2025 NHIS, the most recent year available, includes a chronic pain module covering pain frequency, intensity and location, its impact on daily life and family, and the strategies people report using to manage it.

This project uses that module to ask two things. First, what distinguishes adults whose chronic pain is disabling from those whose chronic pain is not. Second, what those adults report doing to manage their pain.

## 2. Why pain intensity may not be enough

Pain intensity is a subjective report. The same number means different things to different people, and in chronic pain it is a poor indicator of tissue damage.

When pain persists, the nervous system can become sensitised and it is the brain's appraisal of threat, rather than the state of the tissue, that sets the volume. Pain then fluctuates with sleep, emotional state, context, among other factors. Every touch, position, activity, or even the thought of a specific movement is detected as a potential threat by the brain of individuals with chronic pain. The brain becomes dysregulated and stuck in an active alarm state (Butler & Moseley, 2013).

This creates a practical problem. Pain intensity is easy to quantify, but it does not tell us how much pain is disrupting a person's life. Intensity and impact do not always move together. Someone who has stopped working, stopped going out and built their life around avoiding pain may report a high score or a moderate one. The number alone does not tell us which.

If pain intensity is the main criterion used to assess burden, it cannot reliably identify the people whose lives have been most disrupted.

That is why understanding pain can change pain.

## 3. Stakeholder and decision

The results are aimed at people who plan and fund services at population level rather than treat individual patients: health system planners and payers. The cost figures above tell them the total burden is large, in medical spending and in lost work. What a total does not tell them is where that burden concentrates, or what characterises the people who carry most of it.

Two things would change with these results.

First, what gets taken into account when burden is assessed. If pain intensity alone does not separate the disabling cases from the rest, then whatever does separate them belongs in how burden is measured in the first place.

Second, where to look more closely. If reported use of a pain-management strategy varies across income, education, region or cost-related barriers to care, that variation points to subgroups worth examining in service planning.

This analysis is cross-sectional and observational. It can show what is associated with high impact, and how reported use differs between groups. It cannot show that a particular allocation of resources would improve outcomes.

## 4. Research questions

**RQ1 (analytical).** Among adults with chronic pain, what distinguishes those with high-impact chronic pain, and is pain intensity alone enough to distinguish them?

**RQ2 (descriptive).** What pain-management strategies are reported by adults with HICP?

**RQ3 (analytical).** Among adults with HICP, does reported use of pain-management strategies vary across socioeconomic and healthcare-access characteristics?

## 5. Hypotheses

RQ1 carries two hypotheses, RQ2 is descriptive and carries none, and RQ3 carries one.

**H1 (RQ1).** Pain intensity will be associated with high-impact chronic pain, but the information routinely available in a consultation (pain intensity, age, sex and pain location) will not be enough to distinguish adults with HICP from those with chronic pain without high impact. This fails if that baseline model already separates the two groups well.

**H2 (RQ1).** Adding biopsychosocial information to the baseline will improve the distinction between the two groups. This fails if Model B performs no better than Model A. The variables in the biopsychosocial layer are listed in the modelling design section below and are specified before the models are run.

**H3 (RQ3).** Reported use of pain-management strategies will differ across socioeconomic and healthcare-access characteristics. Guy et al. (2025) report that chronic pain disproportionately affects adults with low household incomes. That finding concerns prevalence rather than treatment, but it makes a socioeconomic pattern in reported use plausible here as well. Differences are examined across income-to-poverty ratio, education, region, and two cost-related barriers to care: having delayed medical care because of cost, and having needed medical care but not received it because of cost.

## 6. Modelling design (RQ1)

RQ1 is answered by comparing three models on the same outcome and the same cohort.

**Outcome:** high-impact chronic pain (yes / no), within adults with chronic pain (n = 5,592; 1,956 with HICP, 3,636 without).

**Model 0.** Pain intensity only. (`PAIAMNT_A`, recoded). **The response codes are not ordered by intensity** in the file: 1 is "a little", 2 is "a lot" and 3 is "somewhere in between". The variable is recoded to a correctly ordered scale before use, in `notebooks/02-data-preparation.ipynb`.

**Model A, baseline.** Pain intensity plus the rest of the information a clinician already has in a short consultation: age, sex, and pain location.

**Model B, baseline plus biopsychosocial layer.** Everything in Model A, plus eight biopsychosocial variables. The list was fixed before any model was run, from the domains reported in the literature and from the audit in `notebooks/01-data-audit.ipynb`. It was not selected from any association with the outcome.

| Variable | Domain | Why it is included |
|---|---|---|
| `PHQCAT_A` | Psychological | Depressive symptoms, a core biopsychosocial domain in chronic pain |
| `GADCAT_A` | Psychological | Anxiety symptoms. Correlated with the above (Spearman rho = 0.65) but a distinct construct, and neither is a proxy for the other |
| `WPHSLEEP_A` | Sleep | Sleep quality, a distinct biopsychosocial domain with no evidence of problematic redundancy with the rest of the set |
| `WPHSTRESS_A` | Stress and coping | Perceived ability to manage stress |
| `SUPPORT_A` | Social | Dunn et al. (2024) report weaker support networks with moderate certainty of evidence |
| `EDUCP_A` | Socioeconomic | Dunn et al. report lower socioeconomic status with moderate certainty of evidence |
| `SMKCIGST_A` | Behavioural | Dunn et al. report smoking with moderate certainty of evidence |
| `ARTHEV_A` | Comorbidity | The only biological candidate, and the one least correlated with every other variable in the set |


**Why education and not the income-to-poverty ratio.** Both were audited and they measure the same socioeconomic dimension (Spearman rho = 0.43), so only one is kept. 

**Education** is preferred for two reasons:
- First, *income can be a consequence of the outcome*: an adult who stopped working because of pain has a lower income-to-poverty ratio because of the pain, which is the same reverse-causality concern that excludes the activity-limitation variables from every model here. *Educational attainment is generally less immediately affected by current pain status than current income, reducing the reverse-causality concern*. 
- Second, `POVRATTC_A` is derived from imputed family income, and NCHS distributes only the first of ten imputations, so *it would be the only socioeconomic indicator in the model built on an estimated value*.


**Candidates audited and not kept**:
- `LONELY_A` measures the same social domain as `SUPPORT_A` (Spearman rho = -0.40) and it is the availability of support, not loneliness, that Dunn et al. (2024) name among their moderate-certainty factors.
- `PAYWORRY_A` measures perceived healthcare-related financial strain rather than socioeconomic position or an observed barrier to care. It was therefore not retained in Model B or RQ3.
- `PHSTAT_A`, self-rated general health, is reported by Dunn et al. (2024) at low certainty of evidence. Independently of that, in a cross-sectional design a broad self-rating of health may partly reflect the consequences of high-impact chronic pain rather than characteristics that precede it, which is the same concern that excludes the activity-limitation variables here.


**Limit of the literature used.** Dunn et al. (2024) is an umbrella review of 13
systematic reviews whose outcome is the development of chronic musculoskeletal pain, not high impact within adults who already have chronic pain. It supports the biopsychosocial plausibility of a variable, not its association with HICP.
*Fear avoidance, one of its five moderate-certainty factors, is not measured in the NHIS and cannot be included*.


The three models are compared on the same performance metrics. Model 0 against Model A answers whether pain intensity on its own is enough. Model A against Model B answers whether biopsychosocial information adds anything to what a consultation already captures.

**Why there is a baseline between Model 0 and Model B.** A single-variable model performs poorly almost by construction, so beating Model 0 would prove little on its own. Age, sex and pain location are asked in any consultation, so a fair comparison for the biopsychosocial layer includes them. Model 0 answers the question as it is posed in RQ1; Model A is what Model B has to beat.

**Deliberately excluded from all three models:**

- **Activity-limitation variables** (`DISAB3_A`, `SOCWRKLIM_A`, `SOCSCLPAR_A`, `SOCERRNDS_A`, `EMPDYSMSS3_A`, `PAIAFFM3M_A`). High-impact chronic pain is defined by pain limiting life or work activities, so these variables restate the outcome. A model built on them would perform well and demonstrate nothing.

- **Pain-management strategies** (`PAIPHYSTPY_A`, `PAIOPIOID_A` and the others). The direction of the relationship between treatment and impact cannot be established from a single interview. Someone may report physiotherapy because their pain got worse, or may be functioning better because they have been doing it. Both are plausible, particularly for the non-pharmacological strategies, and cross-sectional data cannot separate them. Including these variables as predictors would produce associations of unknown direction. They are instead the subject of RQ2 and RQ3, where they are the outcome rather than the input.

**Interpretation limit.** NHIS is cross-sectional: one interview, one moment. Results describe what is associated with high-impact chronic pain and what helps distinguish the two groups. They do not identify who will develop it.

## 7. Analysis plan (RQ2 and RQ3)

**RQ2** is answered with a single table: the proportion of adults with HICP reporting each of the 11 strategies, with the number of valid responses shown next to every percentage. The strategies are not mutually exclusive, so respondents are also grouped by whether they report pharmacological approaches only, non-pharmacological only, both, or neither.

**RQ3** compares those reported rates across income-to-poverty ratio, education, region, delayed care because of cost, and needed care but did not receive it because of cost.

**How one strategy is selected for closer analysis.** RQ2 describes all 11 pain-management strategies. Only one of them is then analysed in more detail, and it is selected on criteria set before the results are seen:

1. **Enough people.** No subgroup compared may contain fewer than 50 respondents.
2. **Enough variation.** Reported use must differ meaningfully across the socioeconomic or access characteristics defined above. A strategy used at a similar rate by everyone has nothing to explain.

If no strategy meets both, none is analysed in depth, and that is reported as the result.

Any pattern that emerged from the description rather than from a prior expectation is reported as exploratory.

---

*Full references in `references/sources.md`.*
