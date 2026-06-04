import streamlit as st
from pathlib import Path




st.write(
    "Download the prototype extension and follow the setup steps below."
)

st.markdown("---")

# Important Note Section
st.warning("""
### Important Note

This demo represents approximately **25% of the full tool**.

### Key features in the original tool:
• Ability to add custom instructions to modify prompts  
• 2 to 3 productivity shortcuts  
• Theme options  
• Many additional features and improvements  

### If you like this demo:
• Watch the original tool video below  
• Fill out the form for a free offer when the complete version launches  
""")

# Original Tool Video Link
VIDEO_URL = "https://drive.google.com/file/d/1NMBPLZyV9lmJO_1_sliVk5erjusc8FN3/view"

st.link_button(
    "🎥 Check Original Tool Video",
    VIDEO_URL,
    use_container_width=True
)

# Switch page button for form page
if st.button(
    "🎁 Claim Free Launch Offer",
    use_container_width=True
):
    st.switch_page("pages/form_10.py")   # change filename if needed

st.markdown("---")

# ZIP file path
ZIP_FILE = "Prototype_prompt_polish.zip"


zip_path = Path(ZIP_FILE)

if zip_path.exists():
    with open(zip_path, "rb") as file:
        st.download_button(
            label="📥 Download PromptPolish Prototype",
            data=file,
            file_name="Prototype_prompt_polish.zip",
            mime="application/zip",
            use_container_width=True
        )
else:
    st.warning("ZIP file not found. Place Prototype_prompt_polish.zip in project folder.")

st.markdown("---")

st.header("Setup Instructions")

steps = [
    'Unzip the downloaded item into a new folder (recommended)',
    'Open Chrome and go to: chrome://extensions/',
    'Turn ON Developer Mode',
    'Click "Load unpacked"',
    'Select the extracted folder named "Prototype_prompt_polish"',
    'Open any chatbot (ChatGPT, Gemini, etc.)',
    'Write your coding prompt',
    'Select the text and press Ctrl + Shift + Y'
]

for i, step in enumerate(steps, start=1):
    st.markdown(f"### {i}. {step}")

st.markdown("---")

st.info(
    "If the shortcut does not work immediately, refresh the chatbot tab once after loading the extension."
)