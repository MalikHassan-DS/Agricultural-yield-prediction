   1:
import os

token = os.getenv("FAOSTAT_TOKEN")

print(token is not None)
print(len(token) if token else 0)
   2:
import requests
import os

token = os.getenv("FAOSTAT_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

url = "https://faostatservices.fao.org/api/v1/en/groups"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print(response.text[:500])
   3:
import requests
import os
import pandas as pd

token = os.getenv("FAOSTAT_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

url = "https://faostatservices.fao.org/api/v1/en/groups"

response = requests.get(url, headers=headers)

data = response.json()["data"]

groups = pd.DataFrame(data)

groups
   4:
import requests
import os
import pandas as pd

token = os.getenv("FAOSTAT_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

url = "https://faostatservices.fao.org/api/v1/en/domains/Q/"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

q_data = response.json()["data"]

q_domains = pd.DataFrame(q_data)

q_domains
   5:
import requests
import os
import pandas as pd

token = os.getenv("FAOSTAT_TOKEN")

headers = {
    "Authorization": f"Bearer {token}"
}

url = "https://faostatservices.fao.org/api/v1/en/dimensions/QCL/"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print(response.text[:2000])
   6:
url = "https://faostatservices.fao.org/api/v1/en/codes/element/QCL"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print(response.text[:3000])
   7:
url = "https://faostatservices.fao.org/api/v1/en/codes/item/QCL"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print(response.text[:3000])
   8:
items = response.json()["data"]

items_df = pd.DataFrame(items)

crops = items_df[
    items_df["label"].str.contains(
        "Wheat|Rice|Maize|Sugar cane|Cotton|Potatoes",
        case=False,
        na=False
    )
]

crops[["code", "label", "parent"]]
   9:
url = "https://faostatservices.fao.org/api/v1/en/codes/area/QCL"

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
  10:
areas = response.json()["data"]

areas_df = pd.DataFrame(areas)

pakistan = areas_df[
    areas_df["label"].str.contains("Pakistan", case=False, na=False)
]

pakistan
  11:
url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

params = {
    "area_code": "165",
    "item_code": "15",
    "element_code": "2413",
    "page_size": 10
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

print("Status:", response.status_code)
print(response.url)
print(response.text[:3000])
  12:
url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

response = requests.get(
    url,
    headers=headers,
    params={"area_code__1": "165"}
)

print("Status:", response.status_code)
print(response.text[:2000])
  13:
url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

params = {
    "area": "165",
    "item": "15",
    "element": "2413",
    "year": "2024"
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

print("Status:", response.status_code)
print(response.url)
print(response.text[:3000])
  14:
url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

params = {
    "area": "165",
    "item": "15",
    "element": "2413",
    "year": "2025"
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

print("Status:", response.status_code)
print(response.text[:2000])
  15:
params = {
    "area": "165",
    "item": "15",
    "element": "2413",
    "year": "2000:2024"
}

response = requests.get(
    "https://faostatservices.fao.org/api/v1/en/data/QCL",
    headers=headers,
    params=params
)

print("Status:", response.status_code)

data = response.json()["data"]

wheat_yield = pd.DataFrame(data)

wheat_yield[["Area", "Item", "Year", "Unit", "Value"]]
  16:
print("Status:", response.status_code)
print("Number of rows:", len(data))
print("Columns:", wheat_yield.columns.tolist())
print(wheat_yield.head())
  17:
url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

params = {
    "area": "165",
    "item": "15",
    "element": "2413",
    "year": "2024"
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

result = response.json()

print("Status:", response.status_code)
print("Rows:", len(result.get("data", [])))
print(result.get("data", []))
  18:
import time
import pandas as pd
import requests

url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

years = range(2000, 2025)

all_data = []

for year in years:

    params = {
        "area": "165",
        "item": "15",
        "element": "2413",
        "year": str(year)
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    if response.status_code == 200:
        rows = response.json().get("data", [])
        all_data.extend(rows)
        print(year, "→", len(rows), "rows")
    else:
        print(year, "→ ERROR", response.status_code)

    time.sleep(0.2)

wheat_yield = pd.DataFrame(all_data)

print("\nTotal rows:", len(wheat_yield))
  19:
crops = {
    "Wheat": 15,
    "Rice": 27,
    "Maize": 56,
    "Sugar cane": 156,
    "Potatoes": 116,
    "Cotton": 328
}
  20:
elements = {
    "Area harvested": 2312,
    "Yield": 2413,
    "Production Quantity": 2510
}
  21:
import time
import pandas as pd
import requests

url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

crops = {
    "Wheat": 15,
    "Rice": 27,
    "Maize": 56,
    "Sugar cane": 156,
    "Potatoes": 116,
    "Cotton": 328
}

all_data = []

for crop, item_code in crops.items():

    for year in range(2000, 2025):

        params = {
            "area": "165",
            "item": str(item_code),
            "element": "2413",
            "year": str(year)
        }

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        if response.status_code == 200:

            rows = response.json().get("data", [])

            for row in rows:
                row["Crop"] = crop

            all_data.extend(rows)

            print(crop, year, "→", len(rows))

        else:
            print(crop, year, "→ ERROR", response.status_code)

        time.sleep(0.2)

yield_df = pd.DataFrame(all_data)

print("\nTotal rows:", len(yield_df))
  22:
elements = {
    "Area Harvested": 2312,
    "Production Quantity": 2510
}

feature_data = []

for feature, element_code in elements.items():

    for crop, item_code in crops.items():

        for year in range(2000, 2025):

            params = {
                "area": "165",
                "item": str(item_code),
                "element": str(element_code),
                "year": str(year)
            }

            response = requests.get(
                url,
                headers=headers,
                params=params
            )

            if response.status_code == 200:
                rows = response.json().get("data", [])

                for row in rows:
                    row["Crop"] = crop
                    row["Feature"] = feature

                feature_data.extend(rows)

            else:
                print(
                    feature,
                    crop,
                    year,
                    "→ ERROR",
                    response.status_code
                )

            time.sleep(0.2)

feature_df = pd.DataFrame(feature_data)

print("Total rows:", len(feature_df))
  23: yield_df[["Crop", "Year", "Unit", "Value"]].head()
  24: feature_df[["Crop", "Year", "Feature", "Unit", "Value"]].head(10)
  25: print(feature_df["Feature"].value_counts())
  26: feature_df.groupby(["Feature", "Unit"]).size()
  27:
print("Yield missing:", yield_df["Value"].isna().sum())
print("Features missing:", feature_df["Value"].isna().sum())
  28:
print(
    "Yield duplicates:",
    yield_df.duplicated(["Crop", "Year"]).sum()
)

print(
    "Feature duplicates:",
    feature_df.duplicated(
        ["Crop", "Year", "Feature"]
    ).sum()
)
  29:
yield_clean = yield_df[
    ["Crop", "Year", "Value"]
].copy()

yield_clean = yield_clean.rename(
    columns={"Value": "Yield_kg_ha"}
)

yield_clean["Year"] = pd.to_numeric(
    yield_clean["Year"]
)

yield_clean["Yield_kg_ha"] = pd.to_numeric(
    yield_clean["Yield_kg_ha"]
)
  30:
area_df = feature_df[
    feature_df["Feature"] == "Area Harvested"
][["Crop", "Year", "Value"]].copy()

area_df = area_df.rename(
    columns={"Value": "Area_Harvested_ha"}
)

area_df["Area_Harvested_ha"] = pd.to_numeric(
    area_df["Area_Harvested_ha"]
)
  31:
production_df = feature_df[
    feature_df["Feature"] == "Production Quantity"
][["Crop", "Year", "Value"]].copy()

production_df = production_df.rename(
    columns={"Value": "Production_tonnes"}
)

production_df["Production_tonnes"] = pd.to_numeric(
    production_df["Production_tonnes"]
)
  32:
final_df = (
    yield_clean
    .merge(
        area_df,
        on=["Crop", "Year"],
        how="inner"
    )
    .merge(
        production_df,
        on=["Crop", "Year"],
        how="inner"
    )
)
  33:
area_df["Year"] = pd.to_numeric(area_df["Year"])
production_df["Year"] = pd.to_numeric(production_df["Year"])
  34:
final_df = (
    yield_clean
    .merge(
        area_df,
        on=["Crop", "Year"],
        how="inner"
    )
    .merge(
        production_df,
        on=["Crop", "Year"],
        how="inner"
    )
)
  35:
print("Shape:", final_df.shape)

final_df.head(10)
  36:
final_df.to_csv(
    "faostat_pakistan_crop_data.csv",
    index=False
)

print("Dataset saved successfully!")
print("Shape:", final_df.shape)
  37:
print("Dataset Shape:", final_df.shape)

print("\nData Types:")
print(final_df.dtypes)

print("\nMissing Values:")
print(final_df.isnull().sum())

print("\nDuplicate Rows:")
print(final_df.duplicated().sum())

print("\nBasic Statistics:")
display(final_df.describe())
  38:
crop_summary = final_df.groupby("Crop").agg(
    Years=("Year", "count"),
    Avg_Yield=("Yield_kg_ha", "mean"),
    Min_Yield=("Yield_kg_ha", "min"),
    Max_Yield=("Yield_kg_ha", "max"),
    Avg_Area=("Area_Harvested_ha", "mean"),
    Avg_Production=("Production_tonnes", "mean")
).round(2)

display(crop_summary)
  39:
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

for crop in final_df["Crop"].unique():
    data = final_df[final_df["Crop"] == crop]

    plt.plot(
        data["Year"],
        data["Yield_kg_ha"],
        marker="o",
        label=crop
    )

plt.title("Pakistan Crop Yield Trends (2000–2024)")
plt.xlabel("Year")
plt.ylabel("Yield (kg/ha)")
plt.legend()
plt.grid(True)
plt.show()
  40:
import sys
print(sys.executable)
  41: %pip install matplotlib
  42:
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

for crop in final_df["Crop"].unique():
    data = final_df[final_df["Crop"] == crop]

    plt.plot(
        data["Year"],
        data["Yield_kg_ha"],
        marker="o",
        label=crop
    )

plt.title("Pakistan Crop Yield Trends (2000–2024)")
plt.xlabel("Year")
plt.ylabel("Yield (kg/ha)")
plt.legend()
plt.grid(True)
plt.show()
  43:
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

for crop in final_df["Crop"].unique():
    data = final_df[final_df["Crop"] == crop]
    
    plt.scatter(
        data["Area_Harvested_ha"],
        data["Production_tonnes"],
        label=crop
    )

plt.title("Area Harvested vs Production")
plt.xlabel("Area Harvested (ha)")
plt.ylabel("Production (tonnes)")
plt.legend()
plt.grid(True)
plt.show()
  44:
final_df[
    ["Yield_kg_ha", "Area_Harvested_ha", "Production_tonnes"]
].corr().round(3)
  45:
final_df = final_df.sort_values(
    ["Crop", "Year"]
).reset_index(drop=True)

final_df.head()
  46:
final_df["Previous_Yield"] = (
    final_df.groupby("Crop")["Yield_kg_ha"].shift(1)
)

final_df["Previous_Area"] = (
    final_df.groupby("Crop")["Area_Harvested_ha"].shift(1)
)

final_df["Previous_Production"] = (
    final_df.groupby("Crop")["Production_tonnes"].shift(1)
)

final_df.head(10)
  47:
ml_df = final_df.dropna(
    subset=[
        "Previous_Yield",
        "Previous_Area",
        "Previous_Production"
    ]
).copy()

print("Original shape:", final_df.shape)
print("ML dataset shape:", ml_df.shape)
  48:
print(
    ml_df["Year"].min(),
    "→",
    ml_df["Year"].max()
)

print(sorted(ml_df["Year"].unique()))
  49:
train_df = ml_df[ml_df["Year"] <= 2019].copy()
test_df = ml_df[ml_df["Year"] >= 2020].copy()

print("Training shape:", train_df.shape)
print("Testing shape:", test_df.shape)

print("\nTraining years:")
print(train_df["Year"].min(), "→", train_df["Year"].max())

print("\nTesting years:")
print(test_df["Year"].min(), "→", test_df["Year"].max())
  50:
features = [
    "Crop",
    "Year",
    "Previous_Yield",
    "Previous_Area",
    "Previous_Production"
]

target = "Yield_kg_ha"

X_train = train_df[features]
y_train = train_df[target]

X_test = test_df[features]
y_test = test_df[target]

print("X_train:", X_train.shape)
print("y_train:", y_train.shape)

print("X_test:", X_test.shape)
print("y_test:", y_test.shape)
  51:
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

X_train_crop = encoder.fit_transform(X_train[["Crop"]])
X_test_crop = encoder.transform(X_test[["Crop"]])

print("Encoded train shape:", X_train_crop.shape)
print("Encoded test shape:", X_test_crop.shape)
  52: %pip install scikit-learn
  53:
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

X_train_crop = encoder.fit_transform(X_train[["Crop"]])
X_test_crop = encoder.transform(X_test[["Crop"]])

print("Encoded train shape:", X_train_crop.shape)
print("Encoded test shape:", X_test_crop.shape)
  54:
numeric_features = [
    "Year",
    "Previous_Yield",
    "Previous_Area",
    "Previous_Production"
]

X_train_numeric = X_train[numeric_features].values
X_test_numeric = X_test[numeric_features].values

print("Numeric train:", X_train_numeric.shape)
print("Numeric test:", X_test_numeric.shape)
  55:
X_train_final = np.hstack([
    X_train_numeric,
    X_train_crop
])

X_test_final = np.hstack([
    X_test_numeric,
    X_test_crop
])

print("Final X_train:", X_train_final.shape)
print("Final X_test:", X_test_final.shape)
  56:
import numpy as np
X_train_final = np.hstack([
    X_train_numeric,
    X_train_crop
])

X_test_final = np.hstack([
    X_test_numeric,
    X_test_crop
])

print("Final X_train:", X_train_final.shape)
print("Final X_test:", X_test_final.shape)
  57:
from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train_final, y_train)

print("Random Forest trained successfully!")
  58:
y_pred = rf_model.predict(X_test_final)

print("First 10 predictions:")
print(y_pred[:10])
  59:
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import numpy as np

mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(
    mean_squared_error(y_test, y_pred)
)

r2 = r2_score(y_test, y_pred)

print("MAE :", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R²  :", round(r2, 4))
  60:
results = test_df[["Crop", "Year"]].copy()

results["Actual_Yield"] = y_test.values
results["Predicted_Yield"] = y_pred

results["Error"] = (
    results["Actual_Yield"] -
    results["Predicted_Yield"]
)

results.head(10)
  61:
feature_names = (
    numeric_features +
    list(encoder.get_feature_names_out(["Crop"]))
)

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": rf_model.feature_importances_
}).sort_values(
    "Importance",
    ascending=False
)

importance_df
  62:
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.barh(
    importance_df["Feature"],
    importance_df["Importance"]
)

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Random Forest Feature Importance")
plt.gca().invert_yaxis()

plt.show()
  63:
crop_results = results.copy()

crop_performance = (
    crop_results
    .groupby("Crop")
    .apply(
        lambda x: pd.Series({
            "MAE": mean_absolute_error(
                x["Actual_Yield"],
                x["Predicted_Yield"]
            ),
            "RMSE": np.sqrt(
                mean_squared_error(
                    x["Actual_Yield"],
                    x["Predicted_Yield"]
                )
            ),
            "R2": r2_score(
                x["Actual_Yield"],
                x["Predicted_Yield"]
            )
        }),
        include_groups=False
    )
    .round(2)
)

crop_performance
  64:
final_df = final_df.sort_values(
    ["Crop", "Year"]
).reset_index(drop=True)

final_df["Yield_Lag_2"] = (
    final_df.groupby("Crop")["Yield_kg_ha"].shift(2)
)

final_df["Yield_Lag_3"] = (
    final_df.groupby("Crop")["Yield_kg_ha"].shift(3)
)

final_df["Yield_Rolling_3"] = (
    final_df.groupby("Crop")["Yield_kg_ha"]
    .transform(lambda x: x.shift(1).rolling(3).mean())
)

final_df.head(10)
  65:
# ============================================================
# 1. Create lag features
# ============================================================

df_lag = final_df.copy()

df_lag = df_lag.sort_values(["Crop", "Year"]).reset_index(drop=True)

# Previous 2 years' yield
df_lag["Yield_Lag_2"] = (
    df_lag.groupby("Crop")["Yield_kg_ha"].shift(2)
)

# Previous 3 years' yield
df_lag["Yield_Lag_3"] = (
    df_lag.groupby("Crop")["Yield_kg_ha"].shift(3)
)

# Rolling average of previous 3 years
df_lag["Yield_Rolling_3"] = (
    df_lag.groupby("Crop")["Yield_kg_ha"]
    .transform(lambda x: x.shift(1).rolling(3).mean())
)

df_lag.head(10)
  66: print(df_lag.isnull().sum())
  67:
# Remove rows with missing lag/rolling features
ml_df_lag = ml_df_lag.dropna().reset_index(drop=True)

print("ML dataset after lag features:")
print("Shape:", ml_df_lag.shape)

print("\nMissing values:")
print(ml_df_lag.isnull().sum())
  68:
print(df_lag.columns)
print(df_lag.shape)
  69:
# Remove rows with missing lag/rolling features
ml_df_lag = df_lag.dropna().reset_index(drop=True)

print("ML dataset after lag features:")
print("Shape:", ml_df_lag.shape)

print("\nMissing values:")
print(ml_df_lag.isnull().sum())
  70:
# Target = current Yield
y = ml_df_lag["Yield_kg_ha"]

# Features
X = ml_df_lag[
    [
        "Crop",
        "Year",
        "Area_Harvested_ha",
        "Production_tonnes",
        "Previous_Yield",
        "Previous_Area",
        "Previous_Production",
        "Yield_Lag_2",
        "Yield_Lag_3",
        "Yield_Rolling_3"
    ]
]

print("X shape:", X.shape)
print("y shape:", y.shape)

print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget:")
print(y.name)
  71:
# Time-based train/test split

train_mask = ml_df_lag["Year"] <= 2019
test_mask = ml_df_lag["Year"] >= 2020

X_train = X[train_mask].copy()
X_test = X[test_mask].copy()

y_train = y[train_mask].copy()
y_test = y[test_mask].copy()

print("Training shape:", X_train.shape)
print("Testing shape:", X_test.shape)

print("\nTraining years:")
print(X_train["Year"].min(), "→", X_train["Year"].max())

print("\nTesting years:")
print(X_test["Year"].min(), "→", X_test["Year"].max())
  72:
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# -----------------------------
# Encode Crop
# -----------------------------
encoder = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

X_train_crop = encoder.fit_transform(
    X_train[["Crop"]]
)

X_test_crop = encoder.transform(
    X_test[["Crop"]]
)

print("Encoded train shape:", X_train_crop.shape)
print("Encoded test shape:", X_test_crop.shape)


# -----------------------------
# Numerical features
# -----------------------------
numeric_features = [
    "Year",
    "Area_Harvested_ha",
    "Production_tonnes",
    "Previous_Yield",
    "Previous_Area",
    "Previous_Production",
    "Yield_Lag_2",
    "Yield_Lag_3",
    "Yield_Rolling_3"
]

X_train_numeric = X_train[numeric_features].values
X_test_numeric = X_test[numeric_features].values

print("\nNumeric train:", X_train_numeric.shape)
print("Numeric test:", X_test_numeric.shape)


# -----------------------------
# Combine features
# -----------------------------
X_train_final = np.hstack([
    X_train_numeric,
    X_train_crop
])

X_test_final = np.hstack([
    X_test_numeric,
    X_test_crop
])

print("\nFinal X_train:", X_train_final.shape)
print("Final X_test:", X_test_final.shape)
  73:
from sklearn.ensemble import RandomForestRegressor

# Random Forest Regressor
rf_model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    n_jobs=-1
)

# Train
rf_model.fit(X_train_final, y_train)

print("Random Forest trained successfully!")
  74:
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Predictions
y_pred = rf_model.predict(X_test_final)

# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Model Evaluation")
print("-" * 30)
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")
  75:
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd

# Predictions
y_pred = rf_model.predict(X_test_final)

# Overall evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Model Evaluation")
print("-" * 30)
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")
  76:
feature_names = (
    numeric_features +
    list(encoder.get_feature_names_out(["Crop"]))
)

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": model.feature_importances_
}).sort_values("Importance", ascending=False)

print(importance_df)
  77:
from sklearn.ensemble import RandomForestRegressor

# Train Random Forest
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train_final, y_train)

print("Random Forest trained successfully!")
  78:
feature_names = (
    numeric_features +
    list(encoder.get_feature_names_out(["Crop"]))
)

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": model.feature_importances_
}).sort_values("Importance", ascending=False)

