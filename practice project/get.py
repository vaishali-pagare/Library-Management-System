from admin import Admin
from user import User
from InvalidNumError import InvalidNumError
def main():
    choice = 0
    while(choice != 3):
      
        
        print (""" 
              Welcome to Library Management system..!!
                         ____________________
                         |                   |
               \t\t |    1. ADMIN       |
               \t\t |    2. USER        |
               \t\t |    3. EXIT        |
                         |                   |
                         |___________________|      
        
                """)
      
      
        try:
            choice = int(input("Enter your choice : "))
            if(choice != 1 and choice != 2 and choice != 3):
                raise InvalidNumError(choice)

        except ValueError:
            print("Please Enter integer value..!!!")

        except InvalidNumError as n:
            print(n)
        else:
            if(choice == 1):
                print("Please login")
                Admin.admin()

            elif(choice == 2):
                User.user()

            elif(choice == 3):
                print("Thank you for your valubale time..!!!")
                break
      
                                                                                    

