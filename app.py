import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Agricultural Yield Prediction",
    page_icon="🌾",
    layout="wide"
)

# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).parent

MODEL_PATH = BASE_DIR / "models" / "crop_yield_gradient_boosting.pkl"
ENCODER_PATH = BASE_DIR / "models" / "crop_encoder.pkl"
FEATURE_PATH = BASE_DIR / "models" / "feature_names.pkl"

FORECAST_PATH = BASE_DIR / "2025_crop_yield_forecast.csv"
RESULTS_PATH = BASE_DIR / "test_predictions.csv"
PERFORMANCE_PATH = BASE_DIR / "crop_performance.csv"

# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    features = joblib.load(FEATURE_PATH)

    return model, encoder, features


@st.cache_data
def load_forecast():

    return pd.read_csv(FORECAST_PATH)


# ============================================================
# LOAD PROJECT FILES
# ============================================================

try:

    model, encoder, feature_names = load_model()
    forecast_df = load_forecast()

except Exception as e:

    st.error(
        f"❌ Error loading project files:\n\n{e}"
    )

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🌾 Crop Yield AI")

st.sidebar.markdown(
    """
    ### Navigation

    Explore the agricultural forecasting dashboard:

    - 🌾 2025 Crop Forecasts
    - 📊 Yield Comparison
    - 📈 Actual vs Predicted
    - 🎯 Crop-wise Performance
    - 🤖 Model Information
    """
)

st.sidebar.divider()

st.sidebar.info(
    "Model: Gradient Boosting\n\n"
    "Forecast Year: 2025"
)


# ============================================================
# HEADER
# ============================================================

st.title("🌾 Agricultural Crop Yield Prediction")

st.markdown(
    """
    **Machine Learning–based crop yield forecasting system**

    This dashboard uses a **Gradient Boosting Machine Learning model**
    trained on historical agricultural data to forecast crop yield
    for **2025**.
    """
)

st.divider()


# ============================================================
# KPI SECTION
# ============================================================

highest_yield = forecast_df[
    "Predicted_Yield_kg_ha"
].max()

highest_crop = forecast_df.loc[
    forecast_df["Predicted_Yield_kg_ha"].idxmax(),
    "Crop"
]

lowest_yield = forecast_df[
    "Predicted_Yield_kg_ha"
].min()

lowest_crop = forecast_df.loc[
    forecast_df["Predicted_Yield_kg_ha"].idxmin(),
    "Crop"
]


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Forecast Year",
        "2025"
    )


with col2:

    st.metric(
        "Crops Forecasted",
        len(forecast_df)
    )


with col3:

    st.metric(
        "Highest Predicted Yield",
        f"{highest_yield:,.2f} kg/ha",
        highest_crop
    )


with col4:

    st.metric(
        "Lowest Predicted Yield",
        f"{lowest_yield:,.2f} kg/ha",
        lowest_crop
    )


st.divider()


# ============================================================
# CROP SELECTOR
# ============================================================

st.subheader("🔍 Explore Crop Forecast")


selected_crop = st.selectbox(
    "Select a crop",
    forecast_df["Crop"].tolist()
)


selected_data = forecast_df[
    forecast_df["Crop"] == selected_crop
].iloc[0]


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Crop",
        selected_crop
    )


with col2:

    st.metric(
        "Year",
        int(selected_data["Year"])
    )


with col3:

    st.metric(
        "Predicted Yield",
        f"{selected_data['Predicted_Yield_kg_ha']:,.2f} kg/ha"
    )


st.divider()


# ============================================================
# FORECAST CHART
# ============================================================

st.subheader("📊 2025 Predicted Crop Yield")


chart_data = forecast_df[
    ["Crop", "Predicted_Yield_kg_ha"]
].set_index("Crop")


st.bar_chart(
    chart_data,
    use_container_width=True
)


st.caption(
    "Predicted crop yield is measured in kilograms per hectare (kg/ha)."
)


st.divider()


# ============================================================
# FORECAST TABLE
# ============================================================

st.subheader("📋 2025 Forecast Results")


display_df = forecast_df.copy()


display_df["Predicted_Yield_kg_ha"] = (
    display_df["Predicted_Yield_kg_ha"].round(2)
)


display_df = display_df.rename(
    columns={
        "Crop": "Crop",
        "Year": "Year",
        "Predicted_Yield_kg_ha":
            "Predicted Yield (kg/ha)"
    }
)


st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# DOWNLOAD FORECAST
# ============================================================