print(importance_df)
  79:
# Predictions
y_pred = rf_model.predict(X_test_final)

# Comparison dataframe
results_df = X_test.copy()

results_df["Actual_Yield"] = y_test.values
results_df["Predicted_Yield"] = y_pred
results_df["Error"] = (
    results_df["Actual_Yield"] -
    results_df["Predicted_Yield"]
)

results_df[
    [
        "Crop",
        "Year",
        "Actual_Yield",
        "Predicted_Yield",
        "Error"
    ]
].sort_values(["Crop", "Year"])
  80:
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Gradient Boosting Model
gb_model = GradientBoostingRegressor(
    n_estimators=300,
    learning_rate=0.03,
    max_depth=3,
    random_state=42,
    loss="squared_error"
)

gb_model.fit(X_train_final, y_train)

# Predictions
gb_pred = gb_model.predict(X_test_final)

# Evaluation
gb_mae = mean_absolute_error(y_test, gb_pred)
gb_rmse = np.sqrt(mean_squared_error(y_test, gb_pred))
gb_r2 = r2_score(y_test, gb_pred)

print("Gradient Boosting Evaluation")
print("-" * 30)
print(f"MAE  : {gb_mae:.2f}")
print(f"RMSE : {gb_rmse:.2f}")
print(f"R²   : {gb_r2:.4f}")
  81:
