# 1. Plussa
def addStrings(strOne, strTwo) -> str:
    return strOne + strTwo

a = "Hej, idag "
b = "är det tisdag"
print(addStrings(a, b))

# 2. Moms
def calculateVAT(moneyIn) -> float:
    return moneyIn * 0.20

print("")
print(round(calculateVAT(100), 2))
print(round(calculateVAT(78), 2))
print(round(calculateVAT(65), 2))
print(round(calculateVAT(5237), 2))

# 3. Ålder
def checkAge(ageIn) -> bool:
    return ageIn > 17

print("")
print("Age in: 14")
age = 14
if(checkAge(age)):
    print("Adult!")
else:
    print("Not adult!")

print("Age in: 65")
age = 65
if(checkAge(age)):
    print("Adult!")
else:
    print("Not adult!")

print("Age in: 17")
age = 17
if(checkAge(age)):
    print("Adult!")
else:
    print("Not adult!")

print("Age in: 18")
age = 18
if(checkAge(age)):
    print("Adult!")
else:
    print("Not adult!")

# 4. Längsta ordet
def findLongestWord(wordArray) -> str:
    return max(wordArray, key = len)

print("")
arrayOfWords = ["chocolate", "ice", "teddybear", "batman", "trainstation", "terrifying", "spider", "sky", "frankenstein", "tower", "computers"]
longestWord = findLongestWord(arrayOfWords)
print(f"The longest word was: {longestWord}")

# 5. Räkna skatt
def calculateTaxesOnSalary(salaryIn) -> float:
    if salaryIn > 30000:
        return salaryIn * 0.28
    if salaryIn > 15000:
        return salaryIn * 0.33
    else:
        return salaryIn * 0.12

print("")
salA = 35789
salB = 12899
salC = 25780
salD = 30000
salE = 15000

print(f"{salA}: {round(calculateTaxesOnSalary(salA), 2)}")
print(f"{salB}: {round(calculateTaxesOnSalary(salB), 2)}")
print(f"{salC}: {round(calculateTaxesOnSalary(salC), 2)}")
print(f"{salD}: {round(calculateTaxesOnSalary(salD), 2)}")
print(f"{salE}: {round(calculateTaxesOnSalary(salE), 2)}")