import random

# Loop 1
print("For loop:")
for num in range(0, 11):
    print(num, end = ' ')

print("\nWhile loop:")
counter = 0
while counter <= 10:
    print(counter, end = ' ')
    counter += 1

# Loop 2
smallNum = int(input("\nInput the first number: "))
largeNum = int(input("Input the second number: "))
if smallNum > largeNum:
    smallNum, largeNum = largeNum, smallNum

for num in range(smallNum, largeNum):
    print(num, end = ' ')
print(largeNum)

while smallNum <= largeNum:
    print(smallNum, end = ' ')
    smallNum += 1
print(" ")

# Loop 3
runningLoop = True
while runningLoop:
    loopNumOne = int(input("Enter number a: "))
    loopNumTwo = int(input("Enter number b: "))
    print(f"Sum of a: {loopNumOne} and b: {loopNumTwo} is {loopNumOne + loopNumTwo}.")
    loopQuestion = input("Do you want to continue? (y/n): ").lower()
    match loopQuestion:
        case 'y':
            runningLoop = True
        case 'n':
            runningLoop = False # Går ta bort och använda case _
        case _:
            print("No idea what you want me to do here. Guess I'll just start over.")

# Loop 4
loopFourSum = 0
for times in range(0, 10):
    loopFourSum += int(input(f"Enter number({times + 1}): "))
print(f"Sum: {loopFourSum}")

# Loop 5
startNum = int(input("Enter a number: "))
startNum -= 1
while startNum > 0:
    print(startNum, end = ' ')
    startNum -= 1
print(" ")

# Loop 6
loopSix = True
minRoll = 1
maxRoll = 6
while loopSix:
    print("Rolling the dices...\nThe values are...")
    print(random.randint(minRoll, maxRoll))
    print(random.randint(minRoll, maxRoll))

    loopSixQuestion = input("Roll again? (yes/no or y/n): ").lower()
    match loopSixQuestion:
        case 'y':
            loopSix = True
        case 'yes':
            loopSix = True
        case _:
            print("Bye then!")
            loopSix = False