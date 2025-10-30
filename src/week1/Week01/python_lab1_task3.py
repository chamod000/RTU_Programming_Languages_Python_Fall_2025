"""
Task 3 Function with Combined Logic

"""

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    # remove leading/trailing spaces
    clean_text = text.strip()

    # total number of characters
    char_count = len(clean_text)

    # total number of words
    word_count = len(clean_text.split())

    # check if the word "python" exists (ignore case)
    has_python = "python" in clean_text.lower()

    # return results as a tuple
    return (char_count, word_count, has_python)

if __name__ == "__main__":
    # ask user for input
    sentence = input("Enter a sentence: ")

    # call the function
    chars, words, contains_python = analyze_sentence(sentence)

    # print results in a friendly format
    print(f"Total characters: {chars}")
    print(f"Total words: {words}")
    print(f"Contains 'Python': {contains_python}")
