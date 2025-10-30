"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

import re

def count_characters(text):
    """Count non-space characters in a string (ignores all whitespace)."""
    return sum(1 for ch in text if not ch.isspace())

def count_words(text):
    """Count number of words in a string."""
    return len(text.split())

def extract_numbers(text):
    """Return list of integers found in text (supports negatives)."""
    # Find sequences like -12 or 45
    return [int(m) for m in re.findall(r'-?\d+', text)]

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    chars = count_characters(text)
    words = count_words(text)
    nums = extract_numbers(text)
    total = sum(nums) if nums else 0
    avg = (total / len(nums)) if nums else None
    return {
        "characters": chars,
        "words": words,
        "numbers": nums,
        "total": total,
        "average": avg
    }

if __name__ == "__main__":
    s = input("Enter a sentence with some numbers: ")
    result = analyze_text(s)

    print("\n=== Analysis Summary ===")
    print(f"Non-space characters : {result['characters']}")
    print(f"Word count           : {result['words']}")
    print(f"Integers found       : {result['numbers']}")
    print(f"Sum of numbers       : {result['total']}")
    avg_text = f"{result['average']:.2f}" if result['average'] is not None else "N/A"
    print(f"Average of numbers   : {avg_text}")
