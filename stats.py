def get_num_words(text: str) -> int:
    """Takes a string as input and returns the number of words in the string."""
    words = text.split()
    return len(words)


def get_character_count(text: str) -> dict[str, int]:
    """Takes a string as input and returns a dictionary with the number of times each
    character appears in the string
    """
    character_count: dict[str, int] = {}
    for char in text:
        lower_char = char.lower()
        character_count[lower_char] = character_count.get(lower_char, 0) + 1
    return character_count


def most_frequent_characters(character_count: dict[str, int]) -> list[dict]:
    """Takes a character count dictionary and returns a sorted list of dictionaries.

    Each dictionary has two key-value pairs: one for the character itself and one for the
    character's count.  The list is sorted in decreasing length of character frequency.
    """
    most_frequent_chars = []
    for char, count in sorted(character_count.items(), key=lambda x: -x[1]):
        most_frequent_chars.append({"char": char, "count": count})
    return most_frequent_chars
