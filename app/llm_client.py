import os

from dotenv import load_dotenv
from google import genai
from openai import OpenAI


load_dotenv()


LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini").strip().lower()

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")


def _get_gemini_client():
    """Create and return a Gemini client."""
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set. "
            "Please add it to your .env file."
        )

    return genai.Client(
        api_key=api_key,
        http_options={"api_version": "v1"},
    )


def _get_openai_client():
    """Create and return an OpenAI client."""
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. "
            "Please add it to your .env file."
        )

    return OpenAI(api_key=api_key)


def generate_text(prompt: str) -> str:
    """
    Generate text using the configured LLM provider.

    The provider is selected through the LLM_PROVIDER
    environment variable.
    """

    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string.")

    prompt = prompt.strip()

    if not prompt:
        raise ValueError("Prompt cannot be empty.")

    try:
        if LLM_PROVIDER == "gemini":
            client = _get_gemini_client()

            interaction = client.interactions.create(
                model=GEMINI_MODEL,
                input=prompt,
            )

            output = interaction.output_text

        elif LLM_PROVIDER == "openai":
            client = _get_openai_client()

            response = client.responses.create(
                model=OPENAI_MODEL,
                input=prompt,
            )

            output = response.output_text

        else:
            raise ValueError(
                f"Unsupported LLM_PROVIDER: '{LLM_PROVIDER}'. "
                "Use 'gemini' or 'openai'."
            )

        if not output or not output.strip():
            raise RuntimeError(
                "The LLM returned an empty response."
            )

        return output.strip()

    except (ValueError, TypeError, RuntimeError):
        raise

    except Exception as exc:
        raise RuntimeError(
            f"LLM API request failed: {exc}"
        ) from exc