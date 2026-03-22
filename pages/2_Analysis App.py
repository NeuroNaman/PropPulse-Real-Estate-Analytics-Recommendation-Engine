# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# import pickle
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Configure Streamlit Page
# st.set_page_config(page_title="Real Estate Analytics", layout="wide", page_icon="🏡")

# # Sidebar Navigation
# st.sidebar.header("🔍 Dashboard Navigation")
# section = st.sidebar.radio("Go to", ["🏡 Overview", "📊 Data Visualization", "🔍 Insights"])

# # Load Data
# new_df = pd.read_csv('datasets/data_viz1.csv')
# feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))

# new_df['total_area'] = new_df['built_up_area']  # If you have other columns, you can sum them here

# # Group Data for Map Visualization
# group_df = new_df.groupby('sector').mean(numeric_only=True)[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']]

# # --- Overview Section ---
# if section == "🏡 Overview":
#     st.title("🏡 Real Estate Analytics Dashboard")
    
#     # Display Key Metrics
#     col1, col2, col3, col4 = st.columns(4)
#     col1.metric("🏠 Total Properties", len(new_df))
#     col2.metric("📍 Unique Sectors", new_df['sector'].nunique())
#     col3.metric("💰 Avg Price (₹)", f"{new_df['price'].mean():,.0f}CR")
#     col4.metric("📏 Avg Built-up Area", f"{new_df['built_up_area'].mean():,.0f} sq.ft")
    
#     st.markdown("---")
    
#     # Sector Price per Sqft Geomap
#     st.subheader("🌍 Sector Price per Sqft Geomap")
#     fig_map = px.scatter_mapbox(
#         group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
#         color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
#         mapbox_style="carto-positron", width=1100, height=600, hover_name=group_df.index
#     )
#     st.plotly_chart(fig_map, use_container_width=True)
    
#     # Avg Price per Sector Bar Chart
#     st.subheader("📊 Average Price per Sector")
#     fig_bar = px.bar(group_df, x=group_df.index, y='price', color='price', title='Average Price per Sector',
#                      color_continuous_scale='Viridis')
#     st.plotly_chart(fig_bar, use_container_width=True)

#     #3D Scatter Plot (Price vs Built-up Area vs Bedrooms) --- 
#     st.subheader("🔍 3D Scatter Plot: Price, Built-up Area & Bedrooms")
    
#     # Creating a 3D scatter plot using Plotly
#     fig_3d = px.scatter_3d(new_df, x='built_up_area', y='price', z='bedRoom',
#                            color='property_type', title="Price vs Built-up Area vs Bedrooms",
#                            color_continuous_scale='Viridis')
    
#     # Customizing layout for 3D plot
#     fig_3d.update_layout(
#         scene=dict(
#             xaxis_title='Built-up Area (sq.ft)',
#             yaxis_title='Price (₹)',
#             zaxis_title='Bedrooms (BHK)'
#         ),
#         width=1000, height=700
#     )
    
#     # Show the plot
#     st.plotly_chart(fig_3d, use_container_width=True)


#     st.subheader("Sector-wise Property Price Trend Over Time ")
#     new_df['month'] = (new_df.index % 12) + 1  # Cyclic months from 1 to 12

#     # Group data by sector and month to calculate the average price trend
#     price_trend = new_df.groupby(['sector', 'month'], as_index=False)['price'].mean()

#     # Create Animated Line Chart
#     fig_animated = px.line(
#         price_trend, x="sector", y="price", color="sector",
#         animation_frame="month", title="📈 Sector-wise Property Price Trend Over Time",
#         labels={"price": "Avg Price (₹)", "sector": "Sector"},
#         markers=True
#     )

#     # Show animation in Streamlit
#     st.plotly_chart(fig_animated, use_container_width=True)

# # --- Data Visualization Section ---
# elif section == "📊 Data Visualization":
#     st.title("📊 Data Visualization")
    
#     st.markdown("---")
    
#     # **Property Price Distribution by Property Type (Violin Plot)**
#     st.subheader("🏡 Property Price Distribution by Property Type")
#     fig_violin = px.violin(new_df, x='property_type', y='price', box=True, points="all", title="Property Price Distribution by Property Type")
#     st.plotly_chart(fig_violin, use_container_width=True)
    
#     st.markdown("---")
    
#     st.subheader("🏡 Price Distribution per Square Foot (Heatmap)")

#     # Grouping data by sector and price per sqft for the heatmap
#     price_heatmap_data = new_df.pivot_table(values="price_per_sqft", index="sector", columns="property_type", aggfunc="mean")

#     # Create a Plotly heatmap
#     fig_heatmap = go.Figure(data=go.Heatmap(
#         z=price_heatmap_data.values,
#         x=price_heatmap_data.columns,
#         y=price_heatmap_data.index,
#         colorscale='Viridis',  # You can change this to any other colorscale
#         colorbar=dict(title='Price per Sqft'),
#     ))

