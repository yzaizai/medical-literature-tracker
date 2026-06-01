# AnesthesiaAI - PubMed Latest Papers

**Update Time**: 2026-06-01
**Search Range**: Last 30 days
**Papers Found**: 20

---

## 1. Empirical Comparison of Causal Machine Learning and Post-Hoc AI Interpretability Models for Risk Factor Analysis: An Application to Medical Specialty Choice.

- **PMID**: [42175322](https://pubmed.ncbi.nlm.nih.gov/42175322/)
- **Journal**: Studies in health technology and informatics
- **Publication Date**: 2026 May 21
- **Authors**: Vicente Alvarez David, Abbiati Milena, Bornet Alban, Savoldelli Georges, Bajwa Nadia et al.
- **DOI**: https://doi.org/10.3233/SHTI260654

### Abstract

How medical students choose specialties shapes access to care. Prior work mostly describes patterns; newer prediction tools can rank influential factors but may blur association with true drivers. Using a curated cohort of 399 students, we examined Year 4 motivations for a given specialty (six items, six levels) and personality traits (Big Five) in relation to Year 6 specialty career choice (person vs technically oriented). We estimated effects with Double/debiased machine learning (DoubleML) and contrasted them with SHAP explanations from an earlier predictive model. Strong motivation for surgery at level 6 lowered the probability of a person-oriented choice by 0.37 (p < .001); high motivation for general practice raised it by 0.265 (p < .001). Other motivation signals were smaller. Psychological traits showed no clear effects (p > 0.05). SHAP broadly matched directions for the strongest items but diverged for weaker ones (e.g., anesthesiology, radiology). Comparing causal and predictive explanations, SHAP directions generally matched DoubleML for strong, well-separated motivations (e.g., surgery level 6, general practice) but diverged for weaker or correlated signals (radiology, anesthesiology, emergency medicine, mid-level psychiatry) and for psychological traits. These discrepancies caution that SHAP values reflect model-conditional associations rather than causal effects, so predictive importance should not be interpreted as causal influence.

---

## 2. Guideline-Aligned Machine Learning for Predicting Ondansetron Administration at the End of Anaesthesia: Explainable Decision Support for PONV Prophylaxis.

- **PMID**: [42174910](https://pubmed.ncbi.nlm.nih.gov/42174910/)
- **Journal**: Studies in health technology and informatics
- **Publication Date**: 2026 May 21
- **Authors**: Strube Tom, Weltermann Leoni, Weber Jonas, Defosse Jérôme
- **DOI**: https://doi.org/10.3233/SHTI260235

### Abstract

Artificial Intelligence (AI) and Clinical Practice Guidelines (CPGs) both aim to support clinical decision-making but may provide conflicting suggestions. This manuscript presents a Guideline-Aligned Machine Learning (GAML) model to predict ondansetron administration at the end of anaesthesia, based on Gan et al.'s Fourth Consensus Guidelines for the Management of Postoperative Nausea and Vomiting (PONV). n= 16,240 anaesthesia protocols were analysed for risk factors and administered PONV prophylaxes. Logistic regression, multinomial naïve Bayes, and CatBoost classifiers were trained on 80% of protocols with 12-fold cross-validation; optimal thresholds were set by the mean F1-maximising cut-off across folds. Models were evaluated on the remaining 20%, achieving high accuracy (90 ± 1%) and moderate precision and recall (60 ± 5%, 75 ± 4%) across all models. A SHAP decision plot was further computed on the test set to visualise predictor contributions and illustrate a potential interactive preoperative planning interface. Overall, GAML is a promising basis for explainable decision support in clinical care.

---

## 3. Artificial Intelligence for American Society of Anesthesiologists Physical Status Classification: Agreement with Clinician Consensus and Temporal Stability Analysis.

- **PMID**: [42194832](https://pubmed.ncbi.nlm.nih.gov/42194832/)
- **Journal**: Journal of clinical medicine
- **Publication Date**: 2026 May 18
- **Authors**: Soerensen Anne Lykke, Froeslev-Friis Christina, Kjaergaard Andersen Gunhild, Bhavsar Swati, Quitzau Lisbeth Holmgaard et al.
- **DOI**: https://doi.org/10.3390/jcm15103871

### Abstract

Background: The American Society of Anesthesiologists Physical Status (ASA-PS) classification is widely used for perioperative communication and research with known variation in agreement amongst assessors. Large language models (LLM) are increasingly considered for uniform decision making due to agreement challenges within clinicians under identical inputs. The study compared four contemporary LLMs against clinician-derived consensus and quantified within-model stability across repeated assessments. Methods: In a cross-sectional vignette study, 228 anesthesiologists from Denmark, England, and India classified 20 standardized perioperative vignettes through online survey. The modal response per vignette was considered as clinician consensus. Four LLMs (ChatGPT-5.2 Plus, Gemini 3 Pro, Perplexity AI Pro, Claude 4 Sonnet) received same set of vignettes through identical prompts. Temporal stability was assessed by repeating each vignette query nine times per model (three-time windows across three nonconsecutive days) in fresh sessions. Primary outcome was exact agreement with clinician consensus. Results: Consensus agreement for modal LLM classifications was 18/20 (90%) for ChatGPT, 17/20 (85%) for Gemini, 17/20 (85%) for Claude, and 15/20 (75%) for Perplexity. Disagreement is clustered in vignettes with weak or split clinician consensus. Stability differed by model: Claude was fully stable across all vignettes (20/20), Gemini 19/20, ChatGPT 18/20, and Perplexity 14/20; instability typically involved adjacent-class shifts. Conclusions: Contemporary LLMs often match clinician modal judgement and are largely temporally stable, with discordance concentrated in clinically ambiguous boundary cases.

---

## 4. Generative AI in simulation debriefings: an exploratory study using the Team-FIRST framework and qualitative feedback from simulation experts and learners.

- **PMID**: [41612508](https://pubmed.ncbi.nlm.nih.gov/41612508/)
- **Journal**: Advances in simulation (London, England)
- **Publication Date**: 2026 Jan 29
- **Authors**: Tscholl David W, Ebensperger Max, RahrischRahrisch Arend, Wang Helius, Heckel Hubert et al.
- **DOI**: https://doi.org/10.1186/s41077-026-00407-0

### Abstract

**BACKGROUND**: Effective debriefings in simulation-based education require accurate observation of team interactions, yet facilitators face challenges due to cognitive load, observer bias, and the complexity of team dynamics. Generative artificial intelligence (AI) tools offer a potential means to support this process by analyzing verbal communication and providing structured feedback. This study explored how AI tools can contribute to teamwork observation and debriefing in immersive medical simulations. **METHODS**: We conducted a qualitative, exploratory study using thematic analysis of simulation participants' and debriefers' experiences with AI-generated teamwork reports. Forty-one participants (anesthesia nurses, residents, and attendings) participated in immersive scenarios at the University Hospital Zurich simulation center. Verbal interactions were transcribed with AI-assisted speech recognition and analyzed using two large language model-based systems (Isaac and ChatGPT-4o) guided by a prompt based on the Team-FIRST framework. Structured reports were generated for each scenario and reviewed by four simulation experts. Semi-structured interviews captured learners' perspectives on being observed by AI tools. **RESULTS**: A total of 26 AI-generated reports and 27 learner interviews were analyzed. Experts valued the detailed transcripts and illustrative quotes, which supported structured feedback and captured observations that might otherwise be missed. Limitations included inaccuracies in categorization, misattribution of speakers, overly generalized interpretations, and the absence of contextual or nonverbal information. Learners expressed openness and optimism about AI's potential benefits: efficiency, objectivity, and enhanced perception, while also raising concerns about transparency, data protection, interpretation errors, and risks of overreliance. Both groups emphasized the necessity of human oversight. **CONCLUSION**: Generative AI tools can complemen

---

## 5. Large Language Model-Assisted Point-in-Time Interpretation of Advanced Hemodynamics in Liver Transplant Recipients: A Pilot Evaluation of Content Quality and Safety.

- **PMID**: [41598654](https://pubmed.ncbi.nlm.nih.gov/41598654/)
- **Journal**: Journal of clinical medicine
- **Publication Date**: 2026 Jan 15
- **Authors**: Kahyaoglu Selma, Kaygisiz Abdullah, Alatli Izzet, Boyaci Ayse Isik, Aray Emre et al.
- **DOI**: https://doi.org/10.3390/jcm15020716

### Abstract

Background: Large language models (LLMs) are increasingly used in clinical medicine, yet their ability to interpret advanced intraoperative hemodynamic monitoring-particularly in the context of liver transplantation-remains largely unexplored. In this proof-of-concept study, we evaluated ChatGPT's capacity to interpret multimodal hemodynamic data derived from both standard anesthesia monitoring and the PiCCO system. The study also employed a structured assessment instrument (ARQuAT), adapted through a Delphi-based process to evaluate LLM-generated clinical interpretations. Methods: Ten key surgical-hemodynamic phases of liver transplantation were identified using a modified Delphi approach to capture the major physiological transitions of the procedure. Sequential screenshots representing these phases were obtained from five liver transplant recipients, yielding a total of 50 images. Each screenshot, along with standardized clinical background information, was submitted to ChatGPT. Five expert anesthesiologists independently assessed the model's responses using the modified ARQuAT tool, which includes six content-quality domains (Accuracy, Up-to-dateness, Contextual Consistency, Clinical Usability, Trustworthiness, Clarity) and a separate catastrophic Risk item. Descriptive statistics were calculated for domain-level performance. Inter-rater reliability (Kendall's W) and internal consistency (Cronbach's alpha, McDonald's omega) were also analyzed. All statistical analyses and visualizations were performed using NumIQO. Results: ChatGPT demonstrated consistently high performance across all content-quality domains, with median scores ranging from 4.6 to 4.8 and more than 90% of all ratings classified as satisfactory. Lower scores appeared only in a small subset of frames associated with abrupt hemodynamic changes and did not indicate a recurring weakness in any specific domain. Catastrophic Risk exhibited a pronounced floor effect, with 86% of ratings scored as 0 and 

---

## 6. A comparative evaluation of the quality of responses provided by different large language model chatbots to frequently asked questions regarding nerve blocks.

- **PMID**: [41526832](https://pubmed.ncbi.nlm.nih.gov/41526832/)
- **Journal**: BMC anesthesiology
- **Publication Date**: 2026 Jan 12
- **Authors**: Tulgar Serkan, Aksu Can, Selvi Onur, Sultan Pervez, Dogan Alper Tunga et al.
- **DOI**: https://doi.org/10.1186/s12871-025-03596-9

### Abstract

**STUDY OBJECTIVE**: Large language models (LLMs) are used in all areas of life and have become one of the information sources for those seeking healthcare. Although ChatGPT is the most well-known, Claude, CoPilot, and GEMINI are also among the other LLMs. Some of these models have been studied in terms of their response quality metrics to frequently asked questions (FAQs) about broad content areas like anesthesia and to specific FAQs related to obstetric analgesia. However, no studies have yet been conducted on questions related to nerve blocks. In this study, we evaluated the quality of the answers given by the four LLMs to frequently asked questions related to 'nerve block'. **DESIGN**: Prospective, Delphi study, Survey. **INTERVENTION**: Ten FAQs were identified and presented to four LLMs. A Delphi study was conducted to develop an assessment tool. A survey study was then conducted using the developed tool, in which the evaluators, selected through a thorough process, evaluated the LLM responses. **MEASUREMENTS**: The quality of LLM responses was assessed by raters using the ARQuAT (Assessing Response Quality in AI Texts) tool, determined through Delphi rounds. Evaluation criteria included content criteria such as accuracy, comprehensiveness, security, timeliness, and relevance, as well as communication criteria such as understandability, empathy, ethical considerations, readability, and neutrality. **MAIN RESULTS**: ChatGPT and Claude demonstrated superior performance in ARQuAT-Overall scores compared to GEMINI and CoPilot (p < 0.001). ChatGPT and Claude achieved satisfaction rates above 80% in both content and communication quality metrics, significantly outperforming GEMINI (p < 0.001 for both comparisons), while CoPilot showed intermediate performance. **CONCLUSION**: Responses to FAQs related to nerve blocks were well and acceptably addressed by ChatGPT, Claude, and, to a lesser extent, CoPilot. GEMINI performed poorly compared to the others, exhibiting sub

---

## 7. Optimizing Anesthesia Care: Leveraging Large Language Models for Effective Preoperative Planning.

- **PMID**: [41441519](https://pubmed.ncbi.nlm.nih.gov/41441519/)
- **Journal**: Computers, informatics, nursing : CIN
- **Publication Date**: 2026 Jan 01
- **Authors**: Scott-Herring Mary, Thorpe Katherine, Crowell Nancy, McAuliffe Megan
- **DOI**: https://doi.org/10.1097/CIN.0000000000001305

### Abstract

Although artificial intelligence has quickly gained widespread popularity, there is a gap in the research regarding the usefulness of using large language models in the context of clinical practice. The purpose of this study was to examine the effectiveness of utilizing ChatGPT for the creation of anesthesia care plans. First-year nurse anesthesiology resident participants were instructed to enter perceived key anesthesia care plan variables into ChatGPT. The input provided to ChatGPT by the resident and the ChatGPT-generated output was collected and reviewed independently by three assistant professors of a doctor of nurse anesthesia practice program. It was determined that ChatGPT formed an appropriate anesthetic plan based on medical history and home medications. However, ChatGPT did not adequately address key variables such as ventilator settings, fluid plans, or medication doses . Artificial intelligence programs such as ChatGPT can be useful tools in the creation of anesthesia care plans; however, its effectiveness is reliant on clear input from an educated user.

---

## 8. Do Large Language Models Perform Equally Across Languages? A Comparison of Responses to Frequently Asked Questions in Anesthesiology.

- **PMID**: [41761593](https://pubmed.ncbi.nlm.nih.gov/41761593/)
- **Journal**: Medical science monitor : international medical journal of experimental and clinical research
- **Publication Date**: 2026 Feb 28
- **Authors**: Yörükoğlu Hadi Ufuk, Aksu Can, Sultan Pervez, Tulgar Serkan
- **DOI**: https://doi.org/10.12659/MSM.951815

### Abstract

BACKGROUND With the increasing use of large language model (LLM) chatbots in healthcare, evaluating their ability to provide reliable and understandable information in multiple languages is critical, particularly in fields such as anesthesia, where patient education is essential. The study primarily aimed to compare the quality of ChatGPT 4.0's and DeepSeek V3's English responses, with secondary aims to evaluate content and communication differences between English and Turkish responses. MATERIAL AND METHODS Anesthesiologists proficient in both languages were recruited as experts. Ten frequently asked questions in anesthesia were selected and translated for evaluation. Responses from ChatGPT 4.0 and DeepSeek V3 in both English and Turkish were assessed for overall quality and content quality (accuracy, comprehensiveness, and safety) and communication quality (understanding, empathy/tone, and ethics), and Turkish and English responses were compared by the evaluators. RESULTS Eleven experts evaluated the responses. English responses of ChatGPT 4.0 were superior to the English responses of DeepSeek V3 in overall (P<0.001). English responses of ChatGPT 4.0 were superior to the Turkish responses in the terms of overall, content, and communication quality (P<0.001 each) and English responses of DeepSeek V3 were superior to the Turkish responses in the terms of overall (P<0.001), content (P<0.001) and communication (P=0.001) quality. CONCLUSIONS ChatGPT 4.0 performed better than DeepSeek V3 in the English language in terms of overall quality of responses to 10 frequently asked questions in the field of anesthesia and the English responses provided by ChatGPT 4.0 and DeepSeek V3 outperformed the Turkish responses.

---

## 9. Can AI generate safe anaesthesia plans? A comparative evaluation of three large language models on 100 synthetic cases.

- **PMID**: [41653985](https://pubmed.ncbi.nlm.nih.gov/41653985/)
- **Journal**: Anaesthesia, critical care & pain medicine
- **Publication Date**: 2026 Feb 05
- **Authors**: Jarrassier Audrey, de Saint-Léger Frederik Belot, de Rocquigny Gaël, Ariès Philippe, Joseph Alexandre et al.
- **DOI**: https://doi.org/10.1016/j.accpm.2026.101769

### Abstract

**BACKGROUND**: Preoperative anaesthetic consultation is essential for perioperative care, involving risk assessment, treatment optimisation, and planning of anaesthetic strategies according to established guidelines. Large language models (LLMs) could offer decision-support in this setting, but their autonomous capability to generate comprehensive, guideline-based anaesthetic plans remains unassessed in France and uncertain worldwide. **METHODS**: In this simulation study, 100 synthetic clinical cases spanning various surgical specialties were evaluated. Three AI models-ChatGPT, Mistral, and a domain-specific LLM (Dougall GPT)-were prompted to generate preoperative anaesthetic assessment and plans based on French guidelines. Outputs were compared with expert anaesthesiologist reference plans using structured expert scoring across multiple domains, including guideline adherence and clinical safety. **RESULTS**: Among 1200 evaluated data fields across 100 cases, ChatGPT showed the highest overall guideline conformity, measured using a 0-4 expert-derived ordinal scale per domain (4 = guideline-concordant). ChatGPT provided the most complete outputs (98% of requested items) and achieved the highest median agreement scores in seven of the 12 anaesthesia domains. Dougall GPT performed moderately, whereas Mistral LeChat showed lower conformity and the highest proportion of unsafe or potentially unsafe outputs (scores ≤2). **CONCLUSIONS**: Current LLMs demonstrate encouraging potential to support preoperative anaesthetic planning for routine cases. However, their reliability remains insufficient for high-risk or complex patients without further fine-tuning and safety controls. These findings underscore both the potential and the current limitations of AI in perioperative decision support.

---

## 10. Data sharing statements in five high-impact anesthesiology journals (2020-2023): a cross-sectional study.

- **PMID**: [41963762](https://pubmed.ncbi.nlm.nih.gov/41963762/)
- **Journal**: Canadian journal of anaesthesia = Journal canadien d'anesthesie
- **Publication Date**: 2026 Feb
- **Authors**: Harris Tag, Sanchez Bryce, Hagood Alex, Elfar Annes, Duncan Jacob et al.
- **DOI**: https://doi.org/10.1007/s12630-026-03093-8

### Abstract

**PURPOSE**: In this study, we sought to evaluate the presence, quality, and accessibility of data sharing statements (DSS) in research articles published in five high-impact anesthesiology journals from 2020 to 2023. Data sharing is foundational to research transparency and reproducibility. As anesthesiology evolves, understanding how DSS are implemented in selected high-impact journals can inform open science efforts within anesthesiology research. **METHODS**: We conducted a cross-sectional study of five top-ranked anesthesiology journals selected using 2023 Clarivate Journal Impact Factor (JIF) rankings. Eligible studies (2020-2023) were screened in duplicate using Rayyan, and data were extracted using a structured Google Form. We used a large language model (ChatGPT, GPT-4) to aid in the exploratory thematic development of DSS, with manual validation by investigators. **RESULTS**: Among 1,123 included articles, DSS prevalence varied by journal and year. In Anaesthesia, Critical Care & Pain Medicine, articles with DSS increased from 15% (4/26) in 2020 to 30% (9/30) in 2023, whereas the prevalence of DSS remained below 8% in Anesthesia & Analgesia. Government-funded studies were more likely to include DSS (β = 0.734, P = 0.047), while higher JIF was negatively associated with DSS inclusion (β = -0.298, P = 0.008). Thematic analysis showed "Conditional Data Availability" was the most frequent DSS type (74%). Of authors contacted, 28% responded, and 14% ultimately agreed to share data for replication. **CONCLUSIONS**: We found that DSS were underused in leading anesthesiology journals. Strengthening journal policies, funder mandates, and education on data sharing practices may promote greater transparency in anesthesia research. Because our analysis focused on a limited sample of journals, findings may not be generalizable to the entire field of anesthesiology. RéSUMé: OBJECTIF: Cette étude visait à évaluer la présence, la qualité et l’accessibilité des déclaration

---

## 11. From prediction to practice: closing the translation gap in artificial intelligence for anesthesia.

- **PMID**: [42018224](https://pubmed.ncbi.nlm.nih.gov/42018224/)
- **Journal**: Journal of clinical monitoring and computing
- **Publication Date**: 2026 Apr 22
- **Authors**: Baliga Janardhan, Seshadri Niranjan
- **DOI**: https://doi.org/10.1007/s10877-026-01434-y

---

## 12. Classifying American Society of Anesthesiologists Physical Status With a Low-Rank-Adapted Large Language Model: Development and Validation Study.

- **PMID**: [42013456](https://pubmed.ncbi.nlm.nih.gov/42013456/)
- **Journal**: Journal of medical Internet research
- **Publication Date**: 2026 Apr 21
- **Authors**: Chen Min-Chia, Ruan Shanq-Jang, Wu Jo-Hsin, Chen Pei-Fu
- **DOI**: https://doi.org/10.2196/89540

### Abstract

**BACKGROUND**: The American Society of Anesthesiologists Physical Status (ASA-PS) classification is integral to preoperative risk assessment; yet, assignment remains subjective and labor-intensive. Recent large language models (LLMs) process free-text electronic health records (EHRs), but few studies have evaluated parameter-efficient adaptations that both predict ASA-PS and provide clinician-readable rationales. Low-rank adaptation (LoRA) is a parameter-efficient technique that updates only a small set of add-on parameters rather than the entire model, enabling efficient fine-tuning on modest data and hardware. A lightweight, instruction-tuned LLM with these capabilities could streamline workflow and broaden access to explainable decision support. **OBJECTIVE**: This study aimed to develop and evaluate a LoRA-fine-tuned large language model meta-AI (LLaMA-3) for ASA-PS classification from preoperative clinical narratives and benchmark it against traditional machine learning classifiers and domain-specific LLMs. **METHODS**: Preoperative anesthesia notes and discharge summaries were extracted from the EHR and reformatted into an Alpaca-style instruction-response prompt, requesting ASA-PS class labels (I-V) annotated by anesthesiologists. The LoRA-enhanced LLaMA-3 model was fine-tuned with mixed-precision training and evaluated on a hold-out test set. Baselines included random forest classifier, Extreme Gradient Boosting (XGBoost) classifier, support vector machine, fastText, BioBERT, ClinicalBERT, and untuned LLaMA-3. Performance was assessed with micro- and macroaveraged F1-score and Matthews correlation coefficient (MCC), each reported with 95% bootstrap CIs. Pairwise model error rates were compared using McNemar test. **RESULTS**: The LoRA-LLaMA-3 model achieved a micro-F1-score of 0.780 (95% CI 0.769-0.792) and an MCC of 0.533 (95% CI 0.518-0.546), outperforming other LLM baselines. After fine-tuning, BioBERT reached a micro-F1-score of 0.762 and an MCC of 0.50

---

## 13. The impact of regional block presence on large language model-based postoperative analgesia recommendations in abdominal surgery: a comparative study using real-world patient data.

- **PMID**: [41957712](https://pubmed.ncbi.nlm.nih.gov/41957712/)
- **Journal**: BMC anesthesiology
- **Publication Date**: 2026 Apr 10
- **Authors**: Uslu Bayhan Bahar, Gazioğlu Kişi Tuğçe
- **DOI**: https://doi.org/10.1186/s12871-026-03814-y

### Abstract

**BACKGROUND**: Postoperative pain management is a core component of anesthesiology practice, with regional anesthesia playing a key role in multimodal analgesia strategies. Large language model (LLM)-based artificial intelligence (AI) systems are increasingly proposed as clinical decision support tools; however, their ability to integrate critical perioperative context, such as the presence of an existing regional block, remains insufficiently explored. **METHODS**: This prospective, observational, comparative study included 144 adult patients undergoing elective abdominal surgery at a tertiary care center, after exclusion of four patients due to severe preoperative or intraoperative complications that significantly altered the planned postoperative analgesia. Patients were grouped according to the presence or absence of a regional block (70 per group). For each patient, anonymized and standardized clinical scenarios were evaluated independently by three LLM-based AI systems (ChatGPT, Gemini, and Copilot) to generate postoperative analgesia recommendations. AI outputs were assessed by blinded anesthesiology experts for opioid recommendation, multimodal analgesia, consideration of regional anesthesia, and overall clinical appropriateness using a 5-point Likert scale. Multivariable logistic and ordinal logistic regression analyses were performed to determine the independent effect of regional block presence, adjusting for relevant clinical covariates. Agreement between AI recommendations and actual clinical practice was evaluated using Cohen's kappa. **RESULTS**: Regional block presence was not independently associated with opioid recommendations generated by any AI system (all p > 0.05). However, the likelihood of recommending an additional regional block was significantly reduced by ChatGPT (adjusted odds ratio [aOR] 0.02, p < 0.001) and Copilot (aOR 0.15, p = 0.019). Gemini demonstrated complete separation, consistently recommending regional blocks only in patient

---

## 14. Automated Identification of Cardiopulmonary Disease Cases for Preoperative Risk Stratification Using Machine Learning: A Retrospective Analysis.

- **PMID**: [41985030](https://pubmed.ncbi.nlm.nih.gov/41985030/)
- **Journal**: A&A practice
- **Publication Date**: 2026 Apr 01
- **Authors**: Aggarwal Ishan, Rhee Christopher, Chura Mamta, Bora Vaibhav, Reddy Devarapalli M
- **DOI**: https://doi.org/10.1213/XAA.0000000000002183

### Abstract

**BACKGROUND**: Preoperative chart review is time-consuming and prone to errors, particularly for cardiopulmonary conditions that impact anesthetic planning. We developed a guideline-aligned "clinical insight bot" that mines free-text documentation to surface perioperative cardiovascular risk signals relevant to the 2024 Mult Society perioperative guideline for noncardiac surgery. **METHODS**: We analyzed 1000 de-identified medical cases from the PhysioNet MIMIC database. Medical terminology was extracted using regex-based NLP and categorized into 13 clinical specialties. Text features were encoded using TF-IDF vectorization and 1536-dimensional semantic embeddings stored in a PostgreSQL vector database (pgvector). Four machine learning models-Logistic Regression, Random Forest, Support Vector Machine (SVM), and Naive Bayes-were trained with stratified fivefold cross-validation to classify cases as "cardiopulmonary-only" versus "mixed/other." Performance was evaluated using accuracy, precision, recall, and F1 score, with statistical comparison via McNemar's test and bootstrap confidence intervals. **RESULTS**: In a held-out test set of 200 notes (28 positive; 172 negatives; ~14% prevalence), a linear support vector machine achieved the best overall balance (F1 ≈ 0.71), with high precision (positive predictive value 0.94) and very low false positive rate (FPR) (1/172 ≈ 0.6%). False negatives were the dominant residual error class. The pipeline processed documents near-instantaneously and, when scaled to 1000 notes, replaced on the order of tens of clinician review hours (≈100× efficiency gain) while maintaining performance across common preoperative document types. **CONCLUSIONS**: A lightweight, guideline-aligned insight bot can transform unstructured preoperative notes into concise, stepwise prompts that flag cardiovascular risk signals before the day of surgery. High precision with a very low FPR supports safe integration with anesthesiology workflows by minimizin

---

## 15. Large language models in trauma anesthesia education.

- **PMID**: [41744265](https://pubmed.ncbi.nlm.nih.gov/41744265/)
- **Journal**: Current opinion in anaesthesiology
- **Publication Date**: 2026 Apr 01
- **Authors**: Corpman David, Lang Elodie, Law Tyler J
- **DOI**: https://doi.org/10.1097/ACO.0000000000001617

### Abstract

**PURPOSE OF REVIEW**: Large language model (LLM) use is rapidly growing among trainees and educators in clinical medicine, and new developments with LLM-augmented educational approaches have the potential to enhance learning and ease educator burden. We review LLM fundamentals, their use in clinical education, and how they may be integrated into trauma anesthesia education. **RECENT FINDINGS**: Traditional trauma anesthesia curricula and learning objectives lack granularity and the ability to meet unique learner needs. New approaches to clinical education and curriculum development are leveraging LLM capabilities, but applications for trauma anesthesia education remain insufficiently evaluated. **SUMMARY**: Augmenting traditional trauma anesthesia educational approaches with LLMs bears promise. Integrating numerous trauma anesthesia curricula and enhancing educational tools with LLMs to evaluate learner performance and satisfaction and educator burden would be informative to help refine best practices and target areas for improvement.

---

## 16. Automating Resident Case Logs: Narrative Review and Challenges Ahead.

- **PMID**: [42005891](https://pubmed.ncbi.nlm.nih.gov/42005891/)
- **Journal**: Journal of graduate medical education
- **Publication Date**: 2026 Apr
- **Authors**: Bain Andrew P, Low Alyssa, Zhang Andrew Y, Abdelfattah Kareem R, Clark Audra T et al.
- **DOI**: https://doi.org/10.4300/JGME-D-25-00327.1

### Abstract

**BACKGROUND**: A surgical resident's logs should represent their operative experience. In practice, manually compiled logs are fraught with inaccuracies and incompleteness. Electronic health record (EHR) data may enable case log automation, potentially improving accuracy and reducing resident administrative burden. **OBJECTIVE**: We examined and summarized the current literature on automated case logging systems to understand the current approaches, outcomes, and ongoing challenges. **METHODS**: We performed a narrative review using MEDLINE, Scopus, and Embase databases from January 1946 to February 2025 using keywords associated with resident case and procedure logging. English language, peer-reviewed manuscripts evaluating automated or semiautomated case logging systems were included. Articles focusing on case log analysis without addressing automated logging were excluded. Extracted information included automation methods, integration with residency systems, and measured impacts on accuracy, completeness, or efficiency. **RESULTS**: A total of 64 deduplicated articles were screened, yielding 8 semiautomated case logging systems used in emergency medicine, anesthesiology, general surgery, and ophthalmology. No fully automated end-to-end systems were identified. These systems typically increased number of cases logged as well as accuracy and completeness. Common methods included EHR data aggregation in dashboards, interfaces with logging applications, and machine learning-assisted decision support. Reported outcomes showed improved logging frequency, accuracy, and reduced variability. Studies consistently demonstrated efficiency gains and reduced resident administrative burdens. **CONCLUSIONS**: Automating resident case logging by leveraging EHR data can improve log accuracy and decrease administrative workload. Current implementations remain semiautomated and institution specific, highlighting challenges with data integration, coding consistency, and specialty-sp

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

## 19. Explainable Machine Learning for Prediction of Early Postoperative Nausea and Vomiting After General Anesthesia.

- **PMID**: [41783600](https://pubmed.ncbi.nlm.nih.gov/41783600/)
- **Journal**: Journal of multidisciplinary healthcare
- **Publication Date**: 2026
- **Authors**: Chang Hsiao-Cheng, Chen Li-Yun, Lin Yu-Shiang
- **DOI**: https://doi.org/10.2147/JMDH.S572550

### Abstract

**PURPOSE**: Postoperative nausea and vomiting (PONV) remains one of the most common adverse effects associated with anesthesia care. This study aimed to explore the feasibility of applying machine learning models trained exclusively on routinely available non-invasive clinical indicators to predict early PONV risk. Explainable artificial intelligence techniques were also employed to identify the most influential predictors of early PONV. **PATIENTS AND METHODS**: A retrospective dataset from Cathay General Hospital, including 927 patient cases and 16 non-invasive clinical indicators, was used to investigate early PONV risk prediction. This study evaluated the predictive performance of several traditional machine learning models, deep learning architectures, and ensemble learning methods to compare their classification capabilities. **RESULTS**: Overall, the models demonstrated moderate discriminative performance. The random forest model achieved an accuracy of 83.5% with balanced precision (80.81%) and recall (83.5%), while the logistic regression model attained an AUC of 0.6905. Analysis of positive SHAP values identified the top 7 most influential predictors of early PONV. These included pharmacologic interventions (eg, neostigmine), pre-existing comorbidities (eg, history of nausea and vomiting, history of cardiovascular disease), demographic characteristics (eg, gender), postoperative pain, and anesthetic and surgical factors (eg, type of surgery and duration of anesthesia). Moreover, SHAP analysis revealed that the use of dexamethasone was negatively associated with the predicted risk in the model, suggesting its potential protective role in the prevention of early PONV. **CONCLUSION**: By generating explainable outputs, this study bridges the gap between algorithmic prediction and clinical decision-making, allowing anesthesiologists to better recognize underlying risk factors and make informed, evidence-based decisions in perioperative management.

---

## 20. Multimodal data for predictive medicine: algorithmic fusion of clinical data in anesthesiology and intensive care.

- **PMID**: [41658614](https://pubmed.ncbi.nlm.nih.gov/41658614/)
- **Journal**: Frontiers in medicine
- **Publication Date**: 2026
- **Authors**: Boie Sebastian Daniel, Giesa Niklas, Sekutowicz Maria, Zhumagambetov Rustam, Haufe Stefan et al.
- **DOI**: https://doi.org/10.3389/fmed.2026.1746867

### Abstract

Anesthesiology and intensive care medicine are among the most data-rich fields of medicine, where accurate and timely outcome prediction or risk stratification is important. During patient care, heterogeneous data streams, including structured electronic health records, free-text documentation, and high-frequency physiologic time series are recorded. This provides a fertile ground for machine learning (ML) models to make individualized risk predictions. Yet, secondary use of routine data remains difficult due to heterogeneity, missingness, variable granularity, ambiguously defined outcomes, or poor representation of clinical concepts in routine data. Reproducibility and transparency are difficult to achieve with hospital-specific complex data pipelines. New complexities arise when combining different data modalities. This perspective article discusses three common modalities-tabular data, clinical text, and time series-and outlines data modality-specific challenges, data preprocessing strategies, and ML modeling approaches. We examine multimodal fusion strategies through the common taxonomy of early, intermediate, and late fusion. In early fusion, generated features are aggregated into a unified tabular representation, offering simplicity and often serve as first baseline prediction models. Intermediate fusion uses modality-specific encoders with shared layers to learn cross-modal dependencies. This strategy yields the most complex and powerful models. Late decision-level fusion combines outputs from modality-optimized models, providing modularity and robustness to missing modalities, leading to advantages for real-time deployment where data arrive asynchronously. The growth of multi-centric datasets and federated infrastructures may enable intermediate-fusion architectures and multimodal foundation models to better capture patient trajectories, supporting risk stratification and personalized therapy in perioperative and intensive care settings.

---
