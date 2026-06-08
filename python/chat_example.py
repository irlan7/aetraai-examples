"""
AetraAI API - Python Example
Replace OpenAI in minutes!
"""
from openai import OpenAI

client = OpenAI(
    api_key="sk-aetra-YOUR_API_KEY",
    base_url="https://api.aetraai.com/api/v1"
)

# Basic chat
response = client.chat.completions.create(
    model="aetra-sonnet",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a Go REST API with JWT auth"}
    ]
)
print(response.choices[0].message.content)

# Streaming
stream = client.chat.completions.create(
    model="aetra-coder",
    messages=[{"role": "user", "content": "Write a Python FastAPI hello world"}],
    stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
