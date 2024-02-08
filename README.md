# Modelling the Adoption Process of Technology Using Artificial Intelligence Methods

[![GitHub Repository](https://img.shields.io/badge/GitHub-Forecasting%20Adoption%20Rate-blue?style=flat-square&logo=github)](https://github.com/faridnec/forecasting-tech-adoption) 

![S Curve Output](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/s_curve.png?raw=true)

> [!NOTE]
> This project is still under development.

## CHECKPOINT

- [x] Conducting Research on Patents Analysis, AI Methods, and Adoption/Innovation Models.
- [x] Collecting patents data from the USPTO database.
- [x] Modeling UAV Technologies using S-Curve Adoption/Innovation Difussion Model.
- [x] Data Preprocessing: Data Cleaning, Formatting, Feature Engineering (`['SECTION','YEAR']`)
    - [ ] One Hot Encoding
    - [ ] Missing Values
- [ ] Exploratory Data Analysis (EDA)
- [x] Innovation Models (S-Curve, Logistic Growth Model)
- [ ] SSTT Taxonomy Classificator Model
- [ ] Cluster

## PURPOSE

This project implement machine learning - particularly deep learning methods - to model and predict the adoption process of technology. Utilizing feed-forward multilayered neural networks (such as CNN or RNN or combination). The aim is to compare and evaluate the results from adoption models such as S Curve, BASS Diffusion Model, Pearl, Gompertz, and Logistic Model. Hence, it is to understand, model, predict the rate of technology adoption and informing strategies for enhancing the integration of technologies.

### Project Structure

```plaintext
forecasting-tech-adoption/
├── data/                      # Data files
│   ├── raw/                   
│   └── processed/
├── img/                       # Images
├── notebooks/                 # Jupyter notebooks
├── src/                       # Source code
├── docs/                      # Project documentation
├── .gitattributes             
├── .gitignore                 
└── README.md              
```

## METHODS

1. DATA COLLECTION
   
   - Data collection focused on patent databases from the United States Patent and Trademark Office (USPTO), the European Patent Office (EPO), and TÜRKPATENT for regional markets. Additionally, the World Intellectual Property Organization (WIPO) PatentScope, Google Patents, and academic research databases will be utilized for broader global coverage.
   - The Harvard USPTO Dataset (HUPD) [![arXiv](https://img.shields.io/badge/arXiv-2207.04043-b31b1b.svg)](https://arxiv.org/abs/2207.04043) is a large-scale, well-structured, and multi-purpose corpus of English-language utility patent applications filed to the United States Patent and Trademark Office (USPTO) between January 2004 and December 2018.
  
<br>

2. CLASSIFICATION/ TAXONOMY ALIGNMENT
   
   - **Turkish Defense Industry Technology Taxonomy (Savunma Sanayii Teknoloji Taksonomisi)** [![View PDF](https://img.shields.io/badge/View-PDF-red.svg)](https://www.ostimsavunma.org/content/upload/document-files/ssb-teknoloji-taksonomisi-20200605154245.pdf)
      1. Underpinning technologies (TEMEL TEKNOLOJİLER)
      2. Design technologies for platforms and weapons (PLATFORM VE SİLAHLAR İÇİN TASARIM TEKNOLOJİLERİ)
      3. Systems and products (SİSTEMLER VE ÜRÜNLER)
   - **Patent Categorization**
      1. The goal is to categorize patent applications into predefined categories within the Turkish Defence Industry Technology Taxonomy.

<br>

3. DATA ANALYSIS AND PREPROCESSING

   - After the dataset is ready to use and classified according to SSTT, we will begin to process it.
   - Data Analysis will be implemented to inspect, cleanse, transform, and model data to discover useful information, inform conclusions, and support decision-making.

<br>

4. PREDICTION MODELING
   
   - The aim is to predict the adoption process of technology, informing strategies for enhancing technology integration.
   - A time-series prediction model, such as a recurrent neural network (RNN) or a combination of architectures, potentially suitable for capturing temporal dependencies in the adoption process.