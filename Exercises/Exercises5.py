from tabulate import tabulate
rank=[]

Student=[]

amount=0

while True:
    print("-" * 50)
    while True:
        name = input("Enter your name  (letter <= 50): ")
        if name != "" and len(name) < 50:
            break

    genser = input("Enter your gender (M/F): ")
    genser=genser.upper()
    while genser != "M" and genser != "F":
        genser = input("Enter your gender again(M/F): ")
    group =input("Enter your group: ")

    if amount == 0:
        try:
            amount = int(input("Enter Subject Amount: "))
            while amount < 0:
                amount = int(input("Enter Subject Amount again: "))
        except ValueError:
            print("Invalid input! Please enter number.")


    i=0
    subject = []
    totalScore=0
    while i < amount:
        print("-"*50)
        subjectName=input("Enter Subject Name: ")
        try:
            subjectScore = float(input("Enter Subject Score(0-120): "))
            while subjectScore < 1 or subjectScore > 121:
                subjectScore = float(input("Enter Subject Score(0-120): "))
        except ValueError:
            print("Invalid input! Please enter number.")
        Subject=dict(SubjectName=subjectName, SubjectScore=subjectScore)
        subject.append(Subject)
        i+=1
        totalScore+=subjectScore
    ave=(totalScore/(120*amount))*100
    rank.append(totalScore)
    student = dict(Name=name, Gneder=genser, Group=group,Subject=subject,TotalScore=totalScore,Average=ave)
    Student.append(student)
    again = input("Add more Student(Y/N): ")
    again=again.upper()
    while again != "Y" and again != "N":
        again = input("Add more Student(Y/N): ")
    if again == "N":
        break

rank.sort(reverse=True)
top_rank=[]
for i in range(len(rank)):
    for j in range(len(rank)):
        if rank[i]==rank[j]:
            if rank[j] not in top_rank:
                top_rank.append(rank[j])


table=[]
top=1
count=1
print("-"*50)
for i in range(len(top_rank)):
    for j in range(len(Student)):
        if Student[j]["TotalScore"] == top_rank[i] :
            if top<=3:
                table.append([top, Student[j]["Name"], Student[j]["TotalScore"]])
                count+=1
    top=count
headers = ["top", "Name", "Score"]

print(tabulate(table, headers=headers, tablefmt="github"))
print("-"*50)

id=1
for i in range(len(Student)):
    if Student[i]["Average"] < 50:
        table=[]
        print(f"{id}.{Student[i]["Name"]}")
        print("-" * 50)
        headers = ["Subject Name", "Subject Score"]
        for j in range(amount):
            if Student[i]["Subject"][j]["SubjectScore"]<60:
                table.append([Student[i]["Subject"][j]["SubjectName"],Student[i]["Subject"][j]["SubjectScore"]])
        print(tabulate(table, headers=headers, tablefmt="github"))
        id+=1
        print("-"*50)


