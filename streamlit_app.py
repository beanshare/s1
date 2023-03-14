from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

zip_file = st.file_uploader('上传 .zip 格式的实验数据', type="zip", accept_multiple_files=False)
if zip_file:
    print("hhhhhhhh")
    st.info("正在上传......")
    with open("res.zip", "wb") as f:
        f.write(zip_file.read())

    if os.path.exists("res.zip"):
        st.success("成功！")
    else:
        st.error("失败！")

