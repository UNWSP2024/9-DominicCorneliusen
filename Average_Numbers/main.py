#Title: Average Numbers
#Author: Dominic Corneliusen
#Date last modified: 3/26/2026

#Start
added_number = 0
try:
    with open('numbers.txt', 'r') as numbers_file:
        for number in numbers_file:
            try:
                added_number = added_number + int(number)
            except ValueError:
                print(f"Could not convert '{number.strip()}' to an integer.")
    added_number = int(added_number)
    average = round(added_number / 250, 1)
    print('The average number is', average)
except IOError:
    print("An error occurred while trying to read the file.")