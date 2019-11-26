menuList = []

def showBill():
    print("****** Chawapol's Shop ******")
    for number in range(len(menuList)):
        print(menuList[number])
    print("*****************************")

def totalPrice():
    total = 0
    for number in range(len(menuList)):
        total += int(menuList[number][1])
    print("Total", total)

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])

showBill()
totalPrice()

