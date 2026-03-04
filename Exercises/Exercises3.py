price_list=[]
print("----Enter Product Information----")
while True:
    name = input("Enter Product Name: ")
    qty = input("Enter Quantity(1-10): ")

    while not qty.isdigit() or int(qty) < 1 or int(qty) > 10:
        qty = input("Enter Quantity(1-10) again: ")
    x = float(qty)
    while True:
        try:
            price = float(input("Enter Price(1-100): "))
            while price < 1 or price > 100:
                price = float(input("Enter Price(1-100) again: "))
            break
        except ValueError:
            print("Invalid input! Please enter  number.")
    print("-" * 50)
    more=input("Do you want to add more product? (y/n): ")
    print("-" * 50)
    more.lower()
    while more != "y" and more != "n":
        more=input("choose again (y/n): ")

    x=float(qty)
    if more == "y":

        price_list.append(x*price)
    elif more == "n":
        price_list.append(x*price)
        break
total=sum(price_list)
discount=input("Enter Discount (fix-pct): ")
while discount  != "pct" and discount  != "fix":
    discount=input("Enter Discount (fix-pct) again: ")
Grand=0
if discount=="pct":
    while True:
        try:
            pDiscount=float(input(f"Enter Discount (1$ - 100$): "))
            while pDiscount<1 or pDiscount>100:
                pDiscount=float(input(f"Enter Discount (1$ - 100$) again: "))
            break
        except ValueError:
            print("Invalid input! Please enter number.")

    Grand= total-pDiscount
    print("-" * 50)
    print("DiscountType: ", discount)
    print("Discount Price: ", pDiscount,"$")
    print("Total: ", total,"$")
    print("Grand Total: ", Grand,"$")
    print("-" * 50)

elif discount=="fix":
    while True:
        try:
            pDiscount=float(input("Enter Discount (%,0-100): "))
            while pDiscount<0 or pDiscount>100:
                pDiscount=float(input("Enter Discount (%,0-100) again: "))
            break
        except ValueError:
            print("Enter again number.")
    Grand = (total*pDiscount) / 100
    print("-"*50)
    print("DiscountType: ",discount)
    print("Discount Price: ",Grand,"$")
    print("Total: ",total,"$")
    print("Grand Total: ",(total-Grand),"$")
    print("-" * 50)
# print(total)
