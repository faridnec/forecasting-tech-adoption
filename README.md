# Modelling the Adoption Process of Technology Using Artificial Intelligence Methods

[![GitHub Repository](https://img.shields.io/badge/GitHub-Modelling%20Technology%20Adoption%20Process-blue?style=flat-square&logo=github)](https://github.com/faridnec/forecasting-tech-adoption)

<!-- > [!NOTE]
> This project is still under development. -->

## INTRODUCTION AND PROBLEM DEFINITION

The current era is defined by rapid technological advancements that made innovation a central focus for both academic and industrial sectors. Understanding how new technologies are adopted by individuals, firms, and societies is crucial for strategic planning and development.

With the vast amount of data and computational power available today, there is an opportunity to improve our understanding of technology adoption using AI methods. AI techniques, such as natural language processing (NLP) and machine learning, can streamline complex patent-related tasks like classification and retrieval. This study is carried out to utilize AI methodologies, specifically text embeddings and patent clustering, to analyze patent data and model the technology life cycle and adoption process. By incorporating these findings into S-curve models, we expect to provide a detailed view of technological trends which will benefit industry analysts and researchers.

## CONDUCTED RESEARCH

![Research method](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/flow.png?raw=true)

The suggested methodology is represented with a process flow covering main steps:

1. Data collection
2. Database integration
3. Data preprocessing
4. Text embeddings using pre-trained sentence transformers
5. Patent clustering and topic modelling
6. Filtering relevant patent using semantic search algorithm
7. Modeling and forecasting the S-curves to analyze the technology adoption growth model.

#### Patent Sources

| Patent Database              | Link   |
|:-----------------------------|:-----------------|
|![USPTO logo](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/logo/uspto.jpeg?raw=true)  | [Advanced Search USPTO](https://ppubs.uspto.gov/pubwebapp/)|
|![Patsnap logo](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/logo/patsnap.png?raw=true)| [Patsnap](https://www.patsnap.com/)    |

#### Project Structure

```plaintext
forecasting-tech-adoption/
├── data/                      # collected patent sources
│   ├── raw/                   
│   └── processed/
├── img/                       # Images
├── models/                    # Models for each source and data pipeline
├── notebooks/                 # notebooks storing scrpits for processing and analysis
├── src/                       # common scripts
├── docs/                      # Project documentation
├── .gitattributes             
├── .gitignore                 
└── README.md              
```

## RESULTS AND CONCLUSION

The methodology involves selecting target technologies, obtaining relevant patent data from databases such as USPTO and Patsnap, and processing obtained data using text embeddings, clustering, and topic modeling. This refined data is used for semantic searches, filtering relevant patents, and predicting future trends using logistic growth models. The methodology's application to technologies like 'Unmanned Aerial Vehicle' and 'Security Data Processing' demonstrates its efficiency in extracting trends and related CPC codes. These overall process offers a clear understanding of the selected technologies' development stages.

| Dataset   | S-curves                     | Embedding Vectors| Clusters |
|:----------|:-----------------------------|:-----------------|---------:|
| *USPTO*   | ![S Curve](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/uspto/uav_1.png?raw=true) ![S Curve](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/uspto/uav_2.png?raw=true)  ![S Curve](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/uspto/sec_data_processing_1.png?raw=true)  ![S Curve](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/uspto/sec_data_processing_2.png?raw=true)    | ![USPTO vector](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/uspto/uspto_vec.gif?raw=true)     | ![USPTO cluster](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/uspto/uspto_cluster.png?raw=true)  |
| *Patsnap* | ![S Curve](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/patsnap/uav_device_1.png?raw=true) ![S Curve](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/patsnap/uav_device_2.png?raw=true)  ![S Curve](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/patsnap/system_detection_1.png?raw=true)  ![S Curve](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/patsnap/system_detection_2.png?raw=true)               | ![Patsnap vector](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/patsnap/patsnap_vec.png?raw=true)    | ![Patsnap cluster](https://github.com/faridnec/forecasting-tech-adoption/blob/master/img/patsnap/patsnap_cluster.png?raw=true)|

## FUTURE STUDIES

1. <b>Broadening the Methodology</b>: Can be applied to a wider range of topics across multiple technology areas.
2. <b>Global Perspective</b>: More comprehensive analysis can be done by taking data from additional sources such as European Patent Office (EPO), Japan Patent Office (JPO), TÜRKPATENT, etc.
3. <b>Dynamic Prediction Models</b>: Models that can be updated in real time can be developed.
4. <b>User Friendly Application</b>: An application that allows users to enter queries and create dynamic models can be developed.
