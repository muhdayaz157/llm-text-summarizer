# LLM Text Summarizer

A simple Python-based text summarization tool powered by a Large Language Model (LLM).

The application accepts user-provided text, sends it to an LLM through an API, and returns a concise, structured summary.

## Features

- LLM-powered text summarization
- Reusable `summarize_text()` function
- Structured prompt engineering
- Concise bullet-point summaries
- Input validation
- API error handling
- Environment-based API credentials
- Configurable LLM provider
- Simple command-line interface
- No database or frontend required

## Project Structure

```text
llm-text-summarizer/
│
├── app/
│   ├── __init__.py
│   ├── llm_client.py
│   ├── prompts.py
│   └── summarizer.py
│
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt