class Banking:
    def __init__(self):
        self.User=[]
        self.data="Account.json"
    def addUser(self,Name,gender,age,password,phone,role,money):
        Users={
            'id':len(self.User)+1,
            'name':Name,
            'Gender':gender,
            'Age':age,
            'Password':password,
            'Phone':phone,
            'Role':role,
            'Money':money
        }
        self.User.append(Users)

        print(f"Added User {Name} successfully")
    def login(self,name,password):
        for user in self.User:
            if user['name']==name and user['password']==password:
                if user['role']=='admin':
                    return "admin"
                elif user['role']=='customer':
                    return "customer"
        return print("User not found!")

def main():
        bank=Banking()
        while True:
            print("=====Welcome to Banking=====")
            print()
            try:
                print("1. Login User")
                print("2. Register User")
                print("3. Exit")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    print("=====Welcome to From Login User=====")
                    name=input("Enter your name: ")
                    password=input("Enter your password: ")
                    if bank.login(name,password)=="admin":
                        print("=====Welcome Administrator=====")
                    elif bank.login(name,password)=="customer":
                        print("=====Welcome Customer=====")
                    else:
                        bank.login(name,password)
                elif choice==2:
                    print("=====Welcome to Register User=====")
                    name=input("Enter your name: ")
                    print("Choose Your Gender.")
                    print("1.Male/2.Female")
                    gen=int(input("Enter your gender: "))
                    if gen==1:
                        gender="Male"
                    elif gen==2:
                        gender="Female"
                    age=input("Enter your age: ")
                    password=input("Enter your password: ")
                    phone=input("Enter your phone: ")
                    role="customer"
                    money=input("Enter your money: ")

                elif choice==3:
                    break
            except ValueError:
                print("Please enter a Number choice.")



if __name__ == "__main__":
    main()



