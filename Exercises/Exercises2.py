# if fix -> enter price for discount($) price-discount
# if pct => enter dicount(%,0->100)

print("----Enter Product Information----")
name = input("Enter Product Name: ")
qty=input("Enter Quantity(1-10): ")
while not qty.isdigit() or int(qty)<1 or int(qty)>10:
    qty=input("Enter Quantity(1-10) again: ")
x=float(qty)
while True:
    try:
        price=float(input("Enter Price(1-100): "))
        while price<1 or price>100:
            price=float(input("Enter Price(1-100) again: "))
        break
    except ValueError:
        print("Invalid input! Please enter  number.")
discount=input("Enter Discount (fix-pct): ")
while discount  != "pct" and discount  != "fix":
    discount=input("Enter Discount (fix-pct) again: ")
Grand=0
if discount=="pct":
    while True:
        try:
            pDiscount=float(input("Enter Discount (1-100): "))
            while pDiscount<1 or pDiscount>100:
                pDiscount=float(input("Enter Discount (1-100) again: "))
            break
        except ValueError:
            print("Invalid input! Please enter number.")
    price*=x
    Grand=price-pDiscount
    print("-" * 50)
    print("DiscountType: ", discount)
    print("Discount Price: ", pDiscount, "$")
    print("Total: ", price, "$")
    print("Grand Total: ", Grand, "$")
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
    price *= x
    Grand = (price*pDiscount) / 100
    print("-"*50)
    print("DiscountType: ",discount)
    print("Discount Price: ",Grand,"$")
    print("Total: ",price,"$")
    print("Grand Total: ",(price-Grand),"$")
    print("-" * 50)

