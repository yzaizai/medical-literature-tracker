# AnesthesiaAI - PubMed Latest Papers

**Update Time**: 2026-09-10
**Search Range**: Last 30 days
**Papers Found**: 10

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

## 2. Effects of convolutional neural network models on the segmentation of the interscalene brachial plexus in ultrasound imaging for radiomics.

- **PMID**: [42701471](https://pubmed.ncbi.nlm.nih.gov/42701471/)
- **Journal**: Quantitative imaging in medicine and surgery
- **Publication Date**: 2026 Sep 01
- **Authors**: Zhao Yaoping, Cai Nan, Zhong Hao, Zheng Shaoqiang, Zhu Feng et al.
- **DOI**: https://doi.org/10.21037/qims-2026-0588

### Abstract

**BACKGROUND**: The application of artificial intelligence (AI) in ultrasound (US)-guided regional anesthesia has expanded, particularly in enhancing the accuracy, safety, and training effectiveness of procedures through deep learning-based anatomical segmentation. This study aimed to develop and validate an automatic segmentation model for supraclavicular-to-interscalene brachial plexus block (ISB) using the You Only Look At CoefficienTs (YOLACT) algorithm and to compare its performance with that of a U-Net model. **METHODS**: A total of 1,100 patients scheduled to undergo ISB were enrolled. US images encompassing the anatomical range from the supraclavicular fossa to the C7 vertebral level were acquired by experienced anesthesiologists. Images were annotated to identify the brachial plexus nerve, anterior scalene muscle (ASM), middle scalene muscle (MSM), and subclavian artery (SA). YOLACT and U-Net models were trained for automatic segmentation. Model performance was assessed using Intersection over Union (IoU), Dice similarity coefficient (DSC), Hausdorff distance (HD), the proportion of images with a brachial plexus nerve IoU > 0.5, and segmentation accuracy metrics. **RESULTS**: A total of 6,600 US images were analyzed. The YOLACT model demonstrated significantly higher IoU and DSC values and lower HD values compared with the U-Net model for segmentation of the brachial plexus nerve, ASM, MSM, and SA (P<0.001). The proportion of images with a brachial plexus nerve IoU greater than 0.5 was also significantly higher with YOLACT (P<0.001). **CONCLUSIONS**: An automatic segmentation model for ISB, spanning the supraclavicular region to the C7 level, was developed using the YOLACT algorithm. Although quantitative performance metrics favored YOLACT over U-Net, subjective accuracy assessments were comparable between models. Further studies using larger datasets are required to clarify the potential clinical applicability of this approach.

---

## 3. Dynamic Aware Biopsy Needle Identification in Ultrasound Images Using Temporal Prior Guided U-Net Cross Transformer With Limited Training Data.

- **PMID**: [42486749](https://pubmed.ncbi.nlm.nih.gov/42486749/)
- **Journal**: Ultrasound in medicine & biology
- **Publication Date**: 2026 Oct
- **Authors**: Lee Myeongjin, Beom Dong Gyu, Bae Eun Hui, Kim Soo Wan, Kim Chang Seong et al.
- **DOI**: https://doi.org/10.1016/j.ultrasmedbio.2026.06.024

### Abstract

**OBJECTIVE**: Ultrasound-guided needle placement has been commonly used for minimally invasive clinical procedures, including biopsy, regional anesthesia and localized drug administration. This study aimed to enhance existing deep learning frameworks by incorporating a classical background subtraction, which enriches the inductive bias and thereby enables more reliable needle detection even when the available training dataset is small. **METHODS**: Although deep learning methods such as U-Net and its derivatives have substantially advanced needle localization performance, they remain constrained by a limited receptive field that prevents effective modeling of long-range spatial dependencies. Although Vision Transformer overcomes this limitation through self-attention mechanisms, it demands large-scale training data and tends to sacrifice fine-grained spatial locality. To overcome these limitations, we propose U-Net Cross Transformer (UXFormer), a dynamic-aware hybrid architecture that combines classical background subtraction with an integrated U-Net × Vision Transformer fusion framework. The model comprises three key components: (i) null subspace-based extraction of temporal prior information, (ii) a temporal-to-spatial cross-attention module during encoding and (iii) a global-to-local cross-convolutional block attention module during decoding, enabling continuous bidirectional communication between localized temporal dynamics and globally contextualized spatial representations. **RESULTS**: Experimental results demonstrate that the proposed method outperforms multiple competing approaches, achieving significant improvements: a 14.2% increase in Jaccard index, a 9.0% increase in Dice score, 8.5% increase in recall, 5.5% increase in precision, and 63.5% increase in the 95th percentile Hausdorff distance, thus leading to a 44.0% improvement in tip position error and a 17.7% improvement in trajectory angle error, even under varying needle visibility conditions. **CON

---

## 4. Pupil-DLC: An open-source deep learning pipeline for scalable, marker-less tracking of pupil dynamics across conscious and unconscious states.

- **PMID**: [42401399](https://pubmed.ncbi.nlm.nih.gov/42401399/)
- **Journal**: Journal of neuroscience methods
- **Publication Date**: 2026 Nov
- **Authors**: Seyfourian Parsa, Marks Lydia C, Claar Leslie D, Nahas Yasmeen, Keating Miles et al.
- **DOI**: https://doi.org/10.1016/j.jneumeth.2026.110848

### Abstract

**BACKGROUND**: Pupil diameter is a non-invasive biomarker of brain state, correlating with arousal, attention, cognitive processing, and consciousness. However, existing pupillometry software often lacks scalability and robustness across diverse experimental conditions and species. **NEW METHOD**: We introduce Pupil-DLC, an open-source, offline, DeepLabCut-based pipeline for scalable, marker-less pupil tracking, primarily designed for mice. Trained on 21,909 manually annotated frames from over 140 videos of head-fixed mice spanning wakefulness and drug-induced states, including psychedelics and anesthesia, the dataset was deliberately selected to maximize pupil size variability and model generalization. Pupil-DLC implements a dual-model architecture: a General Model (GM) for high-throughput analysis and an Individual Model (IM) for session-specific optimization. **RESULTS**: Pupil-DLC captures pupil dynamics across awake, psychedelic, and anesthetized conditions with high agreement with ground truth and equal tracking fidelity during active locomotion and quiet rest. Confidence metrics aligned with human frame quality assessments, enabling principled tuning of accuracy-retention trade-offs. As a secondary demonstration, Pupil-DLC extends to unseen human videos across diverse conditions and frame rates, including daylight and smartphone recordings, without retraining. **COMPARISON WITH EXISTING METHODS**: Pupil-DLC outperforms existing automated methods in accuracy and frame retention while maintaining computational efficiency comparable to real-time tools. These improvements stem from a learned keypoint-based representation robust to pupil shape variability, occlusions, reflections, and imaging artifacts. The GM/IM framework supports a tiered strategy balancing throughput and precision. **CONCLUSIONS**: Pupil-DLC provides a reproducible, adaptable platform for quantifying pupil-linked brain state dynamics across experimental paradigms and species, bridging basic mo

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

## 7. An adaptive attention U-network for recognizing ultrasound images.

- **PMID**: [42390122](https://pubmed.ncbi.nlm.nih.gov/42390122/)
- **Journal**: The Journal of international medical research
- **Publication Date**: 2026 Jul
- **Authors**: Jin Shengyu, Duan Jintao, Chen Zhanheng, Chen Fangfang, Fang Wei et al.
- **DOI**: https://doi.org/10.1177/03000605261461196

### Abstract

ObjectiveThe traditional method of intraspinal anesthesia relies on surface anatomical landmarks for positioning, which is associated with a low accuracy rate. In addition, the procedure remains challenging, and the identification of anatomical structures is complex. This study aimed to develop an adaptive attention U-network to enhance the segmentation performance of spinal structures under ultrasound images.MethodsUltrasound videos of the spines were collected from 80 pregnant women, yielding a total of 1000 annotated images that were used to establish a novel database, spine ultrasound image dataset. Adaptive attention U-network uses the multidepth convolution kernel and adaptive local channel attention modules to effectively extract multiscale features. Subsequently, the global attention gate module and multiscale adaptive dynamic modulation were introduced to capture critical features and enhance image super-resolution performance. Comprehensive experiments were conducted on the spine ultrasound image dataset and public breast ultrasound images dataset, in which adaptive attention U-network was juxtaposed with other current medical image segmentation models using metrics including dice similarity coefficient.ResultsOn the spine ultrasound image dataset, adaptive attention U-network achieved a mean dice similarity coefficient of 0.905. In external validation using the breast ultrasound images dataset, the network's segmentation of benign tumor structures reached a dice similarity coefficient of 0.857, demonstrating superior generalization capabilities. Adaptive attention U-network demonstrated consistent segmentation stability across all tested structures.ConclusionsThe proposed adaptive attention U-network significantly enhances the segmentation accuracy for spinal anatomical structures in ultrasound images, demonstrating superior precision compared with existing methods.

---

## 8. Completely free-breathing cardiac MRI using deep learning reconstruction reduces sedation and scan time in children.

- **PMID**: [42658264](https://pubmed.ncbi.nlm.nih.gov/42658264/)
- **Journal**: Pediatric radiology
- **Publication Date**: 2026 Aug 27
- **Authors**: Gupta Aditi, Long William, Young Sara, Blasiole Brian, Mouzakis Nicholas et al.
- **DOI**: https://doi.org/10.1007/s00247-026-06749-1

### Abstract

**BACKGROUND**: Traditional cardiac magnetic resonance (CMR) imaging scan times are long and require breath-holds, often necessitating intubation and mechanical ventilation in young or sick children. **OBJECTIVE**: To compare CMR duration and anesthesia requirement between highly accelerated single cardiac cycle (1RR) free breathing cine acquisition with deep learning reconstruction and conventional segmented breath-hold cine imaging in pediatric patients. **MATERIALS AND METHODS**: Free breathing with deep learning imaging was used in 150 patients and compared to 150 sequential patients imaged with segmented breath-hold imaging. Specifically, CMR duration, use of anesthesia, anesthesia duration, and emergence time were evaluated. A subgroup analysis was performed on patients less than 35 kg. **RESULTS**: CMR duration decreased significantly in the 1RR group (29.2 ± 9.8 min vs 43.0 ± 13.2 min, P<0.01). The use of endotracheal intubation with muscle relaxation during the CMR decreased significantly with free breathing with deep learning sequences for those that required sedation (14% vs 90%, P<0.01), as did anesthesia duration (70.8 ± 24.2 min vs 98.3 ± 26.7 min, P<0.01) and emergence time from anesthesia (15 ± 3.7 min vs 27.1 ± 14.9 min, P<0.01). There was no degradation in contrast-to-noise ratio using blood pool/myocardium contrast difference (534.2 ± 165.1 vs 491.8 ± 165.8, P=0.03). Subanalysis performed on 125 patients (age 12.3 ± 4.1 years) with no significant valve regurgitation confirmed reliable volumetric measurements with free breathing with deep learning given high correlation between both right ventricular cardiac index and main pulmonary artery flow (R=0.92, P<0.001) and left ventricular cardiac index and aorta flow (R=0.84, P<0.001). **CONCLUSIONS**: Free breathing with deep learning single RR acquisition significantly reduces study duration, rates of endotracheal intubation, anesthesia duration, and anesthesia emergence time while maintaining diagnost

---

## 9. Development of a radiomics-vision transformer fusion model based on chest CT for predicting adverse respiratory events during recovery in elderly hip fracture patients under general anesthesia.

- **PMID**: [42620817](https://pubmed.ncbi.nlm.nih.gov/42620817/)
- **Journal**: Frontiers in medicine
- **Publication Date**: 2026
- **Authors**: Hu Jiasen, Wu Yuxuan, Lin Jiancai, Chen Xuewen
- **DOI**: https://doi.org/10.3389/fmed.2026.1907086

### Abstract

**BACKGROUND**: Hip fracture is a common and serious injury in the elderly. With the aging of the global population, the incidence of hip fracture is increasing. Adverse Respiratory Events (AREs) are common in elderly patients with hip fracture during recovery from general anesthesia, which can lead to serious complications. However, current methods for predicting these events are limited. **METHODS**: This retrospective multicohort study analyzed clinical data from 664 patients across two institutions. Radiomic features were extracted from regions of interest (ROIs) in chest CT scans, and deep learning features were extracted using a vision transformer (ViT) model. A radiomics-ViT fusion model was developed by combining these features. The performance of the models was evaluated using metrics such as area under the curve (AUC), sensitivity, specificity, and F1-score. **RESULTS**: The radiomics-ViT fusion model demonstrated excellent performance, with an AUC of 0.994 in the internal training set and 0.875 in the external test set. This was significantly better than the XGBoost model (AUC 0.553) and the ViT model alone (AUC 0.788) in the external test set. The fusion model accurately identified high-risk patients, enabling timely interventions and improved outcomes. **CONCLUSION**: The developed radiomics-ViT fusion model serves as a valuable tool for predicting AREs during recovery in elderly hip fracture patients under general anesthesia, enhancing clinical decision-making and patient care.

---

## 10. Advances in AI for detecting pulmonary inflammation and perioperative medicine: a mini-review.

- **PMID**: [42577597](https://pubmed.ncbi.nlm.nih.gov/42577597/)
- **Journal**: Frontiers in medicine
- **Publication Date**: 2026
- **Authors**: Huang Kecheng, Liang Xiaoyang, Pi Rongpeng, Dai Junmin, Lei Xinping et al.
- **DOI**: https://doi.org/10.3389/fmed.2026.1865505

### Abstract

With increasing human longevity, early recognition and treatment of pneumonia in the elderly are crucial to prevent disease progression. Artificial intelligence (AI) is rapidly transforming the detection and management of pulmonary inflammation (pneumonia, COVID-19 lung damage). Accurate preoperative assessment of pneumonia contributes to improved perioperative surgical and anesthesia management. This mini-review highlights key advances: (1) Hybrid deep learning models achieve high accuracy (>96%) in analyzing ultrasound videos for disease differentiation. (2) Self-supervised learning enables expert-level X-ray interpretation without extensive annotations. (3) Multimodal integration combines imaging (CT/X-ray) with clinical data, enhancing lesion visibility and pathogen-specific diagnosis (viral vs. bacterial AUC: 0.95). Clinically, AI demonstrates high efficacy in COVID-19 detection (AUC: 0.992), pediatric pneumonia diagnosis (89-96% accuracy), and identifying post-COVID complications. Despite this promise, challenges remain, including data bias, limited pediatric datasets, "black-box" model interpretability, and ethical concerns. Future progress depends on expanding diverse training data (e.g., via federated learning), integrating explainable AI (XAI), and ensuring equitable access. In conclusion, AI offers accurate, scalable solutions for pulmonary inflammation diagnostics, with significant potential to augment clinical decision-making and extend into proactive areas like perioperative medicine for complication screening and prevention.

---
