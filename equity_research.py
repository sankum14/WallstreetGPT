import streamlit as st
import yfinance as yf
from datetime import datetime
from ai import call_nvidia
from utils import format_equity_prompt

def get_financials(ticker):
    stock = yf.Ticker(ticker)
    return {
        "info": stock.info,
        "financials": stock.financials,
        "balance": stock.balance_sheet,
        "cashflow": stock.cashflow
    }

def equity_research_flow():
    st.subheader("📊 Equity Research Assistant")

    ticker = st.text_input("Enter Equity Ticker Symbol (e.g., AAPL, TSLA):")

    if ticker:
        try:
            data = get_financials(ticker)
            st.success(f"✅ Financial data loaded for {ticker.upper()}")

            with st.expander("🔍 Raw Financials"):
                st.markdown("**📈 Income Statement:**")
                st.dataframe(data["financials"].iloc[::-1])
                st.dataframe(data["financials"])
                st.markdown("**💼 Balance Sheet:**")
                st.dataframe(data["balance"].iloc[::-1])
                st.markdown("**💸 Cash Flow:**")
                st.dataframe(data["cashflow"].iloc[::-1])

            current_year = datetime.now().year
            current_quarter = (datetime.now().month - 1) // 3 + 1
            quarter_label = f"Q{current_quarter} {current_year}"

            report_prompt = format_equity_prompt(ticker, quarter_label)

            if st.button("📝 Generate Equity Research Report"):
                with st.spinner("🧠 Generating report via NVIDIA NIM..."):
                    result = call_nvidia([
                        {"role": "system", "content": "Act like a hedge fund equity research analyst. Write reports in markdown."},
                        {"role": "user", "content": report_prompt}
                    ])
                st.markdown("### 📄 Equity Research Report")
                st.markdown("---")
                st.markdown(result, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error loading data for {ticker.upper()}: {e}")
