# 🛒 Walmart Sales Analysis

> An end-to-end data analytics project analyzing Walmart sales data using Python, SQL, Power BI, and Streamlit — covering data cleaning, exploratory data analysis, interactive dashboards, and a multi-page web application.

---

## 🌐 Live Demo

**👉 [View Live App](https://walmart-sales-analysis-qjqeshojah8vcsxaducf8i.streamlit.app/)**

---

## 📊 Project Overview

This project demonstrates a complete data analytics workflow — from raw data to a fully deployed interactive web application.

| Step | Description |
|------|-------------|
| 🧹 Data Cleaning | Cleaned and preprocessed raw Walmart sales data using Python & Pandas |
| 🔍 EDA | Explored patterns, trends, and outliers using statistical analysis |
| 🗄️ SQL Analysis | Queried and aggregated data using structured SQL queries |
| 📊 Power BI Dashboard | Built an interactive, multi-page branded dashboard |
| 🚀 Streamlit App | Deployed a live multi-page web app with dynamic filters and Plotly charts |

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Data Cleaning & EDA (Pandas, Seaborn) |
| ![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white) | Data querying and analysis |
| ![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black) | Interactive multi-page dashboard |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Multi-page web app (Plotly visualizations) |

---

## 📁 Project Structure

```
walmart_project/
├── project.ipynb                   # Python EDA and data cleaning
├── project.sql                     # SQL queries
├── walmart_cleaned.csv             # Cleaned dataset
└── walmart_streamlit_app/
    ├── app.py                      # Home page
    └── pages/
        ├── 1_Overview.py
        ├── 2_Store_Analysis.py
        ├── 3_Department_Analysis.py
        └── 4_Raw_Data.py
```

---

## 📈 Key Features

- 💰 **KPI Cards** — Total Sales, Average Sales, Total Stores
- 📅 **Monthly Sales Trend** — Time-series visualization across years
- 🎄 **Holiday vs Non-Holiday** — Sales impact comparison
- 🏆 **Top 10 Stores & Departments** — Ranked by total sales
- 🔽 **Interactive Year Filters** — Dynamic data slicing
- 📋 **Raw Data Table** — Browsable with CSV download option

---

## 🖥️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/SyedAzib/walmart-sales-analysis.git
```

**2. Navigate to the Streamlit app folder**
```bash
cd walmart-sales-analysis/walmart_streamlit_app
```

**3. Install required libraries**
```bash
pip install streamlit pandas plotly
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## 👤 Author

**Syed Azib**
- GitHub: [@SyedAzib](https://github.com/SyedAzib)
