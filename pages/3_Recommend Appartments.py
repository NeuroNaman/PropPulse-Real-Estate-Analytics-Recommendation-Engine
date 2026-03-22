# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np

# # Set Streamlit page config
# st.set_page_config(page_title="🏡 Apartment Recommender", page_icon="🏠", layout="wide")

# # Load Data
# property_data = pd.read_csv("datasets/appartments.csv")  # Load CSV with all property details
# location_df = pickle.load(open('datasets/location_df_merge.pkl', 'rb'))
# cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl', 'rb'))
# cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl', 'rb'))
# cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl', 'rb'))

# # 🎯 Function to Recommend Properties
# def recommend_properties(property_name, w1=0.5, w2=0.8, w3=1, top_n=5):
#     cosine_sim_matrix = w1 * cosine_sim1 + w2 * cosine_sim2 + w3 * cosine_sim3
#     sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
#     sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
#     top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
#     top_scores = [round(i[1], 3) for i in sorted_scores[1:top_n + 1]]  # Round scores
#     top_properties = location_df.index[top_indices].tolist()
#     links = property_data.set_index("PropertyName").loc[top_properties]["Link"].tolist()
    
#     return pd.DataFrame({'Property Name': top_properties, 'Similarity Score': top_scores, 'Link': links})

# # 🔷 Sidebar
# with st.sidebar:
#     st.image("datasets/banner image.jpg", use_container_width=True)
#     st.title("🏡 Apartment Finder")
#     st.markdown("Find the **best apartments** near your location based on multiple similarity measures. Adjust settings and explore!")
#     st.markdown("---")
#     st.markdown("👈 Use the sidebar to navigate!")

# # 🏙️ Section: Location Search
# st.markdown("## 📍 Find Nearby Apartments")
# col1, col2 = st.columns(2)
# with col1:
#     selected_location = st.selectbox('🔍 Select Location:', sorted(location_df.columns.to_list()), help="Start typing to search")
# with col2:
#     radius = st.slider('📏 Radius (in Kms)', 1, 50, 5, 1)

# if st.button('🔎 Search Apartments'):
#     result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()
#     st.success(f"Found **{len(result_ser)}** apartments within {radius} km of **{selected_location}**")
#     for key, value in result_ser.items():
#         st.markdown(f"🏠 **{key}** - {round(value / 1000, 2)} km")

# # 🏡 Section: Apartment Recommendation
# st.markdown("---")
# st.markdown("## 🏡 Get Similar Apartment Recommendations")
# selected_apartment = st.selectbox('🏠 Select an Apartment:', sorted(location_df.index.to_list()), help="Start typing to search")

# # 🎛️ Adjust Similarity Weights
# st.markdown("### ⚖️ Adjust Similarity Weights")
# w1 = st.slider("🔹 Facilities Similarity", 0.0, 1.5, 0.5, 0.1)
# w2 = st.slider("🔹 Pricing Similarity", 0.0, 1.5, 0.8, 0.1)
# w3 = st.slider("🔹 Location Similarity", 0.0, 1.5, 1.0, 0.1)

# if st.button('✨ Show Recommendations'):
#     recommendation_df = recommend_properties(selected_apartment, w1, w2, w3)
    
#     for i, row in recommendation_df.iterrows():
#         st.markdown(f'''
#         <div style="border-radius:10px; padding:15px; margin-bottom:10px; 
#                     background-color:#1E3A5F; color:white; font-size:16px; 
#                     box-shadow: 3px 3px 10px rgba(0,0,0,0.2);">
#         <h4 style="margin:0; padding:5px;">🏠 {row['Property Name']}</h4>
#         <p style="margin:0;">🔹 <b>Similarity Score:</b> {row['Similarity Score']}</p>
#         <p style="margin:0;"><a href="{row['Link']}" target="_blank" style="color:#FFD700; font-weight:bold; text-decoration:none;">🔗 View Property</a></p>
#         </div>
#         ''', unsafe_allow_html=True)


import streamlit as st
import pickle
import pandas as pd
import numpy as np

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NestIQ – Apartment Recommender",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── THEME CSS + JS ────────────────────────────────────────────────────────────
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

.block-container { padding: 0 2.5rem 4rem !important; max-width: 1320px !important; }

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--bg-card); }
::-webkit-scrollbar-thumb { background: var(--blue-600); border-radius: 3px; }

