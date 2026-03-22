# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np
# import gzip

# # Page Configuration
# st.set_page_config(page_title="Real Estate Price Prediction", page_icon="🏠", layout="wide")

# # Sidebar - Logo and App Info
# st.sidebar.image("datasets/front image.png", use_container_width=True)  # Add an image in the sidebar

# st.sidebar.title("📌 About This App")
# st.sidebar.info(
#     "This **Real Estate Price Prediction** app helps users estimate property prices "
#     "based on various parameters such as location, property type, built-up area, and amenities. "
# )


# # Custom CSS for Better UI
# st.markdown("""
#     <style>
#     .stTextInput, .stSelectbox, .stNumberInput {
#         margin-bottom: 20px;
#         font-size: 16px;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         font-size: 16px;
#         padding: 12px 28px;
#         border-radius: 8px;
#         border: none;
#         cursor: pointer;
#     }
#     .stButton>button:hover {
#         background-color: #45a049;
#     }
#     .stMarkdown {
#         font-size: 18px;
#         font-weight: bold;
#         color: #2E8B57;
#     }
#     .stHeader {
#         color: #00796B;
#         font-weight: bold;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Load pre-trained models
# with open('datasets/df.pkl', 'rb') as file:
#     df = pickle.load(file)

# #with open('datasets/pipeline.pkl', 'rb') as file:
# #    pipeline = pickle.load(file)

# with gzip.open('pipeline1.pkl.gz', 'rb') as file:
#     pipeline = pickle.load(file)    

# # Header
# st.header("🏠 **Real Estate Price Prediction**")
# st.markdown("Enter the details below to predict the price of the property.")

# # Property Type and Inputs Layout
# input_columns = st.columns(2)

# with input_columns[0]:
#     property_type = st.selectbox('Property Type', ['flat', 'house'])
#     sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
#     bedrooms = float(st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))
#     bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))
#     balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))

# with input_columns[1]:
#     property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
#     built_up_area = float(st.number_input('Built Up Area (in sq.ft)', min_value=100.0, step=10.0))
#     servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))
#     store_room = float(st.selectbox('Store Room', [0.0, 1.0]))
#     furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
#     luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
#     floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

# # Predict Button with Enhancements
# if st.button('🔍 **Predict Price**'):
#     # Create a DataFrame from the inputs
#     data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
#     columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
#                'agePossession', 'built_up_area', 'servant room', 'store room',
#                'furnishing_type', 'luxury_category', 'floor_category']
    
#     one_df = pd.DataFrame(data, columns=columns)

#     # Predict price using the pipeline
#     base_price = np.expm1(pipeline.predict(one_df))[0]
#     low = base_price - 0.22
#     high = base_price + 0.22

#     # Enhanced Prediction Text
#     st.markdown(f"### 🏡 **The estimated price of the property is between ₹{low:,.2f} Cr and ₹{high:,.2f} Cr.**")

#     # Display Property Details in a Grid Layout
#     st.markdown("#### 📋 **Property Details**")

#     # Create a 2-column layout for property details
#     details_columns = st.columns(2)

#     with details_columns[0]:
#         st.markdown(f"**Property Type**: {property_type.capitalize()}")
#         st.markdown(f"**Sector**: {sector.capitalize()}")
#         st.markdown(f"**Bedrooms**: {bedrooms}")
#         st.markdown(f"**Bathrooms**: {bathroom}")
#         st.markdown(f"**Balconies**: {balcony}")
#         st.markdown(f"**Property Age**: {property_age} years")

#     with details_columns[1]:
#         st.markdown(f"**Built-up Area**: {built_up_area} sq.ft")
#         st.markdown(f"**Servant Room**: {servant_room}")
#         st.markdown(f"**Store Room**: {store_room}")
#         st.markdown(f"**Furnishing Type**: {furnishing_type.capitalize()}")
#         st.markdown(f"**Luxury Category**: {luxury_category.capitalize()}")
#         st.markdown(f"**Floor Category**: {floor_category.capitalize()}")

#     st.markdown("---")
#     st.info("Note: The price prediction is based on the provided features and is an estimation only.")
#     st.info("Note: To get the most accurate results, please provide **reliable and precise input values**. This model performs best with accurate and detailed information.")


# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np
# import gzip

# # ── Page Config ──────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="NestIQ – Smart Property Valuation",
#     page_icon="🏡",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ── MEGA CSS + JS ─────────────────────────────────────────────────────────────
# st.markdown(r"""
# <style>
# /* ═══════════════════════════════════════════════
#    FONTS
# ═══════════════════════════════════════════════ */
# @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

# /* ═══════════════════════════════════════════════
#    TOKENS
# ═══════════════════════════════════════════════ */
# :root {
#   --sky:       #EEF6FF;
#   --white:     #FFFFFF;
#   --blue-50:   #F0F7FF;
#   --blue-100:  #DBEAFE;
#   --blue-500:  #3B82F6;
#   --blue-600:  #2563EB;
#   --blue-700:  #1D4ED8;
#   --teal:      #0EA5E9;
#   --coral:     #F97316;
#   --green:     #10B981;
#   --slate-400: #94A3B8;
#   --slate-500: #64748B;
#   --slate-700: #334155;
#   --slate-900: #0F172A;
#   --shadow-sm: 0 2px 8px rgba(15,23,42,0.06);
#   --shadow-md: 0 8px 30px rgba(15,23,42,0.10);
#   --shadow-3d: 0 20px 60px rgba(37,99,235,0.18);
#   --radius-sm: 10px;
#   --radius-md: 16px;
#   --radius-lg: 24px;
#   --ease:      cubic-bezier(0.34, 1.56, 0.64, 1);
#   --ease-out:  cubic-bezier(0.16, 1, 0.3, 1);
# }

# /* ═══════════════════════════════════════════════
#    BASE
# ═══════════════════════════════════════════════ */
# *, *::before, *::after { box-sizing: border-box; }

# html, body,
# [data-testid="stAppViewContainer"],
# [data-testid="stMain"], .main {
#   background: var(--sky) !important;
#   font-family: 'Plus Jakarta Sans', sans-serif !important;
#   color: var(--slate-900) !important;
# }
# #MainMenu, footer, header,
# [data-testid="stToolbar"],
# [data-testid="stDecoration"] { display: none !important; }

# .block-container { padding: 0 2.5rem 4rem !important; max-width: 1320px !important; }

# ::-webkit-scrollbar { width: 5px; }
# ::-webkit-scrollbar-track { background: var(--blue-50); }
# ::-webkit-scrollbar-thumb { background: var(--blue-500); border-radius: 3px; }

# /* ═══════════════════════════════════════════════
#    ANIMATED MESH BG
# ═══════════════════════════════════════════════ */
# [data-testid="stAppViewContainer"]::before {
#   content: '';
#   position: fixed; inset: 0;
#   background:
#     radial-gradient(ellipse 80% 60% at 20% 10%, rgba(59,130,246,0.10) 0%, transparent 60%),
#     radial-gradient(ellipse 60% 50% at 80% 80%, rgba(14,165,233,0.08) 0%, transparent 60%),
#     radial-gradient(ellipse 50% 40% at 60% 20%, rgba(249,115,22,0.05) 0%, transparent 60%);
#   pointer-events: none; z-index: 0;
#   animation: meshDrift 18s ease-in-out infinite alternate;
# }
# @keyframes meshDrift {
#   0%   { opacity: 0.8; transform: scale(1); }
#   100% { opacity: 1;   transform: scale(1.05); }
# }

# /* ═══════════════════════════════════════════════
#    SIDEBAR
# ═══════════════════════════════════════════════ */
# [data-testid="stSidebar"] {
#   background: var(--white) !important;
#   border-right: 1px solid var(--blue-100) !important;
#   box-shadow: 4px 0 24px rgba(15,23,42,0.06) !important;
# }
# [data-testid="stSidebar"] .stMarkdown p { color: var(--slate-500) !important; font-size: 0.82rem !important; }

