# import streamlit as st

# # Set Streamlit Page Configuration
# st.set_page_config(
#     page_title="Gurgaon Real Estate Analytics App",
#     page_icon="🏙️",
#     layout="wide"
# )

# # Centered Title and Introduction with Animation Effect
# st.markdown(
#     """
#     <div style="text-align: center;">
#         <h1 style="color:#004080; font-size: 48px; font-family: 'Arial', sans-serif; animation: fadeIn 2s;">🏡 Gurgaon Real Estate Analytics App</h1>
#         <h3 style="color:#008080; font-size: 30px; animation: fadeIn 3s;">🔍 Your AI-Powered Guide to Smart Real Estate Decisions</h3>
#         <p style="color:grey; font-size:18px; font-style: italic;">Explore property recommendations, market trends, and price predictions, all in one place. Stay ahead of the curve in Gurgaon real estate!</p>
#     </div>
#     <style>
#         @keyframes fadeIn {
#             from { opacity: 0; }
#             to { opacity: 1; }
#         }
#     </style>
#     """, unsafe_allow_html=True
# )

# # 🖼️ Add an Attractive Image
# st.image("datasets/front image.png", width=800, caption="Start your real estate journey in Gurgaon today!")

# # 📌 Introduction with Icons for Sections
# st.markdown(
#     """
#     ---
#     ## 📢 **Why Use This App?**
#     In the rapidly growing **Gurgaon real estate market**, making informed decisions is crucial.  
#     Whether you are a **homebuyer**, **investor**, or **analyst**, this tool empowers you to:
#     - 🏠 **Find the best properties** based on advanced recommendation algorithms.
#     - 📊 **Analyze real estate trends** with interactive visualizations.
#     - 🤖 **Predict property prices** using AI and machine learning models.
#     - 🛠️ **Customize recommendations** by adjusting similarity weights.

#     🌟 With this app, you will have an all-in-one solution for making smarter real estate decisions!

#     ---
#     """
# )

# # 🎯 **Guide Users on How to Use with Bullet Points and Clear Steps**
# st.markdown(
#     """
#     ## 🚀 **How to Get Started?**
#     Getting started is easy! Here's what you need to do:
    
#     1. **Navigate through the sidebar** to explore different modules.
#     2. **Choose the feature that suits your needs:**
#        - 🏡 **Apartment Recommendation**: Personalized property suggestions based on location and facilities.
#        - 📈 **Market Analytics**: View Gurgaon’s real estate trends through interactive visualizations.
#        - 💰 **Price Prediction**: Estimate future property prices using AI-driven models.
#     3. **Interact with the tool** to get valuable insights instantly and make informed decisions!

#     🎯 All tools are powered by advanced AI algorithms and real-time data, making your decision-making easier and faster.
    
#     ---
#     """
# )

# # 🏆 **Highlight Features with Icons and Bulleted List**
# st.markdown(
#     """
#     ## 🌟 **Key Features at a Glance**
#     - ✅ **AI-Powered Apartment Recommendations**  
#       - Get personalized suggestions based on location, pricing, and facilities.  
#     - ✅ **Data-Driven Market Insights**  
#       - View real estate trends through interactive visualizations.  
#     - ✅ **Smart Price Prediction**  
#       - Estimate future property prices with machine learning models.  
#     - ✅ **Customizable Search and Filters**  
#       - Adjust similarity weights to fine-tune property recommendations.

#     🎯 These features are designed to help you make smarter real estate decisions with confidence!

#     ---
#     """
# )

# # 📌 Sidebar Call-to-Action with Additional Information
# st.sidebar.success("👈 **Select a module from the sidebar to get started!** \nDiscover recommendations, insights, and predictions.")

# # 🔥 **Final Call to Action with Smaller Image**
# st.markdown(
#     """
#     <div style="text-align: center;">
#         <h3 style="color:#004080; font-size: 28px; font-family: 'Arial', sans-serif; font-weight: bold; animation: fadeIn 3s;">🎯 Ready to Explore? Select a module from the sidebar! 🎯</h3>
#     </div>
#     """, unsafe_allow_html=True
# )

# # Display the image using Streamlit's st.image() instead of HTML, and add a call-to-action
# st.image("datasets/banner image.jpg", width=700, caption="Explore Gurgaon Real Estate with Confidence!")

# # Add additional footer with contact information or additional CTA
# st.markdown(
#     """
#     ---
#     ## 📬 **Contact Us**
#     Have questions or need support? Reach out to us at:
#     - 📧 Email: **abhaysingh71711@gmail.com**

#     --- 
#     ## 🔗 **Follow Us on Social Media**  
#     Stay updated with the latest new projects, trends, and data science listings:
#     - 📱 **Instagram**: @ezatom_
#     - 💼 **LinkedIn**: https://www.linkedin.com/in/abhay-singh-050a5b293/
#     - 🐦 **Twitter**: https://x.com/AbhaySingh71711

#     """
# )




import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NestIQ – Gurgaon Real Estate Intelligence",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Load real data ─────────────────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def load_data():
    try:
        return pd.read_csv("datasets/data_viz1.csv")
    except Exception:
        return None

df = load_data()

if df is not None:
    total_props  = f"{len(df):,}"
    num_sectors  = str(df['sector'].nunique())            if 'sector'        in df.columns else "—"
    avg_price    = f"₹{df['price'].mean():.2f} Cr"        if 'price'         in df.columns else "—"
    avg_area     = f"{df['built_up_area'].mean():,.0f} sq.ft" if 'built_up_area' in df.columns else "—"
    max_price    = f"₹{df['price'].max():.1f} Cr"         if 'price'         in df.columns else "—"
    min_price    = f"₹{df['price'].min():.2f} Cr"         if 'price'         in df.columns else "—"
    avg_ppsf     = f"₹{df['price_per_sqft'].mean():,.0f}" if 'price_per_sqft' in df.columns else "—"
    top_sector   = df.groupby('sector')['price'].mean().idxmax() if 'sector' in df.columns else "—"
    flat_count   = int((df['property_type'] == 'flat').sum())    if 'property_type' in df.columns else 0
    house_count  = int((df['property_type'] == 'house').sum())   if 'property_type' in df.columns else 0
