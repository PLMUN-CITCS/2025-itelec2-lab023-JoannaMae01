"""
Word Counter in a Sentence

This program takes a sentence from the user and counts the number of words in it.
It follows a modular approach using functions for input handling and word counting.
"""

def get_sentence_input() -> str:
    """
    Prompts the user to enter a sentence.

    Returns:
        str: The user's input sentence.
    """
    return input("Enter a sentence: ").strip()

def count_words(input_sentence: str) -> int:
    """
    Counts the number of words in the given sentence.

    Args:
        input_sentence (str): The sentence to count words from.

    Returns:
        int: The number of words in the sentence.
    """
    return len(input_sentence.split())

# Main Program Flow
if __name__ == "__main__":
    user_sentence = get_sentence_input()  # Renamed from `sentence`
    word_count = count_words(user_sentence)
    print(f"The sentence has {word_count} words.")