# Gradient Boosting Feature Importance

feature_names = (
    numeric_cols +
    list(encoder.get_feature_names_out(["Crop"]))
)

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": gb_model.feature_importances_
}).sort_values("Importance", ascending=False)

print(importance_df)
  82:
# Gradient Boosting Feature Importance

feature_names = [
    "Year",
    "Area_Harvested_ha",
    "Production_tonnes",
    "Previous_Yield",
    "Previous_Area",
    "Previous_Production",
    "Yield_Lag_2",
    "Yield_Lag_3",
    "Yield_Rolling_3",
    "Crop_Cotton",
    "Crop_Maize",
    "Crop_Potatoes",
    "Crop_Rice",
    "Crop_Sugar cane",
    "Crop_Wheat"
]

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": gb_model.feature_importances_
}).sort_values("Importance", ascending=False)

print(importance_df)
  83:
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor

param_grid = {
    "n_estimators": [100, 200, 300],
    "learning_rate": [0.02, 0.03, 0.05],
    "max_depth": [2, 3, 4],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2]
}

grid_search = GridSearchCV(
    estimator=GradientBoostingRegressor(random_state=42),
    param_grid=param_grid,
    cv=3,
    scoring="neg_mean_absolute_error",
    n_jobs=-1
)

grid_search.fit(X_train_final, y_train)

