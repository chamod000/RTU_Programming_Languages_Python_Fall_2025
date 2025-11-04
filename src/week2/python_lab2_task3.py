"""
Lab 3.3 – Operator Frequency Counter + Expression Result

Goals:
- Practice using strings and dictionaries.
- Count character frequencies in user-provided text.
- Evaluate the arithmetic expression safely.

Instructions:
1. Ask the user for an arithmetic expression, e.g. "3 + 5 * (2 - 1) + 7 / 2".
2. Count how many times each operator occurs: + - * / ( )
3. Store counts in a dictionary.
4. Evaluate the expression.
5. Print the result and operator counts.
"""

# 1. Get input from the user
expression = input("Enter an arithmetic expression: ")

# 2. Define possible operator symbols
operators = ['+', '-', '*', '/', '(', ')']

# 3. Initialize frequency dictionary
operator_counts = {op: 0 for op in operators}

# 4. Count operator occurrences
for char in expression:
    if char in operators:
        operator_counts[char] += 1

# 5. Safely evaluate the arithmetic expression
try:
    result = eval(expression)
except Exception as e:
    result = f"Error evaluating expression: {e}"

# 6. Print results
print("\n=== Operator Frequency Counter ===")
for op, count in operator_counts.items():
    print(f"{op}: {count}")

print("\n=== Expression Result ===")
print(f"Expression: {expression}")
print(f"Result: {result}")
