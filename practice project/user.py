from userInfo import UserInfo
from adminMethods import AdminMethods
from userMethods import UserMethods
from InvalidNumError import InvalidNumError
import get
import random
class User:
    def user():
            print('''
                 ____________________________________________
                 |   ____________________________________    | 
                 |   |                                   |   |
                 |   |       WELCOME TO LIBRARY          |   |
                 |   |___________________________________|   |
                 |___________________________________________|

            ''')

            ch = 0
            while(ch != 3):
                
                print('''
                     

                         ____________________
                         |                   |
               \t\t |    1. SIGN UP     |
               \t\t |    2. SIGN IN     |
               \t\t |    3. EXIT        |
                         |                   |
                         |___________________|      
        
                ''')
      
 
               
                try:
                    ch = int(input("Enter your choice : "))
                    if(ch != 1 and ch !=  2 and ch !=  3):
                        raise InvalidNumError(ch)
                except ValueError:
                    print("Please Enter integer value...!!!")
                except InvalidNumError as n:
                    print(n)
                else: 

                    if(ch == 1):

                        nm = input("Enter your name : ").upper()
                        code = (lambda x : x.isalpha() or x.isspace())
                        value= list(map(code,nm))
                        for i in value:
                            if(i != True):
                                print("Please enter valid name..!!!")
                                break
                        else:
                            pas = input("Create password (atleast 6 characters require..)  : ")
                            if(len(pas) < 5):
                                print("Please create password of atleast more than 5 characters...!!!")
                            else:
                                    id = random.randint(100,999)
                                    print('''
                ___________________________________________________
                |            Register Sucessfully..!!              |
                |__________________________________________________|
                                    ''')
                                    print("Your id is :",id,"\n Please remember this id for login purpose..!!!")
                                    print("Please sign in now for explore more functions...!!!")
                                    print("______________________________________________________________") 
                                    r1 =  UserInfo(id,nm,pas,3)
                                    UserMethods.registerUser(r1)

                    elif(ch == 2):
                        count=0
                        while(count !=3):
                            print("__________________________________________________") 
    
                            try:
                                id = int(input("Enter your id : "))
                                if(id <= 1):
                                    raise InvalidNumError(id)
                            except ValueError:
                                print("Please Enter integer value..!!")
                            except InvalidNumError as n:
                                print(n)
                            else:
                                nm = input("Enter your name : ").upper()                   
                                code = (lambda x : x.isalpha() or x.isspace())
                                value= list(map(code,nm))
                                for i in value:
                                    if(i != True):
                                        print("Please enter valid name..!!")
                                        break
                                else:                        
                                    pas = input("Enter password : ")
                                    print("__________________________________________________") 
                                     
                                    try :
                                        x = open("User details.txt","r")
                                    except FileNotFoundError:
                                        print("File does not exit.")
                                    else:
                                        for line in x:
                                            line = line.strip()
                                            line = line.split(",")
                                            if(id == int(line[0]) and (nm == line[1]) and (pas == line[2])):
                                                print('''
                        ____________________________________
                        |                                   |
                        |       Login Sucessfully..!!       |
                        |___________________________________|   
                                                    ''')
                                                User.menuList(id,nm)  
                                                break
                                        else:
                                            print('''
                            ____________________________________________
                            |                                           |
                            |    Please enter correct information.      |        
                            |___________________________________________|  
                                                    ''')         

                                            count += 1  

                                    
                        else:
                            print('''
                            ____________________________________________
                            |                                           |
                            |         To Many Attempts..!!!             |        
                            |___________________________________________|  
                                    ''')         

                    elif(ch == 3):
                        print("Exit")
                        break
                       

    def menuList(id,nm):
            choice1=0
            while(choice1 != 6):
                print('''

                         ___________________________
                        |                          |
               \t\t|    1. SHOW ALL BOOK      |
               \t\t|    2. SEARCH BOOK        |
               \t\t|    3. ISSUE BOOK         |
               \t\t|    4. SUBMIT BOOK        |
               \t\t|    5. LOST BOOK          |
               \t\t|    6. MAIN MENU          |
                        |                          |
                        |__________________________|      
                ''')
                try:
                    choice1 = int(input("Enter your choice : "))
                    if(choice1 != 1 and choice1 !=  2 and choice1 !=  3 and choice1 !=  4 and choice1 !=  5 and choice1 != 6 ):
                        raise InvalidNumError(choice1)
                except ValueError:
                    print("Please Enter integer value..!!")
                except InvalidNumError as n:
                    print(n)
                else: 
                    if(choice1 == 1):
                        AdminMethods.showBook()
                    
                    elif(choice1 == 2):
                        ch = 0
                        while(ch != 3):
                            print('''
                                    ________________________________________
                                    |                                       |
                          \t    |    1. Search by Name of the book      |
                          \t    |    2. Search by Category of the Book  |
                          \t    |    3.  Exit                           |                             
                                    |_______________________________________|   
                                                
   
                            ''')

                            try:
                                ch = int(input("Enter your choice : "))
                                if(ch != 1 and ch !=  2 and ch !=  3):
                                    raise InvalidNumError(ch)
                            except ValueError:
                                print("Please Enter integer value..!!")
                            except InvalidNumError as n:
                                print(n)
                            else: 
                                if(ch == 1):
                                    nm = input("Enter the name of the book : ").upper()                                                       
                                    code = (lambda x : x.isalpha() or x.isspace())
                                    value= list(map(code,nm))
                                    for i in value:
                                        if(i != True):
                                            print("Please enter valid Book name..!!")
                                            break
                                    else:    
                                        AdminMethods.searchBook(nm)
                                elif(ch == 2):
                                    ct= input("Enter the category of the book : ").upper()
                                    code = (lambda x : x.isalpha() or x.isspace())
                                    value= list(map(code,ct))
                                    for i in value:
                                        if(i != True):
                                            print("Please enter valid Book category..!!")
                                            break
                                    else:                               
                                        UserMethods.searchBookUser(ct)
                                elif(ch == 3):
                                    print("Exit")

                    elif(choice1 == 3):
                        try:
                            id1 = int(input("Enter the id of the book which you want to issue : ")) 
                            if(id1 <= 1):
                                raise InvalidNumError(id1)
                        except ValueError:
                            print("Please Enter integer value..!!")
                        except InvalidNumError as n:
                            print(n)
                        else: 
                            UserMethods.issueRecord(id1,id,nm)
             
                    elif(choice1 == 4):
                        try:
                            id1 = int(input("Enter id of the book which you submit : "))
                            if(id1 <= 1):
                                raise InvalidNumError(id1)
                        except ValueError:
                            print("Please Enter integer value..!!")
                        except InvalidNumError as n:
                            print(n)
                        else: 
                            UserMethods.subRecord(id1,id)
                           
                    elif(choice1 == 5):
                        try:
                            id1 = int(input("Enter the id of the book : "))
                            if(id1 <= 1):
                                raise InvalidNumError(id1)
                        except ValueError:
                            print("Please Enter integer value..!!")
                        except InvalidNumError as n:
                            print(n)
                        else: 
                            UserMethods.bookLost(id,id1)    

                    elif(choice1 == 6):     
                        get.main()
                        break
                


        

 

    


           

