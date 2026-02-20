import json




class Banking:
    def __init__(self):
        self.User=[]
        self.loginUser=[]
        self.data="Account.json"
        self.login_save="Login.json"
        self.load_user()
    def addUser(self,Name,gender,age,password,phone,role,money):
        Users={
            'id':len(self.User)+1,
            'name':Name,
            'Gender':gender,
            'Age':age,
            'Password':password,
            'Phone':phone,
            'role':role,
            'Money':money
        }
        self.User.append(Users)
        self.save_user()
        print(f"Added User {Name} successfully")
    def login(self,name,password):
        for user in self.User:
            if user['name']==name and user['Password']==password:
                if user['role']=='admin':
                    self.loginUser.append(user)
                    self.login_user()
                    return "admin"
                elif user['role']=='customer':
                    self.loginUser.append(user)
                    self.login_user()
                    return "customer"
        return "User not found!"
    def save_user(self):
        """ Save user """
        with open(self.data,"w") as file:
            json.dump(self.User,file,indent=2)

    def load_user(self):
        """ Load user """
        try:
            with open(self.data,"r") as file:
                self.User=json.load(file)
        except FileNotFoundError:
            self.User=[]
            print("User not found!")

    def login_user(self):
        """ Login user """
        with open(self.login_save,"w") as file:
            json.dump(self.loginUser,file,indent=2)
    def clear(self):
        with open(self.login_save,"w") as file:
            file.close()
        print("Logout successfully!")




def customer():
    bank=Banking()
    print("=====Welcome Customer=====")
    while True:
        print("1.Profile User")
        print("2.Money User")
        print("3.Payment Money")
        print("4.Report User")
        print("5.Exit")
        choice=int(input("Enter your choice: "))
        try:
            if choice==1:
                print("1.Profile User")
            elif choice==2:
                print("2.Money User")
            elif choice==3:
                print("3.Payment Money")
            elif choice==4:
                print("4.Report User")
            elif choice==5:
                bank.clear()
                break
        except ValueError:
            print("Please enter a valid choice.")

def admin():
    bank=Banking()
    print("=====Welcome Admin=====")
    while True:
        print("1.Profile Admin")
        print("2.List Users")
        print("3.Add User")
        print("4.Delete User")
        print("5.Update User")
        print("6.Exit")
        choice=int(input("Enter your choice: "))
        try:
            if choice==1:
                print("1.Profile Admin")
            elif choice==2:
                print("2.list Users")
            elif choice==3:
                print("3.Add User")
            elif choice==4:
                print("4.Delete User")
            elif choice==5:
                print("5.Update User")
            elif choice==6:
                bank.clear()
                break
        except ValueError:
            print("Please enter a valid choice.")





def main():
    bank = Banking()
    while True:
        print("=====Welcome to Banking=====")
        print()
        try:
            print("=====Welcome to From Login=====")
            print("1. Login User")
            print("2. Register User")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:

                while True:
                    print("If you went to close you can \"close\" .")
                    print("=====Welcome to From Login User=====")

                    name = input("Enter your name: ")
                    if name == "close":
                        break
                    password = input("Enter your password: ")
                    user = bank.login(name, password)
                    if user == "admin":
                        admin()

                    elif user == "customer":
                        customer()

                    else:
                        print(user)
            elif choice == 2:
                print("=====Welcome to Register User=====")
                name = input("Enter your name: ")
                print("Choose Your Gender.")
                print("1.Male/2.Female")
                gen = int(input("Enter your gender: "))
                if gen == 1:
                    gender = "Male"
                elif gen == 2:
                    gender = "Female"
                age = int(input("Enter your age: "))
                password = input("Enter your password: ")
                phone = input("Enter your phone: ")
                role = "customer"
                money = float(input("Enter your money: "))
                try:
                    bank.addUser(name, gender, age, password, phone, role, money)
                except ValueError:
                    print("Create not successfully!")

            elif choice == 3:
                break
        except ValueError:
            print("Please enter a Number choice.")
if __name__ == "__main__":
    main()
    print("System end!")