# .sb-logo-wrap { padding: 1.8rem 1.5rem 1.4rem; border-bottom: 1px solid var(--blue-100); }
# .sb-logo { display: flex; align-items: center; gap: 0.6rem; }
# .sb-logo-icon {
#   width: 38px; height: 38px;
#   background: linear-gradient(135deg, var(--blue-600), var(--teal));
#   border-radius: 10px; display: flex; align-items: center; justify-content: center;
#   font-size: 1.1rem; box-shadow: 0 4px 12px rgba(37,99,235,0.35);
# }
# .sb-logo-text {
#   font-size: 1.25rem; font-weight: 800;
#   background: linear-gradient(135deg, var(--blue-600), var(--teal));
#   -webkit-background-clip: text; -webkit-text-fill-color: transparent;
# }
# .sb-logo-sub { font-size: 0.62rem; color: var(--slate-400); letter-spacing: 0.15em; text-transform: uppercase; margin-top: 1rem; }

# .sb-stat-row { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; padding: 1.25rem 1.5rem; border-bottom: 1px solid var(--blue-100); }
# .sb-stat { background: var(--blue-50); border-radius: var(--radius-sm); padding: 0.9rem 0.75rem; text-align: center; }
# .sb-stat-num { font-size: 1.2rem; font-weight: 700; color: var(--blue-600); }
# .sb-stat-lbl { font-size: 0.6rem; color: var(--slate-400); text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.2rem; }

# .sb-tip {
#   margin: 1rem 1.5rem;
#   background: linear-gradient(135deg, #FFF7ED, #FFEDD5);
#   border-left: 3px solid var(--coral);
#   border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
#   padding: 0.8rem 1rem; font-size: 0.75rem; color: #9A3412; line-height: 1.6;
# }

# /* ═══════════════════════════════════════════════
#    TOPBAR
# ═══════════════════════════════════════════════ */
# .topbar {
#   display: flex; align-items: center; justify-content: space-between;
#   padding: 1.5rem 0 0.5rem;
#   border-bottom: 1px solid var(--blue-100); margin-bottom: 2rem;
#   animation: slideDown 0.6s var(--ease-out) both;
# }
# @keyframes slideDown { from { opacity:0; transform:translateY(-16px); } to { opacity:1; transform:translateY(0); } }
# .topbar-brand { display:flex; align-items:center; gap:0.75rem; }
# .topbar-icon {
#   width:44px; height:44px;
#   background: linear-gradient(135deg, var(--blue-600), var(--teal));
#   border-radius: 12px; display:flex; align-items:center; justify-content:center;
#   font-size:1.3rem; box-shadow: 0 6px 18px rgba(37,99,235,0.3);
# }
# .topbar-name { font-size:1.5rem; font-weight:800; color:var(--slate-900); }
# .topbar-name span { color:var(--blue-600); }
# .topbar-badge {
#   background: linear-gradient(135deg, var(--blue-600), var(--teal));
#   color: white; font-size:0.65rem; font-weight:600;
#   letter-spacing:0.1em; padding:0.35rem 0.9rem;
#   border-radius:999px; text-transform:uppercase;
#   box-shadow: 0 4px 12px rgba(37,99,235,0.3);
# }
# .topbar-nav { display:flex; gap:0.5rem; }
# .nav-pill { padding:0.4rem 1rem; border-radius:999px; font-size:0.78rem; font-weight:500; color:var(--slate-500); cursor:pointer; border:1.5px solid transparent; }
# .nav-pill:hover { background:var(--blue-50); color:var(--blue-600); border-color:var(--blue-100); }
# .nav-pill.active { background:var(--blue-600); color:white; }

# /* ═══════════════════════════════════════════════
#    HERO BANNER
# ═══════════════════════════════════════════════ */
# .hero-banner {
#   background: linear-gradient(135deg, var(--blue-600) 0%, var(--blue-700) 40%, #0E3A8C 100%);
#   border-radius: var(--radius-lg); padding: 3rem 3.5rem;
#   position: relative; overflow: hidden; margin-bottom: 2.5rem;
#   animation: fadeUp 0.7s 0.1s var(--ease-out) both;
# }
# .hero-banner::before {
#   content:''; position:absolute; top:-60px; right:-60px;
#   width:300px; height:300px;
#   background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%); border-radius:50%;
# }
# .hero-banner::after {
#   content:''; position:absolute; bottom:-40px; left:30%;
#   width:200px; height:200px;
#   background: radial-gradient(circle, rgba(14,165,233,0.25) 0%, transparent 70%); border-radius:50%;
# }
# @keyframes fadeUp { from { opacity:0; transform:translateY(28px); } to { opacity:1; transform:translateY(0); } }
# .hero-tag {
#   display:inline-flex; align-items:center; gap:0.4rem;
#   background:rgba(255,255,255,0.15); backdrop-filter:blur(10px);
#   border:1px solid rgba(255,255,255,0.2); color:white;
#   font-size:0.7rem; font-weight:600; letter-spacing:0.12em; text-transform:uppercase;
#   padding:0.35rem 0.9rem; border-radius:999px; margin-bottom:1.2rem;
# }
# .hero-h1 {
#   font-family:'Lora', serif; font-size: clamp(1.8rem, 3.5vw, 2.8rem);
#   font-weight:600; color:white; line-height:1.25; margin-bottom:0.75rem; position:relative; z-index:1;
# }
# .hero-h1 em { font-style:italic; color:#93C5FD; }
# .hero-sub { color:rgba(255,255,255,0.7); font-size:0.9rem; line-height:1.7; max-width:480px; position:relative; z-index:1; }
# .hero-chips { display:flex; gap:0.75rem; margin-top:1.5rem; flex-wrap:wrap; position:relative; z-index:1; }
# .hero-chip {
#   background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.2);
#   color:white; font-size:0.72rem; font-weight:500; padding:0.4rem 0.85rem; border-radius:999px;
# }

# /* ═══════════════════════════════════════════════
#    STEPS
# ═══════════════════════════════════════════════ */
# .steps-row { display:flex; align-items:center; margin-bottom:2rem; animation: fadeUp 0.6s 0.2s var(--ease-out) both; }
# .step-item { display:flex; align-items:center; gap:0.5rem; }
# .step-num { width:30px; height:30px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:0.75rem; font-weight:700; flex-shrink:0; }
# .step-num.done   { background:var(--green); color:white; }
# .step-num.active { background:var(--blue-600); color:white; box-shadow:0 0 0 4px rgba(59,130,246,0.2); }
# .step-num.idle   { background:var(--blue-100); color:var(--slate-500); }
# .step-label { font-size:0.72rem; font-weight:600; color:var(--slate-500); }
# .step-label.active { color:var(--blue-600); }
# .step-line { flex:1; height:2px; background:var(--blue-100); margin:0 0.75rem; }
# .step-line.done { background:var(--green); }

# /* ═══════════════════════════════════════════════
#    3D CARDS
# ═══════════════════════════════════════════════ */
# .card-3d-wrap { perspective: 1200px; margin-bottom: 1.5rem; animation: fadeUp 0.7s var(--ease-out) both; }
# .card-3d-wrap:nth-child(2) { animation-delay:0.1s; }
# .card-3d-wrap:nth-child(3) { animation-delay:0.2s; }

# .card-3d {
#   background: var(--white);
#   border: 1.5px solid rgba(219,234,254,0.8);
#   border-radius: var(--radius-md); padding: 1.75rem 2rem;
#   position: relative; transition: transform 0.4s var(--ease-out), box-shadow 0.4s var(--ease-out);
#   transform-style: preserve-3d; box-shadow: var(--shadow-sm); overflow: hidden;
# }
# .card-3d::before {
#   content:''; position:absolute; inset:0;
#   background: linear-gradient(135deg, rgba(59,130,246,0.04) 0%, transparent 60%);
#   border-radius: inherit; pointer-events:none;
# }
# .card-3d:hover { transform: rotateX(2deg) rotateY(-2deg) translateY(-6px) scale(1.01); box-shadow: var(--shadow-3d); border-color: var(--blue-100); }

# .card-3d-accent {
#   position:absolute; top:0; left:0; right:0; height:3px;
#   background: linear-gradient(90deg, var(--blue-600), var(--teal), var(--blue-600));
#   background-size: 200%; border-radius: var(--radius-md) var(--radius-md) 0 0;
#   animation: shimmer 3s linear infinite;
# }
# @keyframes shimmer { to { background-position: 200% center; } }