print("Best Parameters:")
print(grid_search.best_params_)

print("\nBest CV MAE:")
print(-grid_search.best_score_)
  84:
# Best Gradient Boosting Model
best_gb_model = grid_search.best_estimator_

# Test predictions
best_gb_pred = best_gb_model.predict(X_test_final)

# Evaluation
best_mae = mean_absolute_error(y_test, best_gb_pred)
best_rmse = np.sqrt(mean_squared_error(y_test, best_gb_pred))
best_r2 = r2_score(y_test, best_gb_pred)

print("Tuned Gradient Boosting Evaluation")
print("-" * 40)
print(f"MAE  : {best_mae:.2f}")
print(f"RMSE : {best_rmse:.2f}")
print(f"R²   : {best_r2:.4f}")
  85:
final_model = gb_model

print("Final model selected: Gradient Boosting")
  86:
import requests
import pandas as pd

base_url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

crop_codes = {
    "Wheat": 15,
    "Rice": 27,
    "Maize": 56,
    "Sugar cane": 156,
    "Potatoes": 116,
    "Cotton": 767
}

results = []

for crop, item_code in crop_codes.items():

    # Area Harvested
    params_area = {
        "area": 165,
        "item": item_code,
        "element": 5312,
        "year": 2025
    }

    response_area = requests.get(base_url, params=params_area)
    data_area = response_area.json().get("data", [])

    # Production Quantity
    params_prod = {
        "area": 165,
        "item": item_code,
        "element": 5510,
        "year": 2025
    }

    response_prod = requests.get(base_url, params=params_prod)
    data_prod = response_prod.json().get("data", [])

    area_value = data_area[0]["Value"] if data_area else None
    prod_value = data_prod[0]["Value"] if data_prod else None

    results.append({
        "Crop": crop,
        "Year": 2025,
        "Area_Harvested_ha": area_value,
        "Production_tonnes": prod_value
    })

