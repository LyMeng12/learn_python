# if fix -> enter price for discount($) price-discount
# if pct => enter dicount(%,0->100)

print("----Enter Product Information----")
name = input("Enter Product Name: ")
qty=int(input("Enter Quantity(1-10): "))
while qty<0 or qty>10:
    qty=int(input("Enter Quantity(1-10) again: "))
price=float(input("Enter Price(1-100): "))
while price<0 or price>100:
    price=float(input("Enter Price(1-100) again: "))
discount=input("Enter Discount (fix-pct): ")
while discount  != "pct" and discount  != "fix":
    discount=input("Enter Discount (fix-pct) again: ")
Grand=0
if discount=="pct":
    pDiscount=float(input("Enter Discount ($): "))
    price*=qty
    Grand=price-pDiscount
    print("-" * 50)
    print("DiscountType: ", discount)
    print("Discount Price: ", pDiscount, "$")
    print("Total: ", price, "$")
    print("Grand Total: ", Grand, "$")
    print("-" * 50)

elif discount=="fix":
    pDiscount=float(input("Enter Discount (%,0-100): "))
    while pDiscount>100 or pDiscount<0:
        pDiscount=float(input("Enter Discount (%,0-100) again: "))
    price *= qty
    Grand=(pDiscount*price)/100
    print("-"*50)
    print("DiscountType: ",discount)
    print("Discount Price: ",Grand,"$")
    print("Total: ",price,"$")
    print("Grand Total: ",(price-Grand),"$")
    print("-" * 50)

