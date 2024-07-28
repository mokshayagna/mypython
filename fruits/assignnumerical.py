def convert_to_numbers(text, mapping):
    return [mapping[char] for char in text.lower() if char in mapping]

# Example text
text = "hello"

# Using alphabetical order mapping
alphabet_to_number = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)}
numbers = convert_to_numbers(text, alphabet_to_number)

print(numbers)
