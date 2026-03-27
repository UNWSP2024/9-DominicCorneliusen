#Title: Random Number File Writer
#Author: Dominic Corneliusen
#Date last modified: 3/26/2026

#Start
import random
fileName = str(input("Enter the name that you want your \n number file to be called: "))
randomNumberCount = int(input("Enter the number of random numbers you want (1-1000): "))
isNumberValid = False
while not isNumberValid:
    if randomNumberCount <= 0 or randomNumberCount > 1000:
        print("Sorry, you have to choose a number between 1 and 1000. \n Please try again.")
        randomNumberCount = int(input("Enter the number of random numbers you want (1-1000): "))
    else:
        isNumberValid = True
with open(fileName, "w") as newFile:
    for number in range(1, randomNumberCount):
        newFile.write(str(random.randint(1, 500)))
        newFile.write("\n")
