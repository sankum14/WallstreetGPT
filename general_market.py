import streamlit as st
import requests
import re
from datetime import datetime
import pytz
import yfinance as yf
from ai import call_nvidia
from utils import is_market_open, extract_ticker

def get_yf_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = info.get("currentPrice") or info.get("previousClose")
        prev_close = info.get("previousClose", 0)
        change = ((price - prev_close) / prev_close * 100) if prev_close else 0
        return round(price, 2), round(change, 2)
    except Exception as e:
        print(f"yfinance error: {e}")
        return None, None

def get_news_yf(ticker):
    try:
        stock = yf.Ticker(ticker)
        news = stock.news[:3]
        return [
            f"- [{item['title']}]({item['link']}) — *{item['publisher']}*" for item in news
        ]
    except Exception:
        return []

def wallstreet_chat():
    st.title("🏛️ Wall Street GPT")
    st.caption("Market-level insights like the big banks. Powered by NIM + yfinance.")

    # Initialize session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    query = st.chat_input("Ask about any stock or the market...")

    if query:
        # Show user message
        st.session_state.chat_history.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # Extract ticker
        ticker = extract_ticker(query)
        news_block = ""
        if ticker:
            news = get_news_yf(ticker)
            if news:
                news_block = "### 📰 Recent News for " + ticker + "\n" + "\n".join(news) + "\n\n"

        # Build prompt nicely
        prompt = f"""
{news_block}
### 💬 User Query:
{query}

Please answer like a professional financial assistant. Respond in markdown. Always mention tickers in (TICKER) format.
"""

        # Send to AI
        response = call_nvidia([
            {
                "role": "system",
                "content": (
                    "You're a professional financial assistant. Respond in markdown. "
                    "Mention stock tickers in (TICKER) format. Include headlines if given. "
                    "Be concise, data-driven, and investor-friendly."
                )
            },
            {"role": "user", "content": prompt}
        ])

        # Append and display AI response
        st.session_state.chat_history.append({"role": "assistant", "content": response})

        with st.chat_message("assistant"):
            st.markdown(response)

        # Optional Ticker Sidebar
        if ticker:
            price, change = get_yf_data(ticker)
            market_status = "🟢 Live" if is_market_open() else "🔴 Closed"
            st.sidebar.markdown(f"""
### 🧾 {ticker} Overview
- **Price:** {"$" + str(price) if price else "Unavailable"}
- **Change:** {f"{change:+.2f}%" if change is not None else "N/A"}
- **Market:** {market_status}
""")
