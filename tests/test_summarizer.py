import pytest

from app import summarizer


VALID_TEXT = (
    "Artificial intelligence is transforming many industries by "
    "enabling machines to perform tasks that traditionally required "
    "human intelligence. Modern AI systems can understand language, "
    "analyze information, recognize patterns, generate content, and "
    "assist people in making decisions."
)


def test_summarize_text_returns_summary(monkeypatch):
    """Test that valid text returns an LLM-generated summary."""

    expected_summary = (
        "- AI is transforming multiple industries.\n"
        "- Modern AI can understand language and analyze information.\n"
        "- LLMs can generate and process human-like text."
    )

    def mock_generate_text(prompt):
        assert VALID_TEXT in prompt
        return expected_summary

    monkeypatch.setattr(
        summarizer,
        "generate_text",
        mock_generate_text,
    )

    result = summarizer.summarize_text(VALID_TEXT)

    assert result == expected_summary


def test_summarize_text_rejects_empty_text():
    """Test that empty input is rejected."""

    with pytest.raises(
        ValueError,
        match="Text cannot be empty.",
    ):
        summarizer.summarize_text("")


def test_summarize_text_rejects_whitespace():
    """Test that whitespace-only input is rejected."""

    with pytest.raises(
        ValueError,
        match="Text cannot be empty.",
    ):
        summarizer.summarize_text("   ")


def test_summarize_text_rejects_short_text():
    """Test that text shorter than the minimum length is rejected."""

    with pytest.raises(
        ValueError,
        match="Text is too short",
    ):
        summarizer.summarize_text("Hello world")


def test_summarize_text_rejects_non_string_input():
    """Test that non-string input is rejected."""

    with pytest.raises(
        TypeError,
        match="Text must be a string.",
    ):
        summarizer.summarize_text(123)


def test_summarize_text_propagates_llm_error(monkeypatch):
    """Test that LLM errors are properly propagated."""

    def mock_generate_text(prompt):
        raise RuntimeError("LLM API request failed")

    monkeypatch.setattr(
        summarizer,
        "generate_text",
        mock_generate_text,
    )

    with pytest.raises(
        RuntimeError,
        match="LLM API request failed",
    ):
        summarizer.summarize_text(VALID_TEXT)