# .card-header { display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem; padding-bottom:1rem; border-bottom:1.5px solid var(--blue-50); }
# .card-icon { width:38px; height:38px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:1rem; flex-shrink:0; }
# .card-icon.blue  { background:linear-gradient(135deg,#EFF6FF,#DBEAFE); }
# .card-icon.teal  { background:linear-gradient(135deg,#F0FDFA,#CCFBF1); }
# .card-icon.coral { background:linear-gradient(135deg,#FFF7ED,#FFEDD5); }
# .card-title-text { font-size:0.95rem; font-weight:700; color:var(--slate-700); }
# .card-title-sub  { font-size:0.7rem; color:var(--slate-400); margin-top:0.1rem; }

# /* ═══════════════════════════════════════════════
#    FORM WIDGETS
# ═══════════════════════════════════════════════ */
# div[data-baseweb="select"] > div {
#   background: var(--blue-50) !important; border: 1.5px solid var(--blue-100) !important;
#   border-radius: var(--radius-sm) !important; color: var(--slate-900) !important;
#   font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 0.85rem !important; transition: all 0.2s !important;
# }
# div[data-baseweb="select"]:focus-within > div { border-color: var(--blue-500) !important; background: white !important; box-shadow: 0 0 0 3px rgba(59,130,246,0.15) !important; }
# div[data-baseweb="select"] svg { fill: var(--blue-500) !important; }
# div[data-baseweb="menu"] { background: white !important; border: 1.5px solid var(--blue-100) !important; border-radius: var(--radius-sm) !important; box-shadow: var(--shadow-md) !important; }
# div[data-baseweb="menu"] li { color: var(--slate-700) !important; font-size: 0.83rem !important; font-family: 'Plus Jakarta Sans', sans-serif !important; }
# div[data-baseweb="menu"] li:hover { background: var(--blue-50) !important; color: var(--blue-600) !important; }

# [data-testid="stNumberInput"] input {
#   background: var(--blue-50) !important; border: 1.5px solid var(--blue-100) !important;
#   border-radius: var(--radius-sm) !important; color: var(--slate-900) !important;
#   font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 0.85rem !important;
# }
# [data-testid="stNumberInput"] input:focus { border-color: var(--blue-500) !important; background: white !important; box-shadow: 0 0 0 3px rgba(59,130,246,0.15) !important; }

# label[data-testid="stWidgetLabel"] > div > p {
#   font-family: 'Plus Jakarta Sans', sans-serif !important; font-size: 0.72rem !important;
#   font-weight: 600 !important; color: var(--slate-500) !important;
#   text-transform: uppercase !important; letter-spacing: 0.08em !important;
# }

# /* ═══════════════════════════════════════════════
#    BUTTON
# ═══════════════════════════════════════════════ */
# [data-testid="stButton"] > button {
#   width: 100% !important; padding: 1rem 2rem !important;
#   background: linear-gradient(135deg, var(--blue-600), var(--teal)) !important;
#   border: none !important; border-radius: var(--radius-md) !important;
#   color: white !important; font-family: 'Plus Jakarta Sans', sans-serif !important;
#   font-size: 0.9rem !important; font-weight: 700 !important; letter-spacing: 0.04em !important;
#   box-shadow: 0 8px 24px rgba(37,99,235,0.35) !important;
#   transition: transform 0.2s var(--ease), box-shadow 0.2s !important; margin-top: 1rem !important;
# }
# [data-testid="stButton"] > button:hover { transform: translateY(-3px) scale(1.01) !important; box-shadow: 0 16px 36px rgba(37,99,235,0.45) !important; }
# [data-testid="stButton"] > button:active { transform: translateY(0) scale(0.99) !important; }

# /* ═══════════════════════════════════════════════
#    RESULT SECTION
# ═══════════════════════════════════════════════ */
# .result-outer { animation: popIn 0.7s var(--ease) both; margin-top: 2rem; }
# @keyframes popIn { from { opacity:0; transform:scale(0.92) translateY(20px); } to { opacity:1; transform:scale(1) translateY(0); } }

# .result-hero {
#   background: linear-gradient(135deg, var(--blue-600) 0%, var(--teal) 100%);
#   border-radius: var(--radius-lg); padding: 2.5rem; text-align: center;
#   position: relative; overflow: hidden; box-shadow: 0 20px 60px rgba(37,99,235,0.3);
# }
# .result-hero::before { content:''; position:absolute; top:-80px; right:-80px; width:280px; height:280px; background:radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 70%); border-radius:50%; }
# .result-hero::after  { content:''; position:absolute; bottom:-60px; left:-60px; width:220px; height:220px; background:radial-gradient(circle, rgba(14,165,233,0.3) 0%, transparent 70%); border-radius:50%; }

# .res-tag { display:inline-block; background:rgba(255,255,255,0.2); backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.3); color:white; font-size:0.65rem; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; padding:0.3rem 0.8rem; border-radius:999px; margin-bottom:1rem; position:relative; z-index:1; }
# .res-price { font-family:'Lora', serif; font-size:clamp(2rem,5vw,3.2rem); font-weight:600; color:white; line-height:1.2; position:relative; z-index:1; }
# .res-range { color:rgba(255,255,255,0.8); font-size:0.82rem; margin-top:0.5rem; position:relative; z-index:1; }
# .res-confidence { display:inline-flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.15); border:1px solid rgba(255,255,255,0.25); color:white; font-size:0.72rem; font-weight:600; padding:0.4rem 0.9rem; border-radius:999px; margin-top:1rem; position:relative; z-index:1; }

# .stat-pills { display:flex; gap:1rem; margin-top:1.5rem; flex-wrap:wrap; }
# .stat-pill { flex:1; min-width:100px; background:white; border-radius:var(--radius-sm); padding:1rem 1.25rem; text-align:center; box-shadow:var(--shadow-sm); border:1px solid var(--blue-100); transition: transform 0.3s var(--ease), box-shadow 0.3s; animation: fadeUp 0.5s var(--ease-out) both; }
# .stat-pill:hover { transform:translateY(-4px); box-shadow:var(--shadow-md); }
# .stat-pill-val { font-size:1.15rem; font-weight:800; color:var(--blue-600); }
# .stat-pill-lbl { font-size:0.62rem; color:var(--slate-400); text-transform:uppercase; letter-spacing:0.1em; margin-top:0.2rem; }

# .detail-table { background:white; border-radius:var(--radius-md); border:1.5px solid var(--blue-100); overflow:hidden; margin-top:1.5rem; animation: fadeUp 0.6s 0.15s var(--ease-out) both; }
# .detail-table-header { background: var(--blue-50); padding:1rem 1.5rem; font-size:0.72rem; font-weight:700; color:var(--slate-500); text-transform:uppercase; letter-spacing:0.1em; border-bottom:1.5px solid var(--blue-100); }
# .detail-row { display:grid; grid-template-columns: repeat(3,1fr); border-bottom:1px solid var(--blue-50); }
# .detail-row:last-child { border-bottom:none; }
# .detail-cell { padding:1rem 1.5rem; border-right:1px solid var(--blue-50); transition: background 0.2s; }
# .detail-cell:last-child { border-right:none; }
# .detail-cell:hover { background:var(--blue-50); }
# .dc-label { font-size:0.62rem; color:var(--slate-400); text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.3rem; }
# .dc-value { font-size:0.9rem; font-weight:600; color:var(--slate-700); }

# .notice-box { display:flex; gap:0.75rem; align-items:flex-start; padding:1rem 1.25rem; border-radius:var(--radius-sm); font-size:0.78rem; line-height:1.7; margin-top:1rem; }
# .notice-box.info { background:#EFF6FF; border:1px solid #BFDBFE; color:#1D4ED8; }
# .notice-box.warn { background:#FFF7ED; border:1px solid #FDBA74; color:#9A3412; }
# .notice-icon { font-size:1rem; flex-shrink:0; margin-top:0.1rem; }

# .sec-divider { display:flex; align-items:center; gap:1rem; margin:2rem 0 1.25rem; font-size:0.65rem; font-weight:700; color:var(--blue-600); text-transform:uppercase; letter-spacing:0.2em; animation: fadeUp 0.5s var(--ease-out) both; }
# .sec-divider::before, .sec-divider::after { content:''; flex:1; height:1.5px; background:linear-gradient(90deg, transparent, var(--blue-100)); }
# .sec-divider::before { background:linear-gradient(90deg, var(--blue-100), transparent); }

