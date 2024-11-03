# Mad Libs Generator

# Get user inputs
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
place = input("Enter a place: ")
adjective2 = input("Enter another adjective: ")
animal = input("Enter an animal: ")
food = input("Enter a type of food: ")
verb2 = input("Enter another verb: ")
adjective3 = input("Enter one more adjective: ")

# Create the story
story = f"""
Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} every day. 
One day, the {noun1} decided to visit the {place}. On the way, the {noun1} met a {adjective2} {animal} who was looking for {food}. 
They decided to {verb2} together and became best friends. They had many {adjective3} adventures and lived happily ever after.
"""

# Print the story
print("\nHere is your story:")
print(story)
