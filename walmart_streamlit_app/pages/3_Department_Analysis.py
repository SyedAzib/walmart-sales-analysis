import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Department Analysis", layout="wide")

df = pd.read_csv("data/walmart_cleaned.csv")

st.title("🏬 Department Analysis")
st.markdown("---")

st.sidebar.header("🔽 Filters")
year_filter = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

df_filtered = df[df["Year"].isin(year_filter)]

st.subheader("🏆 Top 10 Departments by Sales")

top_dept = df_filtered.groupby("Dept")["Weekly_Sales"].sum().nlargest(10).reset_index()

fig1 = px.bar(
    top_dept,
    x="Weekly_Sales",
    y="Dept",
    orientation="h",
    title="Top 10 Departments by Total Sales",
    color_discrete_sequence=["#FFC220"]
)

st.plotly_chart(fig1, use_container_width=True)