df_2025 = pd.DataFrame(results)

print(df_2025)
  87:
import requests

url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

params = {
    "area": 165,
    "item": 15,
    "element": 2413,
    "year": 2025
}

response = requests.get(url, params=params, timeout=120)

print("Status:", response.status_code)
print("URL:", response.url)
print("Response:", response.text[:1000])
  88:
import requests

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=120
)

print("Status:", response.status_code)
print(response.text[:1000])
  89:
# Check common token variable names
for name in ["TOKEN", "token", "API_TOKEN", "FAOSTAT_TOKEN", "api_token"]:
    if name in globals():
        print(f"{name} is defined")
  90:
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=120
)

print("Status:", response.status_code)
print("URL:", response.url)
print("Response:", response.text[:1000])
  91: print("TOKEN" in globals())
  92: TOKEN = "eyJraWQiOiJVSFE2dmwrekFTaGRpSGpsOFFSK0d2ZW13RWIzSjZNdytYNTRURXZtNUNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2MmQ1MDQ0NC01MDExLTcwMWUtMzhkYS0wZWYzY2Q2Mjc3MjUiLCJpc3MiOiJodHRwczovL2NvZ25pdG8taWRwLmV1LXdlc3QtMS5hbWF6b25hd3MuY29tL2V1LXdlc3QtMV9iTkVMTk9DMnYiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiIyY3NsdHNpZ2FvODVpdmhwNm9qcDFhaWM3byIsIm9yaWdpbl9qdGkiOiIwYmQxOWRjYy1jZmJjLTQxMTktOGNiMy0wMGE2ZTg1NzkyMjEiLCJldmVudF9pZCI6ImRkMzY2ZjQyLTM2NzAtNGMzNS1iZjE1LWM4MzI0MjI3M2QzOCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gcGhvbmUgb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE3ODY3NjQ2MzIsImV4cCI6MTc4Njc5MTQxMCwiaWF0IjoxNzg2Nzg3ODEwLCJqdGkiOiI2MzI0M2U2My0wZmUzLTQyMzUtYjQxNS01OGFhZjUxMWFkYmEiLCJ1c2VybmFtZSI6Ik11aGFtbWFkLUhhc3NhbiJ9.DaSJdniSBNrP9NCUAlWr-YDNLKI3MecQYA2aOQMdrN6xz3tBkWHeNsF9izUuJKOZZk3PFLq0XE8TU1xKa-Qw3VmA3wGRodFETFqUkmHW9R0A2QMqje6GovXvfCBlSkdjbhwTpvm4zWvKO_BwtMdcdsGkIzPXSwSAgNoXXJ7PoSXrf6cAB_hx92u113Ksp1TMWMbVX6UwCTEEIlMVkzNmJQH1J_NvByN-T5wgZC1SAaz17-kgrOUqYWVvi9Rzuh3oZgyW9xA5db0d1ynFUooQqxMHuejexBG-pZFGzvktniXrxSdXirhd42eNiXuSlqyvQIBxma4AmAgpGwp1NDA1fg"
  93: print("TOKEN" in globals())
  94:
