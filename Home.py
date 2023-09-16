import streamlit as st
import traceback

from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES

st.set_page_config(
    page_title="Code Editor Tutorial",
    page_icon="📄",
    layout="wide",
)
st.sidebar.title(":memo: Editor settings")

st.title("Code Editor Tutorial")

st.markdown("""
The idea behind these examples is to show how to use text areas as code editors,
or the Streamlit Ace code editor.  Following the examples in the pages, you'll learn how to:
* Use a text area as a code editor
* Use the Streamlit Ace code editor
* See a more complete example of the Streamlit Ace code editor
""")


with st.sidebar:
    reload_button = st.button("↪︎ Reload Page")
    if reload_button:
        st.session_state.clear()
        st.experimental_rerun()
