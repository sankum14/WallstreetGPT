import requests
import logging
from config import NIM_API_KEY, NIM_MODEL, NIM_URL

logging.basicConfig(level=logging.INFO)

def call_nvidia(messages):
    if not NIM_API_KEY:
        return "❌ NVIDIA API key not configured."

    try:
        logging.info(f"Sending request to NIM with model: {NIM_MODEL}")
        response = requests.post(
            NIM_URL,
            headers={
                "Authorization": f"Bearer {NIM_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": NIM_MODEL,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 800
            },
            timeout=60
        )
        response.raise_for_status()
        data = response.json()

        if "choices" in data and data["choices"]:
            return data["choices"][0]["message"]["content"].strip()
        return f"❌ Unexpected API response format: {data}"

    except requests.exceptions.Timeout:
        return "❌ Request timed out. Try again later."
    except requests.exceptions.RequestException as e:
        return f"❌ NIM API error: {e}"
    except Exception as e:
        return f"❌ Unexpected error: {e}"
