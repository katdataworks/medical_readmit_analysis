# Medical Readmission Analysis

This project analyzes geographic trends in patient readmission rates based on state and area type (urban, rural, suburban).

## Objective
The objective of this project is to analyze geographic trends in patient readmission rates based on state and area type (urban, rural, suburban). The analysis aims to provide insights into readmission patterns, which can help healthcare providers and policymakers in targeting interventions to reduce readmission rates.

## Data
The dataset used in this project includes patient information related to readmissions within a month of release, medical conditions, demographics, and geographical details. The primary file used for analysis is `medical_raw_data.csv`, and the data dictionary is provided in `D206 Data Cleaning_ Medical Data Considerations and Dictionary.pdf`.

## Project Structure

medical_readmit_analysis/
├── README.md
├── requirements.txt
├── data/
│   ├── medical_raw_data.csv
│   └── D206 Data Cleaning_ Medical Data Considerations and Dictionary.pdf
└── analysis/
    ├── analysis_script.py
    └── results/
        ├── readmission_rates_by_state.csv
        ├── readmission_rates_by_area.csv
        ├── readmission_rates_by_state.png
        └── readmission_rates_by_area.png

## Steps Performed

1. **Data Preparation**:
   - The raw data was loaded from `data/medical_raw_data.csv`.
   - Rows with missing values in the `State`, `Area`, or `ReAdmis` columns were dropped to ensure the integrity of the analysis.

2. **Data Analysis**:
   - **Readmission Rates by State**:
     The readmission rates for each state were calculated and saved to `analysis/results/readmission_rates_by_state.csv`.
   - **Readmission Rates by Area Type**:
     The readmission rates for each area type (urban, rural, suburban) were calculated and saved to `analysis/results/readmission_rates_by_area.csv`.

3. **Visualization**:
   - Bar charts were created to visualize the readmission rates by state and area type.
   - The charts were saved as `analysis/results/readmission_rates_by_state.png` and `analysis/results/readmission_rates_by_area.png`.

## Results

- **Readmission Rates by State**:
  The readmission rates vary significantly across states, with some states showing higher rates of readmission than others. The results are detailed in `readmission_rates_by_state.csv` and visualized in `readmission_rates_by_state.png`.

- **Readmission Rates by Area Type**:
  The analysis showed differences in readmission rates based on area type. Urban areas generally had higher readmission rates compared to rural and suburban areas. The results are detailed in `readmission_rates_by_area.csv` and visualized in `readmission_rates_by_area.png`.

## Conclusions
The project successfully identified geographic trends in patient readmission rates, providing valuable insights into how readmission rates vary by state and area type. These findings can be used to inform targeted interventions aimed at reducing readmission rates and improving patient outcomes.

## Future Work
Future work could involve:
- Conducting a more detailed analysis to identify specific factors contributing to higher readmission rates in certain states or areas.
- Exploring additional variables in the dataset to uncover further insights.
- Implementing machine learning models to predict readmission risks based on patient and geographic data.

## Repository
The complete project, including data, analysis scripts, and results, is available on GitHub:
[GitHub Repository - Medical Readmission Analysis](https://github.com/katdataworks/medical_readmit_analysis)

## Requirements

Install the required packages using:
```bash
pip install -r requirements.txt
