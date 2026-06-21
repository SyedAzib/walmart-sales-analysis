import streamlit as st

st.set_page_config(
    page_title="Walmart Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Walmart Sales Dashboard")
st.markdown("---")

st.markdown("""
### Welcome! 👋

Use the sidebar on the left to navigate between pages:

- **Overview** → KPIs, Monthly Trend, Holiday vs Non-Holiday
- **Store Analysis** → Top 10 Stores
- **Department Analysis** → Top 10 Departments
- **Raw Data** → Full data table with download option
""")