else:
    total_props = num_sectors = avg_price = avg_area = "—"
    max_price   = min_price   = avg_ppsf  = top_sector = "—"
    flat_count  = house_count = 0

# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR — native Streamlit widgets ONLY (no st.markdown with HTML)
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.title("🏙️ NestIQ")
    st.caption("GURGAON REAL ESTATE INTELLIGENCE")
    st.divider()
    st.subheader("Navigation")
    st.markdown("🏠 **Home** ← you are here")
    st.markdown("🤖 Apartment Recommender")
    st.markdown("📊 Analytics Dashboard")
    st.markdown("💰 Price Predictor")
    st.divider()
    if df is not None:
        st.subheader("Dataset Quick Stats")
        st.metric("Total Listings", total_props)
        st.metric("Sectors Covered", num_sectors)
        st.metric("Avg Price", avg_price)
        st.metric("Avg Built-up Area", avg_area)
    st.divider()
    st.caption("💡 Select a module from the pages to begin your analysis.")

# ══════════════════════════════════════════════════════════════════════════════
#  MAIN PAGE CSS  (only injected into main area, never sidebar)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&display=swap');

:root {
  --bg:    #080E1A;
  --card:  #0F1E35;
  --card2: #112040;
  --bdr:   rgba(59,130,246,0.18);
  --bdrh:  rgba(59,130,246,0.38);
  --t1:    #E2EAF8;
  --t2:    #7A9CC8;
  --t3:    #3D5A80;
  --b4:    #60A5FA;
  --b5:    #3B82F6;
  --b6:    #2563EB;
  --teal:  #0EA5E9;
  --coral: #F97316;
  --grn:   #10B981;
  --gold:  #F59E0B;
  --purp:  #8B5CF6;
  --s3d:   0 20px 60px rgba(37,99,235,0.22);
  --rmd:   16px;
  --rlg:   24px;
  --eout:  cubic-bezier(0.16,1,0.3,1);
  --ease:  cubic-bezier(0.34,1.56,0.64,1);
}

*, *::before, *::after { box-sizing: border-box; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"], .main {
  background: var(--bg) !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  color: var(--t1) !important;
  overflow-x: hidden !important;
}

/* hide streamlit chrome */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }

.block-container {
  padding: 0 !important;
  max-width: 100% !important;
}

/* sidebar dark */
[data-testid="stSidebar"] {
  background: #0C1526 !important;
  border-right: 1px solid var(--bdr) !important;
}
[data-testid="stSidebar"] * {
  color: var(--t2) !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
  color: var(--t1) !important;
}
[data-testid="stSidebar"] [data-testid="stMetric"] {
  background: var(--card2) !important;
  border: 1px solid var(--bdr) !important;
  border-radius: 8px !important;
  padding: 0.6rem 0.8rem !important;
  margin-bottom: 0.4rem !important;
}
[data-testid="stSidebar"] [data-testid="stMetricValue"] {
  color: var(--b4) !important;
  font-size: 1rem !important;
}
[data-testid="stSidebar"] [data-testid="stMetricLabel"] {
  color: var(--t3) !important;
  font-size: 0.65rem !important;
}

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--card); }
::-webkit-scrollbar-thumb { background: var(--b6); border-radius: 3px; }

/* ── HERO ── */
.hero {
  position: relative;
  min-height: 95vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: 0 3rem 2rem;
}
.hero-grid {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(59,130,246,0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(59,130,246,0.06) 1px, transparent 1px);
  background-size: 50px 50px;
  mask-image: radial-gradient(ellipse 90% 80% at 50% 50%, black 30%, transparent 80%);
  animation: gridpan 25s linear infinite;
  pointer-events: none;
}
@keyframes gridpan { to { background-position: 50px 50px; } }

.orb { position: absolute; border-radius: 50%; filter: blur(80px); pointer-events: none; }
.o1  { width:600px; height:600px; top:-200px; right:-150px; background:rgba(37,99,235,0.09); animation:oa 14s ease-in-out infinite; }
.o2  { width:500px; height:500px; bottom:-200px; left:-150px; background:rgba(14,165,233,0.07); animation:ob 18s ease-in-out infinite; }
.o3  { width:300px; height:300px; top:40%; left:40%; background:rgba(139,92,246,0.05); animation:oc 10s ease-in-out infinite; }
@keyframes oa { 0%,100%{transform:translate(0,0)} 50%{transform:translate(-30px,40px)} }
@keyframes ob { 0%,100%{transform:translate(0,0)} 50%{transform:translate(40px,-30px)} }
@keyframes oc { 0%,100%{transform:translate(0,0) scale(1)} 50%{transform:translate(-20px,20px) scale(1.08)} }

.pt { position: absolute; border-radius: 50%; background: rgba(59,130,246,0.45); pointer-events: none; animation: ptf linear infinite; }
@keyframes ptf {
  0%   { transform: translateY(100vh) scale(0); opacity: 0; }
  8%   { opacity: 0.9; }
  90%  { opacity: 0.3; }
  100% { transform: translateY(-10px) scale(1); opacity: 0; }
}

@keyframes fup { from{opacity:0;transform:translateY(22px)} to{opacity:1;transform:translateY(0)} }

.h-eyebrow {
  display: inline-flex; align-items: center; gap: 0.5rem;
  background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.25);
  color: var(--b4); font-size: 0.7rem; font-weight: 700;
  letter-spacing: 0.2em; text-transform: uppercase;
  padding: 0.4rem 1rem; border-radius: 999px;
  margin-bottom: 1.5rem; position: relative; z-index: 2;
  animation: fup 0.8s var(--eout) both;
}
.h-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--teal); box-shadow: 0 0 8px var(--teal);
  animation: dp 2s ease-in-out infinite;
}
@keyframes dp { 0%,100%{box-shadow:0 0 4px var(--teal)} 50%{box-shadow:0 0 14px var(--teal),0 0 28px rgba(14,165,233,0.3)} }