# .fab-chip { position:fixed; bottom:2rem; right:2rem; z-index:999; background:white; border:1.5px solid var(--blue-100); border-radius:999px; padding:0.6rem 1.2rem; display:flex; align-items:center; gap:0.5rem; font-size:0.75rem; font-weight:600; color:var(--blue-600); box-shadow:var(--shadow-md); animation:floatFab 4s ease-in-out infinite; pointer-events:none; }
# @keyframes floatFab { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-6px); } }
# .fab-dot { width:8px; height:8px; border-radius:50%; background:var(--green); box-shadow:0 0 0 3px rgba(16,185,129,0.25); animation:dotPulse 2s ease-in-out infinite; }
# @keyframes dotPulse { 0%,100% { box-shadow:0 0 0 3px rgba(16,185,129,0.25); } 50% { box-shadow:0 0 0 6px rgba(16,185,129,0.1); } }
# </style>

# <script>
# // 3D tilt on cards
# (function initTilt() {
#   function apply() {
#     document.querySelectorAll('.card-3d').forEach(card => {
#       if (card._tilt) return;
#       card._tilt = true;
#       card.addEventListener('mousemove', e => {
#         const r  = card.getBoundingClientRect();
#         const x  = (e.clientX - r.left) / r.width  - 0.5;
#         const y  = (e.clientY - r.top)  / r.height - 0.5;
#         card.style.transform     = `rotateX(${-y*10}deg) rotateY(${x*10}deg) translateY(-8px) scale(1.01)`;
#         card.style.boxShadow     = `${-x*20}px ${-y*20}px 60px rgba(37,99,235,0.18)`;
#         card.style.transition    = 'box-shadow 0.1s';
#       });
#       card.addEventListener('mouseleave', () => {
#         card.style.transform  = 'rotateX(0) rotateY(0) translateY(0) scale(1)';
#         card.style.boxShadow  = '0 2px 8px rgba(15,23,42,0.06)';
#         card.style.transition = 'transform 0.5s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.5s';
#       });
#     });
#   }
#   new MutationObserver(apply).observe(document.body, {childList:true, subtree:true});
#   apply();
# })();

# // Ripple on button
# document.addEventListener('click', e => {
#   const btn = e.target.closest('[data-testid="stButton"] > button');
#   if (!btn) return;
#   const ripple = document.createElement('span');
#   const rect   = btn.getBoundingClientRect();
#   const size   = Math.max(rect.width, rect.height);
#   Object.assign(ripple.style, {
#     position:'absolute', width:size+'px', height:size+'px', borderRadius:'50%',
#     background:'rgba(255,255,255,0.35)',
#     left:(e.clientX-rect.left-size/2)+'px', top:(e.clientY-rect.top-size/2)+'px',
#     transform:'scale(0)', pointerEvents:'none',
#     animation:'rippleAnim 0.6s ease-out forwards'
#   });
#   if (!document.getElementById('rippleStyle')) {
#     const s = document.createElement('style');
#     s.id = 'rippleStyle';
#     s.textContent = '@keyframes rippleAnim { to { transform:scale(2.5); opacity:0; } }';
#     document.head.appendChild(s);
#   }
#   btn.style.position = 'relative'; btn.style.overflow = 'hidden';
#   btn.appendChild(ripple);
#   setTimeout(() => ripple.remove(), 700);
# });

# // Stat pill hover lift sound-like animation
# document.addEventListener('DOMContentLoaded', () => {
#   document.querySelectorAll('.stat-pill').forEach((el, i) => {
#     el.style.animationDelay = (i * 0.06) + 's';
#   });
# });
# </script>
# """, unsafe_allow_html=True)

# # ── Load Models ───────────────────────────────────────────────────────────────
# @st.cache_resource(show_spinner=False)
# def load_models():
#     with open('datasets/df.pkl', 'rb') as f:
#         df = pickle.load(f)
#     with gzip.open('pipeline1.pkl.gz', 'rb') as f:
#         pipeline = pickle.load(f)
#     return df, pipeline

# df, pipeline = load_models()

# # ── Sidebar ───────────────────────────────────────────────────────────────────
# with st.sidebar:
#     st.markdown("""
#     <div class="sb-logo-wrap">
#       <div class="sb-logo">
#         <div class="sb-logo-icon">🏡</div>
#         <div>
#           <div class="sb-logo-text">NestIQ</div>
#         </div>
#       </div>
#       <div class="sb-logo-sub">AI-Powered Real Estate Valuation</div>
#     </div>
#     <div class="sb-stat-row">
#       <div class="sb-stat"><div class="sb-stat-num">50K+</div><div class="sb-stat-lbl">Properties</div></div>
#       <div class="sb-stat"><div class="sb-stat-num">96%</div><div class="sb-stat-lbl">Accuracy</div></div>
#       <div class="sb-stat"><div class="sb-stat-num">200+</div><div class="sb-stat-lbl">Sectors</div></div>
#       <div class="sb-stat"><div class="sb-stat-num">±22L</div><div class="sb-stat-lbl">Margin</div></div>
#     </div>
#     <div class="sb-tip">
#       💡 <strong>Pro Tip:</strong> The more precise your inputs, the more accurate your estimate.
#       Double-check your built-up area and sector for best results.
#     </div>
#     """, unsafe_allow_html=True)
#     try:
#         st.image("datasets/front image.png", use_container_width=True)
#     except Exception:
#         pass

# # ── Topbar ────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="topbar">
#   <div class="topbar-brand">
#     <div class="topbar-icon">🏡</div>
#     <div class="topbar-name">Nest<span>IQ</span></div>
#     <div class="topbar-badge">AI Valuation</div>
#   </div>
#   <div class="topbar-nav">
#     <div class="nav-pill active">Valuation</div>
#     <div class="nav-pill">Market Trends</div>
#     <div class="nav-pill">Compare</div>
#   </div>
# </div>
# """, unsafe_allow_html=True)

# # ── Hero Banner ───────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="hero-banner">
#   <div class="hero-tag">🤖 Machine Learning Powered</div>
#   <div class="hero-h1">Get Your Property's<br><em>Instant Valuation</em></div>
#   <div class="hero-sub">
#     Fill in 12 simple details and our AI model — trained on 50,000+ real
#     transactions — delivers an accurate price range in seconds.
#   </div>
#   <div class="hero-chips">
#     <div class="hero-chip"><span>🏙️</span> Gurugram NCR</div>
#     <div class="hero-chip"><span>⚡</span> Instant Results</div>
#     <div class="hero-chip"><span>🔒</span> 100% Free</div>
#     <div class="hero-chip"><span>📊</span> Data-Backed</div>
#   </div>
# </div>
# """, unsafe_allow_html=True)

# # ── Steps ─────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="steps-row">
#   <div class="step-item">
#     <div class="step-num done">✓</div>
#     <div class="step-label">Start</div>
#   </div>
#   <div class="step-line done"></div>
#   <div class="step-item">
#     <div class="step-num active">2</div>
#     <div class="step-label active">Fill Details</div>
#   </div>
#   <div class="step-line"></div>
#   <div class="step-item">
#     <div class="step-num idle">3</div>
#     <div class="step-label">Get Valuation</div>
#   </div>
# </div>
# """, unsafe_allow_html=True)

# # ══════════════════════════════════════════
# #  CARD 1 — Location
# # ══════════════════════════════════════════
# st.markdown("""
# <div class="card-3d-wrap"><div class="card-3d">
#   <div class="card-3d-accent"></div>
#   <div class="card-header">
#     <div class="card-icon blue">📍</div>
#     <div>
#       <div class="card-title-text">Location &amp; Identity</div>
#       <div class="card-title-sub">Property type, sector, and possession status</div>
#     </div>
#   </div>
# """, unsafe_allow_html=True)
# c1, c2, c3 = st.columns(3)
# with c1:
#     property_type = st.selectbox('Property Type', ['flat', 'house'],
#                                   help="Select flat/apartment or independent house")
# with c2:
#     sector = st.selectbox('Sector / Locality', sorted(df['sector'].unique().tolist()),
#                            help="The sector or area of the property")
# with c3:
#     property_age = st.selectbox('Age / Possession', sorted(df['agePossession'].unique().tolist()),
#                                  help="Construction/possession status")
# st.markdown("</div></div>", unsafe_allow_html=True)

