import re
import string  

text = "I love apples, bananas, and cherries. Mangoes and strawberries are also great."


fruits = {"apple", "apples", "banana", "bananas", "cherry", "cherries", "mango", "mangoes", "strawberry", "strawberries"}


identified_fruits = [word for word in re.findall(r'\b\w+\b', text.lower()) if word in fruits]

print(identified_fruits)
print()

alphabet_to_number = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)}


numerical_fruits = [[alphabet_to_number[char]for char in fruit]for fruit in identified_fruits]
print("Numerical Representation of Identified Fruits:", numerical_fruits)

#print(alphabet_to_number)