import requests

url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

params = {
    "area": 165,
    "item": 15,
    "element": 5412,   # Yield
    "year": 2025
}

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=120
)

print("Status:", response.status_code)
print("URL:", response.url)
print("Response:", response.text[:1000])
  95:
import requests
import pandas as pd

base_url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

crops = {
    "Wheat": 15,
    "Rice": 27,
    "Maize": 56,
    "Sugar cane": 156,
    "Potatoes": 116,
    "Cotton": 826
}

results = []

for crop, item_code in crops.items():

    # Area Harvested
    params_area = {
        "area": 165,
        "item": item_code,
        "element": 5312,
        "year": 2025
    }

    response_area = requests.get(
        base_url,
        params=params_area,
        headers=headers,
        timeout=120
    )

    data_area = response_area.json().get("data", [])

    # Production Quantity
    params_prod = {
        "area": 165,
        "item": item_code,
        "element": 5510,
        "year": 2025
    }

    response_prod = requests.get(
        base_url,
        params=params_prod,
        headers=headers,
        timeout=120
    )

    data_prod = response_prod.json().get("data", [])

    results.append({
        "Crop": crop,
        "Year": 2025,
        "Area_Harvested_ha": float(data_area[0]["Value"]) if data_area else None,
        "Production_tonnes": float(data_prod[0]["Value"]) if data_prod else None
    })