#     # Update layout for better aesthetics
#     fig_heatmap.update_layout(
#         title="Price Distribution per Square Foot",
#         xaxis_title="Property Type",
#         yaxis_title="Sector",
#         height=600,
#         width=1000,
#     )
#     st.plotly_chart(fig_heatmap, use_container_width=True)
    
#     st.markdown("---")
    
#     # Property Price Distribution by Sector
#     st.subheader("📊 Price Distribution by Sector")
#     fig_box = px.box(new_df, x='sector', y='price', color='sector', title='Price Distribution Across Sectors')
#     st.plotly_chart(fig_box, use_container_width=True)

#     st.markdown("---")
    
#     # Price vs Built-up Area Scatter Plot
#     st.subheader("📉 Price vs Built-up Area")
#     fig_scatter = px.scatter(new_df, x="built_up_area", y="price", color="property_type", title="Price vs Built-up Area", trendline="ols")
#     st.plotly_chart(fig_scatter, use_container_width=True)
    
#     st.markdown("---")
    
#     # Price vs Number of Bedrooms (BHK)
#     st.subheader("🛏️ Price vs Number of Bedrooms")
#     fig_bhk_scatter = px.scatter(new_df, x="bedRoom", y="price", color="property_type", title="Price vs Number of Bedrooms", trendline="ols")
#     st.plotly_chart(fig_bhk_scatter, use_container_width=True)
    
#     st.markdown("---")
    
#     # Price per Sqft vs Latitude/Longitude (Location Scatter)
#     st.subheader("📍 Price per Sqft vs Location")
#     fig_loc_scatter = px.scatter(new_df, x="longitude", y="latitude", color="price_per_sqft", size='built_up_area', hover_name="sector",
#                                  title="Price per Sqft vs Latitude/Longitude", color_continuous_scale=px.colors.cyclical.IceFire)
#     st.plotly_chart(fig_loc_scatter, use_container_width=True)

# # --- Insights Section ---
# elif section == "🔍 Insights":
#     st.title("🔍 Insights")
    
#     # BHK Price Comparison Box Plot
#     st.subheader("💰 BHK Price Comparison")
#     fig_bhk_price = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')
#     st.plotly_chart(fig_bhk_price, use_container_width=True)
    
#     st.markdown("---")
    
#     # Side by Side Property Type Price Distribution
#     st.subheader("📈 Property Type Price Distribution")
#     fig_distplot, ax = plt.subplots(figsize=(10, 4))
#     sns.histplot(new_df[new_df['property_type'] == 'house']['price'], label='House', kde=True, color='blue', ax=ax)
#     sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], label='Flat', kde=True, color='red', ax=ax)
#     ax.legend()
#     st.pyplot(fig_distplot)
    
#     st.markdown("---")
    
#     # Average Price by Bedroom Count
#     st.subheader("🏠 Average Price by BHK")
#     avg_price_bhk = new_df.groupby('bedRoom')['price'].mean().reset_index()
#     fig_avg_bhk = px.bar(avg_price_bhk, x='bedRoom', y='price', color='price', title='Average Price by BHK')
#     st.plotly_chart(fig_avg_bhk, use_container_width=True)
    
#     st.markdown("---")
    
#     # Price per Sqft by Property Type
#     st.subheader("🏡 Price per Sqft by Property Type")
#     fig_price_sqft = px.box(new_df, x="property_type", y="price_per_sqft", color="property_type", title="Price per Sqft by Property Type")
#     st.plotly_chart(fig_price_sqft, use_container_width=True)

#     st.subheader("💡 Cluster Analysis: Price vs. Built-up Area across Sectors")

#     # Create a bubble chart to show clusters of properties
#     fig_bubble = px.scatter(
#         new_df, x="built_up_area", y="price", size="price", color="sector",
#         hover_name="sector", title="Property Price Clusters: Built-up Area vs. Price",
#         labels={"built_up_area": "Built-up Area (sq.ft)", "price": "Price (₹)"},
#         opacity=0.7, size_max=40
#     )

#     # Improve layout
#     fig_bubble.update_layout(
#         width=1000, height=600,
#         xaxis_title="Built-up Area (sq.ft)",
#         yaxis_title="Price (₹)",
#         legend_title="Sector"
#     )

