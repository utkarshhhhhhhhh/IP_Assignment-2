menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
print("      MENU")
for item in range(len(menu)):
    print(menu[item][0].ljust(10),"₹",menu[item][1])
order=[]
while True:
    lst=list(map(int,input().split()))
    if lst!=[]:
        order.append(lst)
    else:
        break
print("____________________________________")1
print("              Bill")
print("____________________________________")
Total=0
Quantity=0
for i in range(len(order)):
    if order[i][0]==1:
        print("Samosa,".ljust(10),order[i][1],"items,  ₹".ljust(10),order[i][1]*15)
        Total+=order[i][1]*15
        Quantity+=order[i][1]
    elif order[i][0]==2:
        print("Idli,".ljust(10),order[i][1],"items,  ₹".ljust(10),order[i][1]*30)
        Total+=order[i][1]*30
        Quantity+=order[i][1]
    elif order[i][0]==3:
        print("Maggie,".ljust(10),order[i][1],"items,  ₹".ljust(10),order[i][1]*50)
        Total+=order[i][1]*50
        Quantity+=order[i][1]
    elif order[i][0]==4:
        print("Dosa,".ljust(10),order[i][1],"items,  ₹".ljust(10),order[i][1]*70)
        Total+=order[i][1]*70
        Quantity+=order[i][1]
    elif order[i][0]==5:
        print("Tea,".ljust(10),order[i][1],"items,   ₹".ljust(10),order[i][1]*10)
        Total+=order[i][1]*10
        Quantity+=order[i][1]
    elif order[i][0]==6:
        print("Coffee,".ljust(10),order[i][1],"items,  ₹".ljust(10),order[i][1]*20)
        Total+=order[i][1]*20
        Quantity+=order[i][1]
    elif order[i][0]==7:
        print("Sandwich,".ljust(10),order[i][1],"items,  ₹".ljust(10),order[i][1]*35)
        Total+=order[i][1]*35
        Quantity+=order[i][1]
    else:
        print("Invalid Input")
print("____________________________________")
print("Total:".ljust(10),Quantity,"items,  ₹".ljust(10),Total)
print("____________________________________")
print("                                   ")