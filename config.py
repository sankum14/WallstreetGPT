import os
from dotenv import load_dotenv

load_dotenv()

NIM_API_KEY = os.getenv("NIM_API_KEY")
NIM_MODEL = "meta/llama-4-maverick-17b-128e-instruct"
NIM_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

