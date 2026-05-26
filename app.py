# app.py
import streamlit as st

import requests


SHEETDB_API_URL = "https://sheetdb.io/api/v1/nplizugnr02po"

# Page Config
st.set_page_config(
    page_title="PromptPolish - Coming Soon",
    page_icon="✨",
    layout="wide"
)

# -------------------------------------------------------
# 🔗 ONLINE IMAGE LINKS — replace these with your own URLs
# -------------------------------------------------------
BG_IMAGE_URL = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80"
# ^ Dark blue tech/space background from Unsplash (free to use)

BANNER_IMAGE_URL = "https://raw.githubusercontent.com/y-india/images_hosting/refs/heads/main/pp_banner.png"

# -------------------------------------------------------

st.markdown("""
<style>
    .block-container {
        padding-top: 0rem;
    }

    [data-testid="stImage"] {
        margin-top: -50px;
    }
</style>
""", unsafe_allow_html=True)

# Custom CSS — background + all styles
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{BG_IMAGE_URL}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}

.main {{
    text-align: center;
}}

.big-title {{
    font-size: 70px;
    font-weight: 900;
    color: #11d9ff;
    text-align: center;
    margin-top: 10px;
    text-shadow: 0px 0px 15px rgba(0,255,255,0.4);
    -webkit-text-stroke: 2px #003344;
}}

.coming {{
    font-size: 60px;
    font-weight: bold;
    color: white;
    width: 100%;
    text-align: center;
    margin-top: 10px;
    text-shadow:
        0 0 5px #ffffff,
        0 0 10px #11d9ff,
        0 0 20px #11d9ff,
        0 0 40px #11d9ff;
    animation: glow 1s ease-in-out infinite alternate;
}}

@keyframes glow {{
    from {{
        text-shadow:
            0 0 5px #ffffff,
            0 0 10px #11d9ff,
            0 0 20px #11d9ff;
    }}
    to {{
        text-shadow:
            0 0 10px #ffffff,
            0 0 20px #11d9ff,
            0 0 40px #11d9ff,
            0 0 60px #11d9ff;
    }}
}}

.message {{
    font-size: 32px;
    color: #d7e3ea;
    margin-top: 10px;
    margin-bottom: 25px;
    font-weight: 700;
    width: 100%;
    display: flex;
    justify-content: flex-start;
    text-align: left;
    background: rgba(0, 0, 0, 0.45);
    padding: 18px 24px;
    border-radius: 16px;
    backdrop-filter: blur(6px);
    -webkit-text-stroke: 1px #02141a;
    text-shadow: 0px 2px 6px rgba(0,0,0,0.9);
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
}}

.footer {{
    text-align: center;
    color: #aab7c4;
    margin-top: 100px;
    font-size: 14px;
}}

.stTextInput>div>div>input {{
    background-color: rgba(255,255,255,0.08);
    color: white;
    border: 1px solid #11d9ff;
    border-radius: 12px;
    padding: 12px;
}}

.stButton>button {{
    background: linear-gradient(90deg, #0077ff, #11d9ff);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 16px 40px;
    font-size: 20px;
    font-weight: bold;
    width: 100%;
    height: 45px;
}}

.stButton>button:hover {{
    opacity: 0.7;
}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stTextInput input {
    height: 15px;
    font-size: 22px;
    padding: 12px 20px;
    border-radius: 14px;
    border: 2px solid #11d9ff;
    background-color: rgba(255,255,255,0.08);
    color: white;
}
.stTextInput input::placeholder {
    font-size: 20px;
    color: #cfd8dc;
}
</style>
""", unsafe_allow_html=True)

# ── Banner (online URL, shorter height) ──────────────────────────────────────
st.markdown(f"""
<style>
.block-container {{
    padding-top: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}}

.banner {{
    width: 100%;
    height: 35vh;      
    background-image: url("{BANNER_IMAGE_URL}");
    background-size: cover;
    background-position: center top;  /* keeps the logo/top portion visible */
    background-repeat: no-repeat;
    margin-top: -30px;
}}
</style>

<div class="banner"></div>
""", unsafe_allow_html=True)

# ── Center Layout ─────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <h1 class="big-title" style="margin-top:-40px;">
    PromptPolish
    </h1>
    """, unsafe_allow_html=True)
    st.markdown('<div class="coming">COMING SOON</div>', unsafe_allow_html=True)

st.markdown("""
<div class="message">
<strong>We are currently working continuously to improve and launch the platform as soon as possible. 
Our team is focused on creating the best possible experience for you, and we truly appreciate 
your patience and support during this phase.</strong>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

VIDEO_URL = "https://youtube.com/shorts/v2Z0OpBDPts?si=BSPR3orS9Oc_MhT2"  # replace with actual demo video link
st.markdown(
    f"""
    <style>
    .coming_link {{
        font-size: 60px;
        font-weight: bold;
        color: white;
        width: 100%;
        text-align: center;
        margin-top: 10px;
        text-shadow:
            0 0 5px #ffffff,
            0 0 10px #11d9ff,
            0 0 20px #11d9ff,
            0 0 40px #11d9ff;
        animation: glow 1s ease-in-out infinite alternate;
    }}

    @keyframes glow {{
        from {{
            text-shadow:
                0 0 5px #ffffff,
                0 0 10px #11d9ff,
                0 0 20px #11d9ff;
        }}
        to {{
            text-shadow:
                0 0 10px #ffffff,
                0 0 20px #11d9ff,
                0 0 40px #11d9ff,
                0 0 60px #11d9ff;
        }}
    }}

    .coming a {{
        color: white;
        text-decoration: none;
    }}
    </style>

    <div class="coming_link">
        <a href="{VIDEO_URL}" target="_blank">
            Check Demo video of the Tool
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown("<br>", unsafe_allow_html=True)


if st.button("Fill form and get 1-2 month free premium"):
    st.switch_page("pages/1_form.py")







st.markdown(
    '<div class="message">As a thank-you for supporting us before launch, you will receive 1-2 month of Premium access completely free once we go live.</div>',
    unsafe_allow_html=True
)

col10, col11, col12 = st.columns([1, 2, 1])
with col11:
    st.markdown('<div class="footer">Yuvraj 2026 PromptPolish</div>', unsafe_allow_html=True)