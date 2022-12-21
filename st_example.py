"""
A Streamlit app to showcase the stmd.markdown() function.
"""

import streamlit as st

import stmd

st.set_page_config(
    page_title="An example of how we plot markdowns",
    layout="wide",
)

col_st, col_stmd = st.columns(2)

with col_st:
    st.header("With `st.markdown()`")
    st.code(
        """
import streamlit as st

with open("examples/images.md") as f:
    markdown_string = f.read()
st.markdown(markdown_string)
    """
    )

    with st.expander("Result"):
        with open("examples/images.md", "r", encoding="UTF-8") as f:
            markdown_string = f.read()

        st.markdown(markdown_string)

with col_stmd:
    st.header("With `stmd.markdown()`")
    st.code(
        """
import stmd

stmd.markdown("examples/images.md")

    """
    )

    with st.expander("Result"):
        stmd.markdown("examples/images.md")
