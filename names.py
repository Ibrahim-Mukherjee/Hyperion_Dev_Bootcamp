# Create an empty list to store the names
names = []

# Prompt the user to enter a name
name = input("Enter a name (or 'stop' to end): ")

# Use a while loop to continue prompting the user for names until they enter 'stop'
while name != 'stop':
    # Add the entered name to the list
    names.append(name)
    
    # Prompt the user for another name
    name = input("Enter a name (or 'stop' to end): ")

# Use a for loop to iterate over the list of names
for name in names:
    # Print each name
    print(name)


    
    







    







