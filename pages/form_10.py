import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# -----------------------------
# DEMO LINK
# -----------------------------
DEMO_URL = "https://drive.google.com/file/d/1NMBPLZyV9lmJO_1_sliVk5erjusc8FN3/view?usp=sharing"

# -----------------------------
# GOOGLE SHEETS CONNECTION
# -----------------------------
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=SCOPE
)

client = gspread.authorize(creds)
sheet = client.open("Client_Requests").sheet1

# -----------------------------
# UI
# -----------------------------
st.title("Premium Access Form")

with st.form("premium_form"):

    name = st.text_input("Name")

    occupation = st.selectbox(
        "Occupation",
        ["Student", "Working Professional"]
    )

    email = st.text_input("Email address")

    liked = st.text_area("What you liked most about the idea")

    ai_use = st.text_area("How it can be applied to your work with AI")

    watched = st.radio(
        "Have you watched the demo?",
        ["Yes", "No"]
    )

    if watched == "No":
        st.markdown(f"[Watch Demo Video Here]({DEMO_URL})")

    submitted = st.form_submit_button("Submit")

# -----------------------------
# SUBMIT HANDLER
# -----------------------------
if submitted:

    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        name,
        occupation,
        email,
        liked,
        ai_use,
        watched
    ]

    sheet.append_row(row)

    st.success("THANK YOU")

# -----------------------------
# NAVIGATION
# -----------------------------
if st.button("⬅️ Back to Home"):
    st.switch_page("app.py")