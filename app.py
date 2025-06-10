import streamlit as st

# 🟢 THIS MUST BE FIRST
st.set_page_config(page_title="Wall Street GPT", layout="centered")

from general_market import wallstreet_chat
from equity_research import equity_research_flow

st.title("🏛️ Wall Street GPT")
st.caption("Smart market research. Select a mode below.")

mode = st.radio("Select Assistant Mode:", ["🧠 General Market Chat", "📊 Equity Research Assistant"], horizontal=True)

if mode == "🧠 General Market Chat":
    wallstreet_chat()
elif mode == "📊 Equity Research Assistant":
    equity_research_flow()
