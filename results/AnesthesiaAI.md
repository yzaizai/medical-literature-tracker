# AnesthesiaAI - PubMed Latest Papers

**Update Time**: 2026-09-07
**Search Range**: Last 30 days
**Papers Found**: 20

---

## 1. Artificial intelligence in predicting anesthetic complications: current techniques, clinical applications, and limitations.

- **PMID**: [42248065](https://pubmed.ncbi.nlm.nih.gov/42248065/)
- **Journal**: International journal of medical informatics
- **Publication Date**: 2026 Sep 15
- **Authors**: Mohammadi Ali
- **DOI**: https://doi.org/10.1016/j.ijmedinf.2026.106527

### Abstract

Artificial intelligence (AI) is revolutionizing anesthesiology by enhancing the prediction and management of perioperative complications, including intraoperative hypotension, respiratory failure, postoperative nausea and vomiting (PONV), and pain control challenges. This scoping review synthesizes evidence from 82 studies, identified through a systematic search of PubMed, Scopus, Web of Science, and grey literature from January 2010 to September 2025, to map AI techniques, their clinical applications, and limitations. Techniques include Machine Learning (ML) (e.g., random forests, support vector machines), deep learning, natural language processing (NLP), Computer Vision, Bayesian models, and fuzzy logic, applied across preoperative, intraoperative, and postoperative phases. AI models achieve superior predictive accuracy (AUC 0.85-0.94) compared to traditional methods (AUC 0.76-0.88), enabling early detection of complications and reducing opioid use by 15-35%. Applications include preoperative risk stratification, intraoperative monitoring, and postoperative analgesia optimization. Challenges include algorithmic bias, data reliability, interoperability, and real-time integration barriers. Ethical considerations emphasize transparency, equity, and clinician oversight. This review positions AI as a decision-support tool within the P4 medicine framework (Predictive, Preventive, Personalized, Participatory), advocating for validation, ethical frameworks, and integration with anesthesia information management systems (AIMS) to enhance perioperative safety.

---

## 2. Empirical Comparison of Causal Machine Learning and Post-Hoc AI Interpretability Models for Risk Factor Analysis: An Application to Medical Specialty Choice.

- **PMID**: [42175322](https://pubmed.ncbi.nlm.nih.gov/42175322/)
- **Journal**: Studies in health technology and informatics
- **Publication Date**: 2026 May 21
- **Authors**: Vicente Alvarez David, Abbiati Milena, Bornet Alban, Savoldelli Georges, Bajwa Nadia et al.
- **DOI**: https://doi.org/10.3233/SHTI260654

### Abstract

How medical students choose specialties shapes access to care. Prior work mostly describes patterns; newer prediction tools can rank influential factors but may blur association with true drivers. Using a curated cohort of 399 students, we examined Year 4 motivations for a given specialty (six items, six levels) and personality traits (Big Five) in relation to Year 6 specialty career choice (person vs technically oriented). We estimated effects with Double/debiased machine learning (DoubleML) and contrasted them with SHAP explanations from an earlier predictive model. Strong motivation for surgery at level 6 lowered the probability of a person-oriented choice by 0.37 (p < .001); high motivation for general practice raised it by 0.265 (p < .001). Other motivation signals were smaller. Psychological traits showed no clear effects (p > 0.05). SHAP broadly matched directions for the strongest items but diverged for weaker ones (e.g., anesthesiology, radiology). Comparing causal and predictive explanations, SHAP directions generally matched DoubleML for strong, well-separated motivations (e.g., surgery level 6, general practice) but diverged for weaker or correlated signals (radiology, anesthesiology, emergency medicine, mid-level psychiatry) and for psychological traits. These discrepancies caution that SHAP values reflect model-conditional associations rather than causal effects, so predictive importance should not be interpreted as causal influence.

---

## 3. Guideline-Aligned Machine Learning for Predicting Ondansetron Administration at the End of Anaesthesia: Explainable Decision Support for PONV Prophylaxis.

- **PMID**: [42174910](https://pubmed.ncbi.nlm.nih.gov/42174910/)
- **Journal**: Studies in health technology and informatics
- **Publication Date**: 2026 May 21
- **Authors**: Strube Tom, Weltermann Leoni, Weber Jonas, Defosse Jérôme
- **DOI**: https://doi.org/10.3233/SHTI260235

### Abstract

Artificial Intelligence (AI) and Clinical Practice Guidelines (CPGs) both aim to support clinical decision-making but may provide conflicting suggestions. This manuscript presents a Guideline-Aligned Machine Learning (GAML) model to predict ondansetron administration at the end of anaesthesia, based on Gan et al.'s Fourth Consensus Guidelines for the Management of Postoperative Nausea and Vomiting (PONV). n= 16,240 anaesthesia protocols were analysed for risk factors and administered PONV prophylaxes. Logistic regression, multinomial naïve Bayes, and CatBoost classifiers were trained on 80% of protocols with 12-fold cross-validation; optimal thresholds were set by the mean F1-maximising cut-off across folds. Models were evaluated on the remaining 20%, achieving high accuracy (90 ± 1%) and moderate precision and recall (60 ± 5%, 75 ± 4%) across all models. A SHAP decision plot was further computed on the test set to visualise predictor contributions and illustrate a potential interactive preoperative planning interface. Overall, GAML is a promising basis for explainable decision support in clinical care.

---

## 4. Artificial Intelligence for American Society of Anesthesiologists Physical Status Classification: Agreement with Clinician Consensus and Temporal Stability Analysis.

- **PMID**: [42194832](https://pubmed.ncbi.nlm.nih.gov/42194832/)
- **Journal**: Journal of clinical medicine
- **Publication Date**: 2026 May 18
- **Authors**: Soerensen Anne Lykke, Froeslev-Friis Christina, Kjaergaard Andersen Gunhild, Bhavsar Swati, Quitzau Lisbeth Holmgaard et al.
- **DOI**: https://doi.org/10.3390/jcm15103871

### Abstract

Background: The American Society of Anesthesiologists Physical Status (ASA-PS) classification is widely used for perioperative communication and research with known variation in agreement amongst assessors. Large language models (LLM) are increasingly considered for uniform decision making due to agreement challenges within clinicians under identical inputs. The study compared four contemporary LLMs against clinician-derived consensus and quantified within-model stability across repeated assessments. Methods: In a cross-sectional vignette study, 228 anesthesiologists from Denmark, England, and India classified 20 standardized perioperative vignettes through online survey. The modal response per vignette was considered as clinician consensus. Four LLMs (ChatGPT-5.2 Plus, Gemini 3 Pro, Perplexity AI Pro, Claude 4 Sonnet) received same set of vignettes through identical prompts. Temporal stability was assessed by repeating each vignette query nine times per model (three-time windows across three nonconsecutive days) in fresh sessions. Primary outcome was exact agreement with clinician consensus. Results: Consensus agreement for modal LLM classifications was 18/20 (90%) for ChatGPT, 17/20 (85%) for Gemini, 17/20 (85%) for Claude, and 15/20 (75%) for Perplexity. Disagreement is clustered in vignettes with weak or split clinician consensus. Stability differed by model: Claude was fully stable across all vignettes (20/20), Gemini 19/20, ChatGPT 18/20, and Perplexity 14/20; instability typically involved adjacent-class shifts. Conclusions: Contemporary LLMs often match clinician modal judgement and are largely temporally stable, with discordance concentrated in clinically ambiguous boundary cases.

---

## 5. Evaluating the Effectiveness of Chatbot-Based Patient Education Compared to Traditional Patient Information Leaflets Related to Pediatric Anesthesia: A Pilot Cross-Sectional Study.

- **PMID**: [42255859](https://pubmed.ncbi.nlm.nih.gov/42255859/)
- **Journal**: Cureus
- **Publication Date**: 2026 May
- **Authors**: Ambi Uday, Gajanan Kamath Mahima, Jossie Sneha, Soomar Salman M
- **DOI**: https://doi.org/10.7759/cureus.108426

### Abstract

Background Clear, accurate, and empathetic communication is essential in pediatric anesthesia, where parental anxiety and information needs are high. Traditional patient information leaflets (PILs), while clinically robust, may lack emotional engagement. Large language model (LLM)-based chatbots, such as ChatGPT and Google Gemini, offer a novel, interactive approach to patient education, yet their role in pediatric anesthesia remains inadequately explored. Objective To evaluate and compare the readability, accuracy, completeness, sentiment, and parental satisfaction of artificial intelligence (AI)-generated patient education materials (ChatGPT and Google Gemini) with a clinician-authored departmental PIL (DPIL) for pediatric general anesthesia.  Methods This pilot cross-sectional study evaluated responses generated by ChatGPT and Google Gemini to seven frequently asked questions derived from the departmental PIL. Three blinded leaflets were presented in randomized order using a computer-generated sequence and evaluated by 10 anesthetists for accuracy and completeness using 10-point Likert scales. Readability was assessed using Flesch Reading Ease and Flesch-Kincaid Grade Level scores. Sentiment analysis and parental satisfaction were also assessed. Both descriptive and inferential statistical analyses were performed.  Results The DPIL demonstrated the highest readability, followed by ChatGPT, with Gemini scoring the lowest. All materials exceeded the recommended sixth-grade readability level. No significant differences were observed in accuracy or completeness among the three sources (p > 0.05). Parents consistently perceived ChatGPT responses as more reassuring and relatable, while the DPIL was viewed as informative but formal. Gemini responses were often considered linguistically complex. ChatGPT demonstrated a neutral and more empathetic sentiment compared with the other leaflets. Conclusion Clinician-authored PILS remain the most reliable source of pediatric ane

---

## 6. Evaluation of Five Large Language Models for Parental Education in Pediatric Anesthesia: Reliability and Readability Study.

- **PMID**: [42314147](https://pubmed.ncbi.nlm.nih.gov/42314147/)
- **Journal**: JMIR medical informatics
- **Publication Date**: 2026 Jun 18
- **Authors**: Pu Fulin, Hong Jishuang, Wei Xiaoying, Chen Yanling
- **DOI**: https://doi.org/10.2196/93054

### Abstract

**BACKGROUND**: Although large language models (LLMs) show potential for patient education, their accuracy, usability, and comprehensibility lack validation in high-risk pediatric anesthesia. Rigorous evaluation is therefore essential prior to widespread clinical use in perioperative parental anesthesia education. **OBJECTIVE**: This study aims to evaluate the accuracy, reliability, and readability of responses generated by 5 LLMs to parental inquiries regarding pediatric anesthesia, and to assess their suitability for clinical use in perioperative caregiver education. **METHODS**: Two expert anesthesiologists identified 33 parental questions on pediatric anesthesia by screening authoritative resources and Google Trends. On December 14, 2025, these questions were submitted to 5 LLMs (DeepSeek-V3.2, ChatGPT-5, Gemini 2.5 Flash, Copilot, and Perplexity) via official web interfaces with default settings and zero-shot prompting, with each query in a separate conversation. Responses were standardized for blinded assessment. Two pediatric anesthesiologists with ≥10 years of clinical experience independently evaluated accuracy and reliability using the 4-point Likert accuracy scale, DISCERN, Ensuring Quality Information for Patients (EQIP), Journal of the American Medical Association (JAMA) benchmark, and Global Quality Score (GQS). After text preprocessing, readability was evaluated using 6 algorithms (Automated Readability Index [ARI], Flesch Reading Ease Score [FRES], Gunning Fog Index [GFI], Flesch-Kincaid Grade Level [FKGL], Coleman-Liau Index [CL], and the Simple Measure of Gobbledygook [SMOG]) via an online calculator. Interrater reliability was analyzed using the intraclass correlation coefficient (ICC); differences across models were assessed with the Kruskal-Wallis H test; and deviations from the sixth-grade benchmark were evaluated using 1-sample Wilcoxon signed-rank tests (P<.05 considered significant). **RESULTS**: All 5 LLMs demonstrated high clinical accurac

---

## 7. Transforming perioperative care: The current landscape and future trajectory of artificial intelligence in anesthesia-A narrative review.

- **PMID**: [42297385](https://pubmed.ncbi.nlm.nih.gov/42297385/)
- **Journal**: The Journal of international medical research
- **Publication Date**: 2026 Jun
- **Authors**: Zhang Pan, Wu Ling, Liao Yunxi, Li Hong
- **DOI**: https://doi.org/10.1177/03000605261454051

### Abstract

This narrative review examined how artificial intelligence is increasingly being applied in anesthesiology to support clinical decision-making across the perioperative period. It outlines current applications of artificial intelligence in preoperative risk assessment, intraoperative monitoring and automation, and postoperative complication prediction. We also examined the underlying artificial intelligence architectures that form the technical foundations of these tools, including machine learning, deep learning, and natural language processing. We propose that in the future, rather than narrow task-specific tools, artificial intelligence in anesthesiology should involve the development and clinical translation of large, generalizable foundation models capable of integrating multimodal perioperative data. In addition, developments in multimodal data integration, closed-loop control systems, and interpretable modeling may further refine these approaches. Further progress in artificial intelligence-driven anesthesiology may require multidisciplinary collaboration, prospective clinical validation, and careful integration into perioperative workflows to ensure safe and clinically meaningful adoption.

---

## 8. Prediction of Postoperative Vomiting Within 24 Hours Using Machine Learning With Large Language Model-Enhanced Interpretability: Development and Validation Study.

- **PMID**: [42536998](https://pubmed.ncbi.nlm.nih.gov/42536998/)
- **Journal**: JMIR medical informatics
- **Publication Date**: 2026 Jul 31
- **Authors**: Wang Huan-Jun, Lee Wei-Po, Gau Tz-Ping, Cheng Kuang-I, Wei Cheng-Ru
- **DOI**: https://doi.org/10.2196/84260

### Abstract

**BACKGROUND**: Postoperative nausea and vomiting are common complications after anesthesia. However, vomiting represents a clinically distinct and objectively measurable endpoint. **OBJECTIVE**: This study aimed to develop and internally validate predictive models for postoperative vomiting within 24 hours using structured perioperative data and unstructured clinical text, while introducing a structured framework that separates feature construction from interpretability using large language models (LLMs). **METHODS**: We analyzed 33,460 anesthesia records from a single center (2019-2022). Two temporally defined prediction tasks were constructed to reflect real-world clinical decision-making and prevent information leakage: a preoperative model using variables available before anesthesia induction, and a perioperative model using variables available up to the end of surgery. Structured data were modeled using machine learning algorithms (logistic regression, Extreme Gradient Boosting, Light Gradient Boosting Machine [LightGBM]). Unstructured clinical text was incorporated through a deterministic, concept-driven preprocessing pipeline, where LLMs were used solely for normalization (temperature=0) without feature generation, followed by rule-based concept mapping and feature encoding. Post hoc interpretability was further supported using an LLM-based Question Answering Chain module. Model performance was evaluated using receiver operating characteristic-area under the curve (AUC), precision-recall AUC, calibration metrics, and threshold-based operating characteristics. Classification thresholds were selected using the Youden J statistic, and all metrics were reported with 95% CIs derived from bootstrap resampling. Decision curve analysis was performed to assess clinical utility. **RESULTS**: A total of 33,460 surgical procedures were included, of which 3607 (10.8%) experienced postoperative vomiting within 24 hours. In the preoperative task, LightGBM achieved an AUC o

---

## 9. Simulator development using natural language: clinician-led innovation through artificial intelligence.

- **PMID**: [42458589](https://pubmed.ncbi.nlm.nih.gov/42458589/)
- **Journal**: Advances in simulation (London, England)
- **Publication Date**: 2026 Jul 15
- **Authors**: Barra Federico Lorenzo, Ricci Serena, Moro Edoardo, Travěnec Jiří, Costa Alessandro et al.
- **DOI**: https://doi.org/10.1186/s41077-026-00467-2

### Abstract

**BACKGROUND**: Healthcare simulation training faces significant barriers due to the "clinician-developer gap," where educators lack programming expertise to create customized digital simulators. Natural Language-Driven Development (NLDD) is an emerging paradigm that enables clinicians to develop educational technology through conversational artificial intelligence interfaces. **METHODS**: We implemented NLDD methodology to develop Open Vent Sim, a comprehensive mechanical ventilation simulator designed to replace anesthesia machines and ventilators in educational contexts lacking dedicated equipment. A multidisciplinary team comprising anesthesiologists, residents, a research nurse, IT, and biomedical engineers collaborated using Google AI Studio to iteratively create a web-based application through natural language prompts. Development proceeded through conversational cycles in which clinical requirements were translated into functional code via large language model assistance. **RESULTS**: Open Vent Sim was successfully developed in about 40 h over two weeks, featuring three simulation environments: anesthesia workstation, ICU ventilator, and high-flow oxygenation systems. The simulator incorporates physiological patient profiles (normal, ARDS, COPD) with dynamic compliance calculations and realistic waveform generation. Clinical validation was achieved through the integration of continuous resident feedback during iterative development. The application was successfully implemented in SimZone 1 as an interactive skill trainer and in SimZone 2 for team-based clinical scenarios during formal anesthesia and critical care education. Significant technical adaptation was required to transform the AI-generated prototype into a production-ready application. **CONCLUSIONS**: NLDD demonstrates the potential to democratize the creation of educational technology by empowering clinical domain experts to develop sophisticated simulation tools without traditional programming ex

---

## 10. A large language models-assisted and expert-corrected workflow for preoperative anesthesia assessment drafts: A single-centre exploratory feasibility study.

- **PMID**: [42628268](https://pubmed.ncbi.nlm.nih.gov/42628268/)
- **Journal**: Medicina clinica
- **Publication Date**: 2026 Aug 21
- **Authors**: Gu Shuhan, Ping Jianfan, Lin Huidan, Xu Hui, Fang Fuquan et al.
- **DOI**: https://doi.org/10.1016/j.medcli.2026.107571

### Abstract

**BACKGROUND**: Large language models (LLMs) may help organize clinical information, but their use in perioperative settings requires careful evaluation because errors may have immediate safety implications. This study aimed to describe the feasibility and perceived usefulness of a single-centre, expert-corrected LLM workflow for preparing preoperative anesthesia assessment drafts for complex consultation cases. Secondary aims were to describe error patterns identified by anesthesiologists and to explore residents' perceptions after reviewing expert-corrected materials. **METHODS**: We retrospectively selected 15 complex preoperative anesthesia consultation cases from The First Affiliated Hospital, Zhejiang University School of Medicine. Complex cases were defined as cases referred for specialized preoperative anesthesia consultation because of multiple comorbidities, clinically relevant organ dysfunction, implanted devices, major cardiopulmonary or vascular disease, or other features requiring individualized anesthetic assessment. A large language model-based artificial intelligence system, DeepSeek-R1, was used to generate structured draft assessments from de-identified case information and a standardized prompt. The original LLM-generated drafts were independently reviewed by three experienced anesthesiologists for information completeness, scientific plausibility, and focus on key risk factors. All resident-facing documents were then corrected by senior anesthesiologists before being distributed to first-year anesthesia residents, who completed a questionnaire on perceived usefulness, guidance value, educational support, and error recognition. No comparator group, blinding, or objective performance outcome was included. **RESULTS**: The LLM-generated drafts were structurally complete but contained clinically relevant errors, mainly in risk assessment and anesthetic plan formulation. Thirty-two error instances were identified across the 15 cases, including errors

---

## 11. From prediction to practice: closing the translation gap in artificial intelligence for anesthesia.

- **PMID**: [42018224](https://pubmed.ncbi.nlm.nih.gov/42018224/)
- **Journal**: Journal of clinical monitoring and computing
- **Publication Date**: 2026 Aug
- **Authors**: Baliga Janardhan, Seshadri Niranjan
- **DOI**: https://doi.org/10.1007/s10877-026-01434-y

### Abstract

Artificial intelligence (AI) and machine learning (ML) techniques are rapidly advancing in anesthesiology, showing promise in patient monitoring, outcome prediction, clinical decision support, and automated drug delivery. However, a substantial gap remains between algorithmic capability and practical implementation at the bedside. This narrative review examines the current state of AI/ML applications in anesthesia, including predictive analytics, closed-loop control systems, AI-assisted imaging, workflow optimization, and anesthesia planning, and explores the translational barriers that have limited routine clinical adoption. We discuss technical, organizational, regulatory, and cultural challenges impeding translation, including data quality issues, EHR interoperability constraints, lack of outcome-oriented clinical evidence, business model uncertainty, interpretability concerns, alarm fatigue, and regulatory ambiguity. Strategies to close this gap are proposed, including rigorous prospective validation, interdisciplinary collaboration with industry and payers, post-deployment model surveillance, training data transparency, user-centered design, and implementation science principles. Ethical and legal considerations, encompassing algorithmic bias, accountability for autonomous AI recommendations, privacy beyond de-identification, and equitable access, are also reviewed. A conceptual framework, summary table of applications, and practical implementation checklist are provided. Bridging the translational divide is essential for AI to fulfill its potential in improving anesthesia care, and will require coordinated action from clinicians, researchers, technologists, regulators, and healthcare institutions.

---

## 12. Safety in the Age of Artificial Intelligence: Evaluating Large Language Model Adherence to Antithrombotic Medication and Regional Anesthesia Guidelines.

- **PMID**: [42614371](https://pubmed.ncbi.nlm.nih.gov/42614371/)
- **Journal**: Cureus
- **Publication Date**: 2026 Aug
- **Authors**: Willson Conner M, Thind Birpartap S, Srinivas Jay, Gupta Anita
- **DOI**: https://doi.org/10.7759/cureus.114071

### Abstract

The release of the 2025 American Society of Regional Anesthesia (ASRA) 5th edition guidelines for regional and neuraxial anesthesia procedures for patients receiving antithrombotic medications introduced complex, patient-specific hold times and resumption protocols. As clinicians increasingly utilize large language models (LLMs) as clinical decision support tools, the reliability of these models remains largely unvalidated. This study evaluates the accuracy of two of the foremost LLMs, ChatGPT (OpenAI, San Francisco, CA) and Google Gemini (Google DeepMind, London, UK), in adhering to these new gold-standard safety guidelines. Twenty-five standardized clinical vignettes were developed. Each vignette featured a patient on a specific anticoagulant (e.g., rivaroxaban, apixaban, dabigatran) requiring a neuraxial or regional anesthetic procedure (stratified by high-risk vs. low-risk). Variables included renal function, dose frequency, and procedural urgency. Prompts were submitted to the latest publicly available ChatGPT and Google Gemini models with separate instructions to provide hold and resumption times. LLMs were queried to ensure familiarity with 2025 ASRA guidelines prior to submission of prompts. Responses were graded against the 2025 ASRA guidelines by independent reviewers. Response adherence was categorized as: 1. concordant (100% match); 2. conservative error (LLM recommended time was longer than required); 3. dangerous error (recommended time was shorter than required, a critical safety violation); or 4. omission (no specific timeframe provided). ChatGPT achieved a concordance rate of 64%, compared to Gemini at 62%. However, the models displayed distinct error profiles. ChatGPT produced "dangerous errors" in 20% of evaluations and failed to specify a time in 16% of cases. In contrast, Gemini's dangerous error rate was lower at 12%, but it demonstrated a significant "conservative error" rate of 22%, compared to 0% for ChatGPT. A chi-square test indicated that

---

## 13. Correction: Safety in the Age of Artificial Intelligence: Evaluating Large Language Model Adherence to Antithrombotic Medication and Regional Anesthesia Guidelines.

- **PMID**: [42614330](https://pubmed.ncbi.nlm.nih.gov/42614330/)
- **Journal**: Cureus
- **Publication Date**: 2026 Aug
- **Authors**: Willson Conner M, Thind Birpartap S, Srinivas Jay, Gupta Anita
- **DOI**: https://doi.org/10.7759/cureus.c472

### Abstract

[This corrects the article DOI: 10.7759/cureus.114071.].

---

## 14. Classifying American Society of Anesthesiologists Physical Status With a Low-Rank-Adapted Large Language Model: Development and Validation Study.

- **PMID**: [42013456](https://pubmed.ncbi.nlm.nih.gov/42013456/)
- **Journal**: Journal of medical Internet research
- **Publication Date**: 2026 Apr 21
- **Authors**: Chen Min-Chia, Ruan Shanq-Jang, Wu Jo-Hsin, Chen Pei-Fu
- **DOI**: https://doi.org/10.2196/89540

### Abstract

**BACKGROUND**: The American Society of Anesthesiologists Physical Status (ASA-PS) classification is integral to preoperative risk assessment; yet, assignment remains subjective and labor-intensive. Recent large language models (LLMs) process free-text electronic health records (EHRs), but few studies have evaluated parameter-efficient adaptations that both predict ASA-PS and provide clinician-readable rationales. Low-rank adaptation (LoRA) is a parameter-efficient technique that updates only a small set of add-on parameters rather than the entire model, enabling efficient fine-tuning on modest data and hardware. A lightweight, instruction-tuned LLM with these capabilities could streamline workflow and broaden access to explainable decision support. **OBJECTIVE**: This study aimed to develop and evaluate a LoRA-fine-tuned large language model meta-AI (LLaMA-3) for ASA-PS classification from preoperative clinical narratives and benchmark it against traditional machine learning classifiers and domain-specific LLMs. **METHODS**: Preoperative anesthesia notes and discharge summaries were extracted from the EHR and reformatted into an Alpaca-style instruction-response prompt, requesting ASA-PS class labels (I-V) annotated by anesthesiologists. The LoRA-enhanced LLaMA-3 model was fine-tuned with mixed-precision training and evaluated on a hold-out test set. Baselines included random forest classifier, Extreme Gradient Boosting (XGBoost) classifier, support vector machine, fastText, BioBERT, ClinicalBERT, and untuned LLaMA-3. Performance was assessed with micro- and macroaveraged F1-score and Matthews correlation coefficient (MCC), each reported with 95% bootstrap CIs. Pairwise model error rates were compared using McNemar test. **RESULTS**: The LoRA-LLaMA-3 model achieved a micro-F1-score of 0.780 (95% CI 0.769-0.792) and an MCC of 0.533 (95% CI 0.518-0.546), outperforming other LLM baselines. After fine-tuning, BioBERT reached a micro-F1-score of 0.762 and an MCC of 0.50

---

## 15. Automating Resident Case Logs: Narrative Review and Challenges Ahead.

- **PMID**: [42005891](https://pubmed.ncbi.nlm.nih.gov/42005891/)
- **Journal**: Journal of graduate medical education
- **Publication Date**: 2026 Apr
- **Authors**: Bain Andrew P, Low Alyssa, Zhang Andrew Y, Abdelfattah Kareem R, Clark Audra T et al.
- **DOI**: https://doi.org/10.4300/JGME-D-25-00327.1

### Abstract

**BACKGROUND**: A surgical resident's logs should represent their operative experience. In practice, manually compiled logs are fraught with inaccuracies and incompleteness. Electronic health record (EHR) data may enable case log automation, potentially improving accuracy and reducing resident administrative burden. **OBJECTIVE**: We examined and summarized the current literature on automated case logging systems to understand the current approaches, outcomes, and ongoing challenges. **METHODS**: We performed a narrative review using MEDLINE, Scopus, and Embase databases from January 1946 to February 2025 using keywords associated with resident case and procedure logging. English language, peer-reviewed manuscripts evaluating automated or semiautomated case logging systems were included. Articles focusing on case log analysis without addressing automated logging were excluded. Extracted information included automation methods, integration with residency systems, and measured impacts on accuracy, completeness, or efficiency. **RESULTS**: A total of 64 deduplicated articles were screened, yielding 8 semiautomated case logging systems used in emergency medicine, anesthesiology, general surgery, and ophthalmology. No fully automated end-to-end systems were identified. These systems typically increased number of cases logged as well as accuracy and completeness. Common methods included EHR data aggregation in dashboards, interfaces with logging applications, and machine learning-assisted decision support. Reported outcomes showed improved logging frequency, accuracy, and reduced variability. Studies consistently demonstrated efficiency gains and reduced resident administrative burdens. **CONCLUSIONS**: Automating resident case logging by leveraging EHR data can improve log accuracy and decrease administrative workload. Current implementations remain semiautomated and institution specific, highlighting challenges with data integration, coding consistency, and specialty-sp

---

## 16. Explainable artificial intelligence in anesthesiology prediction models: bridging the gap from black-box algorithms to clinical decision support.

- **PMID**: [42694685](https://pubmed.ncbi.nlm.nih.gov/42694685/)
- **Journal**: Frontiers in medicine
- **Publication Date**: 2026
- **Authors**: Wang Yan, Song Zuoyan, Wang Hang
- **DOI**: https://doi.org/10.3389/fmed.2026.1928394

### Abstract

Machine learning prediction models consistently outperform conventional clinical scoring tools across perioperative outcomes, yet remain largely unadopted at the bedside. This narrative review examines explainable artificial intelligence (XAI) as a bridge between algorithmic performance and clinical translation, drawing on a targeted search of PubMed and Embase (January 2018 to March 2026). Five prediction domains are synthesized: perioperative hypotension, postoperative complications, difficult airway management, depth-of-anesthesia monitoring, and regional anesthesia and pain management. SHAP (SHapley Additive exPlanations) has emerged as the dominant XAI method, identifying modifiable intraoperative targets. Attention mechanisms and GradCAM provide complementary interpretability for time-series and imaging-based models. Critical gaps persist: most delirium prediction models include no XAI analysis; no standardized evaluation framework exists, and no prospective trial has demonstrated that XAI-enhanced recommendations improve patient outcomes. Addressing these gaps is a research priority if XAI is to fulfill its potential as a facilitator of perioperative AI adoption.

---

## 17. Artificial intelligence in anesthesiology education: transformative applications, challenges, and future perspectives.

- **PMID**: [42131594](https://pubmed.ncbi.nlm.nih.gov/42131594/)
- **Journal**: Frontiers in medicine
- **Publication Date**: 2026
- **Authors**: Chen Cheng, Xie Shujing, Luo Zhihui, Hu Ziyan, Du Xiaohong et al.
- **DOI**: https://doi.org/10.3389/fmed.2026.1817855

### Abstract

Artificial intelligence offers the potential to revolutionize anesthesiology education by enabling precision education, a data-driven approach to tailor learning experiences to individual needs, thereby moving beyond the constraints of traditional pedagogical methods. This review examines the emerging applications and potential impact of AI-driven technologies, from virtual reality simulators that facilitate deliberate practice of complex procedures to machine learning platforms that enable precision education and objective competency assessment. We highlight how these tools enhance procedural fluency, clinical reasoning, and educational management. Nevertheless, this technological advancement is accompanied by profound challenges, including the risks of de-skilling, the perpetuation of algorithmic biases, data security vulnerabilities, and issues of equitable access. We argue that AI's role is as an augmentative tool, empowering educators to provide more personalized feedback and facilitate higher-order skill development, while also raising crucial ethical considerations. Navigating the future of anesthesiology education requires a balanced approach: embracing the benefits of AI while implementing robust governance to mitigate its risks, thereby fostering a new generation of anesthesiologists equipped to leverage technology for superior patient care. To this end, future research should prioritize rigorous validation of AI tools in clinical settings and focus on ethical guidelines for responsible AI implementation.

---

## 18. Development and External Validation of a Machine Learning Model for Automated Feedback Quality Assessment in Chinese Anesthesiology Residency Training.

- **PMID**: [42094912](https://pubmed.ncbi.nlm.nih.gov/42094912/)
- **Journal**: Advances in medical education and practice
- **Publication Date**: 2026
- **Authors**: Yao Lifeng, Chen Yijun, Shen Jing, Zhang Junge, Zhang Yiwei et al.
- **DOI**: https://doi.org/10.2147/AMEP.S599543

### Abstract

**PURPOSE**: High-quality narrative feedback is essential for competency-based medical education, but manual evaluation of feedback is time-consuming and subjective. This research aims to develop and validate a machine learning (ML)-based model to automate the bulk evaluation of feedback quality from anesthesiology residency program instructors. **METHODS**: Using 990 narrative feedback entries from October 2023 to November 2025 at the First Affiliated Hospital of Ningbo University, we conducted training and validation. An additional 587 feedback records from Ningbo Li HuiLi Hospital were used as an external test set. Text processing employed the jieba Chinese word segmenter combined with an anesthesia-specific vocabulary database to extract TF-IDF and manual features. Data imbalance was addressed using the Synthetic Minority Oversampling Technique (SMOTE). Logistic regression (LR), random forests (RF), and Gradient Boosting Machine (GBM) were used for training and validation. Model performance was measured using the area under the receiver operating characteristic curve (AUC-ROC), accuracy, cross-validation accuracy, precision, recall, and F1 score. **RESULTS**: In internal training, LR performed optimally, demonstrating the best overall performance (F1 score: 0.941) and stability (cross-validation accuracy: 0.925 ± 0.026), along with the highest precision (0.906). In external testing, the LR model achieved an overall accuracy of 0.840 (95% CI: 0.808-0.867), with high recall (0.956) and moderate precision (0.636) for identifying high-quality feedback, yielding an F1 score of 0.764 and an AUC of 0.729. **CONCLUSION**: This study successfully developed and externally validated a machine learning-based model for automated feedback quality assessment in Chinese anesthesiology residency training. With its high recall and stable internal performance, the model may serve as a screening tool to support competency-based medical education by enabling batch evaluation of narr

---

## 19. Quality, readability, and clinical-risk signals of default public-interface LLM responses to vascular and perioperative patient questions: a cross-sectional snapshot.

- **PMID**: [42638723](https://pubmed.ncbi.nlm.nih.gov/42638723/)
- **Journal**: Frontiers in public health
- **Publication Date**: 2026
- **Authors**: Zhong Wei, Zhang Yuanyuan, Huang Yu, Yang Jin, Zheng Guoxue et al.
- **DOI**: https://doi.org/10.3389/fpubh.2026.1905883

### Abstract

**BACKGROUND**: Patients increasingly use public large language model chatbot interfaces to seek health information. In vascular disease and perioperative management, default first responses may influence how patients interpret urgent symptoms, antithrombotic medications, procedural choices, and anesthesia-related safety issues. **METHODS**: This cross-sectional benchmark study evaluated 110 default first responses returned by five publicly accessible LLM chatbot interfaces during a defined access window on May 28-29, 2026, Beijing time (UTC + 8). Interface names were recorded solely as the public-interface display labels visible at the time of access and should not be interpreted as independently verified API-level model identifiers. Each model was queried with 22 guideline-derived English patient-facing questions, yielding 110 responses. Responses were assessed using DISCERN, Ensuring Quality Information for Patients (EQIP), Global Quality Scale (GQS), Journal of the American Medical Association (JAMA) benchmark criteria, used only as a visible metadata/transparency proxy, six readability formulas, an investigator-developed Guideline Concordance Score, and an investigator-developed Potential Clinical-Risk Severity Flag. Differences across the evaluated public-interface response sets were tested using Friedman tests with Holm-adjusted post hoc comparisons. **RESULTS**: Interrater agreement was high for established instruments: DISCERN ICC(A,1) = 0.940, EQIP ICC(A,1) = 0.830, GQS weighted κ = 0.829, and JAMA weighted κ = 0.898. Observed public-interface response performance differed significantly for DISCERN, EQIP, and JAMA criteria (all p < 0.001), and for GQS (p = 0.011). Within this defined late-May 2026 response set, responses returned by the interface displaying the label 'Grok-4.3' had the highest observed sample means for DISCERN (58.68), EQIP (81.14), GQS (4.27), and the JAMA visible metadata/transparency proxy score (1.00). No evaluated public-interface res

---

## 20. Large language model chatbots as sources of pediatric anesthesia health advice: An evaluation of reliability and readability.

- **PMID**: [42389384](https://pubmed.ncbi.nlm.nih.gov/42389384/)
- **Journal**: Digital health
- **Publication Date**: 2026
- **Authors**: Zhang Xue, Dai Yuchen, Zhao Xin, Wu Lin, Shao Boming et al.
- **DOI**: https://doi.org/10.1177/20552076261464749

### Abstract

**BACKGROUND**: Large language models are increasingly used to obtain health information, but their quality in pediatric anesthesia remains insufficiently evaluated. This study aimed to assess the reliability and readability of four widely used AI chatbots in this context. **METHODS**: This cross-sectional observational study developed 18 pediatric anesthesia-related questions using Medical Subject Headings terms, online search trend analysis, and commonly queried topics reflecting parental information needs. Each question was submitted under standardized conditions to four generative AI-driven chatbots: OpenAI's GPT-5.1 Thinking, Google's Gemini 3 Pro, Anthropic's Claude Opus 4.5 Extended Thinking, and DeepSeek-V3.2-Speciale. Models were accessed in their vendor-deployed configurations without task-specific fine-tuning. The generated responses were evaluated for information reliability using the Ensuring Quality Information for Patients (EQIP) instrument, DISCERN tool, Global Quality Score (GQS), and Journal of the American Medical Association (JAMA) benchmark criteria. Readability was assessed using seven validated indices including Flesch Reading Ease Score, Flesch-Kincaid Grade Level, Gunning Fog Index, Simple Measure of Gobbledygook, Coleman-Liau Index, Automated Readability Index, and Linsear Write Formula. **RESULTS**: A total of 72 chatbot-generated responses were included for analysis. Significant between-model differences were observed in DISCERN, EQIP, and GQS, while JAMA benchmark scores were consistently low across all models. DeepSeek and Gemini showed higher median reliability scores across several instruments, although significant pairwise differences mainly involved ChatGPT. None of the evaluated models achieved the recommended sixth-grade readability level across any index. Correlations between reliability and readability were non-significant, suggesting that these represent independent dimensions of information quality. **CONCLUSIONS**: Current LL

---
