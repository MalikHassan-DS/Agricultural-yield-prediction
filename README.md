\# 🌾 Agricultural Crop Yield Prediction



A machine learning project for predicting agricultural crop yield using historical FAOSTAT data from Pakistan.



The project uses \*\*feature engineering, lag features, rolling averages, one-hot encoding, and Gradient Boosting Regression\*\* to forecast crop yield and provide a 2025 prediction through an interactive Streamlit dashboard.



\---



\## 📌 Project Overview



Agricultural crop yield can vary significantly over time due to changes in production, harvested area, and historical yield patterns.



This project develops a machine learning pipeline to analyze historical agricultural data and predict crop yield for major crops in Pakistan.



\### Crops Covered



\* 🌾 Wheat

\* 🍚 Rice

\* 🌽 Maize

\* 🎋 Sugar cane

\* 🥔 Potatoes

\* 🌿 Cotton



\---



\## 🎯 Objectives



\* Collect agricultural data from FAOSTAT

\* Clean and preprocess historical crop data

\* Perform feature engineering

\* Create historical lag features

\* Create rolling-average features

\* Train and compare machine learning models

\* Evaluate model performance using MAE, RMSE, and R²

\* Select the best-performing model

\* Forecast crop yield for 2025

\* Build an interactive Streamlit dashboard



\---



\## 🔄 Machine Learning Pipeline



```text

FAOSTAT Data

&#x20;    ↓

Data Collection

&#x20;    ↓

Data Cleaning

&#x20;    ↓

Feature Engineering

&#x20;    ↓

Lag Features

&#x20;    ↓

Rolling 3-Year Average

&#x20;    ↓

Train/Test Split

&#x20;    ↓

One-Hot Encoding

&#x20;    ↓

Machine Learning Models

&#x20;    ↓

Model Evaluation

&#x20;    ↓

Gradient Boosting Selection

&#x20;    ↓

2025 Yield Forecast

&#x20;    ↓

Streamlit Dashboard

```



\---



\## 🧮 Feature Engineering



The model uses the following features:



\* Previous Yield

\* Previous Area

\* Previous Production

\* Yield Lag 2

\* Yield Lag 3

\* Rolling 3-Year Yield

\* Area Harvested

\* Production

\* Year

\* Crop category



\### Lag Features



Historical yield values were used to capture temporal patterns.



\* `Previous\_Yield`

\* `Yield\_Lag\_2`

\* `Yield\_Lag\_3`



A three-year rolling average was also created:



\* `Yield\_Rolling\_3`



\---



\## 🤖 Machine Learning Models



The project evaluated tree-based regression models for crop yield prediction.



\### Random Forest



Initial evaluation:



\* MAE: \*\*1810.29 kg/ha\*\*

\* RMSE: \*\*3453.74 kg/ha\*\*

\* R²: \*\*0.9802\*\*



\### Gradient Boosting



Initial evaluation:



\* MAE: \*\*1400.72 kg/ha\*\*

\* RMSE: \*\*3014.09 kg/ha\*\*

\* R²: \*\*0.9849\*\*



After hyperparameter tuning, the selected final model was:



\### 🏆 Final Model: Gradient Boosting



Final test performance:



\* \*\*MAE: 1610.75 kg/ha\*\*

\* \*\*RMSE: 3108.07 kg/ha\*\*

\* \*\*R²: 0.9840\*\*



The model was evaluated on the \*\*2020–2024 test period\*\*.



\---



\## ⚙️ Best Gradient Boosting Parameters



The tuned Gradient Boosting model used:



```text

learning\_rate = 0.05

max\_depth = 2

min\_samples\_leaf = 1

min\_samples\_split = 5

n\_estimators = 300

```



\---



\## 🌾 2025 Crop Yield Forecast



The final Gradient Boosting model generated the following 2025 predictions:



| Crop       | Predicted Yield (kg/ha) |

| ---------- | ----------------------: |

| Wheat      |                 3348.35 |

| Rice       |                 3820.79 |

| Maize      |                 5345.83 |

| Sugar cane |                63499.67 |

| Potatoes   |                24931.90 |

| Cotton     |                 2060.64 |



These predictions are model-generated forecasts and should not be interpreted as official agricultural statistics.



\---



\## 📊 Streamlit Dashboard



The project includes an interactive Streamlit dashboard that provides:



\* 2025 crop yield forecasts

\* Crop selection

\* Highest and lowest predicted yield

\* Forecast visualization

\* Forecast results table

\* CSV download

\* Actual vs Predicted analysis

\* Crop-wise model performance

\* Model information



\---



\## 📁 Project Structure



```text

Agricultural-yield-prediction/

│

├── app.py

│

├── 01\_faostat\_data\_collection.ipynb

│

├── faostat\_history.py

│

├── faostat\_pakistan\_crop\_data.csv

│

├── 2025\_crop\_yield\_forecast.csv

│

├── test\_predictions.csv

│

├── crop\_performance.csv

│

├── models/

│   ├── crop\_encoder.pkl

│   ├── crop\_yield\_gradient\_boosting.pkl

│   └── feature\_names.pkl

│

└── .gitignore

```



\---



\## 🛠️ Technologies Used



\* Python

\* Pandas

\* NumPy

\* Scikit-learn

\* Joblib

\* Requests

\* FAOSTAT API

\* Streamlit

\* Matplotlib

\* Git

\* GitHub



\---



\## 📦 Installation



Clone the repository:



```bash

git clone https://github.com/MalikHassan-DS/Agricultural-yield-prediction.git

```



Navigate to the project:



```bash

cd Agricultural-yield-prediction

```



Create a virtual environment:



```bash

python -m venv .venv

```



Activate it on Windows:



```powershell

.venv\\Scripts\\activate

```



Install the required packages:



```bash

pip install pandas numpy scikit-learn joblib requests streamlit matplotlib

```



\---



\## ▶️ Run the Streamlit Application



From the project directory:



```bash

streamlit run app.py

```



The application will open in your browser.



\---



\## 📈 Model Evaluation



The model was trained using historical agricultural data and evaluated using a time-based split.



\### Training Period



\*\*2003–2019\*\*



\### Testing Period



\*\*2020–2024\*\*



This approach keeps later years for testing rather than randomly mixing historical and future observations.



\---



\## 🔍 Important Features



Feature importance analysis showed that historical production and yield-related features were among the most influential predictors.



Important features included:



\* `Yield\_Lag\_2`

\* `Previous\_Production`

\* `Production\_tonnes`

\* `Yield\_Rolling\_3`

\* `Previous\_Yield`

\* Crop category



\---



\## ⚠️ Limitations



The current model is based primarily on historical agricultural production data and engineered temporal features.



It does not currently include external factors such as:



\* Weather

\* Rainfall

\* Temperature

\* Soil conditions

\* Fertilizer usage

\* Irrigation

\* Pest and disease information



Therefore, the predictions should be considered \*\*machine learning estimates\*\*, not official agricultural forecasts.



\---



\## 🚀 Future Improvements



Possible future improvements include:



\* Add rainfall and weather data

\* Add temperature features

\* Add fertilizer and irrigation information

\* Compare XGBoost and LightGBM

\* Perform advanced time-series validation

\* Add prediction intervals

\* Automate yearly FAOSTAT data updates

\* Deploy the Streamlit application online

\* Add interactive historical trend charts



\---



\## 👨‍💻 Author



\*\*Malik Hassan\*\*



Data Analyst / Machine Learning Enthusiast



GitHub:

https://github.com/MalikHassan-DS



\---



\## ⭐ Project



If you find this project useful, consider giving the repository a ⭐ on GitHub.



