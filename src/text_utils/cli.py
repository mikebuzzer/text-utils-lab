import argparse

from text_utils.basic import word_count, keyword_extract

def main():
    parser = argparse.ArgumentParser(description="Simple text utilities")
    parser.add_argument("text", help="Input text to process")
    parser.add_argument(
        "--mode",
        choices=["word-count", "keywords"],
        default="word-count",
        help="Utility mode to run",
    )

    args = parser.parse_args()

    if args.mode == "word-count":
        print(word_count(args.text))
    elif args.mode == "keywords":
        print(keyword_extract(args.text))

if __name__ == "__main__":
    main()
