# AnesthesiaAI - PubMed Latest Papers

**Update Time**: 2026-10-15
**Search Range**: Last 30 days
**Papers Found**: 10

---

## 1. A real-time machine learning framework for improved intraoperative risk predictions in cardiac surgery patients.

- **PMID**: [42784706](https://pubmed.ncbi.nlm.nih.gov/42784706/)
- **Journal**: Journal of the American Medical Informatics Association : JAMIA
- **Publication Date**: 2026 Sep 24
- **Authors**: Zhu Daoyi, Xue Bing, Lu Chenyang, Abraham Joanna
- **DOI**: https://doi.org/10.1093/jamia/ocag142

### Abstract

**BACKGROUND AND OBJECTIVE**: Cardiac surgeries are associated with a range of serious postoperative complications, and current predictive models often rely on static summaries of preoperative and intraoperative data compiled after the case. Such development limits their utility in real-time clinical settings. To address this challenge, we developed TE-Transformer, an end-to-end deep learning framework that continuously ingests heterogeneous electronic health record (EHR) data-including preoperative variables, high-frequency vital signs, medication administration records, and brief surgical notes texts-to provide real-time, multitask predictions of multiple postoperative complications. **METHODS**: A retrospective cohort of 6416 patients undergoing cardiac surgery was used to develop and evaluate TE-Transformer. The architecture reduced reliance on manually engineered temporal summary features by encoding irregular intraoperative observations as event-level representations. Continuous risk estimates were updated at 30-minute intervals, enabling a dynamic perspective on patient status. Performance was benchmarked against traditional machine learning models (eg, XGBoost, Random Forest) and deep learning comparators (LSTM, GRU, CNN) frequently used in sequential modelling. **RESULTS**: We analyzed 6416 cardiac surgeries (61% male; median [IQR] age 62 [53-70]). Across classification tasks, TE-Transformer achieved AUROC (area under the receiver operating characteristic curve)/AUPRC (area under the precision-recall curve) of 0.8461/0.3994 (mortality), 0.8837/0.8033 (delirium), and 0.7956/0.6666 (acute kidney injury). For continuous endpoints, mean absolute error (MAE) was 0.0633 (low SBP [systolic blood pressure] time), 0.0920 (N glucose high), 0.0020 (N glucose low), and 0.9781 (postoperative ventilation duration). Ablation study showed the full multimodal model improved performance over the preoperative-only baseline, most notably for 30-day mortality AUROC (+0.049), po

---

## 2. Artificial intelligence in predicting anesthetic complications: current techniques, clinical applications, and limitations.

- **PMID**: [42248065](https://pubmed.ncbi.nlm.nih.gov/42248065/)
- **Journal**: International journal of medical informatics
- **Publication Date**: 2026 Sep 15
- **Authors**: Mohammadi Ali
- **DOI**: https://doi.org/10.1016/j.ijmedinf.2026.106527

### Abstract

Artificial intelligence (AI) is revolutionizing anesthesiology by enhancing the prediction and management of perioperative complications, including intraoperative hypotension, respiratory failure, postoperative nausea and vomiting (PONV), and pain control challenges. This scoping review synthesizes evidence from 82 studies, identified through a systematic search of PubMed, Scopus, Web of Science, and grey literature from January 2010 to September 2025, to map AI techniques, their clinical applications, and limitations. Techniques include Machine Learning (ML) (e.g., random forests, support vector machines), deep learning, natural language processing (NLP), Computer Vision, Bayesian models, and fuzzy logic, applied across preoperative, intraoperative, and postoperative phases. AI models achieve superior predictive accuracy (AUC 0.85-0.94) compared to traditional methods (AUC 0.76-0.88), enabling early detection of complications and reducing opioid use by 15-35%. Applications include preoperative risk stratification, intraoperative monitoring, and postoperative analgesia optimization. Challenges include algorithmic bias, data reliability, interoperability, and real-time integration barriers. Ethical considerations emphasize transparency, equity, and clinician oversight. This review positions AI as a decision-support tool within the P4 medicine framework (Predictive, Preventive, Personalized, Participatory), advocating for validation, ethical frameworks, and integration with anesthesia information management systems (AIMS) to enhance perioperative safety.

---

## 3. Artificial Intelligence for Perioperative Risk Prediction in Anesthesiology: A Bibliometric and Knowledge-Mapping Analysis.

- **PMID**: [42736944](https://pubmed.ncbi.nlm.nih.gov/42736944/)
- **Journal**: Healthcare (Basel, Switzerland)
- **Publication Date**: 2026 Sep 01
- **Authors**: Özkılıç Mehmet
- **DOI**: https://doi.org/10.3390/healthcare14172785

### Abstract

Background: Artificial intelligence (AI) is increasingly being investigated in perioperative medicine for risk stratification, complication prediction, patient safety, and clinical decision support. This study characterized the research landscape, intellectual structure, and thematic evolution of AI-based perioperative risk prediction in anesthesiology. Methods: Publications indexed in the Web of Science Core Collection between 2018 and 3 June 2026 were analyzed using Bibliometrix and Biblioshiny. Scientific productivity, citations, collaboration networks, keyword co-occurrence, thematic evolution, and Reference Publication Year Spectroscopy were evaluated. Partial 2026 data were excluded from the compound annual growth-rate calculation. Results: A total of 152 publications were included. Scientific production increased substantially, with a compound annual growth rate of 77.72% between 2018 and 2025. The United States and China led publication output, while the United States had the highest total citation count. Citation and thematic analyses identified perioperative outcome prediction, predictive hemodynamic monitoring, and explainable AI as important components of the field's intellectual structure. Research attention increasingly shifted from methodological machine learning development toward clinically oriented topics, including mortality, postoperative complications, delirium, postoperative nausea and vomiting, and perioperative risk stratification. Emerging themes included explainable AI, large language models, natural language processing, and clinical decision-support systems. Conclusions: Research attention has increasingly shifted from exploratory model development toward clinically oriented risk-stratification and decision-support applications. Emerging directions emphasize interpretability, multimodal data integration, and individualized risk assessment. These bibliometric patterns reflect changes in research emphasis but do not demonstrate clinical adop

---

## 4. Artificial intelligence-assisted perioperative risk prediction, decision support, and supervised automation in anesthesia: A narrative review.

- **PMID**: [42806783](https://pubmed.ncbi.nlm.nih.gov/42806783/)
- **Journal**: The Journal of international medical research
- **Publication Date**: 2026 Sep
- **Authors**: An Ran, Meng Bingbing, Lu Xun
- **DOI**: https://doi.org/10.1177/03000605261491422

### Abstract

Artificial intelligence is increasingly being investigated as a tool for supporting personalized perioperative care. This narrative review, guided by the Scale for the Assessment of Narrative Review Articles principles, examines clinically relevant applications of artificial intelligence and related automation in anesthesiology, with emphasis on three linked functions: risk prediction, clinical decision support, and supervised automation. We performed a structured search of PubMed, Web of Science, and Scopus databases and identified English-language literature published from January 2010 through June 2026. We prioritized clinical studies, guidelines, systematic reviews, and representative methodological studies. A central distinction of this review is that machine-learning prediction, rule-based decision support, conventional feedback control, and genuinely adaptive artificial intelligence-enabled control are not treated as equivalent technologies. Current evidence is strongest for selected prediction tasks and supervised systems that improve process measures such as time within a physiological target range. However, evidence that these technologies improve patient-centered outcomes remains less consistent. Model discrimination alone is insufficient; calibration, actionable thresholds, false-positive burden, external validation, clinical utility, dataset shift, missing data, and workflow consequences must also be considered. The proposed three-level framework is intended to provide anesthesiologists and perioperative teams with a practical way to connect technical capability with bedside action. Near-term implementation should prioritize interpretable prediction and low-burden decision support, whereas closed-loop systems should remain under clinician supervision. Future studies should emphasize prospective multicenter validation, clinically meaningful endpoints, transparent reporting, and post-deployment monitoring rather than technical performance alone.

---

## 5. Empirical Comparison of Causal Machine Learning and Post-Hoc AI Interpretability Models for Risk Factor Analysis: An Application to Medical Specialty Choice.

- **PMID**: [42175322](https://pubmed.ncbi.nlm.nih.gov/42175322/)
- **Journal**: Studies in health technology and informatics
- **Publication Date**: 2026 May 21
- **Authors**: Vicente Alvarez David, Abbiati Milena, Bornet Alban, Savoldelli Georges, Bajwa Nadia et al.
- **DOI**: https://doi.org/10.3233/SHTI260654

### Abstract

How medical students choose specialties shapes access to care. Prior work mostly describes patterns; newer prediction tools can rank influential factors but may blur association with true drivers. Using a curated cohort of 399 students, we examined Year 4 motivations for a given specialty (six items, six levels) and personality traits (Big Five) in relation to Year 6 specialty career choice (person vs technically oriented). We estimated effects with Double/debiased machine learning (DoubleML) and contrasted them with SHAP explanations from an earlier predictive model. Strong motivation for surgery at level 6 lowered the probability of a person-oriented choice by 0.37 (p < .001); high motivation for general practice raised it by 0.265 (p < .001). Other motivation signals were smaller. Psychological traits showed no clear effects (p > 0.05). SHAP broadly matched directions for the strongest items but diverged for weaker ones (e.g., anesthesiology, radiology). Comparing causal and predictive explanations, SHAP directions generally matched DoubleML for strong, well-separated motivations (e.g., surgery level 6, general practice) but diverged for weaker or correlated signals (radiology, anesthesiology, emergency medicine, mid-level psychiatry) and for psychological traits. These discrepancies caution that SHAP values reflect model-conditional associations rather than causal effects, so predictive importance should not be interpreted as causal influence.

---

## 6. Guideline-Aligned Machine Learning for Predicting Ondansetron Administration at the End of Anaesthesia: Explainable Decision Support for PONV Prophylaxis.

- **PMID**: [42174910](https://pubmed.ncbi.nlm.nih.gov/42174910/)
- **Journal**: Studies in health technology and informatics
- **Publication Date**: 2026 May 21
- **Authors**: Strube Tom, Weltermann Leoni, Weber Jonas, Defosse Jérôme
- **DOI**: https://doi.org/10.3233/SHTI260235

### Abstract

Artificial Intelligence (AI) and Clinical Practice Guidelines (CPGs) both aim to support clinical decision-making but may provide conflicting suggestions. This manuscript presents a Guideline-Aligned Machine Learning (GAML) model to predict ondansetron administration at the end of anaesthesia, based on Gan et al.'s Fourth Consensus Guidelines for the Management of Postoperative Nausea and Vomiting (PONV). n= 16,240 anaesthesia protocols were analysed for risk factors and administered PONV prophylaxes. Logistic regression, multinomial naïve Bayes, and CatBoost classifiers were trained on 80% of protocols with 12-fold cross-validation; optimal thresholds were set by the mean F1-maximising cut-off across folds. Models were evaluated on the remaining 20%, achieving high accuracy (90 ± 1%) and moderate precision and recall (60 ± 5%, 75 ± 4%) across all models. A SHAP decision plot was further computed on the test set to visualise predictor contributions and illustrate a potential interactive preoperative planning interface. Overall, GAML is a promising basis for explainable decision support in clinical care.

---

## 7. Artificial Intelligence for American Society of Anesthesiologists Physical Status Classification: Agreement with Clinician Consensus and Temporal Stability Analysis.

- **PMID**: [42194832](https://pubmed.ncbi.nlm.nih.gov/42194832/)
- **Journal**: Journal of clinical medicine
- **Publication Date**: 2026 May 18
- **Authors**: Soerensen Anne Lykke, Froeslev-Friis Christina, Kjaergaard Andersen Gunhild, Bhavsar Swati, Quitzau Lisbeth Holmgaard et al.
- **DOI**: https://doi.org/10.3390/jcm15103871

### Abstract

Background: The American Society of Anesthesiologists Physical Status (ASA-PS) classification is widely used for perioperative communication and research with known variation in agreement amongst assessors. Large language models (LLM) are increasingly considered for uniform decision making due to agreement challenges within clinicians under identical inputs. The study compared four contemporary LLMs against clinician-derived consensus and quantified within-model stability across repeated assessments. Methods: In a cross-sectional vignette study, 228 anesthesiologists from Denmark, England, and India classified 20 standardized perioperative vignettes through online survey. The modal response per vignette was considered as clinician consensus. Four LLMs (ChatGPT-5.2 Plus, Gemini 3 Pro, Perplexity AI Pro, Claude 4 Sonnet) received same set of vignettes through identical prompts. Temporal stability was assessed by repeating each vignette query nine times per model (three-time windows across three nonconsecutive days) in fresh sessions. Primary outcome was exact agreement with clinician consensus. Results: Consensus agreement for modal LLM classifications was 18/20 (90%) for ChatGPT, 17/20 (85%) for Gemini, 17/20 (85%) for Claude, and 15/20 (75%) for Perplexity. Disagreement is clustered in vignettes with weak or split clinician consensus. Stability differed by model: Claude was fully stable across all vignettes (20/20), Gemini 19/20, ChatGPT 18/20, and Perplexity 14/20; instability typically involved adjacent-class shifts. Conclusions: Contemporary LLMs often match clinician modal judgement and are largely temporally stable, with discordance concentrated in clinically ambiguous boundary cases.

---

## 8. Transforming perioperative care: The current landscape and future trajectory of artificial intelligence in anesthesia-A narrative review.

- **PMID**: [42297385](https://pubmed.ncbi.nlm.nih.gov/42297385/)
- **Journal**: The Journal of international medical research
- **Publication Date**: 2026 Jun
- **Authors**: Zhang Pan, Wu Ling, Liao Yunxi, Li Hong
- **DOI**: https://doi.org/10.1177/03000605261454051

### Abstract

This narrative review examined how artificial intelligence is increasingly being applied in anesthesiology to support clinical decision-making across the perioperative period. It outlines current applications of artificial intelligence in preoperative risk assessment, intraoperative monitoring and automation, and postoperative complication prediction. We also examined the underlying artificial intelligence architectures that form the technical foundations of these tools, including machine learning, deep learning, and natural language processing. We propose that in the future, rather than narrow task-specific tools, artificial intelligence in anesthesiology should involve the development and clinical translation of large, generalizable foundation models capable of integrating multimodal perioperative data. In addition, developments in multimodal data integration, closed-loop control systems, and interpretable modeling may further refine these approaches. Further progress in artificial intelligence-driven anesthesiology may require multidisciplinary collaboration, prospective clinical validation, and careful integration into perioperative workflows to ensure safe and clinically meaningful adoption.

---

## 9. Computational Anesthesiology: A New Frontier at the Intersection of Data Science and Perioperative Medicine.

- **PMID**: [42852158](https://pubmed.ncbi.nlm.nih.gov/42852158/)
- **Journal**: Anesthesiology and pain medicine
- **Publication Date**: 2026 Apr 30
- **Authors**: Madadi Firoozeh
- **DOI**: https://doi.org/10.5812/aapm-175132

---

## 10. Explainable artificial intelligence in anesthesiology prediction models: bridging the gap from black-box algorithms to clinical decision support.

- **PMID**: [42694685](https://pubmed.ncbi.nlm.nih.gov/42694685/)
- **Journal**: Frontiers in medicine
- **Publication Date**: 2026
- **Authors**: Wang Yan, Song Zuoyan, Wang Hang
- **DOI**: https://doi.org/10.3389/fmed.2026.1928394

### Abstract

Machine learning prediction models consistently outperform conventional clinical scoring tools across perioperative outcomes, yet remain largely unadopted at the bedside. This narrative review examines explainable artificial intelligence (XAI) as a bridge between algorithmic performance and clinical translation, drawing on a targeted search of PubMed and Embase (January 2018 to March 2026). Five prediction domains are synthesized: perioperative hypotension, postoperative complications, difficult airway management, depth-of-anesthesia monitoring, and regional anesthesia and pain management. SHAP (SHapley Additive exPlanations) has emerged as the dominant XAI method, identifying modifiable intraoperative targets. Attention mechanisms and GradCAM provide complementary interpretability for time-series and imaging-based models. Critical gaps persist: most delirium prediction models include no XAI analysis; no standardized evaluation framework exists, and no prospective trial has demonstrated that XAI-enhanced recommendations improve patient outcomes. Addressing these gaps is a research priority if XAI is to fulfill its potential as a facilitator of perioperative AI adoption.

---
