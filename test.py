mailText = input("Enter email adress: ")
countAtSym = mailText.count('@')
lastPeriod = mailText.rfind('.')
lengthOfLast = len(mailText.split('.')[-1])
isRealEmail = True
if countAtSym != 1 or lastPeriod == -1 or lengthOfLast > 3 or lengthOfLast < 2:
    isRealEmail = False
print(f"Real email: {isRealEmail}")