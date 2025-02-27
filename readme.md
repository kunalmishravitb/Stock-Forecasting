# 📈 Stock Prediction App

This project is a **📊 Stock Prediction App** built using **🖥️ Streamlit** and **📉 Plotly**, leveraging 📡 **Yahoo Finance** data to predict future 📈 stock prices using **🔄 Moving Average Forecasting**.

## 🌟 Features

- 🔍 Fetch stock data using **💰 Yahoo Finance**
- 🔮 Apply **📉 Moving Average Forecasting** for prediction
- 📊 Interactive visualization with **📈 Plotly**
- 🕰️ Display historical & predicted stock prices
- 🎛️ **Streamlit-based** user-friendly interface

## 📂 Folder Structure

```
TIME_S...
│── 📁 pages/
│   ├── 📁 utils/
│   │   ├── 📜 __init__.py
│   │   ├── 🏗️ model_train.py      # Data processing & model training
│   │   ├── 📈 plotly_figure.py    # Functions to generate 📊 graphs
│   │   ├── 📑 Stock_Analysis.py   # 📊 Market analysis functions
│   │   ├── 🔮 Stock_Prediction.py # 📈 Prediction logic
│── 🖼️ app.jpeg                    # Image for the project
│── 🚀 Trading_App.py               # 🎯 Main application file
```

## 🛠️ Installation

1. 📥 Clone this repository:
   ```bash
   git clone <your-github-repo-url>
   cd <your-project-folder>
   ```
2. 🏗️ Install **Streamlit**, **Plotly**, and **Yahoo Finance API**

## ▶️ How to Run

Run the **Streamlit** app using:

```bash
streamlit run Trading_App.py
```

## 🎯 Usage

1. ⌨️ Enter the **stock ticker symbol** (e.g., `TSLA`).
2. 📊 View **historical stock price trends**.
3. 🔮 See the **Moving Average Forecast** for the next **30 days**.

## 🤝 Contributing

Feel free to **submit pull requests** or **open issues**! 🚀

## ⚖️ License

This project is **licensed** under the **MIT License**. 📜

