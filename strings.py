"""
Stränghantering
"""
# String 1
strOne = input("First string: ")
strTwo = input("Second string: ")
strThree = input("Third string: ")
strResult = strOne + strTwo + strThree
print(strResult)

# String 2
henloWorld = "Hello, World"
wCounter = 0
for letter in henloWorld:
    if henloWorld[wCounter].lower() == 'w':
        break
    wCounter += 1
print(f"First time the letter w shows up is at index {wCounter}.")

# String 3
kurre = "kurt andersson"
kurre = kurre.title()
print(kurre)

# String 4
stringToChange = "Detta är en sträng som du skall ändra"
newStringToChange = stringToChange.replace(' ', '*')
changeCounter = 0
for letter in newStringToChange:
    if letter == '*':
        changeCounter += 1
print(f"You changed {changeCounter} spaces to asterisks.")
print(newStringToChange)

# String 5
mailText = input("Enter email adress: ")
countAtSym = mailText.count('@')
lastPeriod = mailText.rfind('.')
lengthOfLast = len(mailText.split('.')[-1])
isRealEmail = True
if countAtSym != 1 or lastPeriod == -1 or lengthOfLast > 3 or lengthOfLast < 2:
    isRealEmail = False
print(f"Real email: {isRealEmail}")

# String 6
inputText = input("Enter text: ")
wordCount = 0
for character in inputText:
    if character == ' ':
        wordCount += 1
print(f"Your text contained {wordCount + 1} words.")

# String 7
textToReverse = input("Enter text: ")
reversedText = textToReverse[::-1]
if textToReverse.lower() == reversedText.lower():
    print("Palindrome!")
else:
    print("Not palindrome!")