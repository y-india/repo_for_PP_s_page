import streamlit as st


st.markdown("""
<div class="message">

<h3>🚀 About PromptPolish</h3>

<strong>PromptPolish is a Chrome extension designed to transform raw prompts into structured, optimized prompts using user-defined custom instructions, default instructions, or advanced professional instructions.</strong>

<br><br>

It is primarily built for:
<ul>
<li>New coders entering development</li>
<li>College students who code</li>
<li>Freshers entering the IT industry</li>
</ul>

Users can also personalize the tool by providing information such as their role, preferred coding language, chatbot platform, and more to generate better prompt outputs.

<br>

<b>How it works:</b>

<ul>
<li>Write a raw prompt in any chatbot like ChatGPT, Claude, Gemini, etc.</li>
<li>Select the text you want to improve</li>
<li>Use a shortcut (example: Ctrl + Shift + Y)</li>
<li>The extension converts it into a structured prompt automatically OR opens a popup containing:</li>
<ul>
<li>Replace button</li>
<li>Copy button</li>
<li>Retry button</li>
</ul>
</ul>

<b>Main Features:</b>

<ul>
<li>🛠️ <b>Custom Instructions</b> → Define how prompts should be transformed</li>

<li>⌨️ <b>Multiple Shortcuts</b> → Quick convert, popup preview mode, and settings shortcut</li>

<li>👤 <b>Personal Context</b> → Add role, coding language, chatbot preference, etc. for improved outputs</li>

<li>🎨 <b>Theme Support</b> → Customize popup appearance based on your preference</li>
</ul>

</div>
""", unsafe_allow_html=True)



st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("⬅️ Back to Home"):
    st.switch_page("app.py")