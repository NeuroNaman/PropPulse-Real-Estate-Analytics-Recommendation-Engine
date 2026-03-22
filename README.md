<div align="center">

<!-- Banner SVG — renders on GitHub, local preview, and any markdown viewer -->
<svg width="100%" viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f0c29"/>
      <stop offset="50%" stop-color="#302b63"/>
      <stop offset="100%" stop-color="#24243e"/>
    </linearGradient>
    <linearGradient id="wave1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#6366f1" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="860" height="200" fill="url(#bg)" rx="14"/>
  <!-- Decorative dot grid -->
  <rect x="0" y="0" width="860" height="200" fill="url(#wave1)" rx="14"/>
  <g fill="#ffffff" fill-opacity="0.04">
    <circle cx="80"  cy="30"  r="80"/>
    <circle cx="760" cy="170" r="100"/>
    <circle cx="430" cy="10"  r="60"/>
  </g>
  <!-- Title -->
  <text x="430" y="100" text-anchor="middle" font-family="'Segoe UI',Arial,sans-serif" font-size="68" font-weight="800" fill="#ffffff" letter-spacing="-2">PropPulse</text>
  <!-- Subtitle -->
  <text x="430" y="138" text-anchor="middle" font-family="'Segoe UI',Arial,sans-serif" font-size="16" font-weight="400" fill="rgba(255,255,255,0.65)" letter-spacing="1">Real Estate Analytics &amp; Recommendation Engine</text>
  <!-- Author line -->
  <text x="430" y="170" text-anchor="middle" font-family="'Segoe UI',Arial,sans-serif" font-size="11" font-weight="400" fill="rgba(255,255,255,0.3)" letter-spacing="2">BY NAMAN NANDA · GITHUB: NEURONAMAN · NOV – DEC 2025</text>
  <!-- Bottom wave decoration -->
  <path d="M0 185 Q215 160 430 185 Q645 210 860 185 L860 200 L0 200 Z" fill="#6366f1" fill-opacity="0.15"/>
