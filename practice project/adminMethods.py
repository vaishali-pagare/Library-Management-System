from book import Book
from InvalidNumError import InvalidNumError

class AdminMethods:
    def addBook(b):
        with open("bookdemo.txt","a") as x:
            x.write(str(b))
            x.write("\n")

    def showBook():
        try:
            x = open("bookdemo.txt","r")
        except FileNotFoundError:
            print("File does not exist.")
            
        else:   
            print("-------------------------------------------------------------------------------------------------")

            print("|ID |      BOOK NAME            |    AUTHOR               | CATEGORY   |  COST      | AVAILABILTY|")
            print("|---|---------------------------|-------------------------|------------|------------|------------|")
            for line in x:
                line = line.strip()
                line = line.split(",")
                
                print("|%-s|  %-25s|  %-23s|  %-10s|  %-10s| %-11s|"%(line[0],line[1],line[2],line[3],line[4],line[5]))
            print("-------------------------------------------------------------------------------------------------")
            
        
    def searchBook(a):
        try:
            x = open("bookdemo.txt","r")
        except FileNotFoundError:
            print("File does not exist.")
        else:
            try:
                for line in x:
                    line = line.strip()
                    line = line.split(",")
                    if(a == int(line[0])):
                        print("Book id is found.")
                        print("-------------------------------------------------------------------------------------------------")
                        print("|ID |      BOOK NAME            |    AUTHOR               | CATEGORY   |  COST      | AVAILABILTY|")
                        print("|---|---------------------------|-------------------------|------------|------------|------------|")
                        print("|%-s|  %-25s|  %-23s|  %-10s|  %-10s| %-11s|"%(line[0],line[1],line[2],line[3],line[4],line[5]))
                        print("-------------------------------------------------------------------------------------------------")
                        break
                    elif(a == line[1]):
                        print("Book name is found.")
                        print("-------------------------------------------------------------------------------------------------")    
                        print("|ID |      BOOK NAME            |    AUTHOR               | CATEGORY   |  COST      | AVAILABILTY|")
                        print("|---|---------------------------|-------------------------|------------|------------|------------|")
                        print("|%-s|  %-25s|  %-23s|  %-10s|  %-10s| %-11s|"%(line[0],line[1],line[2],line[3],line[4],line[5]))
                        print("-------------------------------------------------------------------------------------------------")
                        break
                else:
                    print("Record not Found.")
                x.close()
            except ValueError:
                print("Please check the database..")


    def deleteBook(id):
        try:
            x = open("bookdemo.txt","r")
        except FileNotFoundError:
            print("File does not exist.")
        else:
            try:
                found = False
                allBook = []
                for line in x:
                    line = line.strip()
                    line = line.split(",")
                    if(id == int(line[0])):
                        found = True
                    else:
                        allBook.append(line)         
                if(found):
                    x = open("bookdemo.txt","w")
                    for book in allBook:
                        book = ",".join(book)
                        book += "\n"
                        x.write(book)
                    x.close()
                    print('''
                    ___________________________________________
                    |       RECORD DELETED SUCESSFULLY.        |
                    |__________________________________________|
                    ''')
                 
                    
                else:
                    print("Record not found...!!!")
            except ValueError:
                print("Please check the database...!!!")

    def editRecord(id):
        try:
            x = open("bookdemo.txt","r")
        except FileNotFoundError:
            print("File does not exist.")
        else:
            try:
                found = False
                allBook = []
                for line in x:
                    line = line.strip()
                    line = line.split(",")
                    if(id == int(line[0])):
                        found = True
                        ch = 0
                        while(ch != 6):
                            print('''
                                    _________________________________________
                                    |                                        |
                            \t    |    1. Change name of the book          |
                            \t    |    2. Change author of the book        |
                            \t    |    3. Change category of the book      |
                            \t    |    4. Change cost of the book          | 
                            \t    |    5. Change all data                  |
                            \t    |    6. Exit                             |  
                                    |                                        |
                                    |________________________________________|                                                         
                                        ''' )
                            try:
                                ch = int(input("Enter your choice : "))
                                if(ch != 1 and ch !=  2 and ch !=  3 and ch !=  4  and ch !=  5 and ch != 6  ):
                                    raise InvalidNumError(ch)
                            except ValueError:
                                print("Please Enter integer value..!!")
                            except InvalidNumError as n:
                                print(n)
                            else: 

                                if(ch == 1):
                                    nm = input("Enter new book name : ").upper()                                                     
                                    line[1] = nm   
                                                
                                elif(ch == 2):
                                    auth = input("Enter new author name : ").upper()
                                    code = (lambda x : x.isalpha() or x.isspace())
                                    value= list(map(code,auth))
                                    for i in value:
                                        if(i != True):
                                            print("Please enter valid author name..!!!")
                                            break
                                    else:
                                        line[2] = auth
                                        
                                        
                                elif(ch == 3):
                                    ct = input("Enter new category name : ").upper()
                                    code = (lambda x : x.isalpha() or x.isspace())
                                    value= list(map(code,ct))
                                    for i in value:
                                        if(i != True):
                                            print("Please enter valid category name..!!!")
                                            break   
                                    else:
                                        line[3]=ct
                                        
                                elif(ch == 4):
                                    ct =input("Enter new cost of the book : ").upper()
                                    code = (lambda x : x.isdigit())
                                    value= list(map(code,ct))
                                    for i in value:
                                        if(i != True):
                                            print("Please enter valid integer value...!!!")
                                            break
                                    else:
                                        line[4]=ct
                                        
                                elif(ch == 5):
                                    nm = input(" Enter new book name :").upper()
                                    line[1] = nm 
                                    auth = input("Enter new author name : ").upper()
                                    code = (lambda x : x.isalpha() or x.isspace())
                                    value= list(map(code,auth))
                                    for i in value:
                                        if(i != True):
                                            print("Please enter valid author name...!!!")
                                            break       
                                    else:
                                        line[2] = auth
                                        ct = input("Enter new category name : ").upper()
                                        code = (lambda x : x.isalpha() or x.isspace())
                                        value= list(map(code,ct))
                                        for i in value:
                                            if(i != True):
                                                print("Please enter valid category name...!!!")
                                                break
                                        else:
                                            line[3]=ct
                                            cst =input("Enter new cost of the book : ").upper()
                                            code = (lambda x : x.isdigit())
                                            value= list(map(code,cst))
                                            for i in value:
                                                if(i != True):
                                                    print("Please enter valid integer value...!!!")
                                                    break
                                            else:
                                                line[4]=cst
                                elif(ch == 6):
                                    print("Exit..")
                    allBook.append(line)         
                if(found):
                    x = open("bookdemo.txt","w")
                    for book in allBook:
                        book = ",".join(book)
                        book += "\n"
                        x.write(book)
                    x.close()
                    print('''
                    ___________________________________________
                    |        RECORD EDITED SUCESSFULLY.        |
                    |__________________________________________|
                    ''')
                else:
                    print("Record not found...!!!")
            except ValueError:
                print("Please check the database..!!!")

    def checkId(id):
        try:
            x = open("bookdemo.txt","r")
        except FileNotFoundError:
            print("File does not exist.")
        else: 
            AdminMethods.found = False
            try:
                for line in x:
                    line = line.strip()
                    line = line.split(",")
                    if(id == int(line[0])):
                        print("Id repeated..please enter another book id...!!!")
                        break
                else:
                    AdminMethods.found = True
            except ValueError:
                print("Please check database...!!!")
    


                       
                