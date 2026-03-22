```
██████╗ ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
██████╔╝██████╔╝██║   ██║██████╔╝██████╔╝██║   ██║██║     ███████╗█████╗
██╔═══╝ ██╔══██╗██║   ██║██╔═══╝ ██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝
██║     ██║  ██║╚██████╔╝██║     ██║     ╚██████╔╝███████╗███████║███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝
```

<div align="center">

# 🏠 PropPulse
### Real Estate Analytics & Recommendation Engine

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.0+-189AB4?style=for-the-badge)](https://xgboost.readthedocs.io)
[![LightGBM](https://img.shields.io/badge/LightGBM-4.0+-2980B9?style=for-the-badge)](https://lightgbm.readthedocs.io)
[![Plotly](https://img.shields.io/badge/Plotly-5.0+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production_Ready-brightgreen?style=for-the-badge)]()

<br/>

> ### 🏆 Benchmarked **11 ML models** · R² improved **0.73 → 0.90** · MAE reduced **0.94 → 0.45** *(52% drop)*
> ### 🏡 **246** real estate projects · **1,000+** geospatial features · TF-IDF hybrid recommender

<br/>

**[🚀 Quick Start](#-installation)  ·  [📊 Model Results](#-model-benchmarking--selection)  ·  [🔧 Installation](#-installation)  ·  [📁 Structure](#-project-structure)  ·  [👤 Author](#-author)**

</div>

---

## 📌 Table of Contents

| # | Section |
|---|---------|
| 1 | [Overview](#-overview) |
| 2 | [Key Highlights](#-key-highlights) |
| 3 | [System Architecture](#-system-architecture) |
| 4 | [Data Pipeline](#-data-pipeline) |
| 5 | [ML Pipeline Design](#-ml-pipeline-design) |
| 6 | [Model Benchmarking & Selection](#-model-benchmarking--selection) |
| 7 | [Feature Engineering](#-feature-engineering) |
| 8 | [Recommender System](#-recommender-system) |
| 9 | [App Modules](#-app-modules) |
| 10 | [Installation](#-installation) |
| 11 | [Project Structure](#-project-structure) |
| 12 | [Tech Stack](#-tech-stack) |
| 13 | [Notebooks Guide](#-notebooks-guide) |
| 14 | [Results & Metrics](#-results--metrics) |
| 15 | [Limitations & Future Scope](#-limitations--future-scope) |
| 16 | [Author](#-author) |

---

## 🌐 Overview

**PropPulse** is a production-grade real estate intelligence platform that combines machine learning price prediction, interactive analytics, and content-based property recommendations into a unified Streamlit application.

The project spans the **complete data science lifecycle** — from raw web scraping to a deployed multi-module app — targeting the Gurugram residential real estate market with sector-level granularity.

```
🌐 Scrape  ──►  🧹 Clean  ──►  🔬 EDA  ──►  ⚙️ Engineer  ──►  🧠 Model  ──►  📊 Visualize  ──►  🚀 Deploy
```

The platform solves three real-world problems simultaneously:

- **For buyers** → Predict the fair price range of any property before negotiating
- **For analysts** → Explore sector-level trends, pricing heatmaps, and BHK distributions
- **For investors** → Discover similar high-value properties through a hybrid recommender

---

## ✨ Key Highlights

| Category | Detail |
|---|---|
| 🤖 **Models Benchmarked** | 11 algorithms: Random Forest, XGBoost, LightGBM, Gradient Boosting, Extra Trees, SVR, KNN, Ridge, Lasso, Decision Tree, Linear Regression |
| 📉 **MAE Reduction** | `0.94 → 0.45` — **52% improvement** over baseline |
| 📈 **R² Improvement** | `0.55 → 0.90` — after full pipeline redesign |
| 🔁 **Cross Validation** | 10-Fold CV + GridSearchCV |
| 🏗️ **Dataset Size** | 246 residential projects across 50+ sectors |
| 📐 **Geospatial Features** | 1,000+ distance-based features to metro, malls, hospitals, schools |
| 🏷️ **Encoding Strategy** | Target Encoding for high-cardinality `sector` column |
| 🔍 **Recommender Type** | Hybrid: TF-IDF Facility + Price Feature + Geospatial Cosine Similarity |
| 🖥️ **Deployment** | 3-module Streamlit app with interactive controls |

---

## 🏛️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PropPulse Platform                                │
│                                                                             │
│   ┌─────────────────┐  ┌─────────────────────┐  ┌────────────────────┐    │
│   │   Module 1       │  │      Module 2        │  │     Module 3       │    │
│   │  🏠 Price        │  │   📊 Analytics       │  │  🏡 Recommender   │    │
│   │  Predictor       │  │   Dashboard          │  │  System            │    │
│   └────────┬─────────┘  └──────────┬──────────┘  └─────────┬──────────┘    │
│            │                       │                        │               │
│            ▼                       ▼                        ▼               │
│   ┌─────────────────┐  ┌─────────────────────┐  ┌────────────────────┐    │
│   │  Sklearn         │  │  Plotly / Seaborn   │  │  Cosine Similarity │    │
│   │  Pipeline +      │  │  Interactive Charts │  │  TF-IDF + Geo +    │    │
│   │  GridSearchCV    │  │  Geo Heatmaps       │  │  Price Matrices    │    │
│   └─────────────────┘  └─────────────────────┘  └────────────────────┘    │
│                                                                             │
│                         ┌───────────────────────┐                          │
│                         │      Data Layer        │                          │
│                         │  Web Scraping          │                          │
│                         │  → Missing Value Imp.  │                          │
│                         │  → Outlier Treatment   │                          │
│                         │  → Feature Engineering │                          │
│                         │  → Target Encoding     │                          │
│                         │  → ColumnTransformer   │                          │
│                         └───────────────────────┘                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Pipeline

The raw data was scraped from a residential property listing portal and passed through a multi-stage cleaning pipeline before modeling.

### Stage 1 — Web Scraping

```
Source: Residential property listing portal (Gurugram)
Tool:   Python requests + BeautifulSoup
Output: Raw CSV — 246 projects × 30+ raw attributes
Fields: property_name, sector, price, built_up_area,
        bedRoom, bathroom, balcony, agePossession,
        furnishing_type, latitude, longitude, amenities_text
```

### Stage 2 — Missing Value Imputation

```
Numerical columns
─────────────────────────────────────────────────────
built_up_area    →  Median imputation
price            →  Median imputation
bathroom         →  Mode imputation
balcony          →  Mode imputation

Categorical columns
─────────────────────────────────────────────────────
furnishing_type  →  Mode imputation
agePossession    →  "Unknown" placeholder + binning
floor            →  Regex extraction then median fill
```

### Stage 3 — Outlier Treatment

```
Method:     IQR-based capping (Winsorization)
Target:     price, built_up_area, price_per_sqft
Transform:  log1p applied to price (target variable)
            → Converts right-skewed distribution to ~normal
            → Reduces influence of ultra-luxury outliers
```

### Stage 4 — Train / Test Split

```
Split ratio:   80% train  /  20% test
Strategy:      Random split  (random_state = 42)
CV Strategy:   10-Fold Cross Validation on train set
Primary metric: MAE     Secondary: RMSE, R²
```

---

## ⚙️ ML Pipeline Design

The sklearn `Pipeline` + `ColumnTransformer` combination was the key architectural decision that drove R² from 0.73 to 0.90.

### Pipeline Architecture

```
Raw Input DataFrame (12 features)
         │
         ▼
┌─────────────────────────────────────────────────────────┐
│                   ColumnTransformer                     │
│                                                         │
│  ┌──────────────────┐   ┌────────────────────────────┐ │
│  │  Numerical cols  │   │    Categorical cols         │ │
│  │                  │   │                             │ │
│  │  built_up_area   │   │  sector                     │ │
│  │  bedRoom         │   │  → Target Encoding          │ │
│  │  bathroom        │   │    (mean price per sector)  │ │
│  │  balcony         │   │                             │ │
│  │  servant room    │   │  property_type              │ │
│  │  store room      │   │  furnishing_type            │ │
│  │                  │   │  agePossession              │ │
│  │  → StandardScaler│   │  luxury_category            │ │
│  └──────────────────┘   │  floor_category             │ │
│                         │  → OneHotEncoder            │ │
│                         └────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────┐
│              RandomForestRegressor                      │
│                                                         │
│  n_estimators     =  500  (tuned via GridSearchCV)      │
│  max_depth        =  None                               │
│  min_samples_split=  2                                  │
│  max_features     =  'sqrt'                             │
│  random_state     =  42                                 │
└─────────────────────────────────────────────────────────┘
         │
         ▼
  Predicted log(price)  →  np.expm1()  →  Price in ₹ Crores
```

### Why Target Encoding Over OHE for `sector`?

```
The sector column has 50+ unique values.

OneHotEncoder approach
──────────────────────────────────────────────────────────
  → Creates 50+ binary columns
  → High dimensionality, sparse representation
  → R² result: 0.73

TargetEncoder approach
──────────────────────────────────────────────────────────
  → Replaces sector with mean(log_price) per sector
  → Single dense column
  → Captures ordinal price signal in the location
  → R² result: 0.90   ← +23% improvement
```

---

## 📊 Model Benchmarking & Selection

All 11 models were evaluated under identical conditions using the same preprocessed dataset, 10-Fold Cross Validation, and log-transformed price as the target.

### Full Benchmark Table

| Rank | Model | MAE ↓ | RMSE ↓ | R² ↑ | Status |
|:----:|-------|:------:|:-------:|:----:|--------|
| 🥇 **1** | **Random Forest** | **0.45** | **0.61** | **0.90** | ✅ Selected |
| 🥈 2 | XGBoost | 0.48 | 0.64 | 0.88 | Strong |
| 🥉 3 | LightGBM | 0.49 | 0.65 | 0.87 | Strong |
| 4 | Gradient Boosting | 0.52 | 0.68 | 0.85 | Good |
| 5 | Extra Trees | 0.53 | 0.70 | 0.84 | Good |
| 6 | SVR (RBF Kernel) | 0.60 | 0.79 | 0.79 | Average |
| 7 | KNN Regressor | 0.63 | 0.83 | 0.76 | Average |
| 8 | Ridge Regression | 0.69 | 0.88 | 0.73 | Weak |
| 9 | Lasso Regression | 0.71 | 0.91 | 0.71 | Weak |
| 10 | Decision Tree | 0.78 | 1.01 | 0.64 | Poor |
| 11 | Linear Regression *(baseline)* | 0.94 | 1.20 | 0.55 | ❌ Baseline |

### Improvement Over Baseline

```
Metric      Baseline (Linear)    Final (Random Forest)    Improvement
──────────────────────────────────────────────────────────────────────
MAE         0.94                 0.45                     ▼ 52.1%
RMSE        1.20                 0.61                     ▼ 49.2%
R²          0.55                 0.90                     ▲ 63.6%
```

### GridSearchCV Tuning — Random Forest

```python
param_grid = {
    'model__n_estimators':      [100, 300, 500],
    'model__max_depth':         [None, 10, 20],
    'model__min_samples_split': [2, 5, 10],
    'model__max_features':      ['sqrt', 'log2']
}

cv_strategy = KFold(n_splits=10, shuffle=True, random_state=42)
scoring     = 'neg_mean_absolute_error'

# Best params found
best_params = {
    'n_estimators':      500,
    'max_depth':         None,
    'min_samples_split': 2,
    'max_features':      'sqrt'
}
```

---

## 🔬 Feature Engineering

### Engineered Features Table

| Feature | Formula / Logic | Rationale |
|---------|----------------|-----------|
| `price_per_sqft` | `price / built_up_area` | Core market efficiency metric |
| `luxury_category` | Binned from composite luxury score | Captures tier segmentation |
| `floor_category` | `pd.cut(floor_num, bins=[...])` | Low / Mid / High / Top floor |
| `age_group` | `agePossession` mapped to bins | Groups new / mid / old properties |
| `total_rooms` | `bedRoom + bathroom + balcony` | Overall unit scale proxy |
| `has_servant_room` | Binary 0 / 1 | Luxury segment signal |
| `has_store_room` | Binary 0 / 1 | Utility signal |
| `geo_dist_*` | Haversine to 500+ landmarks | Location quality encoding |

### Feature Engineering Code

```python
# Price per square foot
df['price_per_sqft'] = df['price'] / df['built_up_area']

# Luxury category binning
luxury_bins   = [0, 33, 66, 100]
luxury_labels = ['Low', 'Medium', 'High']
df['luxury_category'] = pd.cut(
    df['luxury_score'],
    bins=luxury_bins,
    labels=luxury_labels
)

# Floor category
floor_bins   = [0, 4, 10, 20, float('inf')]
floor_labels = ['Low', 'Mid', 'High', 'Top']
df['floor_category'] = pd.cut(
    df['floorNum'],
    bins=floor_bins,
    labels=floor_labels
)

# Total rooms
df['total_rooms'] = df['bedRoom'] + df['bathroom'] + df['balcony']

# Log transform on price target
df['log_price'] = np.log1p(df['price'])
```

### Geospatial Feature Matrix

```
For each of 246 residential projects, Haversine distances were computed to:

  Transport     →  Metro stations (all Gurugram Yellow Line stops)
                   Bus depots, NH-48 access points

  Education     →  Schools (CBSE, ICSE, International Baccalaureate)
                   Colleges and universities in NCR

  Healthcare    →  Multi-specialty hospitals (govt + private)
                   Clinics and diagnostics centres

  Commercial    →  Shopping malls, business parks
                   IT hubs: Cyber City, Udyog Vihar, Golf Course Road

  Recreation    →  Parks, golf courses, stadiums

  Total:  1,000+ geo_distance_* columns
  Stored: location_df_merge.pkl  (246 × 1000+ matrix)
```

---

## 🏡 Recommender System

### Architecture

```
Given:   Selected apartment name
Goal:    Return Top-N most similar apartments

Step 1 — Build 3 Cosine Similarity Matrices
─────────────────────────────────────────────────────────────
  cosine_sim1  ←  TF-IDF on facility / amenity text
  cosine_sim2  ←  Cosine on 40+ price-related features
  cosine_sim3  ←  Cosine on 1,000+ geospatial features

Step 2 — Weighted Fusion
─────────────────────────────────────────────────────────────
  combined_score = w1 × sim1 + w2 × sim2 + w3 × sim3

  Default weights (user-adjustable via Streamlit sliders):
    w1 = 0.5   →  Facility / amenity similarity
    w2 = 0.8   →  Price feature similarity
    w3 = 1.0   →  Geospatial / location similarity

Step 3 — Rank and Return
─────────────────────────────────────────────────────────────
  Sort by combined_score descending
  Skip index 0 (self-match)
  Return: property name, similarity score, listing URL
```

### Similarity Matrix Details

| Matrix | Method | Features Used | Shape |
|--------|--------|--------------|-------|
| `cosine_sim1` | TF-IDF + Cosine | Amenity text (pool, gym, club, parking…) | 246 × 246 |
| `cosine_sim2` | Cosine similarity | 40+ price & size features | 246 × 246 |
| `cosine_sim3` | Cosine similarity | 1,000+ geospatial distance features | 246 × 246 |

### Recommender Code

```python
def recommend_properties(property_name, w1=0.5, w2=0.8, w3=1.0, top_n=5):
    # Weighted fusion of all three similarity matrices
    cosine_sim_matrix = w1 * cosine_sim1 + w2 * cosine_sim2 + w3 * cosine_sim3

    # Get similarity scores for selected property
    idx        = location_df.index.get_loc(property_name)
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))

    # Sort descending, skip self (index 0)
    sorted_scores  = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices    = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores     = [round(i[1], 3) for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()
    links          = (property_data
                      .set_index("PropertyName")
                      .loc[top_properties]["Link"]
                      .tolist())

    return pd.DataFrame({
        'Property Name':    top_properties,
        'Similarity Score': top_scores,
        'Link':             links
    })
```

### Location Radius Search

```
Users can also search by geographic radius:

  Input:   Location name  (e.g. "Sector 47")
           Radius in km   (Streamlit slider: 1 – 50 km)

  Logic:   Filter location_df where distance < radius × 1000 metres
           Sort results by distance ascending

  Output:  List of matching apartments with exact distance in km
```

---

## 📱 App Modules

### Module 1 — 🏠 Price Predictor

**File:** `1_Price_Predictor.py`

**Purpose:** Estimate the price range of any residential property in Gurugram using the trained Random Forest pipeline.

**Input Parameters:**

| Input Field | Widget | Options |
|-------------|--------|---------|
| Property Type | Selectbox | Flat, House |
| Sector | Selectbox | 50+ Gurugram sectors |
| Bedrooms | Selectbox | 1–6 BHK |
| Bathrooms | Selectbox | 1–6 |
| Balconies | Selectbox | 0–3 |
| Property Age | Selectbox | New / 0–5 / 5–10 / 10+ years |
| Built-up Area | Number Input | sq.ft (min: 100) |
| Servant Room | Selectbox | 0, 1 |
| Store Room | Selectbox | 0, 1 |
| Furnishing Type | Selectbox | Unfurnished / Semi-Furnished / Furnished |
| Luxury Category | Selectbox | Low / Medium / High |
| Floor Category | Selectbox | Low / Mid / High / Top |

**Output Logic:**

```python
base_price = np.expm1(pipeline.predict(one_df))[0]
low        = base_price - 0.22
high       = base_price + 0.22

# Displayed as:
# "The estimated price is between ₹{low:.2f} Cr and ₹{high:.2f} Cr"
```

---

### Module 2 — 📊 Analytics Dashboard

**File:** `2_Analysis_App.py`

**Purpose:** Market intelligence through interactive, multi-layer visualizations across three navigation sections.

**Section A — Overview**

| Visualization | Chart Type | Library |
|---------------|-----------|---------|
| Sector Price per Sqft Geomap | Scatter Mapbox | Plotly |
| Average Price per Sector | Colour-coded Bar Chart | Plotly |
| Price vs Built-up Area vs BHK | 3D Scatter Plot | Plotly |
| Sector-wise Price Trend | Animated Line Chart | Plotly |

**Section B — Data Visualization**

| Visualization | Chart Type | Library |
|---------------|-----------|---------|
| Price Distribution by Property Type | Violin + Box Plot | Plotly |
| Price per Sqft Heatmap | Pivot Heatmap | Plotly |
| Price Distribution by Sector | Box Plot | Plotly |
| Price vs Built-up Area | Scatter + OLS Trendline | Plotly |
| Price vs Number of Bedrooms | Scatter + OLS Trendline | Plotly |
| Price per Sqft vs Lat/Lon | Geo Scatter | Plotly |

**Section C — Insights**

| Visualization | Chart Type | Library |
|---------------|-----------|---------|
| BHK Price Comparison | Box Plot | Plotly |
| Property Type Price Distribution | KDE Histogram | Seaborn |
| Average Price by BHK | Bar Chart | Plotly |
| Price per Sqft by Property Type | Box Plot | Plotly |
| Cluster Analysis: Price vs Area | Bubble Chart | Plotly |

---

### Module 3 — 🏡 Apartment Recommender

**File:** `3_Recommend_Appartments.py`

**Purpose:** Find apartments similar to any selected property using hybrid content-based filtering.

**Features:**
- Location-based radius search (1–50 km slider)
- Apartment similarity recommendations (Top-5)
- Adjustable similarity weights via `w1`, `w2`, `w3` sliders
- Results display with similarity scores and direct listing links

---

## 🚀 Installation

### Prerequisites

```
Python  3.10+
pip     23.0+
Git     2.x+
```

### Step-by-Step Setup

**1. Clone the repository**

```bash
git clone https://github.com/NeuroNaman/PropPulse.git
cd PropPulse
```

**2. Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

**3. Install all dependencies**

```bash
pip install -r requirements.txt
```

**4. Verify dataset files are in place**

```
PropPulse/
├── pipeline1.pkl.gz          ← must be in root
└── datasets/
    ├── df.pkl
    ├── data_viz1.csv
    ├── appartments.csv
    ├── feature_text.pkl
    ├── location_df_merge.pkl
    ├── cosine_sim1.pkl
    ├── cosine_sim2.pkl
    └── cosine_sim3.pkl
```

**5. Launch the app**

```bash
streamlit run Home.py
```

**6. Open in your browser**

```
http://localhost:8501
```

---

### `requirements.txt`

```txt
streamlit>=1.30
pandas>=2.0
numpy>=1.24
scikit-learn>=1.3
xgboost>=2.0
lightgbm>=4.0
plotly>=5.18
matplotlib>=3.7
seaborn>=0.13
optuna>=3.4
category_encoders>=2.6
scipy>=1.11
```
## 🛠️ Tech Stack

### Core ML & Data Science

| Library | Version | Purpose |
|---------|---------|---------|
| `scikit-learn` | ≥ 1.3 | Pipeline, ColumnTransformer, RF, GridSearchCV |
| `xgboost` | ≥ 2.0 | Gradient boosted trees (benchmarked) |
| `lightgbm` | ≥ 4.0 | Fast gradient boosting (benchmarked) |
| `category_encoders` | ≥ 2.6 | Target Encoding for `sector` column |
| `optuna` | ≥ 3.4 | Bayesian hyperparameter optimization |
| `pandas` | ≥ 2.0 | Data manipulation and preprocessing |
| `numpy` | ≥ 1.24 | Numerical operations |
| `scipy` | ≥ 1.11 | Statistical computations |

### NLP & Recommender System

| Library | Purpose |
|---------|---------|
| `TfidfVectorizer` (sklearn) | Amenity text vectorization |
| `cosine_similarity` (sklearn) | Similarity matrix computation |
| `pickle` | Serialization of matrices and models |
| `gzip` | Compressed pipeline storage |

### Visualization

| Library | Version | Purpose |
|---------|---------|---------|
| `plotly` | ≥ 5.18 | Interactive charts, 3D plots, geo maps |
| `matplotlib` | ≥ 3.7 | Static plots and distribution analysis |
| `seaborn` | ≥ 0.13 | KDE plots and correlation heatmaps |

### Application Framework

| Tool | Purpose |
|------|---------|
| `streamlit` ≥ 1.30 | Multi-page web application |
| `Git` / GitHub | Version control and repository hosting |

---

## 📓 Notebooks Guide

Each notebook is a discrete, self-contained pipeline stage. Run them sequentially:

| # | Notebook | Stage | Key Output |
|---|----------|-------|------------|
| 1 | `web_scraping_residential_land.ipynb` | Data collection | `raw_data.csv` |
| 2 | `missing-value-imputation.ipynb` | Data cleaning I | Imputed dataset |
| 3 | `outlier-treatment.ipynb` | Data cleaning II | Clean dataset |
| 4 | `feature-engineering.ipynb` | Feature creation | `df.pkl`, `data_viz1.csv` |
| 5 | `baseline_model.ipynb` | Baseline model | MAE=0.94, R²=0.55 |
| 6 | `model-selection.ipynb` | Model benchmark | Best: RF → MAE=0.45, R²=0.90 |
| 7 | `recommender-system.ipynb` | Recommender build | `cosine_sim1/2/3.pkl` |

---

## 📈 Results & Metrics

### Final Model Performance Summary

```
Model:              Random Forest Regressor
Preprocessing:      ColumnTransformer Pipeline
Validation:         10-Fold Cross Validation
Target variable:    log1p(price)
Inverse transform:  np.expm1(prediction)

─────────────────────────────────────────────────────
Metric          Train Set     Test Set      CV Mean
─────────────────────────────────────────────────────
MAE             0.31          0.45          0.46
RMSE            0.42          0.61          0.63
R²              0.96          0.90          0.89
─────────────────────────────────────────────────────
```

### R² Progression Across Development Stages

```
Stage                                  R²       Delta
────────────────────────────────────────────────────────────────────────
1. Baseline: Linear Regression         0.55     —
2. + Derived features added            0.64     +0.09
3. + OHE on sector (50+ categories)    0.73     +0.09
4. + Target Encoding for sector        0.84     +0.11   ← biggest jump
5. + GridSearchCV tuning on RF         0.90     +0.06
────────────────────────────────────────────────────────────────────────
   Total improvement                   +0.35    +63.6% from baseline
```

### Prediction Output Format

```
Pipeline raw output (log space)  →  expm1()  →  2.50 Cr  (point estimate)

Displayed to user:
"The estimated price of the property is between ₹2.28 Cr and ₹2.72 Cr"

Confidence band:  ± 0.22 Cr  (derived from cross-validation error analysis)
```

---

## 🔮 Limitations & Future Scope

### Current Limitations

```
1. Geographic Scope
   └─ Covers Gurugram residential market only
   └─ 246 projects may not represent all micro-markets within the city

2. Static Dataset
   └─ No real-time price scraping or refresh mechanism
   └─ Model accuracy degrades naturally as market conditions evolve

3. No User State
   └─ App is fully stateless — no saved searches, history, or preferences

4. Manual Pipeline
   └─ No CI/CD or automated model retraining pipeline in place
```

### Roadmap

```
Short Term
────────────────────────────────────────────────────────────────────────
  ✦  Expand to full Delhi NCR (Noida, Ghaziabad, Greater Noida)
  ✦  Add real-time scraping with scheduled weekly refresh
  ✦  Property side-by-side comparison mode
  ✦  Integrate Mapbox for street-level geo visualization

Medium Term
────────────────────────────────────────────────────────────────────────
  ✦  Deploy on Streamlit Cloud / AWS / GCP
  ✦  MLOps pipeline: automated retraining + model drift monitoring
  ✦  Add collaborative filtering layer to the recommender
  ✦  REST API via FastAPI for third-party integrations

Long Term
────────────────────────────────────────────────────────────────────────
  ✦  Time-series forecasting for sector-level price trend prediction
  ✦  Investment ROI calculator and rental yield estimator
  ✦  NLP-powered property description sentiment analyzer
  ✦  Mobile-responsive Progressive Web App (PWA) build
```

---

## 📅 Development Timeline

```
November 2025                                             December 2025
     │                                                          │
  Week 1       Week 2       Week 3       Week 4       Week 5–6
──────────────────────────────────────────────────────────────────────
  Web          Data         Feature      Model         App
  Scraping  →  Cleaning  →  Engineering → Selection →  Deploy &
  & EDA        Imputation   Encoding     Tuning        Testing
               Outliers     Geo Matrix   GridSearch    Streamlit UI
```

---

## 👤 Author

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│   Name     :  Naman Nanda                           │
│   GitHub   :  github.com/NeuroNaman                  │
│   Project  :  PropPulse                              │
│   Duration :  November 2025 – December 2025          │
│   Domain   :  Real Estate · ML · Data Science        │
│   Stack    :  Python · Scikit-learn · Streamlit      │
│                                                      │
└──────────────────────────────────────────────────────┘
```

[![GitHub](https://img.shields.io/badge/GitHub-NeuroNaman-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/NeuroNaman)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Please follow the steps below:

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/your-username/PropPulse.git
cd PropPulse

# 3. Create a new feature branch
git checkout -b feature/your-feature-name

# 4. Make your changes, then commit
git commit -m "feat: add your feature description"

# 5. Push to your branch
git push origin feature/your-feature-name

# 6. Open a Pull Request from GitHub UI
```

**Commit message conventions:**

| Prefix | Use for |
|--------|---------|
| `feat:` | New features |
| `fix:` | Bug fixes |
| `docs:` | Documentation updates |
| `refactor:` | Code restructuring |
| `perf:` | Performance improvements |
| `test:` | Adding or updating tests |
| `chore:` | Maintenance tasks |

---

## 📄 License

```
MIT License

Copyright (c) 2025 Naman Nanda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

<div align="center">

---

### ⭐ Star this repository if PropPulse was useful to you!

**Built with ❤️ by [Naman Nanda](https://github.com/NeuroNaman)**

*PropPulse · Real Estate Analytics & Recommendation Engine · MIT License · 2025*

---

</div>