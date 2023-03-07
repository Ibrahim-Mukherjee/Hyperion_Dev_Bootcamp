with open(r"Downloads\DOB.txt",'r+') as f:
    lines = f.readlines()
    print(lines)

names = []
birthdates = []

for line in lines:
    data = line.split()
    name = ' '.join(data[:2])
    names.append(name)
    birthdate = ' '.join(data[2:5])
    birthdates.append(birthdate)

print("Names:")
for name in names:
    print(name)

print("\nBirthdates:")
for birthdate in birthdates:
    print(birthdate)
# This script reads in each line of the 'names_and_birthdays.txt' file, 
# splits each line into individual words, 
# and then extracts the first two words as the name and the next three words as the birthdate. 
# It then appends the names and birthdates to separate lists





 
