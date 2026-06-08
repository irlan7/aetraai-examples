# AetraAI API Examples

Official examples for [AetraAI API](https://aetraai.com/api-developer) — OpenAI-compatible AI platform for trading, coding & Web3.

## Quick Start

Get your free API key at **https://aetraai.com/api-dashboard**

## Base URL
https://api.aetraai.com/api/v1
## Available Models

| Model | Description | Best For |
|-------|-------------|----------|
| `aetra-haiku` | Fast & cheap | Simple tasks |
| `aetra-sonnet` | Balanced | Most use cases |
| `aetra-opus` | Most powerful | Complex reasoning |
| `aetra-coder` | Code specialist | 15+ languages |
| `aetra-trader` | Trading analyst | Forex & crypto |
| `aetra-chain` | Web3 specialist | Solidity & DeFi |

## Examples

- [Python](./python/) — Basic chat + streaming
- [Go](./go/) — Go client
- [JavaScript](./javascript/) — Node.js
- [Trading Bot](./trading-bot/) — Forex signal generator

## Drop-in OpenAI Replacement

```python
# Before
client = OpenAI(api_key="sk-...")

# After — same code, just change 2 lines!
client = OpenAI(
    api_key="sk-aetra-YOUR_KEY",
    base_url="https://api.aetraai.com/api/v1"
)
```

## Links

- [API Dashboard](https://aetraai.com/api-dashboard)
- [API Docs](https://aetraai.com/api-developer)
- [Platform](https://aetraai.com/platform)
