# 🛒 Walmart Sales Analysis

An end-to-end data analytics project analyzing Walmart sales data using Python, SQL, Power BI, and Streamlit — covering data cleaning, exploratory data analysis, interactive dashboards, and a multi-page web application.

---

## 📊 Project Overview

This project demonstrates a complete data analytics workflow:
- Cleaning and exploring raw sales data using Python
- Querying and analyzing data using SQL
- Building an interactive, branded Power BI dashboard
- Creating a multi-page Streamlit web app with live filtering and visualizations

---

## 🧰 Tech Stack

- **Python** — Pandas, Seaborn (Data Cleaning & EDA)
- **SQL** — Data querying and analysis
- **Power BI** — Interactive multi-page dashboard
- **Streamlit** — Multi-page web application (Plotly visualizations)

---

## 📁 Project Structure

```
walmart_project/
├── project.ipynb              (Python EDA and data cleaning)
├── project.sql                (SQL queries)
├── walmart_cleaned.csv        (Cleaned dataset)
└── walmart_streamlit_app/
    ├── app.py                 (Home page)
    └── pages/
        ├── 1_Overview.py
        ├── 2_Store_Analysis.py
        ├── 3_Department_Analysis.py
        └── 4_Raw_Data.py
```

---

## 📈 Key Features

- 💰 KPI Cards — Total Sales, Average Sales, Total Stores
- 📅 Monthly Sales Trend visualization
- 🎄 Holiday vs Non-Holiday sales comparison
- 🏆 Top 10 Stores and Top 10 Departments by sales
- 🔽 Interactive Year filters
- 📋 Raw data table with CSV download

---

## 🖥️ How to Run Locally

1. Clone this repository
```bash
git clone https://github.com/SyedAzib/walmart-sales-analysis.git
```

2. Navigate to the Streamlit app folder
```bash
cd walmart-sales-analysis/walmart_streamlit_app
```

3. Install required libraries
```bash
pip install streamlit pandas plotly
```

4. Run the app
```bash
streamlit run app.py
```

---

## 👤 Author

**Syed Azib**
- GitHub: [@SyedAzib](https://github.com/SyedAzib)
