import streamlit as st
import pickle
import gzip
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Property Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("🏙️ AI Property Intelligence Dashboard")
st.markdown(
"""
Interactive analytics and explainable AI insights for the **Real Estate Price Prediction System**.
"""
)

# ---------------------------------------------------
# LOAD DATA (CACHED)
# ---------------------------------------------------
@st.cache_data
def load_data():
    with open('datasets/df.pkl', 'rb') as file:
        df = pickle.load(file)
    return df


@st.cache_resource
def load_pipeline():
    with gzip.open('pipeline1.pkl.gz', 'rb') as file:
        pipeline = pickle.load(file)
    return pipeline


df = load_data()
pipeline = load_pipeline()

model = pipeline.named_steps["regressor"]

# ---------------------------------------------------
# KPI DASHBOARD
# ---------------------------------------------------
st.markdown("## 📈 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Properties", f"{len(df):,}")
col2.metric("Unique Sectors", df["sector"].nunique())
col3.metric("Luxury Categories", df["luxury_category"].nunique())
col4.metric("Furnishing Types", df["furnishing_type"].nunique())

st.divider()

# ---------------------------------------------------
# FEATURE IMPORTANCE (XAI)
# ---------------------------------------------------
st.markdown("## 🧠 Model Explainability")

features = [
    'bedRoom',
    'bathroom',
    'built_up_area',
    'servant room',
    'store room'
]

importances = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importances[:len(features)]
}).sort_values("Importance", ascending=True)

fig_importance = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    color_continuous_scale="viridis",
    title="Feature Importance for Price Prediction"
)

fig_importance.update_layout(
    template="plotly_dark",
    height=400
)

st.plotly_chart(fig_importance, use_container_width=True)

st.divider()

# ---------------------------------------------------
# INTERACTIVE FILTER
# ---------------------------------------------------
st.markdown("## 🔍 Dataset Exploration")

sector_filter = st.multiselect(
    "Select Sector",
    df["sector"].unique(),
    default=df["sector"].unique()[:5]
)

filtered_df = df[df["sector"].isin(sector_filter)]

# ---------------------------------------------------
# SECTOR DISTRIBUTION
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    sector_counts = filtered_df["sector"].value_counts()

    fig_sector = px.bar(
        sector_counts,
        x=sector_counts.index,
        y=sector_counts.values,
        labels={"x": "Sector", "y": "Property Count"},
        title="Top Sectors by Property Count"
    )

    fig_sector.update_layout(template="plotly_dark")

    st.plotly_chart(fig_sector, use_container_width=True)

# ---------------------------------------------------
# BEDROOM DISTRIBUTION
# ---------------------------------------------------
with col2:

    fig_bed = px.histogram(
        filtered_df,
        x="bedRoom",
        nbins=10,
        title="Bedroom Distribution",
        color_discrete_sequence=["#00CC96"]
    )

    fig_bed.update_layout(template="plotly_dark")

    st.plotly_chart(fig_bed, use_container_width=True)

# ---------------------------------------------------
# LUXURY DISTRIBUTION
# ---------------------------------------------------
col3, col4 = st.columns(2)

with col3:

    luxury_counts = filtered_df["luxury_category"].value_counts()

    fig_luxury = px.pie(
        names=luxury_counts.index,
        values=luxury_counts.values,
        title="Luxury Category Distribution",
        hole=0.4
    )

    fig_luxury.update_layout(template="plotly_dark")

    st.plotly_chart(fig_luxury, use_container_width=True)

# ---------------------------------------------------
# FURNISHING DISTRIBUTION
# ---------------------------------------------------
with col4:

    furnish_counts = filtered_df["furnishing_type"].value_counts()

    fig_furnish = px.bar(
        x=furnish_counts.index,
        y=furnish_counts.values,
        labels={"x": "Furnishing Type", "y": "Count"},
        title="Furnishing Type Distribution",
        color=furnish_counts.values,
        color_continuous_scale="blues"
    )

    fig_furnish.update_layout(template="plotly_dark")

    st.plotly_chart(fig_furnish, use_container_width=True)

st.divider()

# ---------------------------------------------------
# ADVANCED AI INSIGHTS
# ---------------------------------------------------
st.markdown("## 🤖 AI Market Insights")

top_sector = df["sector"].value_counts().idxmax()
avg_bedrooms = round(df["bedRoom"].mean(), 2)



import plotly.express as px

st.markdown("## 🗺️ AI Real Estate Market Map")

sector_counts = df["sector"].value_counts().reset_index()
sector_counts.columns = ["sector", "count"]

# Example coordinates (can be expanded)
sector_coordinates = {
    "sector 67": (28.4595, 77.0266),
    "sector 54": (28.4484, 77.1009),
    "sector 65": (28.4473, 77.0817),
    "sector 50": (28.4540, 77.0850),
    "sector 57": (28.4200, 77.0800)
}

sector_counts["lat"] = sector_counts["sector"].map(
    lambda x: sector_coordinates.get(x.lower(), (None, None))[0]
)

sector_counts["lon"] = sector_counts["sector"].map(
    lambda x: sector_coordinates.get(x.lower(), (None, None))[1]
)

sector_counts = sector_counts.dropna()

fig_map = px.scatter_mapbox(
    sector_counts,
    lat="lat",
    lon="lon",
    size="count",
    hover_name="sector",
    hover_data={"count": True},
    zoom=11,
    height=500
)

fig_map.update_layout(
    mapbox_style="carto-darkmatter"
)

st.plotly_chart(fig_map, use_container_width=True)

st.info(
f"""
**Key Observations from Dataset**

• Most active real estate sector: **{top_sector}**

• Average bedroom count across listings: **{avg_bedrooms}**

• Luxury and furnishing features significantly influence perceived property value.

• The Random Forest model relies heavily on **built-up area and structural attributes** for price prediction.
"""
)