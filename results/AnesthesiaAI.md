# AnesthesiaAI - PubMed Latest Papers

**Update Time**: 2026-07-30
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

## 5. Cholinesterase deficiency and anesthesia management: Clinical challenges and coping strategies.

- **PMID**: [42483356](https://pubmed.ncbi.nlm.nih.gov/42483356/)
- **Journal**: Journal of family medicine and primary care
- **Publication Date**: 2026 May
- **Authors**: Liu Tiantian, Sun Chaofeng, Ye Song, Ye Qinsong, Li Ding
- **DOI**: https://doi.org/10.4103/jfmpc.jfmpc_318_26

### Abstract

Cholinesterase deficiency is a rare genetic disorder that impairs the activity of acetylcholinesterase and butyrylcholinesterase. It causes severe perioperative risks due to prolonged neuromuscular blockade induced by succinylcholine and ester-based anesthetics, and may lead to life-threatening complications such as respiratory depression and cardiovascular instability, thus requiring personalized anesthesia protocols for affected patients. A comprehensive literature review was conducted to synthesize the pathophysiology, genetic basis, and pharmacokinetic impacts of cholinesterase deficiency on anesthetic drugs, and clinical case analyses were performed to validate perioperative management strategies. Genetic mutations such as BCHE c. 695T>A are the primary etiology, and butyrylcholinesterase deficiency is more prevalent and associated with significant anesthetic adverse events. The use of alternative anesthetic agents including non-depolarizing neuromuscular blockers and amide-type local anesthetics, as well as reversal agents such as sugammadex, can significantly reduce perioperative risks. Multimodal monitoring including train-of-four and neurophysiologic monitoring and preoperative screening further optimize safety. Five clinical cases confirmed the efficacy of tailored strategies in diverse surgical settings. Proactive preoperative screening, cholinesterase-independent anesthetic regimens, and interdisciplinary collaboration are pivotal for mitigating risks in cholinesterase-deficient patients. Emerging advances including CRISPR gene therapy and AI-driven pharmacokinetic models hold great promise for precision anesthesia, while genetic counseling remains essential for long-term patient management.

---

## 6. Transforming perioperative care: The current landscape and future trajectory of artificial intelligence in anesthesia-A narrative review.

- **PMID**: [42297385](https://pubmed.ncbi.nlm.nih.gov/42297385/)
- **Journal**: The Journal of international medical research
- **Publication Date**: 2026 Jun
- **Authors**: Zhang Pan, Wu Ling, Liao Yunxi, Li Hong
- **DOI**: https://doi.org/10.1177/03000605261454051

### Abstract

This narrative review examined how artificial intelligence is increasingly being applied in anesthesiology to support clinical decision-making across the perioperative period. It outlines current applications of artificial intelligence in preoperative risk assessment, intraoperative monitoring and automation, and postoperative complication prediction. We also examined the underlying artificial intelligence architectures that form the technical foundations of these tools, including machine learning, deep learning, and natural language processing. We propose that in the future, rather than narrow task-specific tools, artificial intelligence in anesthesiology should involve the development and clinical translation of large, generalizable foundation models capable of integrating multimodal perioperative data. In addition, developments in multimodal data integration, closed-loop control systems, and interpretable modeling may further refine these approaches. Further progress in artificial intelligence-driven anesthesiology may require multidisciplinary collaboration, prospective clinical validation, and careful integration into perioperative workflows to ensure safe and clinically meaningful adoption.

---

## 7. Development of an In-House Assistant Application to Reduce Preparation Time of Preoperative Informed Consent Forms for Anesthesia.

- **PMID**: [42491048](https://pubmed.ncbi.nlm.nih.gov/42491048/)
- **Journal**: Cureus
- **Publication Date**: 2026 Jun
- **Authors**: Takekoshi Masaki, Mitsuzawa Kunihiro, Ishida Takashi, Kazuma Aiba, Satoshi Tanaka
- **DOI**: https://doi.org/10.7759/cureus.110998

### Abstract

Introduction Documentation-related tasks, including preparation of informed consent (IC) forms for anesthesia, increase workload and cognitive burden in anesthesiology. This study evaluated the time-saving effect and usability of a semi-automated institution-specific assistant application for anesthesia IC form preparation. Methods We developed a semi-automated Python-based (Python Software Foundation, Wilmington, DE, USA) assistant application using generative AI assistant programming. The application was tailored to our institutional electronic medical record (EMR) workflow and was designed to automatically select relevant checkboxes and insert required text into IC forms for anesthesia. Its time-saving effect and usability were evaluated using a randomized crossover design. Twenty anesthesiologists were randomized into two groups: Group A (n = 10, 50%) prepared IC forms for five mock patients first by manual entry and then using the application, whereas Group B (n = 10, 50%) followed the reverse order. Preparation time was defined as the interval from the start of preparing the first IC form to the completion of the fifth IC form. Usability was assessed using a 5-point Likert scale. Results The mean preparation time was 9.7 (SD 1.7) minutes with the application and 16.0 (SD 2.6) minutes without the application (mean difference, 6.2 minutes; 95% CI, 5.2 to 7.2 minutes; p < 0.001). Use of the application reduced preparation time by approximately 40%. Regarding usability, 11 participants (55%) reported that they "very much wanted to continue using" the application, whereas nine participants (45%) reported that they "wanted to continue using" it. Conclusion The tailored application significantly reduced preparation time compared with manual entry and was well accepted by participants. These findings provide proof-of-concept evidence that generative AI-assisted in-house development may enable clinicians to create institution-specific workflow-support tools for improvi

---

## 8. Real-Time Brachial Plexus Ultrasound Segmentation Using Lightweight Hierarchical Temporal Fusion.

- **PMID**: [42479521](https://pubmed.ncbi.nlm.nih.gov/42479521/)
- **Journal**: IEEE journal of biomedical and health informatics
- **Publication Date**: 2026 Jul 21
- **Authors**: Baek Donghyeon, Choi Hyeyoung, Shin Myungjong, Lee Sanghun, Hong Boohwi et al.
- **DOI**: https://doi.org/10.1109/JBHI.2026.3715777

### Abstract

Identification of the brachial plexus on ultrasound remains difficult and operator-dependent. AI could assist with ultrasound-guided brachial plexus blocks, but real-time segmentation of nerve elements remains understudied. This study introduces a lightweight video segmentation framework for the sequential ultrasound imaging technique used in supraclavicular blocks. To reduce annotation workload, a semi-automated pipeline converts clinician-drawn bounding boxes into pixel-level masks using a tracking algorithm and UltraSam, an ultrasound-specific foundation model. The proposed model inserts a hierarchical temporal fusion module between the encoder and decoder of standard segmentation backbones. It employs a single layer of convolutional recurrent units with depthwise separable convolutions that connect hierarchical temporal features across multiple scales. We train with truncated backpropagation through time on long sequences and with domain-specific temporal-consistency and spatial-compactness losses. On a Sonosite test set of 24 videos, the SegFormer-B0-based model adds only 1.48 GFLOPs and 1.0 M parameters, yet improves the mean IoU from 40.53% to 43.32% and the $F_{1}$ score from 53.90% to 56.67% over the non-temporal baseline. Compared with SAM2 used as a tracker on dense whole-video ground truth, our autonomous model attains 4× higher mean IoU and a 3.6× lower temporal instability score. Cross-vendor validation on GE and Mindray devices shows that fine-tuning with 18 target videos yields consistent gains, and the model runs at 20.2/29.3 ms per frame on the Galaxy Tab S9/S8 mobile NPUs. The findings support safer ultrasound-guided regional anesthesia and could be adapted to other real-time medical image segmentation tasks.

---

## 9. Artificial intelligence-generated color overlay for ultrasound identification of the brachial plexus in regional anesthesia: an external validation study.

- **PMID**: [42479132](https://pubmed.ncbi.nlm.nih.gov/42479132/)
- **Journal**: Journal of anesthesia
- **Publication Date**: 2026 Jul 21
- **Authors**: Kamimura Yuji, Aota Yuki, Oba Soichiro, Tomonari Tsuyoshi, Kawatsu Ayako et al.
- **DOI**: https://doi.org/10.1007/s00540-026-03854-1

### Abstract

**PURPOSE**: Accurate identification of neural structures is essential for safe ultrasound-guided regional anesthesia. Although artificial intelligence (AI)-generated color overlay has been introduced to support anatomical recognition, external validation using clinically oriented evaluation methods remains limited. We evaluated the diagnostic accuracy of an AI-generated color overlay for visualizing neural structures corresponding to the C5 and C6 nerve roots. **METHODS**: In this prospective observational study, two anesthesiology trainees performed bilateral interscalene ultrasound scans in 20 healthy adult volunteers. During live scanning, ultrasound-system video recordings were saved from the initiation of scanning to acquisition of an optimal image, and still images were captured at the optimal image. Subsequently, with the operators blinded to the AI output, the color overlay generated in real time during ultrasound scanning was evaluated. Two board-certified anesthesiologists independently evaluated the datasets and assessed the accuracy of the color overlay in visualizing neural structures corresponding to the C5 and C6 nerve roots using a four-category classification: true positive, true negative, false positive, and false negative. **RESULTS**: Of the 160 evaluated nerve structures, six structures without expert consensus were excluded from analysis. Overall sensitivity, specificity, and accuracy were 93.8% (95% confidence interval [CI], 88.6-96.7), 88.9% (95% CI, 56.5-98.0), and 93.5% (95% CI, 88.5-96.4), respectively. Among all evaluated structures, false-positive and false-negative findings accounted for 0.7% and 5.8%, respectively. **CONCLUSION**: AI-generated color overlay demonstrated high accuracy in visualizing neural structures corresponding to the C5 and C6 nerve roots at the interscalene level on ultrasound images. This technology may enhance anatomical recognition and serve as a useful diagnostic and educational support tool, while complementi

---

## 10. Clinical Evaluation of an AI-Assisted Decision Support System for General Anesthesia Management Based on Data From 6 Centers: Comparative Study.

- **PMID**: [42475676](https://pubmed.ncbi.nlm.nih.gov/42475676/)
- **Journal**: Journal of medical Internet research
- **Publication Date**: 2026 Jul 20
- **Authors**: Chen Dongxu, Xue Qingsheng, Wang Geng, Mu Shanshan, Zeng Zhen et al.
- **DOI**: https://doi.org/10.2196/90023

### Abstract

**BACKGROUND**: AI is rapidly transforming medical practice, with emerging applications in perioperative care and anesthesiology. However, the clinical implementation of AI-assisted decision-making systems in anesthetic management remains challenging and requires comprehensive evaluation. **OBJECTIVE**: This study aimed to assess the performance and clinical applicability of an AI-assisted decision support system (ZW-AA-001) for general anesthesia management by comparing its decisions with those of experienced anesthesiologists across 6 medical centers. **METHODS**: A multicenter retrospective study was conducted using perioperative data from 1008 patients who underwent elective noncardiac surgeries under total intravenous anesthesia. The AI system's recommendations for anesthetic and hemodynamic medication adjustments were compared with anesthesiologists' decisions. Key outcomes included decision concordance rates, temporal performance, and consistency across centers. Advanced statistical methods, including prevalence-adjusted and bias-adjusted κ (PABAK) and Gwet's first-order agreement coefficient (AC1), were used to evaluate agreement metrics. **RESULTS**: The study included 1008 patients, with a median age of 50 (IQR 37-59) years and female predominance (619/1008, 61.4%). During anesthesia maintenance, the AI system demonstrated moderate overall decision agreement with anesthesiologists (73.3%, 95% CI 72.4%-74.3%). Analysis of center-specific data revealed generally consistent performance across all 6 centers. For propofol management, high concordance was observed in dosage adjustment decisions (91.1%, 95% CI 90.4%-91.8%), though fair agreement was found in adjustment direction (68.6%, 95% CI 67.3%-69.8%). The AI system showed significantly faster decision-making time compared to anesthesiologists for the adjustment of propofol (pseudomedian difference -77.5, 95% CI -79.5 to -75.5 seconds; P<.001). Although esmolol-related decisions showed a numerically higher c

---

## 11. First-in-human pilot study of a robotic-assisted system for image-guided trans-thoracic lung biopsy: Clinical feasibility and exploratory post-hoc AI trajectory analysis.

- **PMID**: [42492116](https://pubmed.ncbi.nlm.nih.gov/42492116/)
- **Journal**: European journal of radiology
- **Publication Date**: 2026 Jul 16
- **Authors**: Tan Zehao, Alfred Bingchao Tan, Leong Sum, Sarupraba Arjuna, Goh Alan et al.
- **DOI**: https://doi.org/10.1016/j.ejrad.2026.113089

### Abstract

**BACKGROUND & OBJECTIVE**: This prospective, single-center clinical trial evaluated the technical feasibility and clinical success of the Automatic Needle Targeting (ANT-C) patient-mounted robotic needle-guidance platform for CT-guided trans-thoracic lung biopsy under local anesthesia, incorporating an exploratory post-hoc geometric analysis of parallel artificial intelligence path planning via the NDAnalyzer software. **MATERIALS & METHODS**: Out of thirty-one recruited patients, one was excluded due to on-table lesion resolution, leaving a final cohort of thirty evaluable subjects with a median nodule size of 24 mm. While interventional radiologists executed target acquisition using independently planned trajectories, the automated software generated alternative paths in a parallel, blinded fashion to ensure zero clinical influence on the live procedure. **RESULTS**: The platform demonstrated a high technical success rate of 93.3% and a 100% clinical success rate, successfully harvesting adequate tissue cores for full histopathological and molecular profiling in all cases. Operational efficiency improved significantly as operators gained familiarity, with median procedural durations decreasing from 61.4 min in the first ten cases to 30.5 min in the final ten cases. Concurrently, median total radiation exposure significantly decreased from 427.3 mGy·cm to 303.7 mGy·cm between the early and late deciles. No major complications occurred, and minor, self-limiting Grade A adverse events were limited to asymptomatic perilesional hemorrhage and trace pneumothoraces. Furthermore, exploratory modeling revealed a median angular deviation of only 3.5° between the operator's selected path and the closest automated alternative. **CONCLUSION**: The robotic system is clinically viable and technically feasible for awake patients, though the AI's automated path-ranking cost-function requires further refinement prior to live workflow integration.

---

## 12. Simulator development using natural language: clinician-led innovation through artificial intelligence.

- **PMID**: [42458589](https://pubmed.ncbi.nlm.nih.gov/42458589/)
- **Journal**: Advances in simulation (London, England)
- **Publication Date**: 2026 Jul 15
- **Authors**: Barra Federico Lorenzo, Ricci Serena, Moro Edoardo, Travěnec Jiří, Costa Alessandro et al.
- **DOI**: https://doi.org/10.1186/s41077-026-00467-2

### Abstract

**BACKGROUND**: Healthcare simulation training faces significant barriers due to the "clinician-developer gap," where educators lack programming expertise to create customized digital simulators. Natural Language-Driven Development (NLDD) is an emerging paradigm that enables clinicians to develop educational technology through conversational artificial intelligence interfaces. **METHODS**: We implemented NLDD methodology to develop Open Vent Sim, a comprehensive mechanical ventilation simulator designed to replace anesthesia machines and ventilators in educational contexts lacking dedicated equipment. A multidisciplinary team comprising anesthesiologists, residents, a research nurse, IT, and biomedical engineers collaborated using Google AI Studio to iteratively create a web-based application through natural language prompts. Development proceeded through conversational cycles in which clinical requirements were translated into functional code via large language model assistance. **RESULTS**: Open Vent Sim was successfully developed in about 40 h over two weeks, featuring three simulation environments: anesthesia workstation, ICU ventilator, and high-flow oxygenation systems. The simulator incorporates physiological patient profiles (normal, ARDS, COPD) with dynamic compliance calculations and realistic waveform generation. Clinical validation was achieved through the integration of continuous resident feedback during iterative development. The application was successfully implemented in SimZone 1 as an interactive skill trainer and in SimZone 2 for team-based clinical scenarios during formal anesthesia and critical care education. Significant technical adaptation was required to transform the AI-generated prototype into a production-ready application. **CONCLUSIONS**: NLDD demonstrates the potential to democratize the creation of educational technology by empowering clinical domain experts to develop sophisticated simulation tools without traditional programming ex

---

## 13. Explainable Machine Learning-Based Prediction of Postoperative Hypoxemia in Elderly Patients Undergoing General Anesthesia.

- **PMID**: [42397047](https://pubmed.ncbi.nlm.nih.gov/42397047/)
- **Journal**: Big data
- **Publication Date**: 2026 Jul 03
- **Authors**: Sha Qin, Zhang Long, Song Lijun, Ji Yunjin
- **DOI**: https://doi.org/10.1177/2167647X261466190

### Abstract

In order to predict the risk of postoperative hypoxemia in elderly patients undergoing general anesthesia, this study developed, validated, and interpreted explainable machine learning-based models. One thousand six hundred senior individuals (≥60 years) participated in a retrospective, single-center cohort research. Comprehensive perioperative data were gathered, including laboratory indices, intraoperative physiological parameters, comorbidities, and demographics. To improve the interpretability of the model, feature selection was carried out using least absolute shrinkage and selection operator (LASSO) regression after thorough data preparation. A held-out test dataset was used to design and internally validate four machine learning algorithms: logistic regression, support vector machine, random forest, and extreme gradient boosting (XGBoost). The area under the receiver operating characteristic curve (AUC), accuracy, sensitivity, specificity, calibration curves, and decision curve analysis were used to evaluate the model's performance. To give clear justifications for model predictions, feature importance evaluations were carried out. About 15.0% (240/1,600) of patients experienced postoperative hypoxemia. Preoperative serum albumin level, lowest intraoperative mean arterial pressure, age, total crystalloid infusion volume, and a history of chronic obstructive pulmonary disease were important prognostic factors that were consistently found across models. The XGBoost-based explainable AI model outperformed the other models in terms of predictive performance, with the highest AUC of 0.994 (95% CI: 0.990-0.998), good calibration, and a notable net therapeutic benefit on decision curve analysis. The suggested explainable machine learning XGBoost model predicts postoperative hypoxemia in elderly patients receiving general anesthesia with accuracy and interpretability. This method facilitates focused interventions to improve surgical respiratory outcomes by supporting

---

## 14. Association of Anesthesia Modality With Procedural Parameters and Clinical Outcomes in PVI for Atrial Fibrillation.

- **PMID**: [42396969](https://pubmed.ncbi.nlm.nih.gov/42396969/)
- **Journal**: Pacing and clinical electrophysiology : PACE
- **Publication Date**: 2026 Jul 03
- **Authors**: Gao Jia, Sun Weiwei, Fu Xiaohong, Zhang Nan, Sun Meng et al.
- **DOI**: https://doi.org/10.1111/pace.70345

### Abstract

**BACKGROUND**: Pulmonary vein isolation (PVI) for atrial fibrillation (AF) is performed under general anesthesia (GA) or conscious sedation (CS). Prior studies have linked anesthesia type to postoperative recurrence and catheter metrics, but not to catheter swing, interlesion distance (ILD), or acute pulmonary vein reconnection. We assessed how GA versus CS relates to intraoperative catheter stability, lesion continuity, and clinical outcomes. **METHODS**: This retrospective study included 147 patients undergoing first-time PVI (97 under GA, 50 under CS). We evaluated and compared catheter swing, contact force (CF), ablation index (AI), ILD, acute pulmonary vein reconnection, and 12-month recurrence between groups. **RESULTS**: Catheter swing (all segments p < 0.001), ILD (all segments p < 0.001), and acute pulmonary vein reconnection (20.6% vs. 54.0%, p < 0.001) were significantly lower in the GA group, which was associated with a higher postoperative success rate (12-month recurrence: 23.7% vs. 44.0%, p = 0.007). Anesthesia type was significantly associated with both acute pulmonary vein reconnection (OR 0.22, p < 0.001) and postoperative success (12-month OR 0.40, p = 0.013). Furthermore, catheter swing was significantly associated with acute pulmonary vein reconnection (OR 1.16, p < 0.001), which served as a crucial mediator between anesthesia strategy and overall postoperative success. **CONCLUSIONS**: In this retrospective cohort, GA was associated with reduced catheter swing, shorter ILD, and lower acute pulmonary vein reconnection compared to CS. Acute reconnection significantly mediated the association with 12-month freedom from AF. These findings suggest that GA may facilitate more durable lesion formation during PVI.

---

## 15. Artificial intelligence assisted telemedicine, clinical decision support for anesthesia and critical care in intensive care units: a scoping review.

- **PMID**: [42393540](https://pubmed.ncbi.nlm.nih.gov/42393540/)
- **Journal**: BMC anesthesiology
- **Publication Date**: 2026 Jul 02
- **Authors**: Yang Qingxia, Li Meixia, Lei Yu
- **DOI**: https://doi.org/10.1186/s12871-026-03997-4

### Abstract

**BACKGROUND**: Artificial intelligence (AI) has been increasingly used in care delivery in intensive care units (ICUs) and anesthesia-critical care practice through telemedicine, tele-ICU systems, and remote patient monitoring, and is expected to support real-time clinical decision-making. **METHODS**: This scoping review followed PRISMA-ScR guidelines to map the existing evidence of AI in critical care and anesthesia-related ICU environments for telemedicine, telemonitoring, and clinical decision support systems. PubMed, Scopus, and Google Scholar were used to search for relevant literature, including the use of AI, telemedicine, predictive analytics, remote monitoring, and anesthesia-informed clinical decision support in critical care. **RESULTS**: The literature reviewed primarily focused on the non-generative AI solutions, such as machine learning, deep learning-based monitoring, and AI clinical decision support systems. Such systems can facilitate remote continuous monitoring, early detection of clinical deterioration, and clinical decision-making in the ICU perioperative anesthesia-critical care settings. The results were grouped into the following categories: tele-ICU implementation, predictive analytics, tele-monitoring, and AI-guided clinical decision support. The reported benefits included better monitoring, improved workflow, enhanced anesthesia and critical care decision-making, and greater access to specialist care, but there was substantial variation in the evidence of consistent improvement in patient-centered outcomes, with most of it being observational. Data quality, interoperability, model transparency, ethical issues, and lack of prospective clinical validation were the key difficulties encountered. **CONCLUSION**: AI-enabled telemedicine remains a nascent healthcare space in the ICU and anesthesia-critical care continuum, and further standardization, validation, and prospective clinical testing are needed to ensure its safe and scalable integra

---

## 16. From prediction to practice: closing the translation gap in artificial intelligence for anesthesia.

- **PMID**: [42018224](https://pubmed.ncbi.nlm.nih.gov/42018224/)
- **Journal**: Journal of clinical monitoring and computing
- **Publication Date**: 2026 Aug
- **Authors**: Baliga Janardhan, Seshadri Niranjan
- **DOI**: https://doi.org/10.1007/s10877-026-01434-y

### Abstract

Artificial intelligence (AI) and machine learning (ML) techniques are rapidly advancing in anesthesiology, showing promise in patient monitoring, outcome prediction, clinical decision support, and automated drug delivery. However, a substantial gap remains between algorithmic capability and practical implementation at the bedside. This narrative review examines the current state of AI/ML applications in anesthesia, including predictive analytics, closed-loop control systems, AI-assisted imaging, workflow optimization, and anesthesia planning, and explores the translational barriers that have limited routine clinical adoption. We discuss technical, organizational, regulatory, and cultural challenges impeding translation, including data quality issues, EHR interoperability constraints, lack of outcome-oriented clinical evidence, business model uncertainty, interpretability concerns, alarm fatigue, and regulatory ambiguity. Strategies to close this gap are proposed, including rigorous prospective validation, interdisciplinary collaboration with industry and payers, post-deployment model surveillance, training data transparency, user-centered design, and implementation science principles. Ethical and legal considerations, encompassing algorithmic bias, accountability for autonomous AI recommendations, privacy beyond de-identification, and equitable access, are also reviewed. A conceptual framework, summary table of applications, and practical implementation checklist are provided. Bridging the translational divide is essential for AI to fulfill its potential in improving anesthesia care, and will require coordinated action from clinicians, researchers, technologists, regulators, and healthcare institutions.

---

## 17. Automated Identification of Cardiopulmonary Disease Cases for Preoperative Risk Stratification Using Machine Learning: A Retrospective Analysis.

- **PMID**: [41985030](https://pubmed.ncbi.nlm.nih.gov/41985030/)
- **Journal**: A&A practice
- **Publication Date**: 2026 Apr 01
- **Authors**: Aggarwal Ishan, Rhee Christopher, Chura Mamta, Bora Vaibhav, Reddy Devarapalli M
- **DOI**: https://doi.org/10.1213/XAA.0000000000002183

### Abstract

**BACKGROUND**: Preoperative chart review is time-consuming and prone to errors, particularly for cardiopulmonary conditions that impact anesthetic planning. We developed a guideline-aligned "clinical insight bot" that mines free-text documentation to surface perioperative cardiovascular risk signals relevant to the 2024 Mult Society perioperative guideline for noncardiac surgery. **METHODS**: We analyzed 1000 de-identified medical cases from the PhysioNet MIMIC database. Medical terminology was extracted using regex-based NLP and categorized into 13 clinical specialties. Text features were encoded using TF-IDF vectorization and 1536-dimensional semantic embeddings stored in a PostgreSQL vector database (pgvector). Four machine learning models-Logistic Regression, Random Forest, Support Vector Machine (SVM), and Naive Bayes-were trained with stratified fivefold cross-validation to classify cases as "cardiopulmonary-only" versus "mixed/other." Performance was evaluated using accuracy, precision, recall, and F1 score, with statistical comparison via McNemar's test and bootstrap confidence intervals. **RESULTS**: In a held-out test set of 200 notes (28 positive; 172 negatives; ~14% prevalence), a linear support vector machine achieved the best overall balance (F1 ≈ 0.71), with high precision (positive predictive value 0.94) and very low false positive rate (FPR) (1/172 ≈ 0.6%). False negatives were the dominant residual error class. The pipeline processed documents near-instantaneously and, when scaled to 1000 notes, replaced on the order of tens of clinician review hours (≈100× efficiency gain) while maintaining performance across common preoperative document types. **CONCLUSIONS**: A lightweight, guideline-aligned insight bot can transform unstructured preoperative notes into concise, stepwise prompts that flag cardiovascular risk signals before the day of surgery. High precision with a very low FPR supports safe integration with anesthesiology workflows by minimizin

---

## 18. Automating Resident Case Logs: Narrative Review and Challenges Ahead.

- **PMID**: [42005891](https://pubmed.ncbi.nlm.nih.gov/42005891/)
- **Journal**: Journal of graduate medical education
- **Publication Date**: 2026 Apr
- **Authors**: Bain Andrew P, Low Alyssa, Zhang Andrew Y, Abdelfattah Kareem R, Clark Audra T et al.
- **DOI**: https://doi.org/10.4300/JGME-D-25-00327.1

### Abstract

**BACKGROUND**: A surgical resident's logs should represent their operative experience. In practice, manually compiled logs are fraught with inaccuracies and incompleteness. Electronic health record (EHR) data may enable case log automation, potentially improving accuracy and reducing resident administrative burden. **OBJECTIVE**: We examined and summarized the current literature on automated case logging systems to understand the current approaches, outcomes, and ongoing challenges. **METHODS**: We performed a narrative review using MEDLINE, Scopus, and Embase databases from January 1946 to February 2025 using keywords associated with resident case and procedure logging. English language, peer-reviewed manuscripts evaluating automated or semiautomated case logging systems were included. Articles focusing on case log analysis without addressing automated logging were excluded. Extracted information included automation methods, integration with residency systems, and measured impacts on accuracy, completeness, or efficiency. **RESULTS**: A total of 64 deduplicated articles were screened, yielding 8 semiautomated case logging systems used in emergency medicine, anesthesiology, general surgery, and ophthalmology. No fully automated end-to-end systems were identified. These systems typically increased number of cases logged as well as accuracy and completeness. Common methods included EHR data aggregation in dashboards, interfaces with logging applications, and machine learning-assisted decision support. Reported outcomes showed improved logging frequency, accuracy, and reduced variability. Studies consistently demonstrated efficiency gains and reduced resident administrative burdens. **CONCLUSIONS**: Automating resident case logging by leveraging EHR data can improve log accuracy and decrease administrative workload. Current implementations remain semiautomated and institution specific, highlighting challenges with data integration, coding consistency, and specialty-sp

---

## 19. Artificial intelligence in anesthesiology education: transformative applications, challenges, and future perspectives.

- **PMID**: [42131594](https://pubmed.ncbi.nlm.nih.gov/42131594/)
- **Journal**: Frontiers in medicine
- **Publication Date**: 2026
- **Authors**: Chen Cheng, Xie Shujing, Luo Zhihui, Hu Ziyan, Du Xiaohong et al.
- **DOI**: https://doi.org/10.3389/fmed.2026.1817855

### Abstract

Artificial intelligence offers the potential to revolutionize anesthesiology education by enabling precision education, a data-driven approach to tailor learning experiences to individual needs, thereby moving beyond the constraints of traditional pedagogical methods. This review examines the emerging applications and potential impact of AI-driven technologies, from virtual reality simulators that facilitate deliberate practice of complex procedures to machine learning platforms that enable precision education and objective competency assessment. We highlight how these tools enhance procedural fluency, clinical reasoning, and educational management. Nevertheless, this technological advancement is accompanied by profound challenges, including the risks of de-skilling, the perpetuation of algorithmic biases, data security vulnerabilities, and issues of equitable access. We argue that AI's role is as an augmentative tool, empowering educators to provide more personalized feedback and facilitate higher-order skill development, while also raising crucial ethical considerations. Navigating the future of anesthesiology education requires a balanced approach: embracing the benefits of AI while implementing robust governance to mitigate its risks, thereby fostering a new generation of anesthesiologists equipped to leverage technology for superior patient care. To this end, future research should prioritize rigorous validation of AI tools in clinical settings and focus on ethical guidelines for responsible AI implementation.

---

## 20. Development and External Validation of a Machine Learning Model for Automated Feedback Quality Assessment in Chinese Anesthesiology Residency Training.

- **PMID**: [42094912](https://pubmed.ncbi.nlm.nih.gov/42094912/)
- **Journal**: Advances in medical education and practice
- **Publication Date**: 2026
- **Authors**: Yao Lifeng, Chen Yijun, Shen Jing, Zhang Junge, Zhang Yiwei et al.
- **DOI**: https://doi.org/10.2147/AMEP.S599543

### Abstract

**PURPOSE**: High-quality narrative feedback is essential for competency-based medical education, but manual evaluation of feedback is time-consuming and subjective. This research aims to develop and validate a machine learning (ML)-based model to automate the bulk evaluation of feedback quality from anesthesiology residency program instructors. **METHODS**: Using 990 narrative feedback entries from October 2023 to November 2025 at the First Affiliated Hospital of Ningbo University, we conducted training and validation. An additional 587 feedback records from Ningbo Li HuiLi Hospital were used as an external test set. Text processing employed the jieba Chinese word segmenter combined with an anesthesia-specific vocabulary database to extract TF-IDF and manual features. Data imbalance was addressed using the Synthetic Minority Oversampling Technique (SMOTE). Logistic regression (LR), random forests (RF), and Gradient Boosting Machine (GBM) were used for training and validation. Model performance was measured using the area under the receiver operating characteristic curve (AUC-ROC), accuracy, cross-validation accuracy, precision, recall, and F1 score. **RESULTS**: In internal training, LR performed optimally, demonstrating the best overall performance (F1 score: 0.941) and stability (cross-validation accuracy: 0.925 ± 0.026), along with the highest precision (0.906). In external testing, the LR model achieved an overall accuracy of 0.840 (95% CI: 0.808-0.867), with high recall (0.956) and moderate precision (0.636) for identifying high-quality feedback, yielding an F1 score of 0.764 and an AUC of 0.729. **CONCLUSION**: This study successfully developed and externally validated a machine learning-based model for automated feedback quality assessment in Chinese anesthesiology residency training. With its high recall and stable internal performance, the model may serve as a screening tool to support competency-based medical education by enabling batch evaluation of narr

---