.h-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(3rem, 7vw, 7rem);
  font-weight: 300; color: var(--t1);
  line-height: 1; text-align: center;
  position: relative; z-index: 2;
  animation: fup 0.8s 0.1s var(--eout) both;
}
.h-title em {
  font-style: italic;
  background: linear-gradient(135deg, var(--b4), var(--teal));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.h-title .bl { display: block; }

.h-sub {
  font-size: clamp(0.88rem, 1.5vw, 1rem); color: var(--t2);
  text-align: center; max-width: 540px; line-height: 1.8; margin-top: 1.4rem;
  position: relative; z-index: 2;
  animation: fup 0.8s 0.2s var(--eout) both;
}

.h-cta {
  display: flex; gap: 1rem; margin-top: 2.4rem;
  flex-wrap: wrap; justify-content: center;
  position: relative; z-index: 2;
  animation: fup 0.8s 0.3s var(--eout) both;
}
.btn-p {
  background: linear-gradient(135deg, var(--b6), var(--teal));
  color: white; font-size: 0.82rem; font-weight: 700;
  letter-spacing: 0.08em; text-transform: uppercase;
  padding: 0.85rem 2rem; border-radius: 999px; border: none; cursor: pointer;
  box-shadow: 0 8px 24px rgba(37,99,235,0.35);
  transition: all 0.3s var(--ease);
}
.btn-p:hover { transform: translateY(-3px); box-shadow: 0 14px 36px rgba(37,99,235,0.5); }
.btn-g {
  background: transparent; color: var(--t2); font-size: 0.82rem; font-weight: 600;
  padding: 0.85rem 2rem; border-radius: 999px; border: 1.5px solid var(--bdr); cursor: pointer;
  transition: all 0.3s;
}
.btn-g:hover { border-color: var(--bdrh); color: var(--t1); background: rgba(59,130,246,0.05); }

.sky { position: relative; z-index: 2; width: 100%; max-width: 900px; margin-top: 2.5rem; animation: fup 0.8s 0.4s var(--eout) both; }
.sky svg { width: 100%; height: auto; }

/* ── STATS STRIP ── */
.strip {
  width: 100%;
  background: linear-gradient(90deg, transparent, rgba(37,99,235,0.05), transparent);
  border-top: 1px solid var(--bdr); border-bottom: 1px solid var(--bdr);
  padding: 1.5rem 2rem; display: flex; justify-content: center; gap: 0; overflow-x: auto;
}
.si { text-align: center; padding: 0 3rem; position: relative; white-space: nowrap; }
.si + .si::before { content:''; position:absolute; left:0; top:15%; bottom:15%; width:1px; background:var(--bdr); }
.sn { font-family:'Cormorant Garamond',serif; font-size:2rem; font-weight:400; color:var(--b4); display:block; line-height:1; }
.sl { font-size:0.6rem; font-weight:700; color:var(--t3); text-transform:uppercase; letter-spacing:0.2em; margin-top:0.3rem; }

/* ── CONTENT ── */
.cw { max-width: 1260px; margin: 0 auto; padding: 0 3rem 6rem; }
.ey { font-size:0.62rem; font-weight:700; color:var(--b4); text-transform:uppercase; letter-spacing:0.25em; margin-bottom:0.5rem; }
.st { font-family:'Cormorant Garamond',serif; font-size:clamp(2rem,3.5vw,3rem); font-weight:400; color:var(--t1); line-height:1.2; margin-bottom:0.9rem; }
.st em { font-style:italic; color:var(--teal); }
.ss { font-size:0.88rem; color:var(--t2); line-height:1.8; max-width:560px; }

/* ── METRIC CARDS ── */
.mg { display:grid; grid-template-columns:repeat(4,1fr); gap:1.2rem; margin-top:2.5rem; }
.mc {
  background:var(--card); border:1.5px solid var(--bdr); border-radius:var(--rmd);
  padding:1.4rem 1.5rem; position:relative; overflow:hidden;
  transition:transform 0.35s var(--eout), box-shadow 0.35s, border-color 0.35s;
  animation:fup 0.5s var(--eout) both;
  transform-style: preserve-3d;
}
.mc::before { content:''; position:absolute; top:0; left:0; right:0; height:3px; border-radius:var(--rmd) var(--rmd) 0 0; }
.mc.a::before{background:linear-gradient(90deg,var(--b6),var(--teal))}
.mc.b::before{background:linear-gradient(90deg,var(--teal),var(--grn))}
.mc.c::before{background:linear-gradient(90deg,var(--coral),var(--gold))}
.mc.d::before{background:linear-gradient(90deg,var(--purp),var(--b5))}
.mc.e::before{background:linear-gradient(90deg,var(--grn),var(--teal))}
.mc.f::before{background:linear-gradient(90deg,var(--gold),var(--coral))}
.mc.g::before{background:linear-gradient(90deg,var(--b5),var(--purp))}
.mc.h::before{background:linear-gradient(90deg,var(--teal),var(--b4))}
.mc:hover { transform:translateY(-5px); box-shadow:var(--s3d); border-color:var(--bdrh); }
.mi { font-size:1.25rem; margin-bottom:0.5rem; }
.mv { font-family:'Cormorant Garamond',serif; font-size:1.5rem; font-weight:400; color:var(--t1); line-height:1.1; margin-bottom:0.2rem; word-break:break-word; }
.ml { font-size:0.6rem; font-weight:700; color:var(--t3); text-transform:uppercase; letter-spacing:0.14em; }

/* ── FEATURE CARDS ── */
.fg { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; margin-top:3rem; }
.fc {
  background:var(--card); border:1.5px solid var(--bdr); border-radius:var(--rlg);
  padding:2rem; position:relative; overflow:hidden;
  transition:transform 0.4s var(--eout), box-shadow 0.4s, border-color 0.4s;
  transform-style:preserve-3d; animation:fup 0.6s var(--eout) both;
}
.fc::before { content:''; position:absolute; top:0; left:0; right:0; height:3px; border-radius:var(--rlg) var(--rlg) 0 0; }
.fc.bl::before  { background:linear-gradient(90deg,var(--b6),var(--teal)); }
.fc.co::before  { background:linear-gradient(90deg,var(--coral),var(--gold)); }
.fc.pu::before  { background:linear-gradient(90deg,var(--purp),var(--b5)); }
.fc::after { content:''; position:absolute; inset:0; background:linear-gradient(135deg,rgba(37,99,235,0.04) 0%,transparent 60%); pointer-events:none; transition:opacity 0.4s; opacity:0; }
.fc:hover::after { opacity:1; }
.fc:hover { border-color:var(--bdrh); }
.fcg { position:absolute; width:200px; height:200px; border-radius:50%; filter:blur(60px); pointer-events:none; opacity:0; transition:opacity 0.4s; top:-60px; right:-60px; }
.fc.bl .fcg { background:rgba(37,99,235,0.14); }
.fc.co .fcg { background:rgba(249,115,22,0.11); }
.fc.pu .fcg { background:rgba(139,92,246,0.11); }
.fc:hover .fcg { opacity:1; }
.fiw { width:52px; height:52px; border-radius:13px; display:flex; align-items:center; justify-content:center; margin-bottom:1.3rem; position:relative; z-index:1; }
.fc.bl .fiw { background:rgba(37,99,235,0.15); border:1px solid rgba(37,99,235,0.25); }
.fc.co .fiw { background:rgba(249,115,22,0.12); border:1px solid rgba(249,115,22,0.22); }
.fc.pu .fiw { background:rgba(139,92,246,0.12); border:1px solid rgba(139,92,246,0.22); }
.fct { font-size:1.05rem; font-weight:700; color:var(--t1); margin-bottom:0.55rem; position:relative; z-index:1; }
.fcd { font-size:0.82rem; color:var(--t2); line-height:1.75; position:relative; z-index:1; margin-bottom:1.3rem; }
.ftr { display:flex; gap:0.5rem; flex-wrap:wrap; position:relative; z-index:1; }
.ftg { font-size:0.6rem; font-weight:600; letter-spacing:0.1em; padding:0.22rem 0.6rem; border-radius:999px; text-transform:uppercase; }
.fc.bl .ftg { background:rgba(37,99,235,0.1);  color:var(--b4); border:1px solid rgba(37,99,235,0.2); }
.fc.co .ftg { background:rgba(249,115,22,0.1); color:#FB923C;   border:1px solid rgba(249,115,22,0.2); }
.fc.pu .ftg { background:rgba(139,92,246,0.1); color:#A78BFA;   border:1px solid rgba(139,92,246,0.2); }
.far { display:inline-flex; align-items:center; gap:0.4rem; font-size:0.73rem; font-weight:700; color:var(--b4); text-transform:uppercase; letter-spacing:0.1em; margin-top:1.1rem; transition:gap 0.2s; position:relative; z-index:1; }
.fc:hover .far { gap:0.7rem; }

/* ── HOW IT WORKS ── */
.hg { display:grid; grid-template-columns:repeat(4,1fr); gap:1.4rem; margin-top:3rem; }
.hs {
  background:var(--card); border:1.5px solid var(--bdr); border-radius:var(--rmd);
  padding:1.7rem 1.4rem; text-align:center; position:relative;
  transition:transform 0.3s var(--eout), border-color 0.3s;
  animation:fup 0.5s var(--eout) both;
}
.hs:hover { transform:translateY(-5px); border-color:var(--bdrh); }
.hn { font-family:'Cormorant Garamond',serif; font-size:3rem; font-weight:300; line-height:1; margin-bottom:0.55rem; }
.hs.h1 .hn { color:rgba(59,130,246,0.28); }
.hs.h2 .hn { color:rgba(14,165,233,0.28); }
.hs.h3 .hn { color:rgba(16,185,129,0.28); }
.hs.h4 .hn { color:rgba(245,158,11,0.28); }
.hsi { font-size:1.4rem; margin-bottom:0.6rem; }
.hst { font-size:0.87rem; font-weight:700; color:var(--t1); margin-bottom:0.45rem; }
.hsd { font-size:0.74rem; color:var(--t2); line-height:1.7; }

/* ── TECH PILLS ── */
.tp { display:flex; flex-wrap:wrap; gap:0.7rem; margin-top:1.8rem; }
.tpi { display:flex; align-items:center; gap:0.5rem; background:var(--card); border:1px solid var(--bdr); border-radius:999px; padding:0.45rem 0.95rem; font-size:0.74rem; font-weight:600; color:var(--t2); transition:all 0.2s; }
.tpi:hover { border-color:var(--bdrh); color:var(--t1); background:var(--card2); }
.tpd { width:7px; height:7px; border-radius:50%; flex-shrink:0; }

/* ── FOOTER ── */
.ft { border-top:1px solid var(--bdr); margin-top:4rem; padding:3rem; text-align:center; }
.fl { font-family:'Cormorant Garamond',serif; font-size:2rem; font-weight:400; background:linear-gradient(135deg,var(--b4),var(--teal)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:0.4rem; }
.ftg2 { font-size:0.72rem; color:var(--t3); letter-spacing:0.15em; text-transform:uppercase; margin-bottom:2rem; }
.fc2 { display:flex; justify-content:center; gap:4rem; flex-wrap:wrap; margin-bottom:2rem; }
.fch { font-size:0.6rem; font-weight:700; color:var(--t3); text-transform:uppercase; letter-spacing:0.2em; margin-bottom:0.7rem; }
.fcb { font-size:0.8rem; color:var(--t2); line-height:2.1; }
.fdv { height:1px; background:var(--bdr); margin-bottom:2rem; }
.fcr { font-size:0.78rem; color:var(--t3); }
.fcr span { color:var(--b4); font-weight:600; }

/* ── FAB ── */
.fab { position:fixed; bottom:2rem; right:2rem; z-index:9999; background:var(--card2); border:1.5px solid var(--bdr); border-radius:999px; padding:0.55rem 1.1rem; display:flex; align-items:center; gap:0.5rem; font-size:0.73rem; font-weight:600; color:var(--b5); box-shadow:0 8px 30px rgba(0,0,0,0.45); animation:ff 4s ease-in-out infinite; pointer-events:none; }
@keyframes ff { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-6px)} }
.fbd { width:8px; height:8px; border-radius:50%; background:var(--grn); animation:fdp 2s ease-in-out infinite; }
@keyframes fdp { 0%,100%{box-shadow:0 0 0 3px rgba(16,185,129,0.25)} 50%{box-shadow:0 0 0 6px rgba(16,185,129,0.1)} }

@media(max-width:900px){
  .fg,.hg,.mg{grid-template-columns:1fr 1fr}
  .strip{flex-wrap:wrap}
  .si{padding:0.5rem 1.5rem}
  .fc2{gap:2rem}
}
@media(max-width:600px){
  .fg,.hg,.mg{grid-template-columns:1fr}
  .hero{padding:0 1.2rem 2rem}
  .cw{padding:0 1.2rem 4rem}
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-grid"></div>
  <div class="orb o1"></div>
  <div class="orb o2"></div>
  <div class="orb o3"></div>

  <div class="h-eyebrow"><span class="h-dot"></span>Gurgaon NCR &nbsp;·&nbsp; AI-Powered &nbsp;·&nbsp; Real-Time Data</div>

  <div class="h-title">
    <span class="bl">Smart Real Estate</span>
    <span class="bl"><em>Intelligence</em></span>
  </div>

  <p class="h-sub">
    Harness machine learning and data science to discover properties,
    predict prices, and decode market trends across Gurgaon's
    most sought-after sectors — all in one platform.
  </p>

  <div class="h-cta">
    <button class="btn-p">🚀 &nbsp;Explore the Platform</button>
    <button class="btn-g">📊 &nbsp;View Analytics</button>
  </div>

  <!-- SVG city skyline -->
  <div class="sky">
    <svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" style="overflow:visible">
      <defs>
        <linearGradient id="G1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1D4ED8" stop-opacity=".9"/><stop offset="100%" stop-color="#0F1E35"/></linearGradient>
        <linearGradient id="G2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0EA5E9" stop-opacity=".85"/><stop offset="100%" stop-color="#080E1A"/></linearGradient>
        <linearGradient id="G3" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2563EB" stop-opacity=".88"/><stop offset="100%" stop-color="#0C1526"/></linearGradient>
        <filter id="GL"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
        <style>
          .B{animation:BR 1.2s cubic-bezier(.16,1,.3,1) both}
          @keyframes BR{from{transform:translateY(50px);opacity:0}to{transform:translateY(0);opacity:1}}
          .W{animation:WB 3s ease-in-out infinite}
          @keyframes WB{0%,88%,100%{opacity:.55}93%{opacity:.07}}
        </style>
      </defs>

      <g class="B" style="animation-delay:.05s"><rect x="20" y="165" width="52" height="75" fill="url(#G1)"/><rect x="30" y="153" width="32" height="14" fill="url(#G3)"/><rect x="42" y="142" width="10" height="13" fill="#2563EB" opacity=".7"/>
        <rect class="W" x="27" y="173" width="9" height="6" rx="1" fill="#93C5FD" style="animation-delay:.3s"/>
        <rect class="W" x="41" y="173" width="9" height="6" rx="1" fill="#60A5FA" style="animation-delay:1.4s"/>
        <rect class="W" x="55" y="173" width="9" height="6" rx="1" fill="#93C5FD" style="animation-delay:.8s"/>
        <rect class="W" x="27" y="186" width="9" height="6" rx="1" fill="#60A5FA" style="animation-delay:2s"/>
        <rect class="W" x="55" y="186" width="9" height="6" rx="1" fill="#93C5FD" style="animation-delay:.5s"/>
        <rect class="W" x="41" y="199" width="9" height="6" rx="1" fill="#60A5FA" style="animation-delay:1.7s"/>
        <rect class="W" x="55" y="210" width="9" height="6" rx="1" fill="#93C5FD" style="animation-delay:1.1s"/>
      </g>

      <g class="B" style="animation-delay:.10s"><rect x="88" y="72" width="62" height="168" fill="url(#G3)"/><rect x="102" y="60" width="34" height="14" fill="url(#G1)"/><rect x="114" y="48" width="10" height="14" fill="#2563EB" opacity=".8"/><circle cx="119" cy="45" r="3.5" fill="#3B82F6" filter="url(#GL)"/>
        <rect class="W" x="96" y="82" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:.6s"/>
        <rect class="W" x="113" y="82" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:1.8s"/>
        <rect class="W" x="130" y="82" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:.2s"/>
        <rect class="W" x="96" y="99" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:2.2s"/>
        <rect class="W" x="130" y="99" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:.9s"/>
        <rect class="W" x="96" y="116" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:1.5s"/>
        <rect class="W" x="113" y="116" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:.4s"/>
        <rect class="W" x="130" y="116" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:2.5s"/>
        <rect class="W" x="96" y="133" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:1s"/>
        <rect class="W" x="130" y="150" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:.3s"/>
        <rect class="W" x="113" y="167" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:2.1s"/>
        <rect class="W" x="96" y="184" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:.5s"/>
      </g>

      <g class="B" style="animation-delay:.15s"><rect x="167" y="128" width="56" height="112" fill="url(#G2)"/><rect x="180" y="116" width="30" height="14" fill="url(#G3)"/>
        <rect class="W" x="174" y="138" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:.4s"/>
        <rect class="W" x="190" y="138" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:1.6s"/>
        <rect class="W" x="206" y="138" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:.9s"/>
        <rect class="W" x="174" y="153" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:2s"/>
        <rect class="W" x="206" y="167" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:.2s"/>
        <rect class="W" x="190" y="182" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:1.3s"/>
        <rect class="W" x="174" y="197" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:.7s"/>
      </g>

      <g class="B" style="animation-delay:.20s"><rect x="248" y="22" width="72" height="218" fill="url(#G3)"/><rect x="264" y="10" width="40" height="14" fill="url(#G2)"/><rect x="278" y="0" width="12" height="12" fill="#3B82F6"/><circle cx="284" cy="-3" r="4" fill="#60A5FA" filter="url(#GL)"/>
        <rect class="W" x="256" y="32" width="13" height="9" rx="1" fill="#93C5FD" style="animation-delay:.3s"/>
        <rect class="W" x="276" y="32" width="13" height="9" rx="1" fill="#60A5FA" style="animation-delay:1.7s"/>
        <rect class="W" x="296" y="32" width="13" height="9" rx="1" fill="#93C5FD" style="animation-delay:.8s"/>
        <rect class="W" x="256" y="50" width="13" height="9" rx="1" fill="#60A5FA" style="animation-delay:2.1s"/>
        <rect class="W" x="296" y="50" width="13" height="9" rx="1" fill="#93C5FD" style="animation-delay:.4s"/>
        <rect class="W" x="256" y="68" width="13" height="9" rx="1" fill="#93C5FD" style="animation-delay:1.5s"/>
        <rect class="W" x="276" y="68" width="13" height="9" rx="1" fill="#60A5FA" style="animation-delay:.6s"/>
        <rect class="W" x="256" y="86" width="13" height="9" rx="1" fill="#60A5FA" style="animation-delay:2.4s"/>
        <rect class="W" x="276" y="104" width="13" height="9" rx="1" fill="#93C5FD" style="animation-delay:1.1s"/>
        <rect class="W" x="296" y="122" width="13" height="9" rx="1" fill="#60A5FA" style="animation-delay:.9s"/>
        <rect class="W" x="256" y="140" width="13" height="9" rx="1" fill="#93C5FD" style="animation-delay:2.8s"/>
        <rect class="W" x="276" y="158" width="13" height="9" rx="1" fill="#60A5FA" style="animation-delay:1.4s"/>
        <rect class="W" x="256" y="176" width="13" height="9" rx="1" fill="#93C5FD" style="animation-delay:.7s"/>
        <rect class="W" x="296" y="194" width="13" height="9" rx="1" fill="#60A5FA" style="animation-delay:1.9s"/>
      </g>

      <g class="B" style="animation-delay:.25s"><rect x="340" y="88" width="68" height="152" fill="url(#G1)"/><rect x="354" y="74" width="40" height="16" fill="url(#G3)"/><rect x="368" y="62" width="12" height="14" fill="#1D4ED8"/><circle cx="374" cy="59" r="3.5" fill="#60A5FA" filter="url(#GL)"/>
        <rect class="W" x="348" y="98" width="12" height="8" rx="1" fill="#60A5FA" style="animation-delay:.6s"/>
        <rect class="W" x="367" y="98" width="12" height="8" rx="1" fill="#93C5FD" style="animation-delay:1.9s"/>
        <rect class="W" x="386" y="115" width="12" height="8" rx="1" fill="#60A5FA" style="animation-delay:.2s"/>
        <rect class="W" x="348" y="132" width="12" height="8" rx="1" fill="#93C5FD" style="animation-delay:2.3s"/>
        <rect class="W" x="367" y="149" width="12" height="8" rx="1" fill="#60A5FA" style="animation-delay:1.1s"/>
        <rect class="W" x="386" y="166" width="12" height="8" rx="1" fill="#93C5FD" style="animation-delay:.5s"/>
        <rect class="W" x="348" y="183" width="12" height="8" rx="1" fill="#60A5FA" style="animation-delay:2.7s"/>
        <rect class="W" x="367" y="200" width="12" height="8" rx="1" fill="#93C5FD" style="animation-delay:1.4s"/>
      </g>

      <g class="B" style="animation-delay:.30s"><rect x="430" y="38" width="76" height="202" fill="url(#G2)"/><rect x="446" y="25" width="44" height="15" fill="url(#G3)"/><rect x="460" y="13" width="14" height="14" fill="#0EA5E9"/><circle cx="467" cy="10" r="4" fill="#38BDF8" filter="url(#GL)"/>
        <rect class="W" x="438" y="48" width="13" height="9" rx="1" fill="#BAE6FD" style="animation-delay:.4s"/>
        <rect class="W" x="458" y="48" width="13" height="9" rx="1" fill="#BAE6FD" style="animation-delay:1.8s"/>
        <rect class="W" x="478" y="66" width="13" height="9" rx="1" fill="#BAE6FD" style="animation-delay:.9s"/>
        <rect class="W" x="438" y="84" width="13" height="9" rx="1" fill="#BAE6FD" style="animation-delay:2.2s"/>
        <rect class="W" x="458" y="102" width="13" height="9" rx="1" fill="#BAE6FD" style="animation-delay:.3s"/>
        <rect class="W" x="478" y="120" width="13" height="9" rx="1" fill="#BAE6FD" style="animation-delay:1.5s"/>
        <rect class="W" x="438" y="138" width="13" height="9" rx="1" fill="#BAE6FD" style="animation-delay:.7s"/>
        <rect class="W" x="458" y="156" width="13" height="9" rx="1" fill="#BAE6FD" style="animation-delay:2.5s"/>
        <rect class="W" x="478" y="174" width="13" height="9" rx="1" fill="#BAE6FD" style="animation-delay:1.1s"/>
        <rect class="W" x="438" y="192" width="13" height="9" rx="1" fill="#BAE6FD" style="animation-delay:.5s"/>
      </g>

      <g class="B" style="animation-delay:.35s"><rect x="528" y="100" width="60" height="140" fill="url(#G3)"/><rect x="540" y="88" width="36" height="14" fill="url(#G1)"/>
        <rect class="W" x="536" y="110" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:1.2s"/>
        <rect class="W" x="554" y="128" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:.3s"/>
        <rect class="W" x="572" y="146" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:2.1s"/>
        <rect class="W" x="536" y="164" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:.8s"/>
        <rect class="W" x="554" y="182" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:1.6s"/>
        <rect class="W" x="572" y="200" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:.5s"/>
      </g>

      <g class="B" style="animation-delay:.40s"><rect x="610" y="62" width="68" height="178" fill="url(#G1)"/><rect x="624" y="50" width="40" height="14" fill="url(#G2)"/><rect x="638" y="38" width="12" height="14" fill="#1D4ED8"/><circle cx="644" cy="35" r="3.5" fill="#60A5FA" filter="url(#GL)"/>
        <rect class="W" x="618" y="72" width="12" height="8" rx="1" fill="#60A5FA" style="animation-delay:.7s"/>
        <rect class="W" x="637" y="89" width="12" height="8" rx="1" fill="#93C5FD" style="animation-delay:2s"/>
        <rect class="W" x="656" y="106" width="12" height="8" rx="1" fill="#60A5FA" style="animation-delay:.3s"/>
        <rect class="W" x="618" y="123" width="12" height="8" rx="1" fill="#93C5FD" style="animation-delay:1.5s"/>
        <rect class="W" x="637" y="140" width="12" height="8" rx="1" fill="#60A5FA" style="animation-delay:.9s"/>
        <rect class="W" x="656" y="157" width="12" height="8" rx="1" fill="#93C5FD" style="animation-delay:2.3s"/>
        <rect class="W" x="618" y="174" width="12" height="8" rx="1" fill="#60A5FA" style="animation-delay:.5s"/>
        <rect class="W" x="637" y="191" width="12" height="8" rx="1" fill="#93C5FD" style="animation-delay:2.8s"/>
      </g>

      <g class="B" style="animation-delay:.45s"><rect x="700" y="140" width="58" height="100" fill="url(#G2)"/><rect x="713" y="128" width="32" height="14" fill="url(#G3)"/>
        <rect class="W" x="708" y="150" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:1.3s"/>
        <rect class="W" x="724" y="167" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:.4s"/>
        <rect class="W" x="740" y="184" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:2.1s"/>
        <rect class="W" x="708" y="201" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:.8s"/>
        <rect class="W" x="740" y="218" width="10" height="7" rx="1" fill="#BAE6FD" style="animation-delay:1.7s"/>
      </g>

      <g class="B" style="animation-delay:.50s"><rect x="778" y="112" width="54" height="128" fill="url(#G3)"/><rect x="790" y="100" width="30" height="14" fill="url(#G1)"/><rect x="799" y="89" width="12" height="13" fill="#2563EB"/><circle cx="805" cy="86" r="3" fill="#3B82F6" filter="url(#GL)"/>
        <rect class="W" x="786" y="122" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:.5s"/>
        <rect class="W" x="803" y="139" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:1.8s"/>
        <rect class="W" x="820" y="156" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:.2s"/>
        <rect class="W" x="786" y="173" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:2.2s"/>
        <rect class="W" x="803" y="190" width="11" height="8" rx="1" fill="#93C5FD" style="animation-delay:.9s"/>
        <rect class="W" x="820" y="207" width="11" height="8" rx="1" fill="#60A5FA" style="animation-delay:1.4s"/>
      </g>

      <rect x="0" y="240" width="900" height="20" fill="rgba(8,14,26,.97)"/>
      <line x1="0" y1="240" x2="900" y2="240" stroke="rgba(59,130,246,.28)" stroke-width="1.5"/>
      <line x1="40"  y1="250" x2="100" y2="250" stroke="rgba(59,130,246,.1)" stroke-width="1.5" stroke-dasharray="8 6"/>
      <line x1="190" y1="250" x2="280" y2="250" stroke="rgba(59,130,246,.1)" stroke-width="1.5" stroke-dasharray="8 6"/>
      <line x1="360" y1="250" x2="490" y2="250" stroke="rgba(59,130,246,.1)" stroke-width="1.5" stroke-dasharray="8 6"/>
      <line x1="580" y1="250" x2="690" y2="250" stroke="rgba(59,130,246,.1)" stroke-width="1.5" stroke-dasharray="8 6"/>
      <line x1="760" y1="250" x2="870" y2="250" stroke="rgba(59,130,246,.1)" stroke-width="1.5" stroke-dasharray="8 6"/>
    </svg>
  </div>
</div>


""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  STATS STRIP  — real data
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="strip">
  <div class="si"><span class="sn">{total_props}</span><div class="sl">Properties</div></div>
  <div class="si"><span class="sn">{num_sectors}</span><div class="sl">Sectors</div></div>
  <div class="si"><span class="sn">{avg_price}</span><div class="sl">Avg Price</div></div>
  <div class="si"><span class="sn">{avg_area}</span><div class="sl">Avg Area</div></div>
  <div class="si"><span class="sn">96%</span><div class="sl">Model Accuracy</div></div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
#  CONTENT WRAP
# ─────────────────────────────────────────────────────────────────────────────
st.markdown('<div class="cw">', unsafe_allow_html=True)

# ── METRIC CARDS ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="margin-top:4rem">
  <div class="ey">Live Dataset Snapshot</div>
  <div class="st">What the <em>Data Says</em></div>
  <div class="ss">All figures computed directly from the Gurgaon NCR property dataset.</div>
</div>
<div class="mg">
  <div class="mc a" style="animation-delay:0s">   <div class="mi">🏠</div><div class="mv">{total_props}</div><div class="ml">Total Listings</div></div>
  <div class="mc b" style="animation-delay:.06s"> <div class="mi">📍</div><div class="mv">{num_sectors}</div><div class="ml">Sectors Covered</div></div>
  <div class="mc c" style="animation-delay:.12s"> <div class="mi">💰</div><div class="mv">{avg_price}</div><div class="ml">Average Price</div></div>
  <div class="mc d" style="animation-delay:.18s"> <div class="mi">📏</div><div class="mv">{avg_area}</div><div class="ml">Avg Built-up Area</div></div>
  <div class="mc e" style="animation-delay:.24s"> <div class="mi">📈</div><div class="mv">{max_price}</div><div class="ml">Highest Price</div></div>
  <div class="mc f" style="animation-delay:.30s"> <div class="mi">📉</div><div class="mv">{min_price}</div><div class="ml">Lowest Price</div></div>
  <div class="mc g" style="animation-delay:.36s"> <div class="mi">💹</div><div class="mv">{avg_ppsf}/sqft</div><div class="ml">Avg Price per Sqft</div></div>
  <div class="mc h" style="animation-delay:.42s"> <div class="mi">🏆</div><div class="mv" style="font-size:1.05rem">{top_sector}</div><div class="ml">Top Value Sector</div></div>
</div>
""", unsafe_allow_html=True)

# ── FEATURE CARDS ─────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="margin-top:5rem">
  <div class="ey">Platform Modules</div>
  <div class="st">Three <em>AI-Powered</em> Tools</div>
  <div class="ss">Each module runs its own trained model on the same {total_props}-property verified dataset.</div>
</div>
<div class="fg">

  <div class="fc bl" style="animation-delay:0s">
    <div class="fcg"></div>
    <div class="fiw">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
        <path d="M3 9.5L12 3L21 9.5V20C21 20.55 20.55 21 20 21H15V15H9V21H4C3.45 21 3 20.55 3 20V9.5Z" stroke="#60A5FA" stroke-width="1.8" stroke-linejoin="round"/>
      </svg>
    </div>
    <div class="fct">Apartment Recommender</div>
    <div class="fcd">Enter any apartment and get the top-5 most similar properties using weighted cosine similarity across 3 feature matrices — facilities, pricing, and geo-location. Also supports radius-based search across all {num_sectors} sectors.</div>
    <div class="ftr">
      <div class="ftg">Cosine Similarity</div>
      <div class="ftg">3 Feature Matrices</div>
      <div class="ftg">Radius Search</div>
    </div>
    <div class="far">Open module &nbsp;→</div>
  </div>

  <div class="fc co" style="animation-delay:.1s">
    <div class="fcg"></div>
    <div class="fiw">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" stroke="#FB923C" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <div class="fct">Analytics Dashboard</div>
    <div class="fcd">Explore geo-spatial price maps across {num_sectors} sectors, 3D scatter plots of price vs area vs BHK, animated price trend timelines, heatmaps, and violin plots — all built live on the {total_props}-row dataset.</div>
    <div class="ftr">
      <div class="ftg">Geo Maps</div>
      <div class="ftg">3D Scatter</div>
      <div class="ftg">Heatmaps</div>
      <div class="ftg">Animated</div>
    </div>
    <div class="far">Open module &nbsp;→</div>
  </div>

  <div class="fc pu" style="animation-delay:.2s">
    <div class="fcg"></div>
    <div class="fiw">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
        <circle cx="12" cy="12" r="3" stroke="#A78BFA" stroke-width="1.8"/>
        <path d="M12 1V3M12 21V23M4.22 4.22L5.64 5.64M18.36 18.36L19.78 19.78M1 12H3M21 12H23M4.22 19.78L5.64 18.36M18.36 5.64L19.78 4.22" stroke="#A78BFA" stroke-width="1.8" stroke-linecap="round"/>
      </svg>
    </div>
    <div class="fct">Price Predictor</div>
    <div class="fcd">Enter 12 property parameters — sector, BHK, area, furnishing, luxury tier, floor, age — and receive an AI-generated valuation range. Gradient-boosting model with log-price transformation trained on {total_props} transactions. Margin: ±₹22 Lakhs.</div>
    <div class="ftr">
      <div class="ftg">Gradient Boosting</div>
      <div class="ftg">12 Parameters</div>
      <div class="ftg">Log Transform</div>
      <div class="ftg">±₹22L Margin</div>
    </div>
    <div class="far">Open module &nbsp;→</div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── HOW IT WORKS ──────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-top:5rem">
  <div class="ey">Under the Hood</div>
  <div class="st">How It <em>Works</em></div>
  <div class="ss">From raw property listings to production-ready AI — a four-stage pipeline.</div>
</div>
<div class="hg">
  <div class="hs h1" style="animation-delay:0s">
    <div class="hn">01</div><div class="hsi">🗂️</div>
    <div class="hst">Data Collection &amp; Cleaning</div>
    <div class="hsd">Property listings collected and curated from Gurgaon NCR. Null handling, outlier removal, and sector normalisation applied across 15+ raw features.</div>
  </div>
  <div class="hs h2" style="animation-delay:.08s">
    <div class="hn">02</div><div class="hsi">⚙️</div>
    <div class="hst">Feature Engineering</div>
    <div class="hsd">Geo-coordinate extraction, luxury scoring, floor category binning, furnishing encoding, and log-price transformation for model stability.</div>
  </div>
  <div class="hs h3" style="animation-delay:.16s">
    <div class="hn">03</div><div class="hsi">🤖</div>
    <div class="hst">Model Training</div>
    <div class="hsd">Three specialised models: gradient-boosting regressor for price, TF-IDF cosine similarity for recommendations, and Plotly for analytics visualisation.</div>
  </div>
  <div class="hs h4" style="animation-delay:.24s">
    <div class="hn">04</div><div class="hsi">📱</div>
    <div class="hst">Deployed on Streamlit</div>
    <div class="hsd">All models serialised via Pickle/Gzip and served through a multi-page Streamlit app — predictions and recommendations in under 200ms per query.</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── TECH STACK ────────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-top:5rem">
  <div class="ey">Built With</div>
  <div class="st">Technology <em>Stack</em></div>
  <div class="ss">Production-grade open-source tools — from data ingestion to live deployment.</div>
  <div class="tp">
    <div class="tpi"><div class="tpd" style="background:#3B82F6"></div>Python 3.11</div>
    <div class="tpi"><div class="tpd" style="background:#F97316"></div>Streamlit</div>
    <div class="tpi"><div class="tpd" style="background:#10B981"></div>Scikit-learn</div>
    <div class="tpi"><div class="tpd" style="background:#8B5CF6"></div>Gradient Boosting</div>
    <div class="tpi"><div class="tpd" style="background:#0EA5E9"></div>Pandas &amp; NumPy</div>
    <div class="tpi"><div class="tpd" style="background:#F59E0B"></div>Plotly Express</div>
    <div class="tpi"><div class="tpd" style="background:#EC4899"></div>Cosine Similarity</div>
    <div class="tpi"><div class="tpd" style="background:#60A5FA"></div>Seaborn &amp; Matplotlib</div>
    <div class="tpi"><div class="tpd" style="background:#34D399"></div>Pickle / Gzip</div>
    <div class="tpi"><div class="tpd" style="background:#A78BFA"></div>Geographic APIs</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="ft">
  <div class="fl">NestIQ</div>
  <div class="ftg2">Gurgaon Real Estate Intelligence Platform</div>
  <div class="fc2">
    <div>
      <div class="fch">Modules</div>
      <div class="fcb">🤖 Apartment Recommender<br>📊 Analytics Dashboard<br>💰 Price Predictor</div>
    </div>
    <div>
      <div class="fch">Dataset</div>
      <div class="fcb">📍 {num_sectors} Sectors · Gurgaon NCR<br>🏢 {total_props} Property Listings<br>📐 Avg Area: {avg_area}</div>
    </div>
    <div>
      <div class="fch">Stack</div>
      <div class="fcb">🐍 Python · Streamlit<br>🤖 Scikit-learn · Gradient Boost<br>📊 Plotly · Seaborn</div>
    </div>
  </div>
  <div class="fdv"></div>
  <div class="fcr">Crafted with ❤️ and code by &nbsp;<span>Naman Nanda</span>&nbsp;·&nbsp; NestIQ Real Estate Intelligence &nbsp;·&nbsp; Gurgaon NCR &nbsp;·&nbsp; 2025</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── FAB ───────────────────────────────────────────────────────────────────────
st.markdown('<div class="fab"><div class="fbd"></div> AI Engine Online</div>', unsafe_allow_html=True)