from book import Book
from adminMethods import AdminMethods
from InvalidNumError import InvalidNumError
import random 
import get
class Admin:  
    def admin():

        print('''
                 ____________________________________________
                 |   ____________________________________    | 
                 |   |                                   |   |
                 |   |       WELCOME TO LIBRARY          |   |
                 |   |___________________________________|   |
                 |___________________________________________|

       ''')
                        
         
        username = "vaishali"
        password = "123"
        u = input("Enter the username : ")
        p = input("Enter the password : ")
        if(u == username):
            if(p == password):
                cap = random.randint(10000,99999)
                print(f"Captcha : {cap}")
                ent = int(input("Enter the above captcha : "))
                if(cap == ent):
                    print(''' 
                    ____________________________________
                    |                                   |
                    |       Login Sucessfully..!!       |
                    |___________________________________|   
                    
                    
                    ''')
               
                    choice1 = 0
                    while(choice1 != 6):
                        
                        print('''

                                        ___________________________
                                        |                          |
                           \t\t|    1. ADD BOOK           |
                           \t\t|    2. SHOW ALL BOOK      |
                           \t\t|    3. SEARCH BOOK        |
                           \t\t|    4. Delete BOOK        |
                           \t\t|    5. EDIT BOOK          |
                           \t\t|    6. MAIN MENU          |
                                        |                          |
                                        |__________________________|      
                        ''')
                        try:
                            choice1 = int(input("Enter your choice : "))
                            if(choice1 != 1 and choice1 != 2 and choice1 !=  3 and choice1 !=   4 and choice1 != 5 and choice1 !=  6):
                                raise InvalidNumError(choice1) 
                             
                        except ValueError:
                            print("Please Enter integer value..!!!")
                        except InvalidNumError as n:
                            print(n)
                        else:
                            if(choice1 == 1):
                                try:
                                    id = int(input("Enter the id of the book : "))                      
                                    if(id <= 1):
                                        raise InvalidNumError(id) 
                                                             
                                except ValueError:
                                        print("Please Enter integer value..!!!!")
                                except InvalidNumError as n:
                                        print(n)
                                else:
                                        AdminMethods.checkId(id)
                                        if(AdminMethods.found== True):
                                            try:
                                                cs = int(input("Enter the cost of the book : "))

                                                if(cs < 0):
                                                    raise InvalidNumError(cs) 
                                            except ValueError:
                                                print("Please Enter integer value...!!!!")
                                            except InvalidNumError as n:
                                                print(n)
                                            else:
                                                nm = input("Enter the name of the book : ").upper()
                                                auth = input("Enter the author of the book : ").upper()
                                                code = (lambda x : x.isalpha() or x.isspace() or x == ".")
                                                value= list(map(code,auth))
                                                for i in value:
                                                    if(i != True):
                                                        print("Please enter valid author name..!!!!")
                                                        break
                                                else:
                                                    ctgry = input("Enter the category of the book : ").upper()
                                                    code = (lambda x : x.isalpha() or x.isspace())
                                                    value= list(map(code,ctgry))
                                                    for i in value:
                                                        if(i != True):
                                                            print("Please enter valid category name..!!!!")
                                                            break
                                                    else:
                                                        b1 = Book(id,nm,auth,ctgry,cs,1)
                                                        AdminMethods.addBook(b1)
                                                        print('''
                                                            ___________________________________________
                                                            |        BOOK ADDED SUCESSFULLY..          |
                                                            |__________________________________________|
                                                            ''')

                                                                            
                            elif(choice1 == 2):
                                AdminMethods.showBook()
                            
                            elif(choice1 == 3):
                                ch = 0
                                while(ch != 3):
                                    print('''
                                                
                                    ____________________________________
                                    |                                   |
                          \t    |    1. Search by ID of the book    |
                          \t    |    2. Search by Name of the Book  |
                          \t    |    3.  Exit                       |                             
                                    |___________________________________|        
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
                                            try:
                                                id = int(input("Enter the id of the book : "))
                                                if(id <= 1):
                                                    raise InvalidNumError(id)
                                            except ValueError:
                                                print("Please Enter integer value..!!")
                                            except InvalidNumError as n:
                                                print(n)
                                            else:
                                                AdminMethods.searchBook(id)
                                        elif(ch == 2):
                                                nm = input("Enter the name of the book : ").upper()                                                       
                                                code = (lambda x : x.isalpha() or x.isspace())
                                                value= list(map(code,nm))
                                                for i in value:
                                                    if(i != True):
                                                        print("Please enter valid Book name..!!")
                                                        break
                                                else:                
                                                    AdminMethods.searchBook(nm)
                                               
                                        elif(ch == 3):
                                            print("Exit")

                            elif(choice1 == 4):
                                try:
                                    id = int(input("Enter the book id to be delete : "))

                                    if(id <= 1):
                                        raise InvalidNumError(id)
                                except ValueError:
                                    print("Please Enter integer value...!!!")
                                except InvalidNumError as n:
                                    print(n)
                                else:
                                    AdminMethods.deleteBook(id)

                            elif(choice1 == 5):
                                
                                try:
                                    id = int(input("Enter the book id to be edit : "))
                                    if(id <= 1):
                                        raise InvalidNumError(id)
                                except ValueError:
                                    print("Please Enter integer value...!!!")
                                except InvalidNumError as n:
                                    print(n)
                                else:
                                    AdminMethods.editRecord(id) 

                            elif(choice1 == 6):
                          
                                break
                else:
                    print('''
                    ___________________________________________
                    |         Captcha is Incorrect             |
                    |__________________________________________|
                    ''')



            else:
                print('''
                    ___________________________________________
                    |        Password is Incorrect             |
                    |__________________________________________|
                    ''')

                
        else:
            print('''
                    ___________________________________________
                    |         UserID is Incorrect              |
                    |__________________________________________|
                  


                    ''')

    






                
        


                                                
    
