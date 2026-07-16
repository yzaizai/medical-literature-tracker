# AnesthesiaAI - PubMed Latest Papers

**Update Time**: 2026-07-16
**Search Range**: Last 30 days
**Papers Found**: 18

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

## 5. A Multitask Time-Frequency Deep Learning Approach for Anesthesia Depth Monitoring and Transition Prediction.

- **PMID**: [42351597](https://pubmed.ncbi.nlm.nih.gov/42351597/)
- **Journal**: Diagnostics (Basel, Switzerland)
- **Publication Date**: 2026 Jun 22
- **Authors**: Kavuncu Saliha Kevser, Yalvac Mehmet, Basturk Alper
- **DOI**: https://doi.org/10.3390/diagnostics16121937

### Abstract

Background: Electroencephalography (EEG) signals are widely used for monitoring anesthesia depth during surgery. Current commercial indicators are largely closed-source and may reflect dynamic changes with some delay. Methods: This study proposes a multitask deep learning model for continuous Bispectral Index (BIS) estimation, binary anesthesia-state classification, and prediction of transitions toward light anesthesia at different time intervals. Dual-channel EEG signals from 5471 surgical cases in the VitalDB dataset were divided into 60 s windows. Short-Time Fourier Transform (STFT) captured instantaneous frequency changes to transform the signal into a two-dimensional map. A ResNet-SE architecture incorporating Squeeze-and-Excitation blocks was used to identify EEG features associated with anesthesia depth. Results: A Mean Absolute Error of 3.27 and a Root Mean Square Error of 5.48 were obtained in anesthesia depth estimation. Light anesthesia classification achieved an AUC of 0.99 on the internal test set. Conclusions: The proposed multitask model enables the assessment of anesthesia depth and transitions toward light anesthesia using EEG signals.

---

## 6. A Real-Time Automated Deep Learning Workflow for Non-invasive High-Magnification Imaging of 

- **PMID**: [42282531](https://pubmed.ncbi.nlm.nih.gov/42282531/)
- **Journal**: bioRxiv : the preprint server for biology
- **Publication Date**: 2026 Jun 04
- **Authors**: Safaeian Parsa, Mahbub Tasnuva Binte, Tahrin Rhythem, Tanha Mohammad, Pellegrino Mark W et al.
- **DOI**: https://doi.org/10.64898/2026.06.01.729022

### Abstract

Caenorhabditis elegans is a premier model organism for aging and neurobiology research, valued for its short lifespan, optical transparency, genetic tractability, and well-mapped nervous system. Non-invasive automated recording of biomarkers is a fundamental goal in modern biology because it preserves natural physiology and eliminates confounds from anesthesia, restraint, or repeated handling in C. elegans. Yet high-magnification imaging of freely moving worms remains a persistent challenge: as magnification increases, the narrowing field of view compounds target loss, motion blur, and focal drift, pushing researchers toward immobilization strategies that compromise physiology, suppress natural behavior, and preclude the continuous longitudinal observation essential for aging and neurobiological studies. Here, we present a real-time tracking workflow for imaging individual worms in a microfluidic platform under controlled culture conditions. The system integrates deep learning head detection, image-based autofocus, and rapid motorized-stage feedback to support stable imaging across multiple magnifications, including neuronal-scale imaging. Hundreds of individually housed worms in separate incubation chambers enable repeated daily imaging of the same animals throughout their lifespan. Built entirely on a commercially available inverted microscope without additional custom hardware, the platform features a modular, user-configurable interface adaptable to diverse microscope setups, specimens, and experimental goals. Fluorescence images from freely moving worms were visually comparable to those from immobilized animals, supporting longitudinal phenotyping in aging and neurobiology studies.

---

## 7. Impact of Deep-Learning Reconstruction on MRI Workflows: A Retrospective Analysis at a Large Academic Tertiary Center.

- **PMID**: [42235553](https://pubmed.ncbi.nlm.nih.gov/42235553/)
- **Journal**: RoFo : Fortschritte auf dem Gebiete der Rontgenstrahlen und der Nuklearmedizin
- **Publication Date**: 2026 Jun 03
- **Authors**: Rizzetti Melina, Michael Arwed E, Almansour Haidara, Schöffling Vanessa I, Brockmann Marc A et al.
- **DOI**: https://doi.org/10.1055/a-2857-0974

### Abstract

**PURPOSE**: Artificial intelligence is increasingly integrated in clinical practice. In radiological imaging, deep-learning (DL)-based image reconstruction techniques show potential for accelerating and enhancing the quality of examination procedures in magnetic resonance imaging (MRI). This study evaluated the impact of DL on MRI workflows and protocols over a one-year period following clinical implementation. **MATERIALS AND METHODS**: This retrospective, single-center study included 8,183 MRI examinations performed between 2023 and 2024 to assess daily examination volume, examination duration, and rates of repeated and aborted scans. Furthermore, 43 comparable sequences and 34 protocols on a 1.5T MRI (Siemens Magnetom Sola) were analyzed and surveys were conducted among 23 medical staff members to evaluate the perceived effects of DL on workflow efficiency, diagnostic performance, stress levels, and technology acceptance. **RESULTS**: 88% of the DL-reconstructed sequences demonstrated reduced acquisition times, yielding an overall 13% reduction in protocol duration, despite higher resolution or reduced slice thickness. On days without anesthesia support, the average examination time decreased by 11%, accompanied by increased patient throughput (+7.2%) and fewer repeats (-25%) and aborts (-100%). Medical staff reported high levels of technology acceptance (90%), perceived improvements in image quality (90.5%), and reduced stress levels. Shorter times required for generating medical reports were noted by 45.5% of respondents, particularly among residents (70%). **CONCLUSION**: DL enables significant potential for MRI-workflow optimization and protocol improvements, while maintaining high staff satisfaction, thereby highlighting the great potential of DL in radiology practice. **KEY POINTS**: · While maintaining or increasing image quality, DL reduced examination duration (-11%) and protocol length (-13%).. · Patient throughput increased (+7.2%), while repeats (-25

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

## 9. Pupil-DLC: An open-source deep learning pipeline for scalable, marker-less tracking of pupil dynamics across conscious and unconscious states.

- **PMID**: [42401399](https://pubmed.ncbi.nlm.nih.gov/42401399/)
- **Journal**: Journal of neuroscience methods
- **Publication Date**: 2026 Jul 04
- **Authors**: Seyfourian Parsa, Marks Lydia C, Claar Leslie D, Nahas Yasmeen, Keating Miles et al.
- **DOI**: https://doi.org/10.1016/j.jneumeth.2026.110848

### Abstract

**BACKGROUND**: Pupil diameter is a non-invasive biomarker of brain state, correlating with arousal, attention, cognitive processing, and consciousness. However, existing pupillometry software often lacks scalability and robustness across diverse experimental conditions and species. **NEW METHOD**: We introduce Pupil-DLC, an open-source, offline, DeepLabCut-based pipeline for scalable, marker-less pupil tracking, primarily designed for mice. Trained on 21,909 manually annotated frames from over 140 videos of head-fixed mice spanning wakefulness and drug-induced states, including psychedelics and anesthesia, the dataset was deliberately selected to maximize pupil size variability and model generalization. Pupil-DLC implements a dual-model architecture: a General Model (GM) for high-throughput analysis and an Individual Model (IM) for session-specific optimization. **RESULTS**: Pupil-DLC captures pupil dynamics across awake, psychedelic, and anesthetized conditions with high agreement with ground truth and equal tracking fidelity during active locomotion and quiet rest. Confidence metrics aligned with human frame quality assessments, enabling principled tuning of accuracy-retention trade-offs. As a secondary demonstration, Pupil-DLC extends to unseen human videos across diverse conditions and frame rates, including daylight and smartphone recordings, without retraining. **COMPARISON WITH EXISTING METHODS**: Pupil-DLC outperforms existing automated methods in accuracy and frame retention while maintaining computational efficiency comparable to real-time tools. These improvements stem from a learned keypoint-based representation robust to pupil shape variability, occlusions, reflections, and imaging artifacts. The GM/IM framework supports a tiered strategy balancing throughput and precision. **CONCLUSIONS**: Pupil-DLC provides a reproducible, adaptable platform for quantifying pupil-linked brain state dynamics across experimental paradigms and species, bridging basic mo

---

## 10. Artificial intelligence assisted telemedicine, clinical decision support for anesthesia and critical care in intensive care units: a scoping review.

- **PMID**: [42393540](https://pubmed.ncbi.nlm.nih.gov/42393540/)
- **Journal**: BMC anesthesiology
- **Publication Date**: 2026 Jul 02
- **Authors**: Yang Qingxia, Li Meixia, Lei Yu
- **DOI**: https://doi.org/10.1186/s12871-026-03997-4

### Abstract

**BACKGROUND**: Artificial intelligence (AI) has been increasingly used in care delivery in intensive care units (ICUs) and anesthesia-critical care practice through telemedicine, tele-ICU systems, and remote patient monitoring, and is expected to support real-time clinical decision-making. **METHODS**: This scoping review followed PRISMA-ScR guidelines to map the existing evidence of AI in critical care and anesthesia-related ICU environments for telemedicine, telemonitoring, and clinical decision support systems. PubMed, Scopus, and Google Scholar were used to search for relevant literature, including the use of AI, telemedicine, predictive analytics, remote monitoring, and anesthesia-informed clinical decision support in critical care. **RESULTS**: The literature reviewed primarily focused on the non-generative AI solutions, such as machine learning, deep learning-based monitoring, and AI clinical decision support systems. Such systems can facilitate remote continuous monitoring, early detection of clinical deterioration, and clinical decision-making in the ICU perioperative anesthesia-critical care settings. The results were grouped into the following categories: tele-ICU implementation, predictive analytics, tele-monitoring, and AI-guided clinical decision support. The reported benefits included better monitoring, improved workflow, enhanced anesthesia and critical care decision-making, and greater access to specialist care, but there was substantial variation in the evidence of consistent improvement in patient-centered outcomes, with most of it being observational. Data quality, interoperability, model transparency, ethical issues, and lack of prospective clinical validation were the key difficulties encountered. **CONCLUSION**: AI-enabled telemedicine remains a nascent healthcare space in the ICU and anesthesia-critical care continuum, and further standardization, validation, and prospective clinical testing are needed to ensure its safe and scalable integra

---

## 11. An adaptive attention U-network for recognizing ultrasound images.

- **PMID**: [42390122](https://pubmed.ncbi.nlm.nih.gov/42390122/)
- **Journal**: The Journal of international medical research
- **Publication Date**: 2026 Jul
- **Authors**: Jin Shengyu, Duan Jintao, Chen Zhanheng, Chen Fangfang, Fang Wei et al.
- **DOI**: https://doi.org/10.1177/03000605261461196

### Abstract

ObjectiveThe traditional method of intraspinal anesthesia relies on surface anatomical landmarks for positioning, which is associated with a low accuracy rate. In addition, the procedure remains challenging, and the identification of anatomical structures is complex. This study aimed to develop an adaptive attention U-network to enhance the segmentation performance of spinal structures under ultrasound images.MethodsUltrasound videos of the spines were collected from 80 pregnant women, yielding a total of 1000 annotated images that were used to establish a novel database, spine ultrasound image dataset. Adaptive attention U-network uses the multidepth convolution kernel and adaptive local channel attention modules to effectively extract multiscale features. Subsequently, the global attention gate module and multiscale adaptive dynamic modulation were introduced to capture critical features and enhance image super-resolution performance. Comprehensive experiments were conducted on the spine ultrasound image dataset and public breast ultrasound images dataset, in which adaptive attention U-network was juxtaposed with other current medical image segmentation models using metrics including dice similarity coefficient.ResultsOn the spine ultrasound image dataset, adaptive attention U-network achieved a mean dice similarity coefficient of 0.905. In external validation using the breast ultrasound images dataset, the network's segmentation of benign tumor structures reached a dice similarity coefficient of 0.857, demonstrating superior generalization capabilities. Adaptive attention U-network demonstrated consistent segmentation stability across all tested structures.ConclusionsThe proposed adaptive attention U-network significantly enhances the segmentation accuracy for spinal anatomical structures in ultrasound images, demonstrating superior precision compared with existing methods.

---

## 12. DMRNet: a dynamic multi-scale residual network for Shamrock view and lumbar plexus segmentation.

- **PMID**: [42284483](https://pubmed.ncbi.nlm.nih.gov/42284483/)
- **Journal**: Computer assisted surgery (Abingdon, England)
- **Publication Date**: 2026 Dec
- **Authors**: Cui Haipo, Wang Yuxiang, Lin Liangqing, Wu Qinghua, Zhou Miao et al.
- **DOI**: https://doi.org/10.1080/24699322.2026.2677269

### Abstract

Lumbar plexus block (LPB) is a regional anesthesia technique widely used for hip and knee surgeries. However, despite the assistance of ultrasound guidance, the complex anatomical structure of the lumbar plexus poses significant challenges for anesthesiologists during the procedure. To accurately identify the lumbar plexus located in the posterior third of the psoas major in the Shamrock view, a deep learning-based segmentation model named DMRNet was proposed. This model is designed to precisely delineate muscles, nerves, and bony structures in Shamrock view ultrasound images. DMRNet integrates several innovative modules, including Adaptive Multi-Scale Dilated (AMD) Module that enhances the model's ability to capture multi-scale features; Dense Attention Residual (DAR) Module that adaptively selects salient feature regions; Attention-Enhanced Hybrid (AEH) Module that emphasizes critical features while suppressing irrelevant ones; and two attention mechanisms, Boundary-Aware Spatial Attention Mechanism (BASA) and the Enhanced Residual Multi-Head Attention Mechanism (ER-MHA), that improve the model's capacity to recognize complex contextual patterns. Experimental results demonstrated that DMRNet achieved a mean Intersection over Union of 0.863 and a mean Dice coefficient of 0.926 across all target structures, outperforming other state-of-the-art models. These findings suggest that DMRNet may serve as a useful assistive tool for sonoanatomical recognition in Shamrock view ultrasound images and may provide educational support for ultrasound-guided LPB training. A dynamic multi-scale residual network is proposed for lumbar lexus (LP) segmentation.Two attention mechanisms were improved, and three modules were proposed to improve downsampling, skip connection, and upsampling.We built our own Shamrock view ultrasound database containing the lumbar plexus nerves, and the Anesthesiologist physician of the anesthesiology department annotated it using Labelme.External validatio

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

## 14. From prediction to practice: closing the translation gap in artificial intelligence for anesthesia.

- **PMID**: [42018224](https://pubmed.ncbi.nlm.nih.gov/42018224/)
- **Journal**: Journal of clinical monitoring and computing
- **Publication Date**: 2026 Apr 22
- **Authors**: Baliga Janardhan, Seshadri Niranjan
- **DOI**: https://doi.org/10.1007/s10877-026-01434-y

### Abstract

Artificial intelligence (AI) and machine learning (ML) techniques are rapidly advancing in anesthesiology, showing promise in patient monitoring, outcome prediction, clinical decision support, and automated drug delivery. However, a substantial gap remains between algorithmic capability and practical implementation at the bedside. This narrative review examines the current state of AI/ML applications in anesthesia, including predictive analytics, closed-loop control systems, AI-assisted imaging, workflow optimization, and anesthesia planning, and explores the translational barriers that have limited routine clinical adoption. We discuss technical, organizational, regulatory, and cultural challenges impeding translation, including data quality issues, EHR interoperability constraints, lack of outcome-oriented clinical evidence, business model uncertainty, interpretability concerns, alarm fatigue, and regulatory ambiguity. Strategies to close this gap are proposed, including rigorous prospective validation, interdisciplinary collaboration with industry and payers, post-deployment model surveillance, training data transparency, user-centered design, and implementation science principles. Ethical and legal considerations, encompassing algorithmic bias, accountability for autonomous AI recommendations, privacy beyond de-identification, and equitable access, are also reviewed. A conceptual framework, summary table of applications, and practical implementation checklist are provided. Bridging the translational divide is essential for AI to fulfill its potential in improving anesthesia care, and will require coordinated action from clinicians, researchers, technologists, regulators, and healthcare institutions.

---

## 15. Automated Identification of Cardiopulmonary Disease Cases for Preoperative Risk Stratification Using Machine Learning: A Retrospective Analysis.

- **PMID**: [41985030](https://pubmed.ncbi.nlm.nih.gov/41985030/)
- **Journal**: A&A practice
- **Publication Date**: 2026 Apr 01
- **Authors**: Aggarwal Ishan, Rhee Christopher, Chura Mamta, Bora Vaibhav, Reddy Devarapalli M
- **DOI**: https://doi.org/10.1213/XAA.0000000000002183

### Abstract

**BACKGROUND**: Preoperative chart review is time-consuming and prone to errors, particularly for cardiopulmonary conditions that impact anesthetic planning. We developed a guideline-aligned "clinical insight bot" that mines free-text documentation to surface perioperative cardiovascular risk signals relevant to the 2024 Mult Society perioperative guideline for noncardiac surgery. **METHODS**: We analyzed 1000 de-identified medical cases from the PhysioNet MIMIC database. Medical terminology was extracted using regex-based NLP and categorized into 13 clinical specialties. Text features were encoded using TF-IDF vectorization and 1536-dimensional semantic embeddings stored in a PostgreSQL vector database (pgvector). Four machine learning models-Logistic Regression, Random Forest, Support Vector Machine (SVM), and Naive Bayes-were trained with stratified fivefold cross-validation to classify cases as "cardiopulmonary-only" versus "mixed/other." Performance was evaluated using accuracy, precision, recall, and F1 score, with statistical comparison via McNemar's test and bootstrap confidence intervals. **RESULTS**: In a held-out test set of 200 notes (28 positive; 172 negatives; ~14% prevalence), a linear support vector machine achieved the best overall balance (F1 ≈ 0.71), with high precision (positive predictive value 0.94) and very low false positive rate (FPR) (1/172 ≈ 0.6%). False negatives were the dominant residual error class. The pipeline processed documents near-instantaneously and, when scaled to 1000 notes, replaced on the order of tens of clinician review hours (≈100× efficiency gain) while maintaining performance across common preoperative document types. **CONCLUSIONS**: A lightweight, guideline-aligned insight bot can transform unstructured preoperative notes into concise, stepwise prompts that flag cardiovascular risk signals before the day of surgery. High precision with a very low FPR supports safe integration with anesthesiology workflows by minimizin

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
