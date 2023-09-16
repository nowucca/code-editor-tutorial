import streamlit as st

st.set_page_config(
    page_title="Code Editor Tutorial: Text Area Editor",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.sidebar.title(":memo: Editor settings")

st.title("Code Editor Tutorial: Text Area Editor")

st.markdown("""
    In this page, we'll explore how to use a text area as a code editor, as a simple way to start editing code in Streamlit.  

## Use a text area to edit code
""")

st.markdown("## Example")
st.markdown("""
```python
text_area_code = st.text_area("Code", value="",
                              placeholder="This is placeholder text when no code is present",                              
                              height=200, key="text_area_code_editor")
```
* Pro: Is a great place to start if you're building your application and need a simple way to edit code
* Cons:
    * Does not look like a code editor, does not have syntax highlighting
    * Does not have code completion, keybindings, themes or other features

Let's show an example of using a text area.
""")
text_area_code = st.text_area("Code", value="",
                              placeholder="This is placeholder text when no code is present",
                              height=200, key="text_area_code_editor")

st.write("Use the code editor to write Python code.")
st.write("The code you've written in the editor is:")
st.code(text_area_code, language="python")

