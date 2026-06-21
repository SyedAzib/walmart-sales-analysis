import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Store Analysis", layout="wide")

df = pd.read_csv("data/walmart_cleaned.csv")
st.title("🏪 Store Analysis")
st.markdown("---")

st.sidebar.header("🔽 Filters")
year_filter = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

df_filtered = df[df["Year"].isin(year_filter)]
st.subheader("🏆 Top 10 Stores by Sales")

top_stores = df_filtered.groupby("Store")["Weekly_Sales"].sum().nlargest(10).reset_index()

fig1 = px.bar(
    top_stores,
    x="Weekly_Sales",
    y="Store",
    orientation="h",
    title="Top 10 Stores by Total Sales",
    color_discrete_sequence=["#0071CE"]
)

st.plotly_chart(fig1, use_container_width=True)