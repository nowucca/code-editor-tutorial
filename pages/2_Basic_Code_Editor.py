import streamlit as st

from streamlit_ace import st_ace

st.set_page_config(
    page_title="Code Editor Tutorial: Basic Code Editor",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.sidebar.title(":memo: Editor settings")

st.title("Code Editor Tutorial: Basic Code Editor")


st.markdown("""
In this page, we'll explore how to use the Streamlit Ace code editor.  

## Installing the code editor
The code editor is available on PyPI, so you can install it with `pip install streamlit-ace`.
You can also add `streamlit-ace` to your `requirements.txt` file.

## What is the code editor?
The code editor is a Streamlit component that allows you to edit code in the browser.
Since the code editor is a Streamlit component, so it can be used like any other component.  Here's a simple example:
```python
from streamlit_ace import st_ace
...
code = st_ace(
    value=INITIAL_CODE,
    language="python",
    placeholder="This is placeholder text when no code is present",
    theme="Solarized Light",
    keybinding="vscode",
    font_size=14,
    tab_size=4,
    wrap=False,
    show_gutter=True,
    show_print_margin=True,
    auto_update=False,
    readonly=False,
    key="editor-basic",
)
```
The `st_ace` function returns the code that you've written in the editor.  You can then use that code in your app.

Below is this code editor example in action.  
""")

basic_code = st_ace(
    value="",
    language="python",
    placeholder="This is placeholder text when no code is present",
    theme="solarized_light",
    keybinding="vscode",
    font_size=14,
    tab_size=4,
    wrap=False,
    show_gutter=True,
    show_print_margin=True,
    auto_update=False,
    readonly=False,
    key="editor-basic"
)
st.write("Use the code editor to write code, then hit `CTRL+ENTER` to refresh the app.")
st.write("The code you've written in the editor is:")
st.code(basic_code, language="python")

with st.sidebar:
    reload_button = st.button("↪︎  Reload Page")
    if reload_button:
        st.session_state.clear()
        st.experimental_rerun()
