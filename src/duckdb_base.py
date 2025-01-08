import os
import time
import pandas as pd
import duckdb
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer


@st.cache_resource
def get_pyg_renderer(df: pd.DataFrame) -> str:
    renderer = StreamlitRenderer(df, kernel_computation=True)
    return renderer


# Streamlitページの幅を調整する
st.set_page_config(page_title="pandas_duckdb", layout="wide")

st.title("duckdbベース")

# 計測開始(duckdb)
start = time.time()

# csvフォルダが存在するか確認
if not os.path.exists("csv/diabetes_data.csv"):
    st.error("csv/diabetes_data.csvが存在しません。データを作成してください。")
    st.stop()
read_df = duckdb.read_csv("csv/diabetes_data.csv").to_df()

renderer = get_pyg_renderer(read_df)

renderer.explorer()

# 時間計測終了
elapsed_time = time.time() - start
# 時間を小数点以下3桁まで表示する
elapsed_time = round(elapsed_time, 3)
st.write(f"elapsed_time: {elapsed_time} [sec]")
