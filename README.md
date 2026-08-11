# LLM Text Summarizer

A lightweight Python-based LLM application that generates concise, structured summaries from user-provided text.

The project demonstrates practical LLM application development including prompt engineering, input validation, API integration, error handling, multi-provider support, and automated testing.

## Features

- LLM-powered text summarization
- Reusable `summarize_text()` function
- Structured prompt engineering
- Consistent bullet-point output
- Input validation
- LLM/API error handling
- Environment-based API credentials
- OpenAI and Google Gemini provider support
- Configurable LLM models
- Automated tests with pytest
- Simple command-line interface
- No database or frontend required

## Architecture

```text
User Input
    │
    ▼
CLI (main.py)
    │
    ▼
summarize_text()
    │
    ├── Input Validation
    │
    ▼
Prompt Construction
    │
    ▼
generate_text()
    │
    ├───────────────┐
    ▼               ▼
 Gemini           OpenAI
    │               │
    └───────┬───────┘
            ▼
      Generated Text
            │
            ▼
         Summary