st.download_button(
    label="📥 Download 2025 Forecast CSV",
    data=forecast_df.to_csv(index=False),
    file_name="2025_crop_yield_forecast.csv",
    mime="text/csv"
)


st.divider()


# ============================================================
# ACTUAL VS PREDICTED ANALYSIS
# ============================================================

st.subheader("📈 Actual vs Predicted Yield")

st.markdown(
    """
    Comparison of actual and model-predicted crop yields
    for the **2020–2024 test period**.
    """
)


if RESULTS_PATH.exists():

    results_df = pd.read_csv(RESULTS_PATH)

    selected_analysis_crop = st.selectbox(
        "Select crop for Actual vs Predicted analysis",
        results_df["Crop"].unique(),
        key="analysis_crop"
    )


    crop_analysis = results_df[
        results_df["Crop"] == selected_analysis_crop
    ].sort_values("Year")


    comparison_df = crop_analysis[
        [
            "Year",
            "Actual_Yield",
            "Predicted_Yield"
        ]
    ].copy()


    comparison_df = comparison_df.set_index("Year")


    st.line_chart(
        comparison_df,
        use_container_width=True
    )


    st.subheader(
        f"📋 {selected_analysis_crop} — Actual vs Predicted"
    )


    display_comparison = crop_analysis[
        [
            "Year",
            "Actual_Yield",
            "Predicted_Yield",
            "Error"
        ]
    ].copy()


    display_comparison[
        "Actual_Yield"
    ] = display_comparison[
        "Actual_Yield"
    ].round(2)


    display_comparison[
        "Predicted_Yield"
    ] = display_comparison[
        "Predicted_Yield"
    ].round(2)


    display_comparison[
        "Error"
    ] = display_comparison[
        "Error"
    ].round(2)


    display_comparison = display_comparison.rename(
        columns={
            "Actual_Yield": "Actual Yield (kg/ha)",
            "Predicted_Yield": "Predicted Yield (kg/ha)",
            "Error": "Prediction Error"
        }
    )


    st.dataframe(
        display_comparison,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # DOWNLOAD TEST PREDICTIONS
    # ========================================================

    st.download_button(
        label="📥 Download Test Predictions",
        data=results_df.to_csv(index=False),
        file_name="test_predictions.csv",
        mime="text/csv"
    )


else:

    st.info(
        "ℹ️ test_predictions.csv was not found. "
        "The 2025 forecast dashboard is still available."
    )


st.divider()


# ============================================================
# CROP-WISE MODEL PERFORMANCE
# ============================================================

st.subheader("🎯 Crop-wise Model Performance")


if PERFORMANCE_PATH.exists():

    performance_df = pd.read_csv(
        PERFORMANCE_PATH,
        index_col=0
    )


    performance_df = performance_df.round(2)


    st.dataframe(
        performance_df,
        use_container_width=True
    )


    st.markdown(
        """
        **Metrics:**

        - **MAE:** Mean Absolute Error
        - **RMSE:** Root Mean Squared Error
        - **R²:** Coefficient of Determination
        """
    )


    st.download_button(
        label="📥 Download Crop Performance",
        data=performance_df.to_csv(),
        file_name="crop_performance.csv",
        mime="text/csv"
    )


else:

    st.info(
        "ℹ️ crop_performance.csv was not found."
    )


st.divider()


# ============================================================
# MODEL INFORMATION
# ============================================================

st.subheader("🤖 Model Information")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Model",
        "Gradient Boosting"
    )


with col2:

    st.metric(
        "R²",
        "0.9840"
    )


with col3:

    st.metric(
        "MAE",
        "1610.75 kg/ha"
    )


st.caption(
    "Model evaluation is based on the 2020–2024 test period."
)


st.divider()


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.subheader("📌 Project Information")


info_col1, info_col2 = st.columns(2)


with info_col1:

    st.markdown(
        """
        ### Machine Learning Pipeline

        - Historical agricultural data
        - Data cleaning
        - Feature engineering
        - Previous-year features
        - Lag features
        - Rolling averages
        - One-hot encoding
        - Gradient Boosting
        - Model evaluation
        - 2025 forecasting
        """
    )


with info_col2:

    st.markdown(
        """
        ### Key Features

        - Previous Yield
        - Previous Area
        - Previous Production
        - Yield Lag 2
        - Yield Lag 3
        - Rolling 3-Year Yield
        - Crop category
        - Year
        - Area Harvested
        - Production
        """
    )


st.divider()


# ============================================================
# FOOTER
# ============================================================

st.caption(
    "🌾 Agricultural Yield Prediction System | "
    "Machine Learning Project"
)
