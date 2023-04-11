import termcolor
import os

# List 1
bigNumbers = list()
for numRequest in range(0, 4):
    bigNumbers.append(int(input("Enter number: ")))
print(f"Largest: {max(bigNumbers)}")
tempbuffer = input("Press enter.")
os.system('cls')

# List 2
board = []
square = 1
pawnB = u'\u265F'
pawnW = u'\u2659'
loopIndex = 0
for i in range(8):
   row = [' ' for i in range(8)]
   board.append(row)

for i in range(8):
    board[1][i] = pawnB
    board[6][i] = pawnW

for rows in board:
    for index in rows:
        if square % 2 == 0:
            termcolor.cprint(index + ' ', 'black', 'on_light_grey', end = '')
        else:
            termcolor.cprint(index + ' ', 'white', 'on_dark_grey', end = '')
        square += 1
    print("")
    square += 1
temp = input("Press enter")
os.system('cls')

# List 3
def createAccount(accountList:dict) -> dict:
    os.system('cls')
    tempAccNum = input("Enter account number: ")
    if tempAccNum in accountList:
        print("Account number already exists.")
        temp = input("Press enter")
        return accountList
    else:
        tempAccMoney = int(input("Enter money in account: "))
        if tempAccMoney:
            accountList[tempAccNum] = tempAccMoney
        else:
            temp = input("Input error.\nPress enter")
            return accountList
    return accountList

def deleteAccount(accountList:dict) -> dict:
    os.system('cls')
    tempAccNum = input("Enter account number to delete: ")
    if tempAccNum not in accountList:
        print("Account does not exist.")
        temp = input("Press enter")
        return accountList
    else:
        del accountList[tempAccNum]
        return accountList
    
def listAccNumbers(accountList:dict):
    os.system('cls')
    for accNums in accountList:
        print(accNums)
    temp = input("Press enter")

def listSumOfMoney(accountList:dict):
    os.system('cls')    
    print("Total amount in all accounts:")
    print(sum(accountList.values()))
    temp = input("Press enter")

def listAccAndMoney(accountList:dict):
    os.system('cls')
    for accountNum, money in accountList.items():
        print(f"{accountNum}: {money}")
    temp = input("Press enter")

listThreeMenu = True
accounts = {}
menuSelection = ''
while listThreeMenu:
    os.system('cls')
    print("Menu\n1. Create account\n2. Delete account\n3. List all account numbers\n4. List total sum of money\n5. List all account numbers and money\n6. Exit\n")
    menuSelection = input(">> ")

    match menuSelection:
        case '1':
            createAccount(accounts)
        case '2':
            deleteAccount(accounts)
        case '3':
            listAccNumbers(accounts)
        case '4':
            listSumOfMoney(accounts)
        case '5':
            listAccAndMoney(accounts)
        case '6':
            listThreeMenu = False
        case _:
            print("Input error.\n")
            listThreeMenu = True
