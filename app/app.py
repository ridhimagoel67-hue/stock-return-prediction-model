
import streamlit as st
import pandas as pd
import joblib
st.set_page_config(
    page_title="Equity Insight Engine",
    layout="wide"
)
 
st.title("Equity Insight Engine")

st.caption(
    "Fundamental Stock Return Prediction & Analytics"
)

model = joblib.load(
    "models/stock_return_app_model.pkl"
)

top_drivers = [
    "Debt to Equity",
    "Price to Earnings",
    "Return on Assets",
    "Return on Equity",
    "Dividend Yield"
]

st.divider()

left_col, right_col = st.columns(
    [1.2, 1]
)
with left_col:
    st.subheader("Financial Inputs")

    input_col1, input_col2 = st.columns(2)

    with input_col1:
        st.markdown("### Valuation & Profitability")

        pe_ratio = st.number_input(
            "Price to Earnings",
            value=15.0
        )

        pb_ratio = st.number_input(
            "Price to Book Value",
            value=2.0
        )

        graham_number = st.number_input(
            "Graham Number",
            value=100.0
        )

        current_price = st.number_input(
            "Current Price",
            value=100.0
        )

        roa = st.number_input(
            "Return on Assets",
            value=10.0
        )

        roe = st.number_input(
            "Return on Equity",
            value=15.0
        )

        dividend_yield = st.number_input(
            "Dividend Yield",
            value=1.5
        )

        roce_prev = st.number_input(
            "ROCE Previous Year",
            value=12.0
        )

    with input_col2:
        st.markdown("### Financial Health & Ownership")

        debt_to_equity = st.number_input(
            "Debt to Equity",
            value=0.5
        )

        quick_ratio = st.number_input(
            "Quick Ratio",
            value=1.5
        )

        debtor_days = st.number_input(
            "Debtor Days",
            value=45.0
        )

        working_capital = st.number_input(
            "Working Capital 5Y Back",
            value=100.0
        )

        fii_change = st.number_input(
            "Change in FII Holding",
            value=0.0
        )

        shareholders = st.number_input(
            "Number of Shareholders",
            value=1000.0
        )

        g_factor = st.number_input(
            "G Factor",
            value=1.0
        )


input_df = pd.DataFrame({

    "Debt to equity": [debt_to_equity],
    "Price to Earning": [pe_ratio],
    "Return on assets": [roa],
    "Return on equity": [roe],
    "Dividend yield": [dividend_yield],
    "Change in FII holding": [fii_change],
    "G Factor": [g_factor],
    "Number of Shareholders": [shareholders],
    "Current Price": [current_price],
    "Debtor days": [debtor_days],
    "Graham Number": [graham_number],
    "Price to book value": [pb_ratio],
    "Working capital 5Years back": [working_capital],
    "Quick ratio": [quick_ratio],
    "Return on capital employed preceding year": [roce_prev]

})

 
with right_col:

    st.subheader("Prediction Summary")

    if st.button("Predict Return"):

        prediction = model.predict(input_df)[0]

        st.metric(
            "Predicted Return",
            f"{prediction*100:.2f}%"
        )
        st.markdown("---")

        st.subheader("Model Information")

        st.write("**Algorithm:** CatBoost")
        st.write("**Features:** 15")
        st.write("**CV R²:** 0.40")
        st.write("**Training Rows:** 4,667")

        st.markdown("---")

        st.subheader("Top Drivers")

        st.write("1. Debt to Equity")
        st.write("2. Price to Earnings")
        st.write("3. Return on Assets")
        st.write("4. Return on Equity")
        st.write("5. Dividend Yield")