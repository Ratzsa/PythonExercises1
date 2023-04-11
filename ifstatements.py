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
if numb3 > largerest:
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
    print("You were born in the 1990s.")
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