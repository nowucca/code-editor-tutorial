import traceback

import streamlit as st

from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES

st.set_page_config(
    page_title="Code Editor Tutorial: Advanced Code Editor",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.sidebar.title(":memo: Editor settings")

st.title("Code Editor Tutorial: Advanced Code Editor")

documentation, example = st.columns([1, 1], gap="large")

with documentation:
    st.info("""    
    Make sure you understand:
    * How to control code editor features
    * How to read code from the code editor
    * How to update code using the code editor
    
    """)
    st.code("""
    from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES
    ...
    
    # Every time we reload the page, make a new editor with a new id
    EDITOR_KEY_PREFIX = "ace-editor"
    if 'editor_id' not in st.session_state:
        st.session_state.editor_id = 0
    
    # Empty code on first run
    if "code" not in st.session_state:
        st.session_state.code = ""
    
    # This is how we update code in the editor - saving it in a session variable "code".
    INITIAL_CODE = st.session_state.code
    
    # The component parameters are documented in the Streamlit Ace documentation
    # Command-Click on the st_ace function to see the documentation in PyCharm
    # (Ctrl-Click on Windows)
    code = st_ace(
        value=INITIAL_CODE,
        language=st.sidebar.selectbox("Language mode", options=LANGUAGES, index=121),
        placeholder="Placeholder text when no code is present",
        theme=st.sidebar.selectbox("Theme", options=THEMES, index=25),
        keybinding=st.sidebar.selectbox(
            "Keybinding mode", options=KEYBINDINGS, index=3
        ),
        font_size=st.sidebar.slider("Font size", 5, 24, 14),
        tab_size=st.sidebar.slider("Tab size", 1, 8, 4),
        wrap=st.sidebar.checkbox("Wrap lines", value=False),
        show_gutter=st.sidebar.checkbox("Show gutter", value=True),
        show_print_margin=st.sidebar.checkbox("Show print margin", value=True),
        auto_update=st.sidebar.checkbox("Auto update", value=True),
        readonly=st.sidebar.checkbox("Read only", value=False),
        key=f"{EDITOR_KEY_PREFIX}-{st.session_state.editor_id}",
        height=300,
        min_lines=12,
        max_lines=20
    )
    
    # Let's save the code in session state as the value changes
    st.session_state.code = code
    
    print("STATE", st.session_state, "INITIAL", INITIAL_CODE, "CURRENT", code)
    
    # Let's pretend we are modifying that code...and handle errors
    try:
        modified_code = code + "\n# Modified code"
        st.session_state.code = modified_code
    except Exception as e:
        traceback.print_exc()
        st.error(icon="🔥", body=f":red[Error encountered: {e}]")
        st.session_state.code = code
    
    # Read code from the editor
    st.write("The code you've written in the editor is:")
    st.code(code, language="python")
    
    # Read code from session state
    st.write("The code you've pretended to modify is:")
    st.code(st.session_state.code, language="python")
    
    reload_button = st.button("↪︎ Reload Page")
    if reload_button:
        # Clear the session code
        del st.session_state['code']
    
        # Clear the editor component by id
        for k in st.session_state.keys():
            if k.startswith(EDITOR_KEY_PREFIX):
                del st.session_state[k]
    
        # Increment the editor id
        st.session_state.editor_id += 1
    
        # Restart the page
        st.experimental_rerun()
    
    """)
    

with example:
    st.warning("Note: Open up the sidebar to see editor features.")

    # Every time we reload the page, make a new editor with a new id
    EDITOR_KEY_PREFIX = "ace-editor"
    if 'editor_id' not in st.session_state:
        st.session_state.editor_id = 0

    # Empty code on first run
    if "code" not in st.session_state:
        st.session_state.code = ""

    # This is how we update code in the editor - saving it in a session variable "code".
    INITIAL_CODE = st.session_state.code

    # The component parameters are documented in the Streamlit Ace documentation
    # Command-Click on the st_ace function to see the documentation in PyCharm
    # (Ctrl-Click on Windows)

    st.write(f"#### Code Editor ID: {st.session_state.editor_id}")
    code = st_ace(
        value=INITIAL_CODE,
        language=st.sidebar.selectbox("Language mode", options=LANGUAGES, index=121),
        placeholder="Placeholder text when no code is present",
        theme=st.sidebar.selectbox("Theme", options=THEMES, index=25),
        keybinding=st.sidebar.selectbox(
            "Keybinding mode", options=KEYBINDINGS, index=3
        ),
        font_size=st.sidebar.slider("Font size", 5, 24, 14),
        tab_size=st.sidebar.slider("Tab size", 1, 8, 4),
        wrap=st.sidebar.checkbox("Wrap lines", value=False),
        show_gutter=st.sidebar.checkbox("Show gutter", value=True),
        show_print_margin=st.sidebar.checkbox("Show print margin", value=True),
        auto_update=st.sidebar.checkbox("Auto update", value=True),
        readonly=st.sidebar.checkbox("Read only", value=False),
        key=f"{EDITOR_KEY_PREFIX}-{st.session_state.editor_id}",
        height=300,
        min_lines=12,
        max_lines=20
    )

    # Let's save the code in session state as the value changes
    st.session_state.code = code

    print("STATE", st.session_state, "INITIAL", INITIAL_CODE, "CURRENT", code)

    # Let's pretend we are modifying that code...and handle errors
    try:
        modified_code = code + "\n# Modified code"
        st.session_state.code = modified_code
    except Exception as e:
        traceback.print_exc()
        st.error(icon="🔥", body=f":red[Error encountered: {e}]")
        st.session_state.code = code

    # Read code from the editor
    st.write("The code you've written in the editor is:")
    st.code(code, language="python")

    # Read code from session state
    st.write("The code you've pretended to modify is:")
    st.code(st.session_state.code, language="python")

    reload_button = st.button("↪︎ Reload Page")
    if reload_button:
        # Clear the session code
        del st.session_state['code']

        # Clear the editor component by id
        for k in st.session_state.keys():
            if k.startswith(EDITOR_KEY_PREFIX):
                del st.session_state[k]

        # Increment the editor id
        st.session_state.editor_id += 1

        # Restart the page
        st.experimental_rerun()
