import streamlit as st
import pandas as pd

st.set_page_config(page_title="Raw Data", layout="wide")

df = pd.read_csv("data/walmart_cleaned.csv")

st.title("📋 Raw Data")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    year_filter = st.multiselect(
        "Select Year",
        options=sorted(df["Year"].unique()),
        default=sorted(df["Year"].unique())
    )
with col2:
    store_filter = st.multiselect(
        "Select Store",
        options=sorted(df["Store"].unique()),
        default=sorted(df["Store"].unique())
    )

df_filtered = df[
    (df["Year"].isin(year_filter)) &
    (df["Store"].isin(store_filter))
]

st.markdown(f"**Total Records: {len(df_filtered):,}**")
st.dataframe(df_filtered, use_container_width=True)

csv = df_filtered.to_csv(index=False)
st.download_button(
    label="📥 Download Data as CSV",
    data=csv,
    file_name="walmart_filtered_data.csv",
    mime="text/csv"
)