future_2025 = pd.DataFrame(results)

print(future_2025)
  96:
import requests
import pandas as pd

url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

# Wheat ke saare elements check
params = {
    "area": 165,
    "item": 15,
    "year": 2025
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=120
)

print("Status:", response.status_code)

data = response.json().get("data", [])

element_df = pd.DataFrame(data)

print(element_df[[
    "Element Code",
    "Element",
    "Unit",
    "Value"
]].to_string(index=False))
  97:
print("Status:", response.status_code)
print("URL:", response.url)
print("Response:")
print(response.text[:2000])
  98:
data = response.json().get("data", [])

print("Number of records:", len(data))

if data:
    print(data)
else:
    print("No data returned from FAOSTAT API.")
  99:
import requests
import pandas as pd

url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

crops = {
    "Wheat": 15,
    "Rice": 27,
    "Maize": 56,
    "Sugar cane": 156,
    "Potatoes": 116,
    "Cotton": 826
}

for crop, item_code in crops.items():

    params = {
        "area": 165,
        "item": item_code,
        "year": 2025
    }

    r = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=120
    )

    data = r.json().get("data", [])

    print(f"{crop} → {len(data)} rows")

    if data:
        print(data)
 100:
import requests

url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

crops = {
    "Wheat": 15,
    "Rice": 27,
    "Maize": 56,
    "Sugar cane": 156,
    "Potatoes": 116,
    "Cotton": 826
}

