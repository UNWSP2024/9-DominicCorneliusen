#Title: Item Counter
#Author: Dominic Corneliusen
#Date last modified: 3/26/2026

#Start
with open('names.txt', 'r') as names:
    count = 0
    for name in names:
        count += 1
print("There are", str(count), "names in the file.")