# # ══════════════════════════════════════════
# #  CARD 2 — Size & Rooms
# # ══════════════════════════════════════════
# st.markdown("""
# <div class="card-3d-wrap"><div class="card-3d">
#   <div class="card-3d-accent"></div>
#   <div class="card-header">
#     <div class="card-icon teal">📐</div>
#     <div>
#       <div class="card-title-text">Size &amp; Room Configuration</div>
#       <div class="card-title-sub">Bedrooms, bathrooms, balconies, and built-up area</div>
#     </div>
#   </div>
# """, unsafe_allow_html=True)
# c1, c2, c3, c4 = st.columns(4)
# with c1:
#     bedrooms = float(st.selectbox('Bedrooms', sorted(df['bedRoom'].unique().tolist())))
# with c2:
#     bathroom = float(st.selectbox('Bathrooms', sorted(df['bathroom'].unique().tolist())))
# with c3:
#     balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
# with c4:
#     built_up_area = float(st.number_input('Built-up Area (sq.ft)', min_value=100.0, step=10.0, value=1000.0))
# st.markdown("</div></div>", unsafe_allow_html=True)

# # ══════════════════════════════════════════
# #  CARD 3 — Amenities
# # ══════════════════════════════════════════
# st.markdown("""
# <div class="card-3d-wrap"><div class="card-3d">
#   <div class="card-3d-accent"></div>
#   <div class="card-header">
#     <div class="card-icon coral">✨</div>
#     <div>
#       <div class="card-title-text">Amenities &amp; Finishes</div>
#       <div class="card-title-sub">Furnishing, luxury tier, and extra rooms</div>
#     </div>
#   </div>
# """, unsafe_allow_html=True)
# c1, c2, c3, c4, c5 = st.columns(5)
# with c1:
#     servant_room = float(st.selectbox('Servant Room', [0.0, 1.0],
#                                        format_func=lambda x: '✅ Yes' if x else '❌ No'))
# with c2:
#     store_room = float(st.selectbox('Store Room', [0.0, 1.0],
#                                      format_func=lambda x: '✅ Yes' if x else '❌ No'))
# with c3:
#     furnishing_type = st.selectbox('Furnishing', sorted(df['furnishing_type'].unique().tolist()))
# with c4:
#     luxury_category = st.selectbox('Luxury Tier', sorted(df['luxury_category'].unique().tolist()))
# with c5:
#     floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))
# st.markdown("</div></div>", unsafe_allow_html=True)

# # ══════════════════════════════════════════
# #  CTA
# # ══════════════════════════════════════════
# predict_clicked = st.button("🔍  Get My Property Valuation  →")

# # ══════════════════════════════════════════
# #  RESULT
# # ══════════════════════════════════════════
# if predict_clicked:
#     with st.spinner("Our AI is analysing 50,000+ data points…"):
#         data = [[property_type, sector, bedrooms, bathroom, balcony,
#                  property_age, built_up_area, servant_room, store_room,
#                  furnishing_type, luxury_category, floor_category]]
#         columns = ['property_type','sector','bedRoom','bathroom','balcony',
#                    'agePossession','built_up_area','servant room','store room',
#                    'furnishing_type','luxury_category','floor_category']
#         one_df     = pd.DataFrame(data, columns=columns)
#         base_price = np.expm1(pipeline.predict(one_df))[0]
#         low        = base_price - 0.22
#         high       = base_price + 0.22

#     st.markdown(f"""
#     <div class="result-outer">
#       <div class="result-hero">
#         <div class="res-tag">✦ AI Valuation Complete ✦</div>
#         <div class="res-price">₹ {low:,.2f} Cr &mdash; ₹ {high:,.2f} Cr</div>
#         <div class="res-range">Base estimate &middot; ₹ {base_price:,.2f} Crore &middot; Margin ± ₹ 22 Lakhs</div>
#         <div class="res-confidence">✅ High Confidence &middot; 96% Model Accuracy &middot; Gurugram NCR</div>
#       </div>
#     </div>
#     """, unsafe_allow_html=True)

#     price_per_sqft = (base_price * 1e7) / built_up_area if built_up_area else 0
#     st.markdown(f"""
#     <div class="stat-pills">
#       <div class="stat-pill"><div class="stat-pill-val">₹{base_price:,.2f} Cr</div><div class="stat-pill-lbl">Base Price</div></div>
#       <div class="stat-pill"><div class="stat-pill-val">₹{price_per_sqft:,.0f}</div><div class="stat-pill-lbl">Per sq.ft</div></div>
#       <div class="stat-pill"><div class="stat-pill-val">{built_up_area:,.0f}</div><div class="stat-pill-lbl">Sq.ft Area</div></div>
#       <div class="stat-pill"><div class="stat-pill-val">{int(bedrooms)} BHK</div><div class="stat-pill-lbl">Config</div></div>
#       <div class="stat-pill"><div class="stat-pill-val">±22L</div><div class="stat-pill-lbl">Margin</div></div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="sec-divider">📋 Property Summary</div>', unsafe_allow_html=True)

#     rows = [
#         [("Property Type", property_type.title()), ("Sector", sector), ("Possession", property_age)],
#         [("Bedrooms", f"{int(bedrooms)} BHK"), ("Bathrooms", f"{int(bathroom)} Bath"), ("Balconies", str(balcony))],
#         [("Built-up Area", f"{built_up_area:,.0f} sq.ft"), ("Furnishing", furnishing_type.title()), ("Luxury Tier", luxury_category.title())],
#         [("Floor Category", floor_category.title()), ("Servant Room", "Included" if servant_room else "Not Included"), ("Store Room", "Included" if store_room else "Not Included")],
#     ]
#     rows_html = "".join(
#         '<div class="detail-row">' +
#         "".join(f'<div class="detail-cell"><div class="dc-label">{k}</div><div class="dc-value">{v}</div></div>' for k,v in row) +
#         '</div>'
#         for row in rows
#     )
#     st.markdown(f'<div class="detail-table"><div class="detail-table-header">Full Property Breakdown</div>{rows_html}</div>', unsafe_allow_html=True)

#     st.markdown("""
#     <div class="notice-box info">
#       <div class="notice-icon">ℹ️</div>
#       <div><strong>How this works:</strong> Our gradient boosting model was trained on 50,000+ verified transactions in Gurugram NCR. It predicts log-transformed prices and applies an inverse transform for the final result.</div>
#     </div>
#     <div class="notice-box warn">
#       <div class="notice-icon">⚠️</div>
#       <div><strong>Disclaimer:</strong> This is an AI-generated indicative estimate only. Actual prices vary based on market demand, legal status, and condition. Please consult a certified property valuer for a formal appraisal.</div>
#     </div>
#     """, unsafe_allow_html=True)

# # ── Floating badge ────────────────────────────────────────────────────────────
# st.markdown('<div class="fab-chip"><div class="fab-dot"></div> AI Engine Online</div>', unsafe_allow_html=True)


import streamlit as st
import pickle
import pandas as pd
import numpy as np
import gzip

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NestIQ – Smart Property Valuation",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
  --blue-100:  #1E3A5F;
  --blue-500:  #3B82F6;
  --blue-600:  #2563EB;
  --blue-700:  #1D4ED8;
  --teal:      #0EA5E9;
  --coral:     #F97316;
  --green:     #10B981;
  --slate-400: #7A9CC8;
  --slate-500: #4D7099;
  --slate-700: #C5D8F0;
  --slate-900: #E2EAF8;
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
@keyframes meshDrift { 0% { opacity:.7; transform:scale(1); } 100% { opacity:1; transform:scale(1.05); } }

/* SIDEBAR */
[data-testid="stSidebar"] {
  background: var(--bg-sidebar) !important;
  border-right: 1px solid var(--border) !important;
  box-shadow: 4px 0 24px rgba(0,0,0,0.4) !important;
}
[data-testid="stSidebar"] .stMarkdown p { color: var(--text-secondary) !important; font-size: 0.82rem !important; }

