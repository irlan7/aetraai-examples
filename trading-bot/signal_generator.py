"""
AetraAI Trading Signal Generator
"""
from openai import OpenAI

client = OpenAI(
    api_key="sk-aetra-YOUR_API_KEY",
    base_url="https://api.aetraai.com/api/v1"
)

def get_signal(pair: str, price: float) -> str:
    response = client.chat.completions.create(
        model="aetra-sonnet",
        messages=[
            {"role": "system", "content": "You are a professional forex analyst."},
            {"role": "user", "content": f"Analyze {pair} at {price}. Give BUY/SELL signal with entry, TP, SL."}
        ]
    )
    return response.choices[0].message.content

print(get_signal("XAUUSD", 2345.50))
