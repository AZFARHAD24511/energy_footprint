# Impact of Latitude on European Electricity Prices

This repository contains a data‑driven analysis of how geographic latitude influences day‑ahead wholesale electricity prices across 18 European market zones. Using publicly available EPEX SPOT data (January 2021 – June 2025), we demonstrate that latitude is the strongest predictor of price variation and build a Random Forest regression model to quantify its effect.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Data Collection](#data-collection)  
3. [Data Preparation](#data-preparation)  
4. [Modeling Approach](#modeling-approach)  
5. [Key Results](#key-results)  
6. [How to Run](#how-to-run)  
7. [References](#references)  

---

## Project Overview

Electricity spot prices vary widely across Europe due to differences in generation mix, grid interconnectivity, and weather patterns. We use Python (pandas, scikit‑learn, matplotlib) to:

- Download and merge hourly day‑ahead price CSVs for 18 zones  
- Transform the data from wide (24 columns for hours) to long format  
- Append each zone’s central latitude  
- Train a Random Forest regressor to predict price from latitude and hour‑of‑day  
- Evaluate model performance and extract feature importances  

---

## Data Collection

1. **Source**  
   - Raw CSV files hosted on the EPEX‑Client GitHub repository:  
     `https://raw.githubusercontent.com/tvanlaerhoven/epex-client/main/data/{ZONE}.csv`  
   - 18 zones (e.g., AT, BE, CH, NO4, etc.) covering January 2021 through June 2025.

2. **Download Logic**  
   - Each file is downloaded only if not already present locally.  
   - Files are saved under `data/raw/` to avoid repeated downloads.  
   - After loading, a `Country` column is added and all dataframes are concatenated into `energy_price_merged_data.csv`.

---

## Data Preparation

1. **Wide → Long Transformation**  
   - Original files have 24 separate columns for each hour (e.g., `00-01`, `01-02`, …).  
   - We melt these into a single `Price` column with an `Hour` identifier.

2. **Datetime Construction**  
   - Extract the hour (`"HH"`) from each column name and append `":00"` to build a time string.  
   - Combine `Date` and `Hour` into a unified `datetime` column of type `pd.Timestamp`.

3. **Latitude Mapping**  
   - A dictionary maps each zone code to its central latitude (e.g., `"FR": 46.2`, `"NO4": 65.0`).  
   - The latitude feature is crucial for understanding geographic effects.

4. **One‑Hot Encoding**  
   - Create dummy variables for the 24 hours of day, dropping the first to avoid multicollinearity.

---

## Modeling Approach

- **Train/Test Split**  
  - 70% training, 30% testing, random seed = 42.
- **Random Forest Regressor**  
  - 100 trees, maximum depth = 10, parallel jobs enabled.
- **Evaluation Metrics**  
  - Coefficient of determination ($R^2$)  
  - Mean Absolute Error (MAE)

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

rf = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)
print(f"R²: {r2_score(y_test, y_pred):.3f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f} EUR/MWh")



For access to the full article, please visit:

[http://dx.doi.org/10.13140/RG.2.2.31353.17760](http://dx.doi.org/10.13140/RG.2.2.31353.17760)