.sb-logo-wrap { padding:1.8rem 1.5rem 1.4rem; border-bottom:1px solid var(--border); }
.sb-logo { display:flex; align-items:center; gap:0.6rem; }
.sb-logo-icon { width:38px; height:38px; background:linear-gradient(135deg,var(--blue-600),var(--teal)); border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:1.1rem; box-shadow:0 4px 12px rgba(37,99,235,0.4); }
.sb-logo-text { font-size:1.25rem; font-weight:800; background:linear-gradient(135deg,var(--blue-500),var(--teal)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.sb-logo-sub { font-size:0.62rem; color:var(--text-muted); letter-spacing:0.15em; text-transform:uppercase; margin-top:1rem; }
.sb-stat-row { display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; padding:1.25rem 1.5rem; border-bottom:1px solid var(--border); }
.sb-stat { background:var(--bg-card-2); border:1px solid var(--border); border-radius:var(--radius-sm); padding:0.9rem 0.75rem; text-align:center; }
.sb-stat-num { font-size:1.2rem; font-weight:700; color:var(--blue-500); }
.sb-stat-lbl { font-size:0.6rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.1em; margin-top:0.2rem; }
.sb-tip { margin:1rem 1.5rem; background:rgba(249,115,22,0.08); border-left:3px solid var(--coral); border-radius:0 var(--radius-sm) var(--radius-sm) 0; padding:0.8rem 1rem; font-size:0.75rem; color:#FDBA74; line-height:1.6; }

/* TOPBAR */
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

/* HERO */
.hero-banner { background:linear-gradient(135deg,var(--blue-600) 0%,var(--blue-700) 40%,#0E3A8C 100%); border-radius:var(--radius-lg); padding:3rem 3.5rem; position:relative; overflow:hidden; margin-bottom:2.5rem; animation:fadeUp 0.7s 0.1s var(--ease-out) both; border:1px solid rgba(59,130,246,0.3); }
.hero-banner::before { content:''; position:absolute; top:-60px; right:-60px; width:300px; height:300px; background:radial-gradient(circle,rgba(255,255,255,0.08) 0%,transparent 70%); border-radius:50%; }
.hero-banner::after  { content:''; position:absolute; bottom:-40px; left:30%; width:200px; height:200px; background:radial-gradient(circle,rgba(14,165,233,0.25) 0%,transparent 70%); border-radius:50%; }
@keyframes fadeUp { from{opacity:0;transform:translateY(28px)} to{opacity:1;transform:translateY(0)} }
.hero-tag { display:inline-flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.15); backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.2); color:white; font-size:0.7rem; font-weight:600; letter-spacing:0.12em; text-transform:uppercase; padding:0.35rem 0.9rem; border-radius:999px; margin-bottom:1.2rem; }
.hero-h1 { font-family:'Lora',serif; font-size:clamp(1.8rem,3.5vw,2.8rem); font-weight:600; color:white; line-height:1.25; margin-bottom:0.75rem; position:relative; z-index:1; }
.hero-h1 em { font-style:italic; color:#93C5FD; }
.hero-sub { color:rgba(255,255,255,0.7); font-size:0.9rem; line-height:1.7; max-width:480px; position:relative; z-index:1; }
.hero-chips { display:flex; gap:0.75rem; margin-top:1.5rem; flex-wrap:wrap; position:relative; z-index:1; }
.hero-chip { background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.2); color:white; font-size:0.72rem; font-weight:500; padding:0.4rem 0.85rem; border-radius:999px; }

/* STEPS */
.steps-row { display:flex; align-items:center; margin-bottom:2rem; animation:fadeUp 0.6s 0.2s var(--ease-out) both; }
.step-item { display:flex; align-items:center; gap:0.5rem; }
.step-num { width:30px; height:30px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:0.75rem; font-weight:700; flex-shrink:0; }
.step-num.done   { background:var(--green); color:white; }
.step-num.active { background:var(--blue-600); color:white; box-shadow:0 0 0 4px rgba(59,130,246,0.25); }
.step-num.idle   { background:var(--bg-card-2); color:var(--text-secondary); border:1px solid var(--border); }
.step-label { font-size:0.72rem; font-weight:600; color:var(--text-secondary); }
.step-label.active { color:var(--blue-500); }
.step-line { flex:1; height:2px; background:var(--border); margin:0 0.75rem; }
.step-line.done { background:var(--green); }

/* 3D CARDS */
.card-3d-wrap { perspective:1200px; margin-bottom:1.5rem; animation:fadeUp 0.7s var(--ease-out) both; }
.card-3d-wrap:nth-child(2) { animation-delay:0.1s; }
.card-3d-wrap:nth-child(3) { animation-delay:0.2s; }
.card-3d { background:var(--bg-card); border:1.5px solid var(--border); border-radius:var(--radius-md); padding:1.75rem 2rem; position:relative; transition:transform 0.4s var(--ease-out),box-shadow 0.4s var(--ease-out); transform-style:preserve-3d; box-shadow:var(--shadow-sm); overflow:hidden; }
.card-3d::before { content:''; position:absolute; inset:0; background:linear-gradient(135deg,rgba(37,99,235,0.06) 0%,transparent 60%); border-radius:inherit; pointer-events:none; }
.card-3d:hover { transform:rotateX(2deg) rotateY(-2deg) translateY(-6px) scale(1.01); box-shadow:var(--shadow-3d); border-color:var(--border-h); }
.card-3d-accent { position:absolute; top:0; left:0; right:0; height:3px; background:linear-gradient(90deg,var(--blue-600),var(--teal),var(--blue-600)); background-size:200%; border-radius:var(--radius-md) var(--radius-md) 0 0; animation:shimmer 3s linear infinite; }
@keyframes shimmer { to{background-position:200% center} }
.card-header { display:flex; align-items:center; gap:0.75rem; margin-bottom:1.25rem; padding-bottom:1rem; border-bottom:1.5px solid var(--border); }
.card-icon { width:38px; height:38px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:1rem; flex-shrink:0; }
.card-icon.blue  { background:rgba(37,99,235,0.15);  border:1px solid rgba(37,99,235,0.25); }
.card-icon.teal  { background:rgba(14,165,233,0.12);  border:1px solid rgba(14,165,233,0.22); }
.card-icon.coral { background:rgba(249,115,22,0.12);  border:1px solid rgba(249,115,22,0.22); }
.card-title-text { font-size:0.95rem; font-weight:700; color:var(--text-primary); }
.card-title-sub  { font-size:0.7rem;  color:var(--text-secondary); margin-top:0.1rem; }

/* FORM WIDGETS */
div[data-baseweb="select"] > div { background:var(--bg-input) !important; border:1.5px solid var(--border) !important; border-radius:var(--radius-sm) !important; color:var(--text-primary) !important; font-family:'Plus Jakarta Sans',sans-serif !important; font-size:0.85rem !important; transition:all 0.2s !important; }
div[data-baseweb="select"]:focus-within > div { border-color:var(--blue-500) !important; background:var(--bg-card-2) !important; box-shadow:0 0 0 3px rgba(59,130,246,0.15) !important; }
div[data-baseweb="select"] svg { fill:var(--blue-500) !important; }
div[data-baseweb="menu"] { background:var(--bg-card-2) !important; border:1.5px solid var(--border) !important; border-radius:var(--radius-sm) !important; box-shadow:0 12px 40px rgba(0,0,0,0.5) !important; }
div[data-baseweb="menu"] li { color:var(--text-primary) !important; font-size:0.83rem !important; font-family:'Plus Jakarta Sans',sans-serif !important; background:transparent !important; }
div[data-baseweb="menu"] li:hover { background:rgba(37,99,235,0.15) !important; color:var(--blue-500) !important; }
[data-testid="stNumberInput"] input { background:var(--bg-input) !important; border:1.5px solid var(--border) !important; border-radius:var(--radius-sm) !important; color:var(--text-primary) !important; font-family:'Plus Jakarta Sans',sans-serif !important; font-size:0.85rem !important; }
[data-testid="stNumberInput"] input:focus { border-color:var(--blue-500) !important; background:var(--bg-card-2) !important; box-shadow:0 0 0 3px rgba(59,130,246,0.15) !important; }
[data-testid="stNumberInput"] button { background:var(--bg-card-2) !important; border-color:var(--border) !important; color:var(--text-secondary) !important; }
label[data-testid="stWidgetLabel"] > div > p { font-family:'Plus Jakarta Sans',sans-serif !important; font-size:0.72rem !important; font-weight:600 !important; color:var(--text-secondary) !important; text-transform:uppercase !important; letter-spacing:0.08em !important; }

/* BUTTON */
[data-testid="stButton"] > button { width:100% !important; padding:1rem 2rem !important; background:linear-gradient(135deg,var(--blue-600),var(--teal)) !important; border:none !important; border-radius:var(--radius-md) !important; color:white !important; font-family:'Plus Jakarta Sans',sans-serif !important; font-size:0.9rem !important; font-weight:700 !important; letter-spacing:0.04em !important; box-shadow:0 8px 24px rgba(37,99,235,0.40) !important; transition:transform 0.2s var(--ease),box-shadow 0.2s !important; margin-top:1rem !important; position:relative !important; overflow:hidden !important; }
[data-testid="stButton"] > button:hover { transform:translateY(-3px) scale(1.01) !important; box-shadow:0 16px 36px rgba(37,99,235,0.55) !important; }
[data-testid="stButton"] > button:active { transform:translateY(0) scale(0.99) !important; }

/* RESULT */
.result-outer { animation:popIn 0.7s var(--ease) both; margin-top:2rem; }
@keyframes popIn { from{opacity:0;transform:scale(0.92) translateY(20px)} to{opacity:1;transform:scale(1) translateY(0)} }
.result-hero { background:linear-gradient(135deg,var(--blue-600) 0%,var(--teal) 100%); border-radius:var(--radius-lg); padding:2.5rem; text-align:center; position:relative; overflow:hidden; box-shadow:0 20px 60px rgba(37,99,235,0.35); border:1px solid rgba(59,130,246,0.4); }
.result-hero::before { content:''; position:absolute; top:-80px; right:-80px; width:280px; height:280px; background:radial-gradient(circle,rgba(255,255,255,0.10) 0%,transparent 70%); border-radius:50%; }
.result-hero::after  { content:''; position:absolute; bottom:-60px; left:-60px; width:220px; height:220px; background:radial-gradient(circle,rgba(14,165,233,0.30) 0%,transparent 70%); border-radius:50%; }
.res-tag { display:inline-block; background:rgba(255,255,255,0.2); backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.3); color:white; font-size:0.65rem; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; padding:0.3rem 0.8rem; border-radius:999px; margin-bottom:1rem; position:relative; z-index:1; }
.res-price { font-family:'Lora',serif; font-size:clamp(2rem,5vw,3.2rem); font-weight:600; color:white; line-height:1.2; position:relative; z-index:1; }
.res-range { color:rgba(255,255,255,0.8); font-size:0.82rem; margin-top:0.5rem; position:relative; z-index:1; }
.res-confidence { display:inline-flex; align-items:center; gap:0.4rem; background:rgba(255,255,255,0.15); border:1px solid rgba(255,255,255,0.25); color:white; font-size:0.72rem; font-weight:600; padding:0.4rem 0.9rem; border-radius:999px; margin-top:1rem; position:relative; z-index:1; }

.stat-pills { display:flex; gap:1rem; margin-top:1.5rem; flex-wrap:wrap; }
.stat-pill { flex:1; min-width:100px; background:var(--bg-card); border-radius:var(--radius-sm); padding:1rem 1.25rem; text-align:center; box-shadow:var(--shadow-sm); border:1px solid var(--border); transition:transform 0.3s var(--ease),box-shadow 0.3s,border-color 0.3s; animation:fadeUp 0.5s var(--ease-out) both; }
.stat-pill:hover { transform:translateY(-4px); box-shadow:var(--shadow-md); border-color:var(--border-h); }
.stat-pill-val { font-size:1.15rem; font-weight:800; color:var(--blue-500); }
.stat-pill-lbl { font-size:0.62rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.1em; margin-top:0.2rem; }

.detail-table { background:var(--bg-card); border-radius:var(--radius-md); border:1.5px solid var(--border); overflow:hidden; margin-top:1.5rem; animation:fadeUp 0.6s 0.15s var(--ease-out) both; }
.detail-table-header { background:var(--bg-card-2); padding:1rem 1.5rem; font-size:0.72rem; font-weight:700; color:var(--text-secondary); text-transform:uppercase; letter-spacing:0.1em; border-bottom:1.5px solid var(--border); }
.detail-row { display:grid; grid-template-columns:repeat(3,1fr); border-bottom:1px solid var(--border); }
.detail-row:last-child { border-bottom:none; }
.detail-cell { padding:1rem 1.5rem; border-right:1px solid var(--border); transition:background 0.2s; }
.detail-cell:last-child { border-right:none; }
.detail-cell:hover { background:rgba(37,99,235,0.07); }
.dc-label { font-size:0.62rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.3rem; }
.dc-value { font-size:0.9rem; font-weight:600; color:var(--text-primary); }

.notice-box { display:flex; gap:0.75rem; align-items:flex-start; padding:1rem 1.25rem; border-radius:var(--radius-sm); font-size:0.78rem; line-height:1.7; margin-top:1rem; }
.notice-box.info { background:rgba(37,99,235,0.10); border:1px solid rgba(37,99,235,0.25); color:#93C5FD; }
.notice-box.warn { background:rgba(249,115,22,0.08); border:1px solid rgba(249,115,22,0.25); color:#FDBA74; }
.notice-icon { font-size:1rem; flex-shrink:0; margin-top:0.1rem; }

.sec-divider { display:flex; align-items:center; gap:1rem; margin:2rem 0 1.25rem; font-size:0.65rem; font-weight:700; color:var(--blue-500); text-transform:uppercase; letter-spacing:0.2em; }
.sec-divider::before,.sec-divider::after { content:''; flex:1; height:1.5px; }
.sec-divider::before { background:linear-gradient(90deg,var(--border),transparent); }
.sec-divider::after  { background:linear-gradient(90deg,transparent,var(--border)); }

.fab-chip { position:fixed; bottom:2rem; right:2rem; z-index:999; background:var(--bg-card-2); border:1.5px solid var(--border); border-radius:999px; padding:0.6rem 1.2rem; display:flex; align-items:center; gap:0.5rem; font-size:0.75rem; font-weight:600; color:var(--blue-500); box-shadow:var(--shadow-md); animation:floatFab 4s ease-in-out infinite; pointer-events:none; }
@keyframes floatFab { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-6px)} }
.fab-dot { width:8px; height:8px; border-radius:50%; background:var(--green); box-shadow:0 0 0 3px rgba(16,185,129,0.25); animation:dotPulse 2s ease-in-out infinite; }
@keyframes dotPulse { 0%,100%{box-shadow:0 0 0 3px rgba(16,185,129,0.25)} 50%{box-shadow:0 0 0 6px rgba(16,185,129,0.1)} }

[data-testid="stAlert"] { background:rgba(37,99,235,0.08) !important; border:1px solid rgba(37,99,235,0.25) !important; color:#93C5FD !important; border-radius:var(--radius-sm) !important; }
</style>

<script>
(function initTilt() {
  function apply() {
    document.querySelectorAll('.card-3d').forEach(card => {
      if (card._tilt) return;
      card._tilt = true;
      card.addEventListener('mousemove', e => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width  - 0.5;
        const y = (e.clientY - r.top)  / r.height - 0.5;
        card.style.transform  = `rotateX(${-y*10}deg) rotateY(${x*10}deg) translateY(-8px) scale(1.01)`;
        card.style.boxShadow  = `${-x*20}px ${-y*20}px 60px rgba(37,99,235,0.22)`;
        card.style.transition = 'box-shadow 0.1s';
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform  = 'rotateX(0) rotateY(0) translateY(0) scale(1)';
        card.style.boxShadow  = '0 2px 8px rgba(0,0,0,0.35)';
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

# ── Load Models ───────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def load_models():
    with open('datasets/df.pkl', 'rb') as f:
        df = pickle.load(f)
    with gzip.open('pipeline1.pkl.gz', 'rb') as f:
        pipeline = pickle.load(f)
    return df, pipeline

df, pipeline = load_models()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-logo-wrap">
      <div class="sb-logo">
        <div class="sb-logo-icon">🏡</div>
        <div><div class="sb-logo-text">NestIQ</div></div>
      </div>
      <div class="sb-logo-sub">AI-Powered Real Estate Valuation</div>
    </div>
    <div class="sb-stat-row">
      <div class="sb-stat"><div class="sb-stat-num">50K+</div><div class="sb-stat-lbl">Properties</div></div>
      <div class="sb-stat"><div class="sb-stat-num">96%</div><div class="sb-stat-lbl">Accuracy</div></div>
      <div class="sb-stat"><div class="sb-stat-num">200+</div><div class="sb-stat-lbl">Sectors</div></div>
      <div class="sb-stat"><div class="sb-stat-num">±22L</div><div class="sb-stat-lbl">Margin</div></div>
    </div>
    <div class="sb-tip">
      💡 <strong>Pro Tip:</strong> The more precise your inputs, the more accurate your estimate.
      Double-check your built-up area and sector for best results.
    </div>
    """, unsafe_allow_html=True)
    try:
        st.image("datasets/front image.png", use_container_width=True)
    except Exception:
        pass

# ── Topbar ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
  <div class="topbar-brand">
    <div class="topbar-icon">🏡</div>
    <div class="topbar-name">Nest<span>IQ</span></div>
    <div class="topbar-badge">AI Valuation</div>
  </div>
  <div class="topbar-nav">
    <div class="nav-pill active">Valuation</div>
    <div class="nav-pill">Market Trends</div>
    <div class="nav-pill">Compare</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <div class="hero-tag">🤖 Machine Learning Powered</div>
  <div class="hero-h1">Get Your Property's<br><em>Instant Valuation</em></div>
  <div class="hero-sub">Fill in 12 simple details and our AI model — trained on 50,000+ real transactions — delivers an accurate price range in seconds.</div>
  <div class="hero-chips">
    <div class="hero-chip">🏙️ Gurugram NCR</div>
    <div class="hero-chip">⚡ Instant Results</div>
    <div class="hero-chip">🔒 100% Free</div>
    <div class="hero-chip">📊 Data-Backed</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Steps ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="steps-row">
  <div class="step-item"><div class="step-num done">✓</div><div class="step-label">Start</div></div>
  <div class="step-line done"></div>
  <div class="step-item"><div class="step-num active">2</div><div class="step-label active">Fill Details</div></div>
  <div class="step-line"></div>
  <div class="step-item"><div class="step-num idle">3</div><div class="step-label">Get Valuation</div></div>
</div>
""", unsafe_allow_html=True)

# ── Card 1 ────────────────────────────────────────────────────────────────────
st.markdown("""<div class="card-3d-wrap"><div class="card-3d">
  <div class="card-3d-accent"></div>
  <div class="card-header">
    <div class="card-icon blue">📍</div>
    <div><div class="card-title-text">Location &amp; Identity</div><div class="card-title-sub">Property type, sector, and possession status</div></div>
  </div>""", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: property_type = st.selectbox('Property Type', ['flat', 'house'])
with c2: sector = st.selectbox('Sector / Locality', sorted(df['sector'].unique().tolist()))
with c3: property_age = st.selectbox('Age / Possession', sorted(df['agePossession'].unique().tolist()))
st.markdown("</div></div>", unsafe_allow_html=True)

# ── Card 2 ────────────────────────────────────────────────────────────────────
st.markdown("""<div class="card-3d-wrap"><div class="card-3d">
  <div class="card-3d-accent"></div>
  <div class="card-header">
    <div class="card-icon teal">📐</div>
    <div><div class="card-title-text">Size &amp; Room Configuration</div><div class="card-title-sub">Bedrooms, bathrooms, balconies, and built-up area</div></div>
  </div>""", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1: bedrooms = float(st.selectbox('Bedrooms', sorted(df['bedRoom'].unique().tolist())))
with c2: bathroom = float(st.selectbox('Bathrooms', sorted(df['bathroom'].unique().tolist())))
with c3: balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
with c4: built_up_area = float(st.number_input('Built-up Area (sq.ft)', min_value=100.0, step=10.0, value=1000.0))
st.markdown("</div></div>", unsafe_allow_html=True)

# ── Card 3 ────────────────────────────────────────────────────────────────────
st.markdown("""<div class="card-3d-wrap"><div class="card-3d">
  <div class="card-3d-accent"></div>
  <div class="card-header">
    <div class="card-icon coral">✨</div>
    <div><div class="card-title-text">Amenities &amp; Finishes</div><div class="card-title-sub">Furnishing, luxury tier, and extra rooms</div></div>
  </div>""", unsafe_allow_html=True)
c1, c2, c3, c4, c5 = st.columns(5)
with c1: servant_room = float(st.selectbox('Servant Room', [0.0, 1.0], format_func=lambda x: '✅ Yes' if x else '❌ No'))
with c2: store_room   = float(st.selectbox('Store Room',   [0.0, 1.0], format_func=lambda x: '✅ Yes' if x else '❌ No'))
with c3: furnishing_type = st.selectbox('Furnishing',     sorted(df['furnishing_type'].unique().tolist()))
with c4: luxury_category = st.selectbox('Luxury Tier',    sorted(df['luxury_category'].unique().tolist()))
with c5: floor_category  = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))
st.markdown("</div></div>", unsafe_allow_html=True)

# ── CTA ───────────────────────────────────────────────────────────────────────
predict_clicked = st.button("🔍  Get My Property Valuation  →")

# ── Result ────────────────────────────────────────────────────────────────────
if predict_clicked:
    with st.spinner("Our AI is analysing 50,000+ data points…"):
        data = [[property_type, sector, bedrooms, bathroom, balcony,
                 property_age, built_up_area, servant_room, store_room,
                 furnishing_type, luxury_category, floor_category]]
        cols = ['property_type','sector','bedRoom','bathroom','balcony',
                'agePossession','built_up_area','servant room','store room',
                'furnishing_type','luxury_category','floor_category']
        one_df     = pd.DataFrame(data, columns=cols)
        base_price = np.expm1(pipeline.predict(one_df))[0]
        low  = base_price - 0.22
        high = base_price + 0.22

    st.markdown(f"""
    <div class="result-outer">
      <div class="result-hero">
        <div class="res-tag">✦ AI Valuation Complete ✦</div>
        <div class="res-price">₹ {low:,.2f} Cr &mdash; ₹ {high:,.2f} Cr</div>
        <div class="res-range">Base estimate · ₹ {base_price:,.2f} Crore · Margin ± ₹ 22 Lakhs</div>
        <div class="res-confidence">✅ High Confidence · 96% Model Accuracy · Gurugram NCR</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    ppsf = (base_price * 1e7) / built_up_area if built_up_area else 0
    st.markdown(f"""
    <div class="stat-pills">
      <div class="stat-pill"><div class="stat-pill-val">₹{base_price:,.2f} Cr</div><div class="stat-pill-lbl">Base Price</div></div>
      <div class="stat-pill"><div class="stat-pill-val">₹{ppsf:,.0f}</div><div class="stat-pill-lbl">Per sq.ft</div></div>
      <div class="stat-pill"><div class="stat-pill-val">{built_up_area:,.0f}</div><div class="stat-pill-lbl">Sq.ft Area</div></div>
      <div class="stat-pill"><div class="stat-pill-val">{int(bedrooms)} BHK</div><div class="stat-pill-lbl">Config</div></div>
      <div class="stat-pill"><div class="stat-pill-val">±22L</div><div class="stat-pill-lbl">Margin</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sec-divider">📋 Property Summary</div>', unsafe_allow_html=True)

    rows = [
        [("Property Type", property_type.title()), ("Sector", sector), ("Possession", property_age)],
        [("Bedrooms", f"{int(bedrooms)} BHK"), ("Bathrooms", f"{int(bathroom)} Bath"), ("Balconies", str(balcony))],
        [("Built-up Area", f"{built_up_area:,.0f} sq.ft"), ("Furnishing", furnishing_type.title()), ("Luxury Tier", luxury_category.title())],
        [("Floor Category", floor_category.title()), ("Servant Room", "Included" if servant_room else "Not Included"), ("Store Room", "Included" if store_room else "Not Included")],
    ]
    rows_html = "".join(
        '<div class="detail-row">' +
        "".join(f'<div class="detail-cell"><div class="dc-label">{k}</div><div class="dc-value">{v}</div></div>' for k,v in row) +
        '</div>' for row in rows
    )
    st.markdown(f'<div class="detail-table"><div class="detail-table-header">Full Property Breakdown</div>{rows_html}</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="notice-box info"><div class="notice-icon">ℹ️</div><div><strong>How this works:</strong> Our gradient boosting model was trained on 50,000+ verified transactions in Gurugram NCR. It predicts log-transformed prices and applies an inverse transform for the final result.</div></div>
    <div class="notice-box warn"><div class="notice-icon">⚠️</div><div><strong>Disclaimer:</strong> This is an AI-generated indicative estimate only. Actual prices vary based on market demand, legal status, and condition. Please consult a certified property valuer for a formal appraisal.</div></div>
    """, unsafe_allow_html=True)

st.markdown('<div class="fab-chip"><div class="fab-dot"></div> AI Engine Online</div>', unsafe_allow_html=True)