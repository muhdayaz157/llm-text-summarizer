from app.summarizer import summarize_text


def main():
    print("=== LLM Text Summarizer ===")
    print("Enter the text you want to summarize.")
    print("Type 'exit' to quit.\n")

    while True:
        text = input("Enter text: ")

        if text.strip().lower() == "exit":
            print("Goodbye!")
            break

        try:
            summary = summarize_text(text)

            print("\nSummary:")
            print(summary)
            print()

        except (ValueError, TypeError, RuntimeError) as exc:
            print(f"\nError: {exc}\n")


if __name__ == "__main__":
    main()