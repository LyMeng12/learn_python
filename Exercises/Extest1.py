from tabulate import tabulate

from Exercises.Exe4 import amount

amount=0
student_list=[]
while True:
    try:
        value=input("Enter Student Amount N: ")
        if value=="":
            amount=0
            break
        amount=int(value)
        if amount>=0:
            break
    except ValueError:
        print("please enter number value!")
if amount==0:
    while True:
        Name=input("Enter Student Name: ")
        Gender=input("Enter Student Gender: ")
        Gender.lower()
        while Gender!="male" and Gender!="female":
            Gender=input("Enter Student Gender Again: ")

        while True:
            try:
                Age = int(input("Enter Student Age: "))
                if Age>0 or Age<50:

                    break
            except ValueError:
                print("Invalid Input!")
        while True:
            try:
                Score = float(input("Enter Student Score: "))
                if Score>0 or Score<150:

                    break
            except ValueError:
                print("Invalid Input!")
        moer=input("Enter Student More(y/n): ")
        moer.lower()
        student={
            "Name":Name,
            "Gender":Gender,
            "Age":Age,
            "Score":Score,
        }
        student_list.append(student)
        while moer!="y" and moer!="n":
            moer=input("Enter Student More Again: ")
            moer.lower()
        if moer=="n":
            break
        elif moer=="y":
            print("===================================================")
elif amount!=0:
    for i in range(amount):
        Name = input("Enter Student Name: ")
        Gender = input("Enter Student Gender: ")
        Gender.lower()
        while Gender != "male" and Gender != "female":
            Gender = input("Enter Student Gender Again: ")

        while True:
            try:
                Age = int(input("Enter Student Age: "))
                if Age > 0 or Age < 50:
                    break
            except ValueError:
                print("Invalid Input!")
        while True:
            try:
                Score = float(input("Enter Student Score: "))
                if Score > 0 or Score < 150:
                    break
            except ValueError:
                print("Invalid Input!")
        student={
            "Name":Name,
            "Gender":Gender,
            "Age":Age,
            "Score":Score,
        }
        student_list.append(student)
        print("===================================================")

print("=============== Student Information ===============")
print(tabulate([[1.2345],[123.45],[12.345],[12345],[1234.5]]))