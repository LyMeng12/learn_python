print("==============================")
print("\tShopping Cart System")
print("==============================")
print("Welcome to Shopping Cart System.")
item=[]
while True:
    print("=============================")
    print("1.Add item")
    print("2.View items")
    print("3.Delete item")
    print("4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("=============================")
        print("Added Item")
        item.append(input("Enter your task: "))
    elif choice==2:
        print("=============================")
        print("View Items")
        il=0
        for i in item:
            il += 1
            print("ID:",il,"Item Name:",i)
    elif choice==3:
        print("=============================")
        print("Delete Item")
        while True:
            id = 0
            for i in item:
                id += 1
                print("ID:", id, "Item Name:", i)
            name = input("Enter your name: ")
            if name not in item:
                print("Item Not Found")
            else:
                item.remove(name)
                print("Item Removed Already!")
                break
            print("=============================")
    elif choice==4:
        break
    else:
        print("Invalid Choice")
print("==============================")
print("System End !")
