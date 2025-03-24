import sys

from stats import get_character_count, get_num_words, most_frequent_characters


def get_book_text(filepath: str) -> str:
    """Takes a filepath as input and returns the contents of the file as a string."""
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def main() -> None:
    """Make a jazz noise here"""
    # Check that we have a book path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    # Get the statistics
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    most_frequent_chars = most_frequent_characters(character_count)
    # Print the report
    print(" BOOKBOT ".center(34, "="))
    print(f"Analyzing book found at {path}...")
    print(" Word Count ".center(34, "-"))
    print(f"Found {num_words} total words")
    print(" Character Count ".center(34, "-"))
    for char_count in most_frequent_chars:
        if char_count["char"].isalpha():
            print(f"{char_count['char']}: {char_count['count']}")

    print(" END ".center(34, "="))


if __name__ == "__main__":
    main()
