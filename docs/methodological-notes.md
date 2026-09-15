# Why a population-level perspective is appropriate

High-impact chronic pain was developed within a population-research framework, not only as an individual clinical label. The US National Pain Strategy identified population-research objectives that include:
- estimating the prevalence of chronic pain and high-impact chronic pain, 
- studying patterns of pain treatment and healthcare use,
- developing measures that can track changes in pain impact, treatment and costs over time. 

The purpose of this population-level work is to support evaluation of interventions, policy and emerging needs (Von Korff et al., 2016).

This is also consistent with the way NHIS data are currently used. The National Center for Health Statistics uses NHIS to estimate chronic pain and HICP in the US population and to examine how prevalence differs across demographic and geographic groups (Lucas & Sohi, 2024). Earlier NHIS work also used these data
to estimate chronic pain and HICP prevalence and identify differences across
population subgroups (Dahlhamer et al., 2018).

Therefore, using health-system planners and payers as the main stakeholders is consistent with the population-health origins and current surveillance use of HICP. The model is not intended to diagnose an individual patient or directly determine treatment allocation. **Instead, it tests which information improves the identification and characterization of the high-impact subgroup within the chronic-pain population.**




## Transferability beyond the US

**The analytical framework may be transferable to other countries, but the fitted model itself should not be assumed to generalize internationally without external validation or recalibration.**

Prediction models can perform differently when applied to new populations or settings because of differences in case mix, predictor distributions, healthcare provision, baseline risk and even how predictors or outcomes are measured. External validation is therefore needed to assess whether a model remains transportable outside the population in which it was developed, and recalibration or model updating may be required before use in a new setting (Riley et al., 2024; Collins et al., 2024).

For this project, this means that the **analytical approach** could be replicated using comparable population data in another country, but the fitted US model should not be assumed to perform equally well elsewhere without validation.



# Why threshold analysis is methodologically relevant

**Prediction performance and decision usefulness are not the same thing.** Measures such as ROC-AUC, sensitivity and specificity describe different aspects of model performance, but they do not by themselves determine the consequences of using a prediction model for a decision. 

Decision Curve Analysis was developed specifically to incorporate the consequences of true and false-positive classifications across different probability thresholds (Vickers & Elkin, 2006).

More recent methodological guidance makes the same point: 
-> **the choice of a classification threshold depends on the setting, the consequences of false positive and false negative decisions, available resources and the intended use of the model**. 

-> Lower thresholds generally identify more true positives, but at the cost of accepting more false positives. 

Importantly, decision-curve analysis cannot determine which threshold *should* be chosen; the relevant threshold depends on the decision context (Efthimiou et al., 2024).

**There is therefore no universally "correct" classification threshold.**
The conventional 0.50 cutoff used by a binary classifier is not automatically
the most appropriate threshold for a particular application.



## So: What the threshold actually means in this project

Model B has the best overall discrimination, with a ROC-AUC of 0.761. However, at the conventional 0.50 classification threshold, sensitivity remains limited and the model favours specificity over sensitivity.

Lowering the probability threshold would classify more respondents as HICP and therefore identify a larger share of the actual HICP population, but it would also incorrectly include more non-HICP respondents.

From a population-planning perspective, these two errors have different implications:

- **False negatives** can lead to under-identification of the population carrying high impact.
- **False positives** can broaden that population beyond those who actually meet the HICP definition and reduce the precision of population stratification.

There is no threshold that performs best on everything. If planners want to avoid under-identifying the HICP population, they would need to accept more false positives. If they want a more specific classification, they will inevitably miss more true HICP cases.

**Which balance is preferable cannot be determined from model performance alone. It depends on how planners intend to use the information and on the relative consequences of under- versus over-identifying the high-impact population.**