</svg>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-5.0+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![XGBoost](https://img.shields.io/badge/XGBoost-Enabled-189AB4?style=for-the-badge)](https://xgboost.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

<br/>

> **🏆 Benchmarked 11 ML models · R² improved from 0.73 → 0.90 · MAE reduced from 0.94 → 0.45**  
> **🏡 246 real estate projects · 1,000+ geospatial features · TF-IDF hybrid recommender**

<br/>

[🚀 Live Demo](#-live-demo) · [📊 Model Results](#-model-performance) · [🔧 Installation](#-installation) · [📁 Project Structure](#-project-structure) · [👤 Author](#-author)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Highlights](#-key-highlights)
- [System Architecture](#-system-architecture)
- [ML Pipeline](#-ml-pipeline)
- [Model Performance](#-model-performance)
- [Recommender System](#-recommender-system)
- [Feature Engineering](#-feature-engineering)
- [App Modules](#-app-modules)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Author](#-author)

---

## 🌐 Overview

**PropPulse** is a full-stack real estate intelligence platform built to predict property prices, uncover market insights, and recommend the most relevant properties to prospective buyers — all powered by machine learning and advanced data science techniques.

The project covers the complete data science lifecycle: **web scraping → data cleaning → EDA → feature engineering → model selection → deployment**, packaged into an interactive Streamlit application with 3 dedicated modules.

```
🔎 Scrape  →  🧹 Clean  →  🔬 Analyze  →  🧠 Model  →  📊 Visualize  →  🚀 Deploy
```

---

## ✨ Key Highlights

| Feature | Detail |
|---|---|
| 🤖 **Models Benchmarked** | 11 algorithms including XGBoost, LightGBM, Random Forest, Ridge, Lasso |
| 📉 **MAE Reduction** | `0.94 → 0.45` (52% improvement) |
| 📈 **R² Score** | `0.73 → 0.90` after pipeline redesign |
| 🏗️ **Properties Covered** | 246 real estate projects across sectors |
| 📐 **Geospatial Features** | 1,000+ location-based distance features |
| 🧮 **CV Strategy** | 10-Fold Cross Validation + GridSearchCV |
| 🏷️ **Encoding** | Target Encoding for high-cardinality sector features |
| 🔍 **Recommender** | Hybrid: TF-IDF + Price + Geospatial similarity |

---

## 🏛️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         PropPulse Platform                          │
├─────────────┬──────────────────────────┬───────────────────────────┤
│  Module 1   │        Module 2          │        Module 3           │
│  🏠 Price   │     📊 Analytics         │    🏡 Recommender         │
│  Predictor  │       Dashboard          │       System              │
└──────┬──────┴────────────┬─────────────┴────────────┬──────────────┘
       │                   │                          │
       ▼                   ▼                          ▼
┌─────────────┐   ┌────────────────┐      ┌──────────────────────┐
│ ML Pipeline │   │  Plotly/Seaborn│      │  Cosine Similarity   │
│ + GridSearch│   │  Visualizations│      │  TF-IDF + Geo + Price│
└──────┬──────┘   └────────────────┘      └──────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        Data Layer                                   │
│   Web Scraping → Missing Value Imputation → Outlier Treatment       │
│   Feature Engineering → Target Encoding → ColumnTransformer        │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🔬 ML Pipeline

The end-to-end pipeline was designed with `ColumnTransformer` for modular preprocessing and `Pipeline` for reproducible predictions.

```
Raw Data
   │
   ▼
┌────────────────────────────────────┐
│   Missing Value Imputation         │
│   • Median for numerical           │
│   • Mode / KNN for categorical     │
└──────────────┬─────────────────────┘
               │
               ▼
┌────────────────────────────────────┐
│   Outlier Treatment                │
│   • IQR capping                    │
│   • Log transformation (price)     │
└──────────────┬─────────────────────┘
               │
               ▼
┌────────────────────────────────────┐
│   Feature Engineering              │
│   • Luxury Score                   │
│   • Floor Category                 │
│   • Age Possession Bins            │
│   • Price Per SqFt                 │
│   • Geospatial Clustering          │
└──────────────┬─────────────────────┘
               │
               ▼
┌────────────────────────────────────┐
│   ColumnTransformer                │
│   • OHE for low-cardinality cols   │
│   • Target Encoding for 'sector'   │
│   • StandardScaler for numerics    │
└──────────────┬─────────────────────┘
               │
               ▼
┌────────────────────────────────────┐
│   Model Training + GridSearchCV    │
│   • 10-Fold Cross Validation       │
│   • Random Forest (Best)           │
└──────────────┬─────────────────────┘
               │
               ▼
         Final Model
     MAE: 0.45 | R²: 0.90
```

---

## 📊 Model Performance

All 11 models were benchmarked under identical 10-fold CV conditions on log-transformed price targets.

| Rank | Model | MAE ↓ | RMSE ↓ | R² ↑ |
|------|-------|--------|--------|------|
| 🥇 1 | **Random Forest** | **0.45** | **0.61** | **0.90** |
| 🥈 2 | XGBoost | 0.48 | 0.64 | 0.88 |
| 🥉 3 | LightGBM | 0.49 | 0.65 | 0.87 |
| 4 | Gradient Boosting | 0.52 | 0.68 | 0.85 |
| 5 | Extra Trees | 0.53 | 0.70 | 0.84 |
| 6 | SVR (RBF) | 0.60 | 0.79 | 0.79 |
| 7 | KNN Regressor | 0.63 | 0.83 | 0.76 |
| 8 | Ridge Regression | 0.69 | 0.88 | 0.73 |
| 9 | Lasso Regression | 0.71 | 0.91 | 0.71 |
| 10 | Decision Tree | 0.78 | 1.01 | 0.64 |
| 11 | Linear Regression | 0.94 | 1.20 | 0.55 |

> 📌 **Baseline (Linear Regression): MAE = 0.94, R² = 0.55**  
> 📌 **Final Model (Random Forest + Pipeline): MAE = 0.45, R² = 0.90**  
> 🔺 **52% MAE reduction · 63% R² improvement**

---

## 🏡 Recommender System

A **hybrid content-based recommender** was built for 246 residential projects using three complementary similarity matrices combined via weighted fusion.

```
┌──────────────────────────────────────────────────────────┐
│              Hybrid Similarity Score                     │
│                                                          │
│   Final_Score = w1×S_facility + w2×S_price + w3×S_geo   │
│                                                          │
│   Default Weights:                                       │
│   • w1 = 0.5  (TF-IDF facility similarity)              │
│   • w2 = 0.8  (40+ price-based features)                │
│   • w3 = 1.0  (1,000+ geospatial features)              │
└──────────────────────────────────────────────────────────┘

Cosine Similarity Matrix  →  Top-N Ranked Results
       (246 × 246)               with links + scores
```

### Similarity Components

| Component | Method | Features Used |
|-----------|--------|---------------|
| 🏊 Facility Similarity | TF-IDF + Cosine | Amenities text (pool, gym, parking…) |
| 💰 Price Similarity | Cosine on scaled features | 40+ price & size-related attributes |
| 📍 Geospatial Similarity | Cosine on distance matrix | 1,000+ distances to landmarks/schools |

Users can **interactively adjust weights** (w1, w2, w3) via sliders in the Streamlit UI to personalize recommendations.

---

## ⚙️ Feature Engineering

New features engineered to improve model performance:

```python
# Key engineered features
df['price_per_sqft']   = df['price'] / df['built_up_area']
df['luxury_category']  = pd.cut(df['luxury_score'], bins=[...], labels=['Low', 'Medium', 'High'])
df['floor_category']   = pd.cut(df['floorNum'], bins=[...], labels=['Low', 'Mid', 'High', 'Top'])
df['total_rooms']      = df['bedRoom'] + df['bathroom'] + df['balcony']
df['age_group']        = df['agePossession'].map(age_bucket_fn)
```

| Feature Group | Count | Description |
|---|---|---|
| Property Attributes | 12 | BHK, area, floor, age, furnishing… |
| Location Features | 1,000+ | Distance to metro, schools, hospitals |
| Derived Features | 8 | Luxury score, price/sqft, room ratio |
| Encoded Features | ~30 | OHE + Target Encoding expansions |
| **Total Features** | **~1,050+** | |

**Target Encoding** was applied to the `sector` column (high-cardinality: 50+ unique sectors) — replacing naive OHE which caused dimensionality explosion and worsened R² from 0.90 → 0.73.

---

## 📱 App Modules

### Module 1 — 🏠 Price Predictor
```
Input: property_type, sector, bedrooms, bathrooms, balconies,
       age, built_up_area, servant_room, store_room,
       furnishing_type, luxury_category, floor_category

Output: Predicted price range in ₹ Crores
        [Base − 0.22 Cr, Base + 0.22 Cr]
```

### Module 2 — 📊 Analytics Dashboard

Three sections powered by Plotly/Seaborn:

| Section | Visualizations |
|---------|---------------|
| 🏡 Overview | Geo-heatmap, sector bar chart, 3D scatter, animated trends |
| 📊 Data Viz | Violin plots, heatmaps, box plots, scatter w/ trendline |
| 🔍 Insights | BHK price box, distribution plots, bubble cluster analysis |

### Module 3 — 🏡 Apartment Recommender
- **Location Search**: Find all apartments within a user-defined radius (km)
- **Similarity Recommendations**: Top-5 similar projects with adjustable weights
- **Property Links**: Direct links to listings

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/NeuroNaman/PropPulse.git
cd PropPulse

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run Home.py
```

### Requirements

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
```

---

## 📁 Project Structure

```
PropPulse/
│
├── 📂 pages/
│   ├── 1_Price_Predictor.py          # ML price prediction app
│   ├── 2_Analysis_App.py             # Analytics dashboard
│   └── 3_Recommend_Appartments.py   # Hybrid recommender
│
├── 📂 notebooks/
│   ├── web_scraping_residential_land.ipynb
│   ├── missing-value-imputation.ipynb
│   ├── outlier-treatment.ipynb
│   ├── feature-engineering.ipynb
│   ├── baseline_model.ipynb
│   ├── model-selection.ipynb
│   └── recommender-system.ipynb
│
├── 📂 datasets/
│   ├── df.pkl                        # Processed dataframe
│   ├── data_viz1.csv                 # Visualization dataset
│   ├── appartments.csv               # Property listings
│   ├── feature_text.pkl              # TF-IDF feature text
│   ├── location_df_merge.pkl         # Geospatial distances
│   ├── cosine_sim1.pkl               # Facility similarity matrix
│   ├── cosine_sim2.pkl               # Price similarity matrix
│   └── cosine_sim3.pkl               # Geo similarity matrix
│
├── pipeline1.pkl.gz                  # Compressed ML pipeline
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **ML Framework** | Scikit-learn, XGBoost, LightGBM |
| **NLP / Recommender** | TF-IDF (sklearn), Cosine Similarity |
| **Hyperparameter Tuning** | GridSearchCV, Optuna |
| **Encoding** | Target Encoding (category_encoders) |
| **Web Framework** | Streamlit |
| **Visualization** | Plotly, Matplotlib, Seaborn |
| **Data Processing** | Pandas, NumPy |
| **Serialization** | Pickle, Gzip |
| **Version Control** | Git / GitHub |

</div>

---

## 📅 Timeline

```
Nov 2025                                                    Dec 2025
   │                                                            │
   ▼                                                            ▼
[Week 1]──────[Week 2]──────[Week 3]──────[Week 4]──────[Week 5]
Web Scrape   Data Clean   Feature Eng   Model Select   App Deploy
& EDA        & Imputation  & Encoding    & Tuning       & Testing
```

---

## 👤 Author

<div align="center">

<img src="https://avatars.githubusercontent.com/NeuroNaman" width="100" style="border-radius:50%"/>

### Naman Nanda

[![GitHub](https://img.shields.io/badge/GitHub-NeuroNaman-181717?style=for-the-badge&logo=github)](https://github.com/NeuroNaman)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/naman-nanda)

*Data Science · Machine Learning · Full Stack Analytics*

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

<svg width="100%" viewBox="0 0 860 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgf" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#24243e"/>
      <stop offset="50%" stop-color="#302b63"/>
      <stop offset="100%" stop-color="#0f0c29"/>
    </linearGradient>
  </defs>
  <path d="M0 20 Q215 0 430 20 Q645 40 860 20 L860 80 L0 80 Z" fill="url(#bgf)" rx="0"/>
</svg>

**⭐ If you found PropPulse useful, please star the repository!**

*Built with ❤️ by [Naman Nanda](https://github.com/NeuroNaman)*

</div>