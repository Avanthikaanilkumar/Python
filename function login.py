
key=[]
def main_menu():
    while True:
        print("Menu Driven")
        print("1.Registration\n 2.Login\n 3.Exit\n")
        choice=int(input("Enter the choice"))
        if choice==1:
            registration()
        elif choice==2:
            login()
        elif choice==3:
            quit()
def registration():
        d1={}
        a=input("Enter the name:")
        d1["name"]=a
        for i in key:
             if i["name"]==a:
                  print("Name Already exists")
             else:
                  print("Name not foumnd")
             
        e=int(input("Enter the password"))
        d1["password"]=e

        b=int(input("Enter the age:"))
        d1["age"]=b
        c=int(input("Enter the phone number"))
        d1["phone"]=c
        d=input("Enter the Address")
        d1["Address"]=d
        
        key.append(d1)
        print("Registration successful")
        print(key)
def login():
     username=input("Enter the Username")
     password=int(input("Enter the password"))
     
     for i in key:
          if i["name"]==username and i["password"]==password:
               print("Login Successful")
          else:
               print("Invalid username or password")

def quit():
     print("Exit")
main_menu()


        
     





