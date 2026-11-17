# AI_SWOT-Analaysis-
# 📊 AI Business Intelligence & SWOT Analysis System

An end-to-end, evidence-driven business analytics platform. This system ingests raw business data, performs data cleaning, generates key performance indicators (KPIs), visualizes trends, forecasts future sales using machine learning, and automatically generates a data-backed SWOT analysis. It also features a conversational AI Analyst capable of answering business queries based on the data.

## 🚀 Key Features

*   **Data Ingestion & Cleaning:** Handles missing values, duplicates, and data type conversions automatically.
*   **Business Analytics (EDA):** Generates actionable visualizations including Sales by Product Line, Gender Distribution, and Payment Methods.
*   **KPI Generation:** Automatically calculates Total Sales, Average Customer Ratings, and Top-Performing Product Lines.
*   **Machine Learning Forecasting:** Utilizes Linear Regression (via `scikit-learn`) to predict future sales trends with model evaluation (MAE, RMSE).
*   **Automated SWOT Analysis:** Dynamically extracts Internal Strengths & Weaknesses from data, and combines them with External Opportunities & Threats.
*   **Agentic AI Analyst:** A conversational AI agent powered by Google Gemini that uses custom tools to answer questions like *"What were our total sales?"* or *"What is our biggest weakness?"*
*   **Interactive Dashboard:** (Phase 8) A Streamlit web application to upload data and view all insights in a single UI.

## 🛠️ Tech Stack

*   **Programming Language:** Python 3.x
*   **Data Manipulation:** Pandas, NumPy
*   **Data Visualization:** Matplotlib, Seaborn
*   **Machine Learning:** Scikit-Learn
*   **Generative AI:** Google Gemini API (`google-genai`)
*   **Environment Management:** `python-dotenv`, `venv`
*   **UI (Upcoming):** Streamlit

## 📁 Project Structure

```text
snip/
│
├── app.py                     # (Upcoming) Streamlit dashboard entry point
├── requirements.txt           # Project dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore file
├── README.md                  # Project documentation
│
├── data/
│   ├── raw/                   # Original, immutable data
│   └── processed/             # Cleaned and transformed data
│
├── reports/                   # Generated charts, forecasts, and SWOT reports
│   ├── sales_by_product_line.png
│   └── swot_report.txt
│
├── src/
│   ├── data_processing/
│   │   ├── loader.py          # Data loading logic
│   │   └── cleaner.py         # Data cleaning and preprocessing
│   │
│   ├── analytics/
│   │   ├── kpi.py             # KPI calculations
│   │   └── eda.py             # Exploratory Data Analysis (Charts)
│   │
│   ├── machine_learning/
│   │   └── forecasting.py     # Sales forecasting model
│   │
│   ├── swot_analysis/
│   │   ├── internal_analysis.py
│   │   ├── external_analysis.py
│   │   └── swot_generator.py  # Combines internal/external SWOT
│   │
│   └── ai_agent/
│       ├── tools.py           # Custom tools for the AI agent
│       └── agent.py           # AI Agent logic (Gemini API)
│
└── tests/                     # Unit tests
