amount=0
name=[]
gender=[]
age=[]
score=[]


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
                if Age>0 or Age<100:

                    break
            except ValueError:
                print("Invalid Input!")
        while True:
            try:
                Score = float(input("Enter Student Score: "))
                if Score>0:

                    break
            except ValueError:
                print("Invalid Input!")
        moer=input("Enter Student More(y/n): ")
        moer.lower()
        while moer!="y" and moer!="n":
            moer=input("Enter Student More Again: ")
            moer.lower()
        if moer=="n":
            name.append(Name)
            gender.append(Gender)
            age.append(Age)
            score.append(Score)
            break
        elif moer=="y":
            name.append(Name)
            gender.append(Gender)
            age.append(Age)
            score.append(Score)
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
                if Age > 0 or Age < 100:
                    break
            except ValueError:
                print("Invalid Input!")
        while True:
            try:
                Score = float(input("Enter Student Score: "))
                if Score > 0:
                    break
            except ValueError:
                print("Invalid Input!")
        name.append(Name)
        gender.append(Gender)
        age.append(Age)
        score.append(Score)
        print("===================================================")
ma=0
fe=0
index =0
sc=0;
bigger=score.copy()
bigger.sort(reverse=True)
print(bigger)
tname=[]

print("=============== Student Information ===============")
print("#\t\tName\t\tGender\t\tAge\t\tScore")
for i in range(len(name)):
    if gender[i]=="male":
        ma+=1
    elif gender[i]=="female":
        fe+=1
    print(f"{i+1}\t\t{name[i]}\t\t{gender[i]}\t\t{age[i]}\t\t{score[i]}")
    index=i+1
print("===================================================")
print(f"Total Student:{index}")
print(f"Male:{ma},Female:{fe}")

for i in range(len(name)):
    for j in range(len(name)):
        if score[j] == bigger[i]:
            tname.append(name[j])
            break

top_rank=[]
for i in range(len(score)):
    for j in range(len(score)):
        if score[j]==bigger[i]:
            if score[j] not in top_rank:
                top_rank.append(score[j])

# print(top_rank)
id=1
count=1
for i in range(len(top_rank)):
    for j in range(len(score)):
        if top_rank[i]==bigger[j]:
            print(f"Top {id} Score: {tname[j]} - {bigger[j]}" )
            count+=1
    id=count

print("===================================================")


