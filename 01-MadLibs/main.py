def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

noun1 = get_input("noun")
adjective1 = get_input("adjective")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb2 = get_input("verb")

story = f"""
Once upon at time,there was a {adjective1} {noun1} who loved to {verb1} all day.

The End.
"""

print(story)