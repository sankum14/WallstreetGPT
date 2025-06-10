# 🏛️ Wall Street GPT

**Wall Street GPT** is a smart market research assistant designed to deliver market-level insights — just like the big investment banks. Powered by OpenAI's models, NVIDIA NIM, and `yfinance`, it provides interactive market intelligence for traders, analysts, and financial enthusiasts.

## 🔍 Features

- 🧠 **General Market Chat**: Ask questions about the market, sectors, or economic events.
- 📊 **Equity Research Assistant**: Get structured insights into specific stocks, including fundamentals and trends.
- 📈 **Live Stock Data**: Fetches real-time data using `yfinance`.
- 🏦 **Investment Bank Intelligence**: See how the largest investment banks are ranked and analyzed.
- 🌙 **Dark UI Theme**: Clean, professional design with intuitive layout.

## 📸 Preview

![Screenshot 2025-06-10 124045](https://github.com/user-attachments/assets/9560abcb-ab7c-4a71-8203-1bd45978a69b)
![Screenshot 2025-06-10 124032](https://github.com/user-attachments/assets/84c21407-58b6-4409-a4e5-b9434f919743)
![Screenshot 2025-06-10 124807](https://github.com/user-attachments/assets/215242a4-6e46-40b6-8e00-a33421b13ef3)
![Screenshot 2025-06-10 124824](https://github.com/user-attachments/assets/48a6c20e-fd39-44ce-ab92-3584f5407aba)



 <!-- Add real image path or keep as placeholder -->

## 🚀 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/sankum14/WallstreetGPT.git
cd WallstreetGPT
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Add your `.env` file**

```env
OPENAI_API_KEY=your_openai_key_here
```

4. **Run the app**

```bash
streamlit run app.py
```

## 🛠️ Project Structure

```
WallstreetGPT/
├── app.py                 # Main Streamlit app
├── ai.py                  # Handles LLM responses
├── config.py              # Environment & settings
├── equity_research.py     # Handles stock-specific analysis
├── general_market.py      # Handles broader market logic
├── utils.py               # Helper functions
├── .env                   # API keys & config (excluded from git)
├── README.md              # Project overview
└── LICENSE                # MIT License
```

## 🧠 Powered By

* 🧠 OpenAI (NIM / GPT)
* 📊 YFinance
* ⚙️ Streamlit
* 💻 Python

## 👨‍💼 Creator

Developed by [Sanjith Kumar Santhosh](https://www.linkedin.com/in/sanjith-kumar-santhosh-b5aab31b8), a passionate finance + AI engineer building next-gen trading and research tools.