#     # Display the plot
#     st.plotly_chart(fig_bubble, use_container_width=True)

   
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NestIQ – Real Estate Analytics",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── THEME ─────────────────────────────────────────────────────────────────────
st.markdown(r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

:root {
  --bg-page:    #080E1A;
  --bg-sidebar: #0C1526;
  --bg-card:    #0F1E35;
  --bg-card-2:  #112040;
  --bg-input:   #0A1628;
  --border:     rgba(59,130,246,0.18);
  --border-h:   rgba(59,130,246,0.40);
  --text-primary:   #E2EAF8;
  --text-secondary: #7A9CC8;
  --text-muted:     #3D5A80;
  --blue-500:  #3B82F6;
  --blue-600:  #2563EB;
  --blue-700:  #1D4ED8;
  --teal:      #0EA5E9;
  --coral:     #F97316;
  --green:     #10B981;
  --gold:      #F59E0B;
  --purple:    #8B5CF6;
  --shadow-sm: 0 2px 8px  rgba(0,0,0,0.35);
  --shadow-md: 0 8px 30px rgba(0,0,0,0.45);
  --shadow-3d: 0 20px 60px rgba(37,99,235,0.25);
  --radius-sm: 10px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --ease:     cubic-bezier(0.34,1.56,0.64,1);
  --ease-out: cubic-bezier(0.16,1,0.3,1);
}

*, *::before, *::after { box-sizing: border-box; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"], .main {
  background: var(--bg-page) !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  color: var(--text-primary) !important;
}
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"] { display: none !important; }

.block-container { padding: 0 2.5rem 4rem !important; max-width: 1400px !important; }

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--bg-card); }
::-webkit-scrollbar-thumb { background: var(--blue-600); border-radius: 3px; }

[data-testid="stAppViewContainer"]::before {
  content: '';
  position: fixed; inset: 0;
  background:
    radial-gradient(ellipse 80% 60% at 20% 10%,  rgba(37,99,235,0.12)  0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 80% 80%,  rgba(14,165,233,0.10) 0%, transparent 60%),
    radial-gradient(ellipse 50% 40% at 60% 20%,  rgba(139,92,246,0.06) 0%, transparent 60%);
  pointer-events: none; z-index: 0;
  animation: meshDrift 18s ease-in-out infinite alternate;
}
@keyframes meshDrift { 0%{opacity:.7;transform:scale(1)} 100%{opacity:1;transform:scale(1.05)} }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
  background: var(--bg-sidebar) !important;
  border-right: 1px solid var(--border) !important;
  box-shadow: 4px 0 24px rgba(0,0,0,0.4) !important;
}
[data-testid="stSidebar"] * { font-family: 'Plus Jakarta Sans', sans-serif !important; }
[data-testid="stSidebar"] .stMarkdown p { color: var(--text-secondary) !important; font-size:0.82rem !important; }
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 { color: var(--text-primary) !important; }

/* Sidebar radio */
[data-testid="stSidebar"] [data-testid="stRadio"] label {
  color: var(--text-secondary) !important;
  font-size: 0.85rem !important;
  font-weight: 500 !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] + div {
  color: var(--blue-500) !important;
}
[data-testid="stSidebar"] [role="radiogroup"] > label:hover { color: var(--blue-500) !important; }

