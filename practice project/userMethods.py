from issueinfo import IssueInfo

class UserMethods:
    
    def registerUser(a):
        with open("User details.txt","a") as x:
            x.write(str(a))
            x.write("\n")
    
    def addRecord(a):
        with open("issuedemo.txt","a") as x:
            x.write(str(a))
            x.write("\n")

    def searchBookUser(a):
        try:
            x = open("bookdemo.txt","r")
        except FileNotFoundError:
            print("File does not exist.")
        else:
            try:
                found = False
                print("-------------------------------------------------------------------------------------------------")
                print("|ID |      BOOK NAME            |    AUTHOR               | CATEGORY   |  COST      | AVAILABILTY|")
                print("|---|---------------------------|-------------------------|------------|------------|------------|") 
                
                for line in x:
                    line = line.strip()
                    line = line.split(",")
                    if(a == line[3]):
                        found = True
                        print("|%-s|  %-25s|  %-23s|  %-10s|  %-10s| %-11s|"%(line[0],line[1],line[2],line[3],line[4],line[5]))
                print("-------------------------------------------------------------------------------------------------")
                        
                if(found):

                    print("Book category found...!!!")
                else:
                    print("Book category not found...!!!")
                x.close()
            except ValueError:
                print("Please check the database...!!!")

    def deleteRecord(id):
        try:
            x = open("issuedemo.txt","r")
        except FileNotFoundError:
            print("File does not exist.")
        else:
            try:
                found = False
                allRecord = []
                for line in x:
                    line = line.strip()
                    line = line.split(",")
                    if(id == int(line[0])):
                        found = True
                    else:
                        allRecord.append(line)

                if(found):
                    x = open("issuedemo.txt","w")
                    for record in allRecord:
                        record = ",".join(record)
                        record += "\n"
                        x.write(record)
                    x.close()
            except ValueError:
                print("please check the database...!!!")
    
    def issueRecord(id1,id,nm):
        try:
            fp = open("User details.txt","r")
        except FileNotFoundError:
            print("File does not exist.")
        else:
            try:
                record = []
                found = False
                for i in fp:
                    i = i.strip()
                    i = i.split(",")
                    if(id == int(i[0]) and int(i[3]) == 0):
                        print('''
                    ___________________________________________
                    |    Your already issued 3 books..         |
                    |__________________________________________|
                            ''')

                    elif(id == int(i[0]) and int(i[3]) != 0):
                        found = True 
                        try:
                            x = open("bookdemo.txt","r")
                        except FileNotFoundError:
                            print("File does not exist...!!!")
                        else:
                            found = False
                            allBook = []
                            for line in x:
                                line = line.strip()
                                line = line.split(",")
                                if(id1 == int(line[0]) and line[5]=="1") :
                                    found = True

                                    date = input("Enter the date in YY-MM-DD : ")
                                    code = lambda x : x.isdigit() or x == "-" or x == "/" or x == "."
                                    value = list(map(code,date))
                                    for x in value:
                                        if( x != True):
                                            print("Please enter date in YY-MM-DD Format..!!")
                                            break
                                    else:     
                                        line[5] = "0"
                                        i[3] = str(int(i[3])-1)
                                        u1 = IssueInfo(id1,id,nm,date)
                                        UserMethods.addRecord(u1)
                                        print('''
                                ___________________________________________
                                |        Your Entry is recorded..          |
                                |   Please Return book within 7 days..!!   |
                                |__________________________________________|
                                        ''')
                     
                                allBook.append(line)
                            if(found):
                                x = open("bookdemo.txt","w")
                                for book in allBook:
                                    book = ",".join(book)
                                    book += "\n"
                                    x.write(book)
                                x.close()                 
                            else:
                                print("Book is currently not available..!!")
                    record.append(i)

                if(found):
                    fp = open("User details.txt","w")
                    for x in record:
                        x = ",".join(x)
                        x += "\n"
                        fp.write(x)
                    fp.close()        
            except ValueError:
                print("Please check the database...!!!")

    def subRecord(id1,id):
       
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
                    if(id1 == int(line[0]) and line[5]=="0" ):
                        found = True
                        line[5] = "1"
                        try:
                            a = open("issuedemo.txt","r")
                        except FileNotFoundError:
                            print("File does not exist.")
                        else:
                            for data in a:
                                data = data.strip()
                                data = data.split(",")
                                if(id1 == int(data[0])):
                                    date = data[3]
                                    y = input("Enter the date in YY-MM-DD : ")
                                    code = lambda x : x.isdigit() or x == "-" or x == "/" or x == "."
                                    value = list(map(code,y))
                                    for i in value:
                                        if( i != True):
                                            print("Please enter date in YY-MM-DD Format...!!!")
                                            break
                                    else:
                                        data1 = ""
                                        for i in date:
                                            if(i.isdigit()):
                                                data1 += i
                                        data2 = ""
                                        for i in y:
                                            if (i.isdigit()):
                                                data2 += i
                                        z = int(data2)-int(data1)
                                        fine = 5
                                        if(z > 7):
                                            print("Please pay fine of : ",(z-7)*fine,"Rs") 
                                        else:                                       
                                            print('''
                                ___________________________________________
                                |     Your retun book within time.         |
                                |    Thank you for submitting book..       |
                                |__________________________________________|
                                        ''')
                        UserMethods.deleteRecord(id1)
                        UserMethods.update(id)
                    allBook.append(line)
                if(found):
                    x = open("bookdemo.txt","w")
                    for book in allBook:
                        book = ",".join(book)
                        book += "\n"
                        x.write(book)
                    x.close()
                    print("Your entry is recorded...!!!")
            except:
                print("Please check the database..!!!")
        
    def bookLost(id,id1):
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
                    if(id1 == int(line[0])):
                        found = True
                        print("Please pay fine of",line[4],"RS.")
                        UserMethods.deleteRecord(id1)
                        UserMethods.update(id)
                    else:
                        allBook.append(line)         
                if(found):
                    x = open("bookdemo.txt","w")
                    for book in allBook:
                        book = ",".join(book)
                        book += "\n"
                        x.write(book)
                    x.close()
            except ValueError:
                print("Please check the database...!!!") 


    def update(id):
        try:
            fp = open("User details.txt","r")
        except FileNotFoundError:
            print("File does not exist.")
        else:
            try:
                record = []
                found = False
                for i in fp:
                    i = i.strip()
                    i = i.split(",")
                    if(id == int(i[0]) and int(i[3]) < 3):
                        found = True
                        i[3] = str(int(i[3])+1)
                    record.append(i)
                if(found):
                    fp = open("User details.txt","w")
                    for x in record:
                        x = ",".join(x)
                        x += "\n"
                        fp.write(x)
                    fp.close()        
            except ValueError:
                print("Please chcek the database...!!!")

    

    
 