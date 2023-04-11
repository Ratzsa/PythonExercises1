import random
"""
Variabler
"""

# String och int
nameStr = "Daniel"
ageInt = random.randint(18, 99)

print(f"My name is {nameStr} and I am {ageInt} years old.")

# För och efternamn
firstName = input("First name: ")
lastName = input("Last name: ")
print(f"Your name: {lastName} {firstName}")

#Operators
numOne = int(input("Enter number a: "))
numTwo = int(input("Enter number b: "))

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
nOne = float(input("Enter number a: "))
nTwo = float(input("Enter number b: "))

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