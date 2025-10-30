"""
Task 2 – Greeting Function with String Manipulation

"""

def greet_user(name):
    """Return a greeting message after cleaning and capitalizing the name."""
    # remove leading/trailing spaces and capitalize first letter
    clean_name = name.strip().capitalize()
    return f"Hello, {clean_name}! Welcome to Python!"

if __name__ == "__main__":
    # ask user for their name
    user_input = input("Enter your name: ")
    # call the function and print result
    message = greet_user(user_input)
    print(message)
