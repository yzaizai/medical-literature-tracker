# AnesthesiaAI - PubMed Latest Papers

**Update Time**: 2026-08-27
**Search Range**: Last 30 days
**Papers Found**: 18

---

## 1. Artificial intelligence in onco-anaesthesia: Current applications, challenges, and future directions.

- **PMID**: [42625971](https://pubmed.ncbi.nlm.nih.gov/42625971/)
- **Journal**: World journal of methodology
- **Publication Date**: 2026 Sep 20
- **Authors**: Sirohiya Prashant, Maurya Prateek, Gupta Nishkarsh, Ratre Brajesh Kumar, Vig Saurabh et al.
- **DOI**: https://doi.org/10.5662/wjm.117916

### Abstract

Artificial intelligence (AI) is transforming onco-anaesthesia by shifting practice from reactive physiological management toward predictive and precision-based care. This review outlines current AI applications across the perioperative cancer pathway. Preoperatively, machine learning and deep learning models enhance risk stratification through automated frailty assessment, electronic health record phenotyping, and prediction of cancer-specific outcomes. Intraoperatively, AI-enabled technologies such as closed-loop anaesthesia delivery systems, predictive haemodynamic monitoring, and automated depth-of-anaesthesia control optimize drug dosing, reduce physiological stress, and may help preserve perioperative immune function, with potential implications for long-term oncologic outcomes. Postoperatively, AI-driven integration of multimodal data-including genomics, radiomics, wearable biosignals, and high-resolution physiological waveforms-facilitates early detection of complications such as delirium, persistent pain, acute kidney injury, and anastomotic leakage. The review also examines the role of AI in evaluating the "onco-anaesthesia hypothesis" by clarifying links between anaesthetic techniques, inflammation, and cancer recurrence. Despite these advances, significant challenges persist, including data heterogeneity, limited generalisability, algorithmic opacity, regulatory uncertainty, and ethical concerns related to equity and clinical implementation. Future progress will depend on explainable AI, federated learning, real-time clinical decision-support systems, and validation through large, prospective studies to fully realise AI's potential in personalised onco-anaesthetic care.

---

## 2. Dynamic Aware Biopsy Needle Identification in Ultrasound Images Using Temporal Prior Guided U-Net Cross Transformer With Limited Training Data.

- **PMID**: [42486749](https://pubmed.ncbi.nlm.nih.gov/42486749/)
- **Journal**: Ultrasound in medicine & biology
- **Publication Date**: 2026 Oct
- **Authors**: Lee Myeongjin, Beom Dong Gyu, Bae Eun Hui, Kim Soo Wan, Kim Chang Seong et al.
- **DOI**: https://doi.org/10.1016/j.ultrasmedbio.2026.06.024

### Abstract

**OBJECTIVE**: Ultrasound-guided needle placement has been commonly used for minimally invasive clinical procedures, including biopsy, regional anesthesia and localized drug administration. This study aimed to enhance existing deep learning frameworks by incorporating a classical background subtraction, which enriches the inductive bias and thereby enables more reliable needle detection even when the available training dataset is small. **METHODS**: Although deep learning methods such as U-Net and its derivatives have substantially advanced needle localization performance, they remain constrained by a limited receptive field that prevents effective modeling of long-range spatial dependencies. Although Vision Transformer overcomes this limitation through self-attention mechanisms, it demands large-scale training data and tends to sacrifice fine-grained spatial locality. To overcome these limitations, we propose U-Net Cross Transformer (UXFormer), a dynamic-aware hybrid architecture that combines classical background subtraction with an integrated U-Net × Vision Transformer fusion framework. The model comprises three key components: (i) null subspace-based extraction of temporal prior information, (ii) a temporal-to-spatial cross-attention module during encoding and (iii) a global-to-local cross-convolutional block attention module during decoding, enabling continuous bidirectional communication between localized temporal dynamics and globally contextualized spatial representations. **RESULTS**: Experimental results demonstrate that the proposed method outperforms multiple competing approaches, achieving significant improvements: a 14.2% increase in Jaccard index, a 9.0% increase in Dice score, 8.5% increase in recall, 5.5% increase in precision, and 63.5% increase in the 95th percentile Hausdorff distance, thus leading to a 44.0% improvement in tip position error and a 17.7% improvement in trajectory angle error, even under varying needle visibility conditions. **CON

---

## 3. Pupil-DLC: An open-source deep learning pipeline for scalable, marker-less tracking of pupil dynamics across conscious and unconscious states.

- **PMID**: [42401399](https://pubmed.ncbi.nlm.nih.gov/42401399/)
- **Journal**: Journal of neuroscience methods
- **Publication Date**: 2026 Nov
- **Authors**: Seyfourian Parsa, Marks Lydia C, Claar Leslie D, Nahas Yasmeen, Keating Miles et al.
- **DOI**: https://doi.org/10.1016/j.jneumeth.2026.110848

### Abstract

**BACKGROUND**: Pupil diameter is a non-invasive biomarker of brain state, correlating with arousal, attention, cognitive processing, and consciousness. However, existing pupillometry software often lacks scalability and robustness across diverse experimental conditions and species. **NEW METHOD**: We introduce Pupil-DLC, an open-source, offline, DeepLabCut-based pipeline for scalable, marker-less pupil tracking, primarily designed for mice. Trained on 21,909 manually annotated frames from over 140 videos of head-fixed mice spanning wakefulness and drug-induced states, including psychedelics and anesthesia, the dataset was deliberately selected to maximize pupil size variability and model generalization. Pupil-DLC implements a dual-model architecture: a General Model (GM) for high-throughput analysis and an Individual Model (IM) for session-specific optimization. **RESULTS**: Pupil-DLC captures pupil dynamics across awake, psychedelic, and anesthetized conditions with high agreement with ground truth and equal tracking fidelity during active locomotion and quiet rest. Confidence metrics aligned with human frame quality assessments, enabling principled tuning of accuracy-retention trade-offs. As a secondary demonstration, Pupil-DLC extends to unseen human videos across diverse conditions and frame rates, including daylight and smartphone recordings, without retraining. **COMPARISON WITH EXISTING METHODS**: Pupil-DLC outperforms existing automated methods in accuracy and frame retention while maintaining computational efficiency comparable to real-time tools. These improvements stem from a learned keypoint-based representation robust to pupil shape variability, occlusions, reflections, and imaging artifacts. The GM/IM framework supports a tiered strategy balancing throughput and precision. **CONCLUSIONS**: Pupil-DLC provides a reproducible, adaptable platform for quantifying pupil-linked brain state dynamics across experimental paradigms and species, bridging basic mo

---

## 4. A Multitask Time-Frequency Deep Learning Approach for Anesthesia Depth Monitoring and Transition Prediction.

- **PMID**: [42351597](https://pubmed.ncbi.nlm.nih.gov/42351597/)
- **Journal**: Diagnostics (Basel, Switzerland)
- **Publication Date**: 2026 Jun 22
- **Authors**: Kavuncu Saliha Kevser, Yalvac Mehmet, Basturk Alper
- **DOI**: https://doi.org/10.3390/diagnostics16121937

### Abstract

Background: Electroencephalography (EEG) signals are widely used for monitoring anesthesia depth during surgery. Current commercial indicators are largely closed-source and may reflect dynamic changes with some delay. Methods: This study proposes a multitask deep learning model for continuous Bispectral Index (BIS) estimation, binary anesthesia-state classification, and prediction of transitions toward light anesthesia at different time intervals. Dual-channel EEG signals from 5471 surgical cases in the VitalDB dataset were divided into 60 s windows. Short-Time Fourier Transform (STFT) captured instantaneous frequency changes to transform the signal into a two-dimensional map. A ResNet-SE architecture incorporating Squeeze-and-Excitation blocks was used to identify EEG features associated with anesthesia depth. Results: A Mean Absolute Error of 3.27 and a Root Mean Square Error of 5.48 were obtained in anesthesia depth estimation. Light anesthesia classification achieved an AUC of 0.99 on the internal test set. Conclusions: The proposed multitask model enables the assessment of anesthesia depth and transitions toward light anesthesia using EEG signals.

---

## 5. Off-target effects of DREADD ligands revealed by an anesthesia emergence paradigm in mice.

- **PMID**: [42468535](https://pubmed.ncbi.nlm.nih.gov/42468535/)
- **Journal**: Cell reports methods
- **Publication Date**: 2026 Jul 17
- **Authors**: Moreno-Gomez Miryam, Foffani Guglielmo, Humanes-Valera Desire
- **DOI**: https://doi.org/10.1016/j.crmeth.2026.101531

### Abstract

Designer receptors exclusively activated by designer drugs (DREADDs) enable reversible control of specific neural circuits, but the pharmacological neutrality of their ligands is increasingly questioned. Here, we introduce an anesthesia emergence paradigm to systematically assess the off-target effects of DREADD ligands in DREADD-naive mice. We show that intraperitoneal administration of clozapine N-oxide (CNO), compound 21 (C21), or deschloroclozapine (DCZ) delays motor recovery from isoflurane anesthesia. CNO produced the largest delay, likely due to its back-conversion to clozapine. DCZ showed the smallest effect magnitude, although its difference from C21 remained inconclusive. We then show that subcutaneous administration, which should reduce clozapine back-conversion, reduces the CNO-induced recovery delay to levels comparable to those of C21. Finally, we provide a freely available, deep-learning-based automated behavioral pipeline that integrates the anesthesia emergence paradigm with a reproducible analysis tool for future studies. Together, these results underscore the importance of accounting for ligand off-target effects through careful dose selection and DREADD-free, ligand-treated controls in chemogenetic experiments.

---

## 6. Artificial intelligence assisted telemedicine, clinical decision support for anesthesia and critical care in intensive care units: a scoping review.

- **PMID**: [42393540](https://pubmed.ncbi.nlm.nih.gov/42393540/)
- **Journal**: BMC anesthesiology
- **Publication Date**: 2026 Jul 02
- **Authors**: Yang Qingxia, Li Meixia, Lei Yu
- **DOI**: https://doi.org/10.1186/s12871-026-03997-4

### Abstract

**BACKGROUND**: Artificial intelligence (AI) has been increasingly used in care delivery in intensive care units (ICUs) and anesthesia-critical care practice through telemedicine, tele-ICU systems, and remote patient monitoring, and is expected to support real-time clinical decision-making. **METHODS**: This scoping review followed PRISMA-ScR guidelines to map the existing evidence of AI in critical care and anesthesia-related ICU environments for telemedicine, telemonitoring, and clinical decision support systems. PubMed, Scopus, and Google Scholar were used to search for relevant literature, including the use of AI, telemedicine, predictive analytics, remote monitoring, and anesthesia-informed clinical decision support in critical care. **RESULTS**: The literature reviewed primarily focused on the non-generative AI solutions, such as machine learning, deep learning-based monitoring, and AI clinical decision support systems. Such systems can facilitate remote continuous monitoring, early detection of clinical deterioration, and clinical decision-making in the ICU perioperative anesthesia-critical care settings. The results were grouped into the following categories: tele-ICU implementation, predictive analytics, tele-monitoring, and AI-guided clinical decision support. The reported benefits included better monitoring, improved workflow, enhanced anesthesia and critical care decision-making, and greater access to specialist care, but there was substantial variation in the evidence of consistent improvement in patient-centered outcomes, with most of it being observational. Data quality, interoperability, model transparency, ethical issues, and lack of prospective clinical validation were the key difficulties encountered. **CONCLUSION**: AI-enabled telemedicine remains a nascent healthcare space in the ICU and anesthesia-critical care continuum, and further standardization, validation, and prospective clinical testing are needed to ensure its safe and scalable integra

---

## 7. Anesthesiologists' Assessment of the Correctness, Completeness, and Coherence of ChatGPT Answers to Patient Preoperative Questions.

- **PMID**: [42592434](https://pubmed.ncbi.nlm.nih.gov/42592434/)
- **Journal**: Cureus
- **Publication Date**: 2026 Jul
- **Authors**: Werry Daniel, Barry Garrett, Uppal Vishal, Bailey Jonathan G
- **DOI**: https://doi.org/10.7759/cureus.112602

### Abstract

Introduction Patients are increasingly turning to large language models (LLMs) for answers. However, LLMs like ChatGPT are relatively new technology and are untested for this purpose. Inconsistency and "hallucinations" are commonly described problems with LLMs. This study tested the consistency, correctness, completeness, and coherence of answers to frequently asked patient questions, as scored by expert anesthesiologists. Methods We gathered commonly asked patient questions from professional association websites. Patient partners were consulted to confirm relevance of the questions. A subset of questions was tested for consistency using intraclass correlation ICC (3,k) across multiple leading prompts. Then anesthesiologists and trainees scored the responses on a Likert scale for 10 anesthesia-related patient questions, with and without a leading prompt. Interrater agreement was calculated, and Likert scores were described. Results In terms of consistency, all ICC (3,k) values were below the prespecified threshold of 0.75, although confidence intervals were wide. Overall median ratings of the correctness, completeness, and coherence of each question ranged from 3.4 to 3.9, corresponding to average ratings between "good" and "very good." Ratings for all responses were similar regardless of whether the question was submitted with or without the prompt. Excellent scores were rarer, receiving 81 (16%) for correctness, 66 (13%) for completeness, and 121 (23%) for coherence. Discussion ChatGPT offers appropriate and moderately consistent answers to anesthesia-related patient questions. Anesthesiologists should be aware that while ChatGPT responses are generally correct, complete, and coherent, this does not translate to patient comprehension, and the answers may not be appropriate for the particular patient and institution.

---

## 8. An adaptive attention U-network for recognizing ultrasound images.

- **PMID**: [42390122](https://pubmed.ncbi.nlm.nih.gov/42390122/)
- **Journal**: The Journal of international medical research
- **Publication Date**: 2026 Jul
- **Authors**: Jin Shengyu, Duan Jintao, Chen Zhanheng, Chen Fangfang, Fang Wei et al.
- **DOI**: https://doi.org/10.1177/03000605261461196

### Abstract

ObjectiveThe traditional method of intraspinal anesthesia relies on surface anatomical landmarks for positioning, which is associated with a low accuracy rate. In addition, the procedure remains challenging, and the identification of anatomical structures is complex. This study aimed to develop an adaptive attention U-network to enhance the segmentation performance of spinal structures under ultrasound images.MethodsUltrasound videos of the spines were collected from 80 pregnant women, yielding a total of 1000 annotated images that were used to establish a novel database, spine ultrasound image dataset. Adaptive attention U-network uses the multidepth convolution kernel and adaptive local channel attention modules to effectively extract multiscale features. Subsequently, the global attention gate module and multiscale adaptive dynamic modulation were introduced to capture critical features and enhance image super-resolution performance. Comprehensive experiments were conducted on the spine ultrasound image dataset and public breast ultrasound images dataset, in which adaptive attention U-network was juxtaposed with other current medical image segmentation models using metrics including dice similarity coefficient.ResultsOn the spine ultrasound image dataset, adaptive attention U-network achieved a mean dice similarity coefficient of 0.905. In external validation using the breast ultrasound images dataset, the network's segmentation of benign tumor structures reached a dice similarity coefficient of 0.857, demonstrating superior generalization capabilities. Adaptive attention U-network demonstrated consistent segmentation stability across all tested structures.ConclusionsThe proposed adaptive attention U-network significantly enhances the segmentation accuracy for spinal anatomical structures in ultrasound images, demonstrating superior precision compared with existing methods.

---

## 9. A large language models-assisted and expert-corrected workflow for preoperative anesthesia assessment drafts: A single-centre exploratory feasibility study.

- **PMID**: [42628268](https://pubmed.ncbi.nlm.nih.gov/42628268/)
- **Journal**: Medicina clinica
- **Publication Date**: 2026 Aug 21
- **Authors**: Gu Shuhan, Ping Jianfan, Lin Huidan, Xu Hui, Fang Fuquan et al.
- **DOI**: https://doi.org/10.1016/j.medcli.2026.107571

### Abstract

**BACKGROUND**: Large language models (LLMs) may help organize clinical information, but their use in perioperative settings requires careful evaluation because errors may have immediate safety implications. This study aimed to describe the feasibility and perceived usefulness of a single-centre, expert-corrected LLM workflow for preparing preoperative anesthesia assessment drafts for complex consultation cases. Secondary aims were to describe error patterns identified by anesthesiologists and to explore residents' perceptions after reviewing expert-corrected materials. **METHODS**: We retrospectively selected 15 complex preoperative anesthesia consultation cases from The First Affiliated Hospital, Zhejiang University School of Medicine. Complex cases were defined as cases referred for specialized preoperative anesthesia consultation because of multiple comorbidities, clinically relevant organ dysfunction, implanted devices, major cardiopulmonary or vascular disease, or other features requiring individualized anesthetic assessment. A large language model-based artificial intelligence system, DeepSeek-R1, was used to generate structured draft assessments from de-identified case information and a standardized prompt. The original LLM-generated drafts were independently reviewed by three experienced anesthesiologists for information completeness, scientific plausibility, and focus on key risk factors. All resident-facing documents were then corrected by senior anesthesiologists before being distributed to first-year anesthesia residents, who completed a questionnaire on perceived usefulness, guidance value, educational support, and error recognition. No comparator group, blinding, or objective performance outcome was included. **RESULTS**: The LLM-generated drafts were structurally complete but contained clinically relevant errors, mainly in risk assessment and anesthetic plan formulation. Thirty-two error instances were identified across the 15 cases, including errors

---

## 10. Real-Time AI Voice Translation for International Medical Conferences and Beyond: Enabling Multilingual Scientific Exchange.

- **PMID**: [42619416](https://pubmed.ncbi.nlm.nih.gov/42619416/)
- **Journal**: Paediatric anaesthesia
- **Publication Date**: 2026 Aug 19
- **Authors**: Matava Clyde, Voit Benjamin, Schmitz Achim, Engelhardt Thomas
- **DOI**: https://doi.org/10.1002/pan.70288

### Abstract

**BACKGROUND**: Language barriers continue to limit participation in international medical communication, and recent advances in artificial intelligence now enable real-time voice translation to support multilingual scientific exchange. **APPROACH**: We describe a demonstration of a bidirectional AI-mediated voice translation configuration at a pediatric anesthesia conference and consider its broader applicability across medical communication contexts. Outbound delivery used real-time speech translation with speaker-matched voice synthesis; inbound comprehension of audience questions used earpiece-based live translation. The system was assembled using widely available consumer and enterprise technologies and required no dedicated institutional infrastructure. **OBSERVATIONS**: A presession check indicated that most attendees were comfortable in English, so the outbound synthesized voice was used only for the introduction of the lecture, with the remainder delivered in English; inbound earpiece translation was used throughout the question-and-answer period. No audience-level outcomes were measured, and no evaluative claims about comprehension or accuracy are made. **IMPLICATIONS**: This approach highlights three features relevant to international medical exchange: preservation of the speaker's vocal identity, bidirectional communication, and scalability without reliance on professional interpretation services. This novel configuration lies within a rapidly evolving ecosystem of AI translation tools and discusses practical considerations, including technical limitations, acoustic requirements, and the importance of transparent disclosure. Although not a substitute for professional interpretation in all contexts, real-time AI voice translation may represent a feasible and increasingly accessible strategy to reduce linguistic barriers in conferences and other forms of international collaboration. Wider adoption may support more inclusive participation and improve the gl

---

## 11. Safety in the Age of Artificial Intelligence: Evaluating Large Language Model Adherence to Antithrombotic Medication and Regional Anesthesia Guidelines.

- **PMID**: [42614371](https://pubmed.ncbi.nlm.nih.gov/42614371/)
- **Journal**: Cureus
- **Publication Date**: 2026 Aug
- **Authors**: Willson Conner M, Thind Birpartap S, Srinivas Jay, Gupta Anita
- **DOI**: https://doi.org/10.7759/cureus.114071

### Abstract

The release of the 2025 American Society of Regional Anesthesia (ASRA) 5th edition guidelines for regional and neuraxial anesthesia procedures for patients receiving antithrombotic medications introduced complex, patient-specific hold times and resumption protocols. As clinicians increasingly utilize large language models (LLMs) as clinical decision support tools, the reliability of these models remains largely unvalidated. This study evaluates the accuracy of two of the foremost LLMs, ChatGPT (OpenAI, San Francisco, CA) and Google Gemini (Google DeepMind, London, UK), in adhering to these new gold-standard safety guidelines. Twenty-five standardized clinical vignettes were developed. Each vignette featured a patient on a specific anticoagulant (e.g., rivaroxaban, apixaban, dabigatran) requiring a neuraxial or regional anesthetic procedure (stratified by high-risk vs. low-risk). Variables included renal function, dose frequency, and procedural urgency. Prompts were submitted to the latest publicly available ChatGPT and Google Gemini models with separate instructions to provide hold and resumption times. LLMs were queried to ensure familiarity with 2025 ASRA guidelines prior to submission of prompts. Responses were graded against the 2025 ASRA guidelines by independent reviewers. Response adherence was categorized as: 1. concordant (100% match); 2. conservative error (LLM recommended time was longer than required); 3. dangerous error (recommended time was shorter than required, a critical safety violation); or 4. omission (no specific timeframe provided). ChatGPT achieved a concordance rate of 64%, compared to Gemini at 62%. However, the models displayed distinct error profiles. ChatGPT produced "dangerous errors" in 20% of evaluations and failed to specify a time in 16% of cases. In contrast, Gemini's dangerous error rate was lower at 12%, but it demonstrated a significant "conservative error" rate of 22%, compared to 0% for ChatGPT. A chi-square test indicated that

---

## 12. Correction: Safety in the Age of Artificial Intelligence: Evaluating Large Language Model Adherence to Antithrombotic Medication and Regional Anesthesia Guidelines.

- **PMID**: [42614330](https://pubmed.ncbi.nlm.nih.gov/42614330/)
- **Journal**: Cureus
- **Publication Date**: 2026 Aug
- **Authors**: Willson Conner M, Thind Birpartap S, Srinivas Jay, Gupta Anita
- **DOI**: https://doi.org/10.7759/cureus.c472

### Abstract

[This corrects the article DOI: 10.7759/cureus.114071.].

---

## 13. Current Status and Future Projections of Artificial Intelligence-Assisted Ultrasonography and Needle Visibility Methods in Regional Anesthesia.

- **PMID**: [42364233](https://pubmed.ncbi.nlm.nih.gov/42364233/)
- **Journal**: The Eurasian journal of medicine
- **Publication Date**: 2026 Apr 24
- **Authors**: Tire Yasin, Mermer Aydın, Aydemir Mustafa, Keklicek Ömer, Koç Muhammed Nezih et al.
- **DOI**: https://doi.org/10.5152/eurasianjmed.2026.261453

### Abstract

Ultrasound-guided regional anesthesia (UGRA) has revolutionized regional anesthesia by enabling direct visualization of neural structures, surrounding anatomy, and local anesthetic spread. However, consistent needle visualization remains challenging due to anisotropy, steep insertion angles, tissue deformation, and ultrasound artifacts, potentially increasing procedural difficulty and the risk of complications such as vascular puncture, pneumothorax, or intraneural injection. Recent advances in artificial intelligence (AI) offer promising solutions. Artificial intelligence-assisted ultrasound systems using deep learning and convolutional neural networks can perform real-time anatomical segmentation, automated needle tracking, and image optimization. These platforms highlight nerves, vessels, and fascial planes with color overlays, guide needle trajectory, and provide feedback on image quality and probe positioning. In addition to procedural assistance, AI may improve training by accelerating anatomical recognition and reducing inter-operator variability. Nevertheless, concerns persist regarding automation bias, algorithm performance in atypical anatomy, and the necessity of ongoing clinician oversight. Overall, AI-assisted ultrasonography represents a significant step toward safer, more standardized, and potentially more efficient regional anesthesia practice. Cite this article as: Tire Y, Mermer A, Aydemir M, Keklicek Ö, Koç MN, Yazar MA. Current status and future projections of artificial intelligence-assisted ultrasonography and needle visibility methods in regional anesthesia. Eurasian J Med. 2026, 58(3), 1453, doi: 10.5152/eurasianjmed.2026.261453.

---

## 14. Advances in AI for detecting pulmonary inflammation and perioperative medicine: a mini-review.

- **PMID**: [42577597](https://pubmed.ncbi.nlm.nih.gov/42577597/)
- **Journal**: Frontiers in medicine
- **Publication Date**: 2026
- **Authors**: Huang Kecheng, Liang Xiaoyang, Pi Rongpeng, Dai Junmin, Lei Xinping et al.
- **DOI**: https://doi.org/10.3389/fmed.2026.1865505

### Abstract

With increasing human longevity, early recognition and treatment of pneumonia in the elderly are crucial to prevent disease progression. Artificial intelligence (AI) is rapidly transforming the detection and management of pulmonary inflammation (pneumonia, COVID-19 lung damage). Accurate preoperative assessment of pneumonia contributes to improved perioperative surgical and anesthesia management. This mini-review highlights key advances: (1) Hybrid deep learning models achieve high accuracy (>96%) in analyzing ultrasound videos for disease differentiation. (2) Self-supervised learning enables expert-level X-ray interpretation without extensive annotations. (3) Multimodal integration combines imaging (CT/X-ray) with clinical data, enhancing lesion visibility and pathogen-specific diagnosis (viral vs. bacterial AUC: 0.95). Clinically, AI demonstrates high efficacy in COVID-19 detection (AUC: 0.992), pediatric pneumonia diagnosis (89-96% accuracy), and identifying post-COVID complications. Despite this promise, challenges remain, including data bias, limited pediatric datasets, "black-box" model interpretability, and ethical concerns. Future progress depends on expanding diverse training data (e.g., via federated learning), integrating explainable AI (XAI), and ensuring equitable access. In conclusion, AI offers accurate, scalable solutions for pulmonary inflammation diagnostics, with significant potential to augment clinical decision-making and extend into proactive areas like perioperative medicine for complication screening and prevention.

---

## 15. Transforming endoscopic retrograde cholangiopancreatography: the role of artificial intelligence in pre-operative planning, intraoperative navigation, and post-operative risk prediction.

- **PMID**: [42558445](https://pubmed.ncbi.nlm.nih.gov/42558445/)
- **Journal**: Frontiers in medicine
- **Publication Date**: 2026
- **Authors**: Wang Yaoqi, Peng Ya, Wang Zheng, Liu Peng, Chen Zhiyuan
- **DOI**: https://doi.org/10.3389/fmed.2026.1879402

### Abstract

Endoscopic Retrograde Cholangiopancreatography (ERCP) is a technically demanding procedure for pancreaticobiliary diseases. Artificial intelligence (AI) is transforming ERCP by improving diagnostic accuracy, procedural safety, and postoperative risk prediction. This review synthesizes AI applications across the entire workflow: preoperative planning using multimodal risk models, intraoperative navigation via real-time anatomical localization and augmented reality, and postoperative complication prediction with dynamic algorithms. AI also optimizes anesthesia and ambulatory surgery workflows. Challenges remain in data standardization, legal accountability, and clinical integration. We advocate for multicenter collaboration, ethical oversight, and comprehensive patient management systems to establish AI-assisted ERCP as a new standard for personalized interventional care.

---

## 16. Machine learning-based prediction of postoperative nausea and vomiting after spinal anesthesia: A retrospective observational study.

- **PMID**: [42555606](https://pubmed.ncbi.nlm.nih.gov/42555606/)
- **Journal**: PloS one
- **Publication Date**: 2026
- **Authors**: Hoshijima Hiroshi, Miyazaki Tomo, Omachi Shinichiro, Konno Daisuke, Sugino Shigekazu et al.
- **DOI**: https://doi.org/10.1371/journal.pone.0333162

### Abstract

Postoperative nausea and vomiting (PONV) is a frequent and serious complication after surgery. PONV also reduces patient satisfaction with surgery under spinal anesthesia and increases medical costs due to prolonged hospitalization. The purpose of this study is to apply artificial intelligence (AI) machine learning analysis to identify risk factors for PONV in patients undergoing surgery with spinal anesthesia. This retrospective study used artificial intelligence to analyze data of adult patients (aged ≥20 years) who underwent surgery under spinal anesthesia at Tohoku University Hospital from January 1, 2010 to December 31, 2022. To evaluate PONV, patients who experienced nausea and/or vomiting or used antiemetics within 24 hours after surgery were extracted from postoperative medical records. The selected data were analyzed after propensity score matching with patients who did not experience PONV. We created an ensemble model for predicting the probability of PONV using five machine learning algorithms: random forest, gradient boosting machine, k-nearest neighbor, multilayer perceptron, and decision tree. Data were available for 4,574 patients. We performed propensity score matching and selected 538 patients for analysis (269 in the PONV group and 269 in the non-PONV group). The use of postoperative fentanyl was identified as the strongest contributor to PONV, followed by duration of surgery, body mass index (BMI), total urine output, and duration of anesthesia. The identified risk factors were female sex, BMI < 25 kg/m2, and duration of surgery (< 60 min), duration of anesthesia (< 100 min), cesarean section, use of postoperative fentanyl, administration of fentanyl/ morphine into the spinal arachnoid, and puncture level of epidural anesthesia (Th7-12) were identified as anesthesia/surgery-related risk factors. We used machine learning AI to evaluate risk factors for PONV after spinal anesthesia. We identified several patient-related and anesthesia/surgery-relate

---

## 17. Evaluating ChatGPT's accuracy in predicting postoperative nausea and vomiting risk and antiemetic prophylaxis planning: A study on simulated patient profiles.

- **PMID**: [42553948](https://pubmed.ncbi.nlm.nih.gov/42553948/)
- **Journal**: Saudi journal of anaesthesia
- **Publication Date**: 2026
- **Authors**: Ahmed Hubba, Usman Tooba, Mahmood Alina, Masnoon Umama, Hashmi Maria et al.
- **DOI**: https://doi.org/10.4103/sja.sja_212_26

### Abstract

**BACKGROUND**: Postoperative nausea and vomiting (PONV) is a distressing condition following general anesthesia. The Apfel Simplified Score (SRS) is used to calculate the score and guide antiemetic prophylaxis as per Society of Ambulatory Anesthesia (SAMBA) guidelines. The use of generative AI models in exploring the risk calculation and guiding antiemetic prophylaxis remains unexplored. **OBJECTIVE**: The study aims to investigate the accuracy of ChatGPT 4.0 unpaid version in determining the Apfel score and its adherence to the SAMBA antiemetic prophylaxis guideline recommendations using simulated patient profiles. **METHODOLOGY**: Our study was conducted in the Department of Anesthesiology on 100 simulated patient profiles. The study was completed in 2 months after approval by the Institutional Review Board of Dow University of Health Sciences. Data were collected and analyzed using SPSS. A pilot study was conducted to determine the sample size for the study. The simulated profiles were generated by the researchers, and then ChatGPT was asked to calculate their Apfel scores. Experienced anesthesiologists were asked to calculate the same variables for the profiles, but they were blinded to ChatGPT's responses. **RESULTS**: Among 100 simulated patient profiles, 99 profiles were scored correctly by ChatGPT and showed near-perfect agreement with anesthesiologists (Cohen's κ = 0.975, P < 0.001), with 98% concordance in risk stratification (κ = 0.953, P < 0.001). However, ChatGPT's adherence to SAMBA anti-emetic prophylaxis guidelines was low, showing only 31% correct recommendations in simulated profiles (κ = 0.141, P < 0.001). **CONCLUSION**: ChatGPT can be reliably used to determine the correct Apfel score of the patients, and it can accurately classify patients into risk categories. However, its recommendations of antiemetic agents as per the SAMBA guidelines are inconsistent, necessitating human oversight for guideline-based management. Such large language models 

---

## 18. Development of a radiomics-vision transformer fusion model based on chest CT for predicting adverse respiratory events during recovery in elderly hip fracture patients under general anesthesia.

- **PMID**: [42620817](https://pubmed.ncbi.nlm.nih.gov/42620817/)
- **Journal**: Frontiers in medicine
- **Publication Date**: 2026
- **Authors**: Hu Jiasen, Wu Yuxuan, Lin Jiancai, Chen Xuewen
- **DOI**: https://doi.org/10.3389/fmed.2026.1907086

### Abstract

**BACKGROUND**: Hip fracture is a common and serious injury in the elderly. With the aging of the global population, the incidence of hip fracture is increasing. Adverse Respiratory Events (AREs) are common in elderly patients with hip fracture during recovery from general anesthesia, which can lead to serious complications. However, current methods for predicting these events are limited. **METHODS**: This retrospective multicohort study analyzed clinical data from 664 patients across two institutions. Radiomic features were extracted from regions of interest (ROIs) in chest CT scans, and deep learning features were extracted using a vision transformer (ViT) model. A radiomics-ViT fusion model was developed by combining these features. The performance of the models was evaluated using metrics such as area under the curve (AUC), sensitivity, specificity, and F1-score. **RESULTS**: The radiomics-ViT fusion model demonstrated excellent performance, with an AUC of 0.994 in the internal training set and 0.875 in the external test set. This was significantly better than the XGBoost model (AUC 0.553) and the ViT model alone (AUC 0.788) in the external test set. The fusion model accurately identified high-risk patients, enabling timely interventions and improved outcomes. **CONCLUSION**: The developed radiomics-ViT fusion model serves as a valuable tool for predicting AREs during recovery in elderly hip fracture patients under general anesthesia, enhancing clinical decision-making and patient care.

---
