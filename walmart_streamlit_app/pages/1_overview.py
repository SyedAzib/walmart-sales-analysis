import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Overview", layout="wide")

# Load data
df = pd.read_csv("data/walmart_cleaned.csv")

# Header
st.markdown(
    "<h2 style='color:#0071CE;'>📊 Sales Overview</h2>",
    unsafe_allow_html=True
)
st.markdown("---")

# Sidebar filters
st.sidebar.markdown(
    "<h3 style='color:white;'>🔽 Filters</h3>",
    unsafe_allow_html=True
)
year_filter = st.sidebar.multiselect(
    "Select Year",
    options=df["Year"].unique(),
    default=df["Year"].unique()
)
df_filtered = df[df["Year"].isin(year_filter)]

# KPI Cards
st.markdown(
    "<h3 style='color:#0071CE;'>Key Metrics</h3>",
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        label="💰 Total Sales",
        value=f"${df_filtered['Weekly_Sales'].sum():,.0f}"
    )
with col2:
    st.metric(
        label="📈 Average Sales",
        value=f"${df_filtered['Weekly_Sales'].mean():,.0f}"
    )
with col3:
    st.metric(
        label="🏪 Total Stores",
        value=df_filtered['Store'].nunique()
    )

st.markdown("---")

# Monthly Sales Trend
st.markdown(
    "<h3 style='color:#0071CE;'>📅 Monthly Sales Trend</h3>",
    unsafe_allow_html=True
)
monthly = df_filtered.groupby("Month")["Weekly_Sales"].sum().reset_index()
fig1 = px.line(
    monthly,
    x="Month",
    y="Weekly_Sales",
    title="Monthly Sales Trend",
    color_discrete_sequence=["#0071CE"]
)
fig1.update_layout(
    plot_bgcolor="#F5F5F5",
    paper_bgcolor="#F5F5F5",
    title_font_color="#0071CE",
    legend=dict(font=dict(color="black"))
)
st.plotly_chart(fig1, use_container_width=True)

# Holiday vs Non Holiday
st.markdown(
    "<h3 style='color:#0071CE;'>🎄 Holiday vs Non-Holiday Sales</h3>",
    unsafe_allow_html=True
)
holiday = df_filtered.groupby("IsHoliday")["Weekly_Sales"].sum().reset_index()
holiday["IsHoliday"] = holiday["IsHoliday"].map(
    {True: "Holiday", False: "Non-Holiday"}
)
fig2 = px.pie(
    holiday,
    names="IsHoliday",
    values="Weekly_Sales",
    title="Holiday vs Non-Holiday Sales",
    color_discrete_sequence=["#FFC220", "#0071CE"],
    hole=0.4
)
fig2.update_layout(
    plot_bgcolor="#F5F5F5",
    paper_bgcolor="#F5F5F5",
    title_font_color="#0071CE",
    legend=dict(font=dict(color="black"))
)
st.plotly_chart(fig2, use_container_width=True)