from app.summarizer import summarize_text


def main():
    print("=" * 50)
    print("             LLM TEXT SUMMARIZER")
    print("=" * 50)
    print("Enter the text you want to summarize.")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            text = input("Enter text: ")

            if text.strip().lower() == "exit":
                print("\nGoodbye!")
                break

            summary = summarize_text(text)

            print("\nSummary:")
            print("-" * 50)
            print(summary)
            print()

        except (ValueError, TypeError, RuntimeError) as exc:
            print(f"\nError: {exc}\n")

        except (KeyboardInterrupt, EOFError):
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()