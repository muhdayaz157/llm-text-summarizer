import os
from functools import lru_cache

from dotenv import load_dotenv
from google import genai
from openai import OpenAI


load_dotenv()


SUPPORTED_PROVIDERS = {"gemini", "openai"}

DEFAULT_PROVIDER = "gemini"
DEFAULT_GEMINI_MODEL = "gemini-3.6-flash"
DEFAULT_OPENAI_MODEL = "gpt-5-mini"


@lru_cache(maxsize=1)
def _get_gemini_client():
    """Create and cache a Gemini client."""

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


@lru_cache(maxsize=1)
def _get_openai_client():
    """Create and cache an OpenAI client."""

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

    Args:
        prompt: Prompt sent to the selected LLM provider.

    Returns:
        Generated text from the LLM.

    Raises:
        TypeError: If prompt is not a string.
        ValueError: If prompt is empty or provider configuration is invalid.
        RuntimeError: If the LLM request fails or returns empty output.
    """

    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string.")

    prompt = prompt.strip()

    if not prompt:
        raise ValueError("Prompt cannot be empty.")

    provider = os.getenv(
        "LLM_PROVIDER",
        DEFAULT_PROVIDER,
    ).strip().lower()

    if provider not in SUPPORTED_PROVIDERS:
        raise ValueError(
            f"Unsupported LLM_PROVIDER: '{provider}'. "
            f"Supported providers: {', '.join(sorted(SUPPORTED_PROVIDERS))}."
        )

    try:
        if provider == "gemini":
            client = _get_gemini_client()

            model = os.getenv(
                "GEMINI_MODEL",
                DEFAULT_GEMINI_MODEL,
            )

            interaction = client.interactions.create(
                model=model,
                input=prompt,
            )

            output = interaction.output_text

        else:
            client = _get_openai_client()

            model = os.getenv(
                "OPENAI_MODEL",
                DEFAULT_OPENAI_MODEL,
            )

            response = client.responses.create(
                model=model,
                input=prompt,
            )

            output = response.output_text

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