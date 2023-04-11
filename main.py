"""
Variabler
"""

# String och int
nameStr = "Daniel"
ageInt = 40

print(f"Jag heter {nameStr} och är {ageInt} år gammal.")

# För och efternamn
firstName = input("Skriv in ditt förnamn: ")
lastName = input("Skriv in ditt efternamn: ")
print(f"Du heter: {lastName} {firstName}")

#Operators
numOne = int(input("Mata in tal 1: "))
numTwo = int(input("Mata in tal 2: "))
"""
Tal 1 upphöjt till tal 2
Tal 1 gånger tal 2
Tal 1 delat med tal 2 (kolla datatypen på resultatet)
Tal 1 plus tal 2
Tal 1 minus tal 2
Tal 1 % tal 2 (heltalsdividerat)
Tal 1 // tal 2 (rest)
"""

result = numOne ** numTwo
print(f"a ** b: {result}")

result = numOne * numTwo
print(f"a * b: {result}")

result = numOne / numTwo
print(f"a / b: {result}")
print(f"Datatype of result: {type(result)}")

result = numOne + numTwo
print(f"a + b: {result}")

result = numOne - numTwo
print(f"a - b: {result}")

result = numOne % numTwo
print(f"a % b: {result}")

result = numOne // numTwo
print(f"a // b: {result}")

# Samma sak fast med flyttal
nOne = float(input("Mata in tal 1: "))
nTwo = float(input("Mata in tal 2: "))
"""
Tal 1 upphöjt till tal 2
Tal 1 gånger tal 2
Tal 1 delat med tal 2 (kolla datatypen på resultatet)
Tal 1 plus tal 2
Tal 1 minus tal 2
Tal 1 % tal 2 (heltalsdividerat)
Tal 1 // tal 2 (rest)
"""

result = nOne ** nTwo
print(f"a ** b: {result}")

result = nOne * nTwo
print(f"a * b: {result}")

result = nOne / nTwo
print(f"a / b: {result}")
print(f"Datatype of result: {type(result)}")

result = nOne + nTwo
print(f"a + b: {result}")

result = nOne - nTwo
print(f"a - b: {result}")

result = nOne % nTwo
print(f"a % b: {result}")

result = nOne // nTwo
print(f"a // b: {result}")

# Strängoperatorer
nameOnce = input("Input your name: ")
nameMult = nameOnce * 5
print(f"Your name five times: {nameMult}")

# Jämför-operatorer
numberOneHundred = int(input("Enter number: "))
print(numberOneHundred >= 100)

"""
If-satser
"""
# IF1
ifNum = int(input("Enter a number: "))
if ifNum > 10:
    print("Number is higher than 10.")
elif ifNum < 10:
    print("Number is lower than 10.")
else:
    print("Number is 10 or something, I don't know, this is not even supposed to happen.")

# IF2
milkNum = int(input("How many milks are left? "))
if milkNum < 10:
    print("Order 30 milks.")
elif milkNum <= 20:
    print("Order 20 milks.")
else:
    print("Don't need to order milk.")

# IF3
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
largest = number2
if number1 > number2:
    largest = number1
print(f"Biggest number is {largest}.")

# IF4
numb1 = int(input("Enter first number: "))
numb2 = int(input("Enter second number: "))
numb3 = int(input("Enter third number: "))
largerest = numb1
if numb1 < numb2:
    largerest = numb2
if numb3 > numb2:
    largerest = numb3
print(f"Biggest number is {largerest}.")

# IF5
tripCategory = int(input("Enter category\n1. Retired\n2. Student\n3. Adult\nCategory: "))
if tripCategory == 1 or tripCategory == 2:
    print("Trip costs 20 money.")
elif tripCategory == 3:
    print("Trip costs 30 money.")
else:
    print("Incorrect input.")

# IF6
birthYear = int(input("Enter your year of birth: "))
if birthYear >= 1980 and birthYear < 1990:
    print("You were born in the 1980s.")
elif birthYear >= 1990 and birthYear < 2000:
    print("You were born int he 1990s.")
else:
    print("You were not born in the 80s or 90s.")

# IF7
country = input("Enter your country: ")
if country.lower() == "sweden" or country.lower() == "sverige" or country.lower() == "norway" or country.lower() == "norge" or country.lower() == "denmark" or country.lower() == "danmark":
    print("You live in Scandinavia!")
else:
    print("You do not live in Scandinavia.")

# IF8
money = float(input("Enter how much money you have: "))
discount = input("Do you have a discount? (y/n)")
discount = discount.lower()

if money >= 15 and money <= 25 and discount != "y":
    print("You can buy a small burger.")
if money >= 15 and money <= 25 and discount == "y":
    print("You can buy a small burger and fries.")
if money > 25 and money <= 50 and discount != "y":
    print("You can buy a big burger.")
if money > 25 and money <= 50 and discount == "y":
    print("You can buy a big burger and fries.")
if (money >= 60) or (money > 50 and money < 60 and discount == 'y'):
    print("You can buy a Happy Meal with soda.")

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