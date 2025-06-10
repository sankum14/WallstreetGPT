from datetime import datetime
import pytz
import re

def is_market_open():
    now = datetime.now(pytz.timezone("US/Eastern"))
    return now.weekday() < 5 and 9 <= now.hour < 16

def extract_ticker(text):
    match = re.search(r'\(([A-Z]{1,5})\)', text)
    return match.group(1) if match else None

def format_equity_prompt(ticker: str, quarter_label: str) -> str:
    return f"""
Generate a hedge-fund style equity research report on ({ticker.upper()}).

### 📅 Latest Earnings: {quarter_label}

Include the following:
- Business Overview
- Key Financial Highlights from {quarter_label}
- Beats or misses vs analyst expectations if known
- Revenue, EBITDA, and margin trends (QoQ & YoY)
- Management guidance and current quarter indicators
- Valuation multiples (PE, EV/EBITDA) if available
- Investment risks and industry headwinds
- Final Recommendation: **Buy**, **Hold**, or **Sell** — with clear reasoning (DCF model with next quarter in mind derive a mini dcf with stock price target)

Format the entire report in clean markdown.
"""

