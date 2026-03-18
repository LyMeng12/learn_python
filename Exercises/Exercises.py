print("===========================")
print("\tTodo List System")
print("===========================")
task=[]
mark=[]
while True:
    print("===========================")
    print("1. Add task")
    print("2. View task")
    print("3. Mark task")
    print("4. Delete task")
    print("5. Exit")
    choice =int(input("Choose: "))
    if choice == 1:
        print("Add task")
        while True:
            name = input("Enter task name: ")
            if name not in task:
                task.append(name)
                print("Task already exists")
                break
            else:
                print("it have .")
    elif choice == 2:
        print("View task")
        id = 0
        for i in task:
            id+=1
            print("ID:",id,".",i)
            for j in mark:
                num=str(id-1)
                if num in j:
                    print("Marking task:",end=" ")
                    for x in j:
                        if x!=num:
                            print(x,end="")
                    print()
            print("========================")
    elif choice == 3:
        id=0
        for name in task:
            id+=1
            print("ID:",id,"Name:", name)
        while True:
            id=0
            name = int(input("Enter task id: "))
            for i in task:
                if id==name-1:
                    marks = input("Enter done: ")
                    done=str(id)
                    mark.append(marks+done)
                    print("Mark done:", mark
                          )
                    break
                else:
                    print("Task does not exist")
                id+=1
            break
    elif choice == 4:
        print("Delete task")

        if name not in task:
            print("deleted already")
        else:
            print("Task does not exist")
    elif choice == 5:
        break
    else:
        print("Invalid Choice")