.sb-logo-wrap { padding:1.8rem 1.5rem 1.4rem; border-bottom:1px solid var(--border); }
.sb-logo { display:flex; align-items:center; gap:0.6rem; }
.sb-logo-icon { width:38px; height:38px; background:linear-gradient(135deg,var(--blue-600),var(--teal)); border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:1.1rem; box-shadow:0 4px 12px rgba(37,99,235,0.4); }
.sb-logo-text { font-size:1.25rem; font-weight:800; background:linear-gradient(135deg,var(--blue-500),var(--teal)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.sb-logo-sub { font-size:0.62rem; color:var(--text-muted); letter-spacing:0.15em; text-transform:uppercase; margin-top:1rem; }
.sb-nav-label { font-size:0.62rem; font-weight:700; color:var(--text-muted); letter-spacing:0.2em; text-transform:uppercase; padding:1.2rem 1.5rem 0.5rem; }
.sb-tip { margin:1.2rem 1.5rem; background:rgba(245,158,11,0.08); border-left:3px solid var(--gold); border-radius:0 var(--radius-sm) var(--radius-sm) 0; padding:0.8rem 1rem; font-size:0.75rem; color:#FDE68A; line-height:1.6; }

/* ── TOPBAR ── */
.topbar { display:flex; align-items:center; justify-content:space-between; padding:1.5rem 0 0.5rem; border-bottom:1px solid var(--border); margin-bottom:2rem; animation:slideDown 0.6s var(--ease-out) both; }
@keyframes slideDown { from{opacity:0;transform:translateY(-16px)} to{opacity:1;transform:translateY(0)} }
.topbar-brand { display:flex; align-items:center; gap:0.75rem; }
.topbar-icon { width:44px; height:44px; background:linear-gradient(135deg,var(--blue-600),var(--teal)); border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:1.3rem; box-shadow:0 6px 18px rgba(37,99,235,0.35); }
.topbar-name { font-size:1.5rem; font-weight:800; color:var(--text-primary); }
.topbar-name span { color:var(--blue-500); }
.topbar-badge { background:linear-gradient(135deg,var(--blue-600),var(--teal)); color:white; font-size:0.65rem; font-weight:600; letter-spacing:0.1em; padding:0.35rem 0.9rem; border-radius:999px; text-transform:uppercase; box-shadow:0 4px 12px rgba(37,99,235,0.3); }
.topbar-nav { display:flex; gap:0.5rem; }
.nav-pill { padding:0.4rem 1rem; border-radius:999px; font-size:0.78rem; font-weight:500; color:var(--text-secondary); cursor:pointer; border:1.5px solid transparent; }
.nav-pill:hover { background:var(--bg-card-2); color:var(--blue-500); border-color:var(--border); }
.nav-pill.active { background:var(--blue-600); color:white; }

/* ── PAGE HERO ── */
.page-hero { background:linear-gradient(135deg,var(--blue-600) 0%,var(--blue-700) 40%,#0E3A8C 100%); border-radius:var(--radius-lg); padding:2.5rem 3.5rem; position:relative; overflow:hidden; margin-bottom:2rem; animation:fadeUp 0.7s 0.1s var(--ease-out) both; border:1px solid rgba(59,130,246,0.3); }
.page-hero::before { content:''; position:absolute; top:-60px; right:-60px; width:300px; height:300px; background:radial-gradient(circle,rgba(255,255,255,0.08) 0%,transparent 70%); border-radius:50%; }
.page-hero::after  { content:''; position:absolute; bottom:-40px; left:30%; width:200px; height:200px; background:radial-gradient(circle,rgba(14,165,233,0.25) 0%,transparent 70%); border-radius:50%; }
@keyframes fadeUp { from{opacity:0;transform:translateY(28px)} to{opacity:1;transform:translateY(0)} }
.page-hero-tag { display:inline-flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.15); backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.2); color:white; font-size:0.7rem; font-weight:600; letter-spacing:0.12em; text-transform:uppercase; padding:0.35rem 0.9rem; border-radius:999px; margin-bottom:1rem; }
.page-hero-h1 { font-family:'Lora',serif; font-size:clamp(1.6rem,3vw,2.4rem); font-weight:600; color:white; line-height:1.25; margin-bottom:0.5rem; position:relative; z-index:1; }
.page-hero-h1 em { font-style:italic; color:#93C5FD; }
.page-hero-sub { color:rgba(255,255,255,0.7); font-size:0.88rem; line-height:1.7; position:relative; z-index:1; }

/* ── METRIC CARDS ── */
.metric-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:1rem; margin-bottom:2rem; }
.metric-card { background:var(--bg-card); border:1.5px solid var(--border); border-radius:var(--radius-md); padding:1.4rem 1.6rem; position:relative; overflow:hidden; transition:transform 0.3s var(--ease-out),box-shadow 0.3s,border-color 0.3s; animation:fadeUp 0.5s var(--ease-out) both; }
.metric-card::before { content:''; position:absolute; top:0; left:0; right:0; height:3px; border-radius:var(--radius-md) var(--radius-md) 0 0; }
.metric-card.blue::before  { background:linear-gradient(90deg,var(--blue-600),var(--teal)); }
.metric-card.teal::before  { background:linear-gradient(90deg,var(--teal),var(--green)); }
.metric-card.coral::before { background:linear-gradient(90deg,var(--coral),var(--gold)); }
.metric-card.purple::before{ background:linear-gradient(90deg,var(--purple),var(--blue-500)); }
.metric-card:hover { transform:translateY(-4px); box-shadow:var(--shadow-3d); border-color:var(--border-h); }
.metric-icon { font-size:1.5rem; margin-bottom:0.6rem; }
.metric-val { font-family:'Lora',serif; font-size:1.6rem; font-weight:600; color:var(--text-primary); line-height:1; margin-bottom:0.3rem; }
.metric-lbl { font-size:0.65rem; font-weight:700; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.15em; }

/* ── CHART CARDS ── */
.chart-card { background:var(--bg-card); border:1.5px solid var(--border); border-radius:var(--radius-md); padding:1.75rem 2rem; margin-bottom:1.5rem; position:relative; overflow:hidden; animation:fadeUp 0.6s var(--ease-out) both; transition:box-shadow 0.3s, border-color 0.3s; }
.chart-card:hover { box-shadow:var(--shadow-3d); border-color:var(--border-h); }
.chart-card::after { content:''; position:absolute; top:0; left:0; right:0; height:3px; background:linear-gradient(90deg,var(--blue-600),var(--teal),var(--blue-600)); background-size:200%; border-radius:var(--radius-md) var(--radius-md) 0 0; animation:shimmer 4s linear infinite; }
@keyframes shimmer { to{background-position:200% center} }
.chart-card.coral-accent::after { background:linear-gradient(90deg,var(--coral),var(--gold),var(--coral)); background-size:200%; }
.chart-card.purple-accent::after { background:linear-gradient(90deg,var(--purple),var(--blue-500),var(--purple)); background-size:200%; }
.chart-card.teal-accent::after { background:linear-gradient(90deg,var(--teal),var(--green),var(--teal)); background-size:200%; }
.chart-card.gold-accent::after { background:linear-gradient(90deg,var(--gold),var(--coral),var(--gold)); background-size:200%; }

.chart-header { display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem; padding-bottom:1rem; border-bottom:1.5px solid var(--border); }
.chart-icon { width:36px; height:36px; border-radius:9px; display:flex; align-items:center; justify-content:center; font-size:0.95rem; flex-shrink:0; }
.chart-icon.blue   { background:rgba(37,99,235,0.15);  border:1px solid rgba(37,99,235,0.25); }
.chart-icon.teal   { background:rgba(14,165,233,0.12);  border:1px solid rgba(14,165,233,0.22); }
.chart-icon.coral  { background:rgba(249,115,22,0.12);  border:1px solid rgba(249,115,22,0.22); }
.chart-icon.purple { background:rgba(139,92,246,0.12);  border:1px solid rgba(139,92,246,0.22); }
.chart-icon.gold   { background:rgba(245,158,11,0.12);  border:1px solid rgba(245,158,11,0.22); }
.chart-title { font-size:0.95rem; font-weight:700; color:var(--text-primary); }
.chart-sub   { font-size:0.7rem; color:var(--text-secondary); margin-top:0.1rem; }

/* ── SECTION DIVIDER ── */
.sec-divider { display:flex; align-items:center; gap:1rem; margin:2rem 0 1.5rem; font-size:0.65rem; font-weight:700; color:var(--blue-500); text-transform:uppercase; letter-spacing:0.2em; }
.sec-divider::before { content:''; flex:1; height:1.5px; background:linear-gradient(90deg,var(--border),transparent); }
.sec-divider::after  { content:''; flex:1; height:1.5px; background:linear-gradient(90deg,transparent,var(--border)); }

/* ── FAB ── */
.fab-chip { position:fixed; bottom:2rem; right:2rem; z-index:999; background:var(--bg-card-2); border:1.5px solid var(--border); border-radius:999px; padding:0.6rem 1.2rem; display:flex; align-items:center; gap:0.5rem; font-size:0.75rem; font-weight:600; color:var(--blue-500); box-shadow:var(--shadow-md); animation:floatFab 4s ease-in-out infinite; pointer-events:none; }
@keyframes floatFab { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-6px)} }
.fab-dot { width:8px; height:8px; border-radius:50%; background:var(--green); box-shadow:0 0 0 3px rgba(16,185,129,0.25); animation:dotPulse 2s ease-in-out infinite; }
@keyframes dotPulse { 0%,100%{box-shadow:0 0 0 3px rgba(16,185,129,0.25)} 50%{box-shadow:0 0 0 6px rgba(16,185,129,0.1)} }
</style>

<script>
(function() {
  function applyTilt() {
    document.querySelectorAll('.metric-card, .chart-card').forEach(card => {
      if (card._tilt) return;
      card._tilt = true;
      card.addEventListener('mousemove', e => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width  - 0.5;
        const y = (e.clientY - r.top)  / r.height - 0.5;
        card.style.transform  = `rotateX(${-y*6}deg) rotateY(${x*6}deg) translateY(-4px)`;
        card.style.transition = 'box-shadow 0.1s';
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform  = '';
        card.style.transition = 'transform 0.5s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.5s';
      });
    });
  }
  new MutationObserver(applyTilt).observe(document.body, {childList:true, subtree:true});
  applyTilt();
})();
</script>
""", unsafe_allow_html=True)

# ── Plotly dark template ──────────────────────────────────────────────────────
PLOTLY_THEME = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(15,30,53,0)",
    plot_bgcolor="rgba(15,30,53,0)",
    font=dict(family="Plus Jakarta Sans", color="#E2EAF8", size=12),
    title_font=dict(family="Lora", color="#E2EAF8", size=16),
    colorway=["#3B82F6","#0EA5E9","#10B981","#F59E0B","#F97316","#8B5CF6","#EC4899"],
    margin=dict(l=16, r=16, t=48, b=16),
    legend=dict(bgcolor="rgba(15,30,53,0.6)", bordercolor="rgba(59,130,246,0.2)", borderwidth=1),
    xaxis=dict(gridcolor="rgba(59,130,246,0.08)", linecolor="rgba(59,130,246,0.15)"),
    yaxis=dict(gridcolor="rgba(59,130,246,0.08)", linecolor="rgba(59,130,246,0.15)"),
)

def apply_theme(fig, **kwargs):
    fig.update_layout(**PLOTLY_THEME, **kwargs)
    return fig

# ── Load Data ─────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def load_data():
    new_df = pd.read_csv('datasets/data_viz1.csv')
    feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))
    return new_df, feature_text

new_df, feature_text = load_data()
new_df['total_area'] = new_df['built_up_area']
group_df = new_df.groupby('sector').mean(numeric_only=True)[['price','price_per_sqft','built_up_area','latitude','longitude']]

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-logo-wrap">
      <div class="sb-logo">
        <div class="sb-logo-icon">📊</div>
        <div><div class="sb-logo-text">NestIQ</div></div>
      </div>
      <div class="sb-logo-sub">Real Estate Analytics</div>
    </div>
    <div class="sb-nav-label">Dashboard Sections</div>
    """, unsafe_allow_html=True)

    section = st.sidebar.radio(
        "", ["🏡 Overview", "📊 Data Visualization", "🔍 Insights"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <div class="sb-tip">
      💡 Use the navigation above to switch between the Overview, detailed charts, and analytical Insights.
    </div>
    """, unsafe_allow_html=True)

# ── Topbar ────────────────────────────────────────────────────────────────────
active_overview = "active" if section == "🏡 Overview" else ""
active_viz      = "active" if section == "📊 Data Visualization" else ""
active_insights = "active" if section == "🔍 Insights" else ""

st.markdown(f"""
<div class="topbar">
  <div class="topbar-brand">
    <div class="topbar-icon">📊</div>
    <div class="topbar-name">Nest<span>IQ</span></div>
    <div class="topbar-badge">Analytics</div>
  </div>
  <div class="topbar-nav">
    <div class="nav-pill {active_overview}">Overview</div>
    <div class="nav-pill {active_viz}">Visualizations</div>
    <div class="nav-pill {active_insights}">Insights</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
#  SECTION 1 — OVERVIEW
# ══════════════════════════════════════════════════════
if section == "🏡 Overview":

    st.markdown("""
    <div class="page-hero">
      <div class="page-hero-tag">🏡 Market Intelligence</div>
      <div class="page-hero-h1">Real Estate <em>Analytics Dashboard</em></div>
      <div class="page-hero-sub">Geo-spatial maps, price trends, and 3D scatter analysis across Gurugram NCR sectors.</div>
    </div>
    """, unsafe_allow_html=True)

    # Metric cards
    avg_price = new_df['price'].mean()
    avg_area  = new_df['built_up_area'].mean()
    st.markdown(f"""
    <div class="metric-grid">
      <div class="metric-card blue" style="animation-delay:0s">
        <div class="metric-icon">🏠</div>
        <div class="metric-val">{len(new_df):,}</div>
        <div class="metric-lbl">Total Properties</div>
      </div>
      <div class="metric-card teal" style="animation-delay:0.07s">
        <div class="metric-icon">📍</div>
        <div class="metric-val">{new_df['sector'].nunique()}</div>
        <div class="metric-lbl">Unique Sectors</div>
      </div>
      <div class="metric-card coral" style="animation-delay:0.14s">
        <div class="metric-icon">💰</div>
        <div class="metric-val">₹{avg_price:,.1f} Cr</div>
        <div class="metric-lbl">Avg Price</div>
      </div>
      <div class="metric-card purple" style="animation-delay:0.21s">
        <div class="metric-icon">📏</div>
        <div class="metric-val">{avg_area:,.0f}</div>
        <div class="metric-lbl">Avg sq.ft</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Geomap
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon blue">🌍</div>
      <div><div class="chart-title">Sector Price per Sqft — Geo Map</div>
      <div class="chart-sub">Bubble size = avg built-up area · Colour = price per sqft</div></div>
    </div>""", unsafe_allow_html=True)
    fig_map = px.scatter_mapbox(
        group_df, lat="latitude", lon="longitude",
        color="price_per_sqft", size='built_up_area',
        color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=10, mapbox_style="carto-darkmatter",
        hover_name=group_df.index
    )
    fig_map.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", margin=dict(l=0,r=0,t=0,b=0), height=520
    )
    st.plotly_chart(fig_map, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Bar chart
    st.markdown('<div class="chart-card teal-accent">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon teal">📊</div>
      <div><div class="chart-title">Average Price per Sector</div>
      <div class="chart-sub">Colour intensity reflects relative pricing</div></div>
    </div>""", unsafe_allow_html=True)
    fig_bar = px.bar(
        group_df, x=group_df.index, y='price',
        color='price', color_continuous_scale='Blues'
    )
    apply_theme(fig_bar, xaxis_tickangle=-45)
    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 3D scatter
    st.markdown('<div class="chart-card purple-accent">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon purple">🔍</div>
      <div><div class="chart-title">3D Scatter: Price · Built-up Area · Bedrooms</div>
      <div class="chart-sub">Rotate and zoom to explore pricing clusters</div></div>
    </div>""", unsafe_allow_html=True)
    fig_3d = px.scatter_3d(
        new_df, x='built_up_area', y='price', z='bedRoom',
        color='property_type', color_continuous_scale='Blues'
    )
    fig_3d.update_layout(
        **{k: v for k, v in PLOTLY_THEME.items() if k != 'xaxis' and k != 'yaxis'},
        scene=dict(
            xaxis=dict(title='Built-up Area (sq.ft)', gridcolor='rgba(59,130,246,0.12)', backgroundcolor='rgba(15,30,53,0.5)'),
            yaxis=dict(title='Price (₹ Cr)', gridcolor='rgba(59,130,246,0.12)', backgroundcolor='rgba(15,30,53,0.5)'),
            zaxis=dict(title='Bedrooms', gridcolor='rgba(59,130,246,0.12)', backgroundcolor='rgba(15,30,53,0.5)'),
        ),
        height=600
    )
    st.plotly_chart(fig_3d, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Animated line
    st.markdown('<div class="chart-card coral-accent">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon coral">📈</div>
      <div><div class="chart-title">Sector-wise Property Price Trend</div>
      <div class="chart-sub">Animated across cyclic months — press ▶ to play</div></div>
    </div>""", unsafe_allow_html=True)
    new_df['month'] = (new_df.index % 12) + 1
    price_trend = new_df.groupby(['sector','month'], as_index=False)['price'].mean()
    fig_anim = px.line(
        price_trend, x="sector", y="price", color="sector",
        animation_frame="month",
        labels={"price":"Avg Price (₹ Cr)","sector":"Sector"},
        markers=True
    )
    apply_theme(fig_anim, xaxis_tickangle=-45, height=480)
    st.plotly_chart(fig_anim, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
#  SECTION 2 — DATA VISUALIZATION
# ══════════════════════════════════════════════════════
elif section == "📊 Data Visualization":

    st.markdown("""
    <div class="page-hero">
      <div class="page-hero-tag">📊 Chart Explorer</div>
      <div class="page-hero-h1">Data <em>Visualization Suite</em></div>
      <div class="page-hero-sub">Violin plots, heatmaps, box plots, scatter analysis — dive deep into the data.</div>
    </div>
    """, unsafe_allow_html=True)

    # Violin
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon blue">🎻</div>
      <div><div class="chart-title">Property Price Distribution by Type</div>
      <div class="chart-sub">Violin with embedded box + all data points</div></div>
    </div>""", unsafe_allow_html=True)
    fig_violin = px.violin(new_df, x='property_type', y='price', box=True, points="all")
    apply_theme(fig_violin)
    st.plotly_chart(fig_violin, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Heatmap
    st.markdown('<div class="chart-card teal-accent">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon teal">🌡️</div>
      <div><div class="chart-title">Price per Sqft Heatmap</div>
      <div class="chart-sub">Sector × Property Type — mean price per sqft</div></div>
    </div>""", unsafe_allow_html=True)
    hm_data = new_df.pivot_table(values="price_per_sqft", index="sector", columns="property_type", aggfunc="mean")
    fig_hm = go.Figure(data=go.Heatmap(
        z=hm_data.values, x=hm_data.columns, y=hm_data.index,
        colorscale='Blues', colorbar=dict(title='₹/sqft', tickfont=dict(color='#E2EAF8'), titlefont=dict(color='#E2EAF8'))
    ))
    apply_theme(fig_hm, height=560, xaxis_title="Property Type", yaxis_title="Sector")
    st.plotly_chart(fig_hm, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Box — sector
    st.markdown('<div class="chart-card coral-accent">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon coral">📦</div>
      <div><div class="chart-title">Price Distribution by Sector</div>
      <div class="chart-sub">Box plot showing spread, median, and outliers per sector</div></div>
    </div>""", unsafe_allow_html=True)
    fig_box = px.box(new_df, x='sector', y='price', color='sector')
    apply_theme(fig_box, showlegend=False, xaxis_tickangle=-45)
    st.plotly_chart(fig_box, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Scatter price vs area
    st.markdown('<div class="chart-card purple-accent">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon purple">📉</div>
      <div><div class="chart-title">Price vs Built-up Area</div>
      <div class="chart-sub">OLS trendline by property type</div></div>
    </div>""", unsafe_allow_html=True)
    fig_sc = px.scatter(new_df, x="built_up_area", y="price", color="property_type", trendline="ols")
    apply_theme(fig_sc)
    st.plotly_chart(fig_sc, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Scatter price vs bedrooms
    st.markdown('<div class="chart-card gold-accent">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon gold">🛏️</div>
      <div><div class="chart-title">Price vs Number of Bedrooms</div>
      <div class="chart-sub">OLS trendline by property type</div></div>
    </div>""", unsafe_allow_html=True)
    fig_bhk_sc = px.scatter(new_df, x="bedRoom", y="price", color="property_type", trendline="ols")
    apply_theme(fig_bhk_sc)
    st.plotly_chart(fig_bhk_sc, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Location scatter
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon blue">📍</div>
      <div><div class="chart-title">Price per Sqft vs Location</div>
      <div class="chart-sub">Lat/Long scatter · Bubble size = built-up area · Colour = price/sqft</div></div>
    </div>""", unsafe_allow_html=True)
    fig_loc = px.scatter(
        new_df, x="longitude", y="latitude",
        color="price_per_sqft", size='built_up_area',
        hover_name="sector", color_continuous_scale=px.colors.cyclical.IceFire
    )
    apply_theme(fig_loc)
    st.plotly_chart(fig_loc, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
#  SECTION 3 — INSIGHTS
# ══════════════════════════════════════════════════════
elif section == "🔍 Insights":

    st.markdown("""
    <div class="page-hero">
      <div class="page-hero-tag">🔍 Deep Analysis</div>
      <div class="page-hero-h1">Market <em>Insights</em></div>
      <div class="page-hero-sub">BHK price ranges, property type distributions, per-sqft analysis, and cluster intelligence.</div>
    </div>
    """, unsafe_allow_html=True)

    # BHK box
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon blue">💰</div>
      <div><div class="chart-title">BHK Price Comparison</div>
      <div class="chart-sub">Price range spread for 1–4 BHK configurations</div></div>
    </div>""", unsafe_allow_html=True)
    fig_bhk_box = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price')
    apply_theme(fig_bhk_box)
    st.plotly_chart(fig_bhk_box, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Histogram — matplotlib styled dark
    st.markdown('<div class="chart-card teal-accent">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon teal">📈</div>
      <div><div class="chart-title">Property Type Price Distribution</div>
      <div class="chart-sub">KDE histogram overlay — House vs Flat</div></div>
    </div>""", unsafe_allow_html=True)

    plt.rcParams.update({
        'figure.facecolor':  '#0F1E35',
        'axes.facecolor':    '#0F1E35',
        'axes.edgecolor':    '#1E3A5F',
        'axes.labelcolor':   '#7A9CC8',
        'xtick.color':       '#7A9CC8',
        'ytick.color':       '#7A9CC8',
        'grid.color':        '#1E3A5F',
        'text.color':        '#E2EAF8',
        'legend.facecolor':  '#112040',
        'legend.edgecolor':  '#1E3A5F',
    })
    fig_dist, ax = plt.subplots(figsize=(11, 4))
    fig_dist.patch.set_facecolor('#0F1E35')
    sns.histplot(new_df[new_df['property_type']=='house']['price'], label='House', kde=True, color='#3B82F6', ax=ax, alpha=0.6)
    sns.histplot(new_df[new_df['property_type']=='flat']['price'],  label='Flat',  kde=True, color='#0EA5E9', ax=ax, alpha=0.6)
    ax.set_xlabel('Price (₹ Cr)', fontsize=10)
    ax.set_ylabel('Count', fontsize=10)
    ax.grid(True, alpha=0.15)
    ax.spines[['top','right']].set_visible(False)
    ax.legend(fontsize=10)
    st.pyplot(fig_dist)
    plt.close()
    st.markdown('</div>', unsafe_allow_html=True)

    # Avg price by BHK
    st.markdown('<div class="chart-card coral-accent">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon coral">🏠</div>
      <div><div class="chart-title">Average Price by BHK</div>
      <div class="chart-sub">Mean price across bedroom configurations</div></div>
    </div>""", unsafe_allow_html=True)
    avg_bhk = new_df.groupby('bedRoom')['price'].mean().reset_index()
    fig_avg_bhk = px.bar(avg_bhk, x='bedRoom', y='price', color='price', color_continuous_scale='Blues')
    apply_theme(fig_avg_bhk)
    st.plotly_chart(fig_avg_bhk, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Price/sqft by type
    st.markdown('<div class="chart-card purple-accent">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon purple">🏡</div>
      <div><div class="chart-title">Price per Sqft by Property Type</div>
      <div class="chart-sub">Box plot — median and spread comparison</div></div>
    </div>""", unsafe_allow_html=True)
    fig_psq = px.box(new_df, x="property_type", y="price_per_sqft", color="property_type")
    apply_theme(fig_psq, showlegend=False)
    st.plotly_chart(fig_psq, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Bubble cluster
    st.markdown('<div class="chart-card gold-accent">', unsafe_allow_html=True)
    st.markdown("""<div class="chart-header">
      <div class="chart-icon gold">💡</div>
      <div><div class="chart-title">Cluster Analysis: Price vs Built-up Area</div>
      <div class="chart-sub">Bubble size = price · Colour = sector · Opacity = density</div></div>
    </div>""", unsafe_allow_html=True)
    fig_bubble = px.scatter(
        new_df, x="built_up_area", y="price",
        size="price", color="sector",
        hover_name="sector",
        labels={"built_up_area":"Built-up Area (sq.ft)","price":"Price (₹ Cr)"},
        opacity=0.7, size_max=40
    )
    apply_theme(fig_bubble, height=560, legend_title_text="Sector")
    st.plotly_chart(fig_bubble, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── FAB ───────────────────────────────────────────────────────────────────────
st.markdown('<div class="fab-chip"><div class="fab-dot"></div> Analytics Live</div>', unsafe_allow_html=True)