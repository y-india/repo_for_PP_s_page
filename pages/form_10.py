import streamlit as st

DEMO_URL = "https://your-demo-video-link-here"

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

if submitted:
    st.success("THANK YOU")
    