/* Animated mesh background */
[data-testid="stAppViewContainer"]::before {
  content: '';
  position: fixed; inset: 0;
  background:
    radial-gradient(ellipse 80% 60% at 20% 10%,  rgba(37,99,235,0.12)  0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 80% 80%,  rgba(14,165,233,0.10) 0%, transparent 60%),
    radial-gradient(ellipse 50% 40% at 60% 20%,  rgba(249,115,22,0.05) 0%, transparent 60%);
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
[data-testid="stSidebar"] .stMarkdown p { color: var(--text-secondary) !important; font-size:0.82rem !important; }

.sb-logo-wrap { padding:1.8rem 1.5rem 1.4rem; border-bottom:1px solid var(--border); }
.sb-logo { display:flex; align-items:center; gap:0.6rem; }
.sb-logo-icon { width:38px; height:38px; background:linear-gradient(135deg,var(--blue-600),var(--teal)); border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:1.1rem; box-shadow:0 4px 12px rgba(37,99,235,0.4); }
.sb-logo-text { font-size:1.25rem; font-weight:800; background:linear-gradient(135deg,var(--blue-500),var(--teal)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.sb-logo-sub { font-size:0.62rem; color:var(--text-muted); letter-spacing:0.15em; text-transform:uppercase; margin-top:1rem; }

.sb-tip { margin:1.2rem 1.5rem; background:rgba(249,115,22,0.08); border-left:3px solid var(--coral); border-radius:0 var(--radius-sm) var(--radius-sm) 0; padding:0.8rem 1rem; font-size:0.75rem; color:#FDBA74; line-height:1.6; }

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

/* ── HERO BANNER ── */
.hero-banner { background:linear-gradient(135deg,var(--blue-600) 0%,var(--blue-700) 40%,#0E3A8C 100%); border-radius:var(--radius-lg); padding:3rem 3.5rem; position:relative; overflow:hidden; margin-bottom:2.5rem; animation:fadeUp 0.7s 0.1s var(--ease-out) both; border:1px solid rgba(59,130,246,0.3); }
.hero-banner::before { content:''; position:absolute; top:-60px; right:-60px; width:300px; height:300px; background:radial-gradient(circle,rgba(255,255,255,0.08) 0%,transparent 70%); border-radius:50%; }
.hero-banner::after  { content:''; position:absolute; bottom:-40px; left:30%; width:200px; height:200px; background:radial-gradient(circle,rgba(14,165,233,0.25) 0%,transparent 70%); border-radius:50%; }
@keyframes fadeUp { from{opacity:0;transform:translateY(28px)} to{opacity:1;transform:translateY(0)} }
.hero-tag { display:inline-flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.15); backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.2); color:white; font-size:0.7rem; font-weight:600; letter-spacing:0.12em; text-transform:uppercase; padding:0.35rem 0.9rem; border-radius:999px; margin-bottom:1.2rem; }
.hero-h1 { font-family:'Lora',serif; font-size:clamp(1.8rem,3.5vw,2.8rem); font-weight:600; color:white; line-height:1.25; margin-bottom:0.75rem; position:relative; z-index:1; }
.hero-h1 em { font-style:italic; color:#93C5FD; }
.hero-sub { color:rgba(255,255,255,0.7); font-size:0.9rem; line-height:1.7; max-width:520px; position:relative; z-index:1; }
.hero-chips { display:flex; gap:0.75rem; margin-top:1.5rem; flex-wrap:wrap; position:relative; z-index:1; }
.hero-chip { background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.2); color:white; font-size:0.72rem; font-weight:500; padding:0.4rem 0.85rem; border-radius:999px; }

/* ── 3D CARDS ── */
.card-3d-wrap { perspective:1200px; margin-bottom:1.5rem; animation:fadeUp 0.7s var(--ease-out) both; }
.card-3d { background:var(--bg-card); border:1.5px solid var(--border); border-radius:var(--radius-md); padding:1.75rem 2rem; position:relative; transition:transform 0.4s var(--ease-out),box-shadow 0.4s var(--ease-out); transform-style:preserve-3d; box-shadow:var(--shadow-sm); overflow:hidden; }
.card-3d::before { content:''; position:absolute; inset:0; background:linear-gradient(135deg,rgba(37,99,235,0.06) 0%,transparent 60%); border-radius:inherit; pointer-events:none; }
.card-3d:hover { transform:rotateX(2deg) rotateY(-2deg) translateY(-6px) scale(1.005); box-shadow:var(--shadow-3d); border-color:var(--border-h); }
.card-3d-accent { position:absolute; top:0; left:0; right:0; height:3px; background:linear-gradient(90deg,var(--blue-600),var(--teal),var(--blue-600)); background-size:200%; border-radius:var(--radius-md) var(--radius-md) 0 0; animation:shimmer 3s linear infinite; }
@keyframes shimmer { to{background-position:200% center} }
.card-header { display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem; padding-bottom:1rem; border-bottom:1.5px solid var(--border); }
.card-icon { width:38px; height:38px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:1rem; flex-shrink:0; }
.card-icon.blue  { background:rgba(37,99,235,0.15);  border:1px solid rgba(37,99,235,0.25); }
.card-icon.teal  { background:rgba(14,165,233,0.12);  border:1px solid rgba(14,165,233,0.22); }
.card-icon.coral { background:rgba(249,115,22,0.12);  border:1px solid rgba(249,115,22,0.22); }
.card-icon.gold  { background:rgba(245,158,11,0.12);  border:1px solid rgba(245,158,11,0.22); }
.card-title-text { font-size:0.95rem; font-weight:700; color:var(--text-primary); }
.card-title-sub  { font-size:0.7rem; color:var(--text-secondary); margin-top:0.1rem; }

/* ── FORM WIDGETS ── */
div[data-baseweb="select"] > div { background:var(--bg-input) !important; border:1.5px solid var(--border) !important; border-radius:var(--radius-sm) !important; color:var(--text-primary) !important; font-family:'Plus Jakarta Sans',sans-serif !important; font-size:0.85rem !important; transition:all 0.2s !important; }
div[data-baseweb="select"]:focus-within > div { border-color:var(--blue-500) !important; background:var(--bg-card-2) !important; box-shadow:0 0 0 3px rgba(59,130,246,0.15) !important; }
div[data-baseweb="select"] svg { fill:var(--blue-500) !important; }
div[data-baseweb="menu"] { background:var(--bg-card-2) !important; border:1.5px solid var(--border) !important; border-radius:var(--radius-sm) !important; box-shadow:0 12px 40px rgba(0,0,0,0.5) !important; }
div[data-baseweb="menu"] li { color:var(--text-primary) !important; font-size:0.83rem !important; font-family:'Plus Jakarta Sans',sans-serif !important; background:transparent !important; }
div[data-baseweb="menu"] li:hover { background:rgba(37,99,235,0.15) !important; color:var(--blue-500) !important; }
label[data-testid="stWidgetLabel"] > div > p { font-family:'Plus Jakarta Sans',sans-serif !important; font-size:0.72rem !important; font-weight:600 !important; color:var(--text-secondary) !important; text-transform:uppercase !important; letter-spacing:0.08em !important; }

/* Slider */
[data-testid="stSlider"] > div > div > div { background:var(--bg-card-2) !important; }
[data-testid="stSlider"] [data-testid="stTickBar"] { color:var(--text-muted) !important; }
div[data-baseweb="slider"] [role="slider"] { background:var(--blue-500) !important; border-color:var(--blue-500) !important; box-shadow:0 0 0 4px rgba(59,130,246,0.2) !important; }
div[data-baseweb="slider"] div[data-testid] { background:linear-gradient(90deg,var(--blue-600),var(--teal)) !important; }

/* ── BUTTONS ── */
[data-testid="stButton"] > button { width:100% !important; padding:1rem 2rem !important; background:linear-gradient(135deg,var(--blue-600),var(--teal)) !important; border:none !important; border-radius:var(--radius-md) !important; color:white !important; font-family:'Plus Jakarta Sans',sans-serif !important; font-size:0.9rem !important; font-weight:700 !important; letter-spacing:0.04em !important; box-shadow:0 8px 24px rgba(37,99,235,0.40) !important; transition:transform 0.2s var(--ease),box-shadow 0.2s !important; margin-top:0.5rem !important; position:relative !important; overflow:hidden !important; }
[data-testid="stButton"] > button:hover { transform:translateY(-3px) scale(1.01) !important; box-shadow:0 16px 36px rgba(37,99,235,0.55) !important; }
[data-testid="stButton"] > button:active { transform:translateY(0) scale(0.99) !important; }

/* ── SECTION DIVIDER ── */
.sec-divider { display:flex; align-items:center; gap:1rem; margin:2rem 0 1.5rem; font-size:0.65rem; font-weight:700; color:var(--blue-500); text-transform:uppercase; letter-spacing:0.2em; }
.sec-divider::before { content:''; flex:1; height:1.5px; background:linear-gradient(90deg,var(--border),transparent); }
.sec-divider::after  { content:''; flex:1; height:1.5px; background:linear-gradient(90deg,transparent,var(--border)); }

/* ── RESULT: Search results list ── */
.result-list-item {
  display:flex; align-items:center; gap:1rem;
  background:var(--bg-card); border:1.5px solid var(--border);
  border-radius:var(--radius-sm); padding:0.9rem 1.25rem;
  margin-bottom:0.6rem;
  transition:transform 0.25s var(--ease-out), border-color 0.25s, box-shadow 0.25s;
  animation:fadeUp 0.4s var(--ease-out) both;
}
.result-list-item:hover { transform:translateX(6px); border-color:var(--border-h); box-shadow:var(--shadow-md); }
.result-list-dot { width:8px; height:8px; border-radius:50%; background:var(--teal); flex-shrink:0; box-shadow:0 0 0 3px rgba(14,165,233,0.2); }
.result-list-name { font-size:0.88rem; font-weight:600; color:var(--text-primary); flex:1; }
.result-list-dist { font-size:0.75rem; font-weight:500; color:var(--blue-500); background:rgba(37,99,235,0.1); border:1px solid rgba(37,99,235,0.2); border-radius:999px; padding:0.2rem 0.7rem; white-space:nowrap; }

/* ── RESULT: Success count banner ── */
.count-banner {
  background:linear-gradient(135deg,rgba(16,185,129,0.12),rgba(14,165,233,0.08));
  border:1px solid rgba(16,185,129,0.25); border-radius:var(--radius-sm);
  padding:0.9rem 1.25rem; margin-bottom:1.25rem;
  display:flex; align-items:center; gap:0.75rem;
  font-size:0.85rem; color:var(--text-primary);
  animation:fadeUp 0.4s var(--ease-out) both;
}
.count-banner-dot { width:10px; height:10px; border-radius:50%; background:var(--green); box-shadow:0 0 0 3px rgba(16,185,129,0.25); animation:dotPulse 2s ease-in-out infinite; flex-shrink:0; }
@keyframes dotPulse { 0%,100%{box-shadow:0 0 0 3px rgba(16,185,129,0.25)} 50%{box-shadow:0 0 0 6px rgba(16,185,129,0.1)} }

/* ── RESULT: Recommendation cards ── */
.rec-card {
  background:var(--bg-card); border:1.5px solid var(--border);
  border-radius:var(--radius-md); padding:1.4rem 1.6rem;
  margin-bottom:1rem; position:relative; overflow:hidden;
  transition:transform 0.35s var(--ease-out), box-shadow 0.35s, border-color 0.35s;
  animation:fadeUp 0.5s var(--ease-out) both;
  transform-style:preserve-3d;
}
.rec-card::before { content:''; position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(90deg,var(--blue-600),var(--teal),var(--blue-600)); background-size:200%; animation:shimmer 3s linear infinite; }
.rec-card:hover { transform:translateY(-5px) scale(1.005); box-shadow:var(--shadow-3d); border-color:var(--border-h); }
.rec-card-rank { position:absolute; top:1rem; right:1.25rem; font-size:0.65rem; font-weight:700; color:var(--text-muted); letter-spacing:0.15em; text-transform:uppercase; }
.rec-card-name { font-family:'Lora',serif; font-size:1.1rem; font-weight:600; color:var(--text-primary); margin-bottom:0.6rem; padding-right:3rem; }
.rec-card-meta { display:flex; align-items:center; gap:0.75rem; flex-wrap:wrap; }
.rec-score-badge {
  display:inline-flex; align-items:center; gap:0.4rem;
  background:rgba(37,99,235,0.12); border:1px solid rgba(37,99,235,0.25);
  color:var(--blue-500); font-size:0.72rem; font-weight:700;
  padding:0.3rem 0.8rem; border-radius:999px; letter-spacing:0.04em;
}
.rec-score-fill {
  height:4px; border-radius:2px; margin-top:0.6rem;
  background:linear-gradient(90deg,var(--blue-600),var(--teal));
  transition:width 0.8s var(--ease-out);
}
.rec-link {
  display:inline-flex; align-items:center; gap:0.4rem;
  background:linear-gradient(135deg,var(--blue-600),var(--teal));
  color:white !important; font-size:0.72rem; font-weight:700;
  padding:0.35rem 0.9rem; border-radius:999px; text-decoration:none !important;
  box-shadow:0 4px 12px rgba(37,99,235,0.3);
  transition:box-shadow 0.2s, transform 0.2s;
}
.rec-link:hover { transform:translateY(-1px); box-shadow:0 8px 20px rgba(37,99,235,0.45); }

/* ── WEIGHT SLIDERS PANEL ── */
.weight-panel { background:var(--bg-card); border:1.5px solid var(--border); border-radius:var(--radius-md); padding:1.5rem 2rem; margin-bottom:1.5rem; position:relative; overflow:hidden; }
.weight-panel::before { content:''; position:absolute; top:0; left:0; right:0; height:3px; background:linear-gradient(90deg,var(--coral),var(--gold),var(--coral)); background-size:200%; animation:shimmer 3s linear infinite; }
.weight-row { display:flex; align-items:center; gap:1rem; margin-bottom:0.4rem; }
.weight-label { font-size:0.7rem; font-weight:700; color:var(--text-secondary); text-transform:uppercase; letter-spacing:0.1em; width:160px; flex-shrink:0; }

/* ── FAB ── */
.fab-chip { position:fixed; bottom:2rem; right:2rem; z-index:999; background:var(--bg-card-2); border:1.5px solid var(--border); border-radius:999px; padding:0.6rem 1.2rem; display:flex; align-items:center; gap:0.5rem; font-size:0.75rem; font-weight:600; color:var(--blue-500); box-shadow:var(--shadow-md); animation:floatFab 4s ease-in-out infinite; pointer-events:none; }
@keyframes floatFab { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-6px)} }
.fab-dot { width:8px; height:8px; border-radius:50%; background:var(--green); box-shadow:0 0 0 3px rgba(16,185,129,0.25); animation:dotPulse 2s ease-in-out infinite; }

/* st.success / st.info overrides */
[data-testid="stAlert"] { background:rgba(16,185,129,0.08) !important; border:1px solid rgba(16,185,129,0.25) !important; color:#6EE7B7 !important; border-radius:var(--radius-sm) !important; }
</style>

<script>
(function initTilt() {
  function apply() {
    document.querySelectorAll('.card-3d,.rec-card').forEach(card => {
      if (card._tilt) return;
      card._tilt = true;
      card.addEventListener('mousemove', e => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width  - 0.5;
        const y = (e.clientY - r.top)  / r.height - 0.5;
        card.style.transform  = `rotateX(${-y*8}deg) rotateY(${x*8}deg) translateY(-5px) scale(1.005)`;
        card.style.boxShadow  = `${-x*16}px ${-y*16}px 50px rgba(37,99,235,0.2)`;
        card.style.transition = 'box-shadow 0.1s';
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform  = '';
        card.style.boxShadow  = '';
        card.style.transition = 'transform 0.5s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.5s';
      });
    });
  }
  new MutationObserver(apply).observe(document.body, {childList:true, subtree:true});
  apply();
})();

document.addEventListener('click', e => {
  const btn = e.target.closest('[data-testid="stButton"] > button');
  if (!btn) return;
  const ripple = document.createElement('span');
  const rect   = btn.getBoundingClientRect();
  const size   = Math.max(rect.width, rect.height);
  Object.assign(ripple.style, {
    position:'absolute', width:size+'px', height:size+'px', borderRadius:'50%',
    background:'rgba(255,255,255,0.25)',
    left:(e.clientX-rect.left-size/2)+'px', top:(e.clientY-rect.top-size/2)+'px',
    transform:'scale(0)', pointerEvents:'none',
    animation:'rippleAnim 0.6s ease-out forwards'
  });
  if (!document.getElementById('rippleStyle')) {
    const s = document.createElement('style');
    s.id = 'rippleStyle';
    s.textContent = '@keyframes rippleAnim { to { transform:scale(2.5); opacity:0; } }';
    document.head.appendChild(s);
  }
  btn.style.position = 'relative'; btn.style.overflow = 'hidden';
  btn.appendChild(ripple);
  setTimeout(() => ripple.remove(), 700);
});
</script>
""", unsafe_allow_html=True)

# ── Load Data ─────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def load_data():
    property_data = pd.read_csv("datasets/appartments.csv")
    location_df   = pickle.load(open('datasets/location_df_merge.pkl', 'rb'))
    cosine_sim1   = pickle.load(open('datasets/cosine_sim1.pkl', 'rb'))
    cosine_sim2   = pickle.load(open('datasets/cosine_sim2.pkl', 'rb'))
    cosine_sim3   = pickle.load(open('datasets/cosine_sim3.pkl', 'rb'))
    return property_data, location_df, cosine_sim1, cosine_sim2, cosine_sim3

property_data, location_df, cosine_sim1, cosine_sim2, cosine_sim3 = load_data()

# ── Recommend Function ────────────────────────────────────────────────────────
def recommend_properties(property_name, w1=0.5, w2=0.8, w3=1.0, top_n=5):
    cosine_sim_matrix = w1 * cosine_sim1 + w2 * cosine_sim2 + w3 * cosine_sim3
    sim_scores   = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices  = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores   = [round(i[1], 3) for i in sorted_scores[1:top_n + 1]]
    top_props    = location_df.index[top_indices].tolist()
    links        = property_data.set_index("PropertyName").loc[top_props]["Link"].tolist()
    return pd.DataFrame({'Property Name': top_props, 'Similarity Score': top_scores, 'Link': links})

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-logo-wrap">
      <div class="sb-logo">
        <div class="sb-logo-icon">🏡</div>
        <div><div class="sb-logo-text">NestIQ</div></div>
      </div>
      <div class="sb-logo-sub">AI-Powered Apartment Finder</div>
    </div>
    """, unsafe_allow_html=True)
    try:
        st.image("datasets/banner image.jpg", use_container_width=True)
    except Exception:
        pass
    st.markdown("""
    <div class="sb-tip">
      💡 <strong>How it works:</strong> Select a location to find nearby apartments by distance, 
      or pick an apartment to get AI-powered similarity recommendations.
    </div>
    """, unsafe_allow_html=True)

# ── Topbar ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
  <div class="topbar-brand">
    <div class="topbar-icon">🏡</div>
    <div class="topbar-name">Nest<span>IQ</span></div>
    <div class="topbar-badge">Apartment Finder</div>
  </div>
  <div class="topbar-nav">
    <div class="nav-pill">Valuation</div>
    <div class="nav-pill active">Recommender</div>
    <div class="nav-pill">Compare</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <div class="hero-tag">🤖 AI Similarity Engine</div>
  <div class="hero-h1">Discover Your<br><em>Perfect Apartment</em></div>
  <div class="hero-sub">
    Search apartments near any location by radius, or let our AI recommend 
    similar properties based on facilities, pricing, and location signals.
  </div>
  <div class="hero-chips">
    <div class="hero-chip">📍 Location Search</div>
    <div class="hero-chip">🤖 AI Recommendations</div>
    <div class="hero-chip">⚖️ Weighted Similarity</div>
    <div class="hero-chip">🔗 Direct Links</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════
#  SECTION 1 — Location Search
# ══════════════════════════════════════════════════
st.markdown('<div class="sec-divider">📍 Location-Based Search</div>', unsafe_allow_html=True)

st.markdown("""<div class="card-3d-wrap"><div class="card-3d">
  <div class="card-3d-accent"></div>
  <div class="card-header">
    <div class="card-icon teal">🗺️</div>
    <div>
      <div class="card-title-text">Find Apartments Near You</div>
      <div class="card-title-sub">Select a location and set a search radius to discover nearby properties</div>
    </div>
  </div>""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    selected_location = st.selectbox(
        'Search Location',
        sorted(location_df.columns.to_list()),
        help="Start typing to filter locations"
    )
with col2:
    radius = st.slider('Radius (km)', 1, 50, 5, 1)

search_clicked = st.button('🔎  Search Nearby Apartments')
st.markdown("</div></div>", unsafe_allow_html=True)

if search_clicked:
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()
    count = len(result_ser)

    st.markdown(f"""
    <div class="count-banner">
      <div class="count-banner-dot"></div>
      <div>Found <strong style="color:var(--green)">{count} apartment{'s' if count != 1 else ''}</strong>
      within <strong style="color:var(--teal)">{radius} km</strong>
      of <strong style="color:var(--text-primary)">{selected_location}</strong></div>
    </div>
    """, unsafe_allow_html=True)

    if count == 0:
        st.markdown("""
        <div style="text-align:center; padding:2rem; color:var(--text-muted); font-size:0.9rem;">
          No apartments found in this radius. Try increasing the distance.
        </div>""", unsafe_allow_html=True)
    else:
        for i, (key, value) in enumerate(result_ser.items()):
            dist_km = round(value / 1000, 2)
            st.markdown(f"""
            <div class="result-list-item" style="animation-delay:{i * 0.05}s">
              <div class="result-list-dot"></div>
              <div class="result-list-name">{key}</div>
              <div class="result-list-dist">📍 {dist_km} km</div>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════
#  SECTION 2 — AI Recommendations
# ══════════════════════════════════════════════════
st.markdown('<div class="sec-divider">🤖 AI-Powered Recommendations</div>', unsafe_allow_html=True)

st.markdown("""<div class="card-3d-wrap"><div class="card-3d">
  <div class="card-3d-accent"></div>
  <div class="card-header">
    <div class="card-icon blue">🏠</div>
    <div>
      <div class="card-title-text">Select an Apartment</div>
      <div class="card-title-sub">Our AI will find the most similar properties based on your chosen weights</div>
    </div>
  </div>""", unsafe_allow_html=True)

selected_apartment = st.selectbox(
    'Apartment to Match',
    sorted(location_df.index.to_list()),
    help="Start typing to filter apartments"
)
st.markdown("</div></div>", unsafe_allow_html=True)

# Weight sliders card
st.markdown("""<div class="card-3d-wrap"><div class="card-3d">
  <div class="card-3d-accent" style="background:linear-gradient(90deg,var(--coral),var(--gold),var(--coral));background-size:200%"></div>
  <div class="card-header">
    <div class="card-icon coral">⚖️</div>
    <div>
      <div class="card-title-text">Similarity Weights</div>
      <div class="card-title-sub">Adjust how much each factor influences the recommendations</div>
    </div>
  </div>""", unsafe_allow_html=True)

wc1, wc2, wc3 = st.columns(3)
with wc1:
    w1 = st.slider("🏢 Facilities", 0.0, 1.5, 0.5, 0.1,
                   help="Weight for facilities/amenities similarity")
with wc2:
    w2 = st.slider("💰 Pricing", 0.0, 1.5, 0.8, 0.1,
                   help="Weight for price similarity")
with wc3:
    w3 = st.slider("📍 Location", 0.0, 1.5, 1.0, 0.1,
                   help="Weight for location/proximity similarity")

st.markdown("</div></div>", unsafe_allow_html=True)

recommend_clicked = st.button('✨  Get AI Recommendations')

if recommend_clicked:
    with st.spinner("Analysing similarity vectors…"):
        rec_df = recommend_properties(selected_apartment, w1, w2, w3)

    st.markdown(f"""
    <div class="count-banner">
      <div class="count-banner-dot"></div>
      <div>Showing top <strong style="color:var(--blue-500)">{len(rec_df)} recommendations</strong>
      similar to <strong style="color:var(--text-primary)">{selected_apartment}</strong></div>
    </div>
    """, unsafe_allow_html=True)

    max_score = rec_df['Similarity Score'].max() if not rec_df.empty else 1

    for i, row in rec_df.iterrows():
        bar_pct = int((row['Similarity Score'] / max_score) * 100) if max_score > 0 else 0
        st.markdown(f"""
        <div class="rec-card" style="animation-delay:{i * 0.08}s">
          <div class="rec-card-rank">#{i + 1} Match</div>
          <div class="rec-card-name">{row['Property Name']}</div>
          <div class="rec-card-meta">
            <div class="rec-score-badge">
              ◆ Similarity &nbsp;{row['Similarity Score']}
            </div>
            <a href="{row['Link']}" target="_blank" class="rec-link">🔗 View Property</a>
          </div>
          <div class="rec-score-fill" style="width:{bar_pct}%"></div>
        </div>
        """, unsafe_allow_html=True)

# ── FAB ───────────────────────────────────────────────────────────────────────
st.markdown('<div class="fab-chip"><div class="fab-dot"></div> AI Engine Online</div>', unsafe_allow_html=True)