for crop, item_code in crops.items():

    params = {
        "area": 165,
        "item": item_code,
        "year": 2025
    }

    r = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=120
    )

    print(f"\n{crop}")
    print("Status:", r.status_code)

    # JSON response check
    if r.status_code != 200:
        print("Response:", r.text[:300])
        continue

    try:
        result = r.json()
    except ValueError:
        print("Response is not JSON:")
        print(r.text[:300])
        continue

    data = result.get("data", [])

    print("Rows:", len(data))

    if data:
        print(data[0])
    else:
        print("No 2025 data available.")
 101:
print("TOKEN exists:", "TOKEN" in globals())
print("TOKEN length:", len(TOKEN) if "TOKEN" in globals() else 0)
 102:
import requests

url = "https://faostatservices.fao.org/api/v1/en/data/QCL"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

params = {
    "area": 165,
    "item": 15,
    "year": 2025
}

r = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=120
)

print("Status:", r.status_code)
print("URL:", r.url)
print("Response:", r.text[:1000])
 103: TOKEN ="eyJraWQiOiJVSFE2dmwrekFTaGRpSGpsOFFSK0d2ZW13RWIzSjZNdytYNTRURXZtNUNJPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2MmQ1MDQ0NC01MDExLTcwMWUtMzhkYS0wZWYzY2Q2Mjc3MjUiLCJpc3MiOiJodHRwczovL2NvZ25pdG8taWRwLmV1LXdlc3QtMS5hbWF6b25hd3MuY29tL2V1LXdlc3QtMV9iTkVMTk9DMnYiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiIyY3NsdHNpZ2FvODVpdmhwNm9qcDFhaWM3byIsIm9yaWdpbl9qdGkiOiIwYmQxOWRjYy1jZmJjLTQxMTktOGNiMy0wMGE2ZTg1NzkyMjEiLCJldmVudF9pZCI6ImRkMzY2ZjQyLTM2NzAtNGMzNS1iZjE1LWM4MzI0MjI3M2QzOCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gcGhvbmUgb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE3ODY3NjQ2MzIsImV4cCI6MTc4Njc5MTQxMCwiaWF0IjoxNzg2Nzg3ODEwLCJqdGkiOiI2MzI0M2U2My0wZmUzLTQyMzUtYjQxNS01OGFhZjUxMWFkYmEiLCJ1c2VybmFtZSI6Ik11aGFtbWFkLUhhc3NhbiJ9.DaSJdniSBNrP9NCUAlWr-YDNLKI3MecQYA2aOQMdrN6xz3tBkWHeNsF9izUuJKOZZk3PFLq0XE8TU1xKa-Qw3VmA3wGRodFETFqUkmHW9R0A2QMqje6GovXvfCBlSkdjbhwTpvm4zWvKO_BwtMdcdsGkIzPXSwSAgNoXXJ7PoSXrf6cAB_hx92u113Ksp1TMWMbVX6UwCTEEIlMVkzNmJQH1J_NvByN-T5wgZC1SAaz17-kgrOUqYWVvi9Rzuh3oZgyW9xA5db0d1ynFUooQqxMHuejexBG-pZFGzvktniXrxSdXirhd42eNiXuSlqyvQIBxma4AmAgpGwp1NDA1fg"
 104:
print("TOKEN exists:", "TOKEN" in globals())
print("TOKEN length:", len(TOKEN))
 105: %history -n -f faostat_history.py
