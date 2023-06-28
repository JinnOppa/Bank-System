def time():
    import datetime as Time
    nowdate = Time.datetime.now()
    nowdate = nowdate.strftime("%Y-%m-%d  %H:%M:%S")
    return nowdate

def ttime():
    import datetime as Time
    nowdate = Time.datetime.now()
    nowdate = nowdate.strftime("%Y-%m-%d")
    return nowdate

def date_checker():
    flag1 = False
    while flag1 == False:
        date = input("Enter date: ")
        month = input("Enter month: ")
        year =  input("Enter year: ")
        if int(year) > 0 :
            if (int(month) == 1) or (int(month) == 3) or (int(month) == 5) or (int(month) == 7) or (int(month) == 8) or (int(month) == 10) or (int(month) == 12) : #to check given month has 31 days
                if int(date) > 0 and int(date) < 32 : #to check the given date in a given month is correct
                    ttime = year + "-" + month + "-" + date
                    return ttime
                else:
                    print("invalid date")
            elif (int(month) == 4) or (int(month) == 6) or (int(month) == 9) or (int(month) == 11) : #to check given month has 31 days
                if int(date) > 0 and int(date) < 31: #to check the given date in a given month is correct
                    ttime = year + "-" + month + "-" + date
                    return ttime
                else:
                    print("invalid date")
            elif (int(month) == 2): #to check given month has 31 days
                if int(year) % 4 != 0 :
                    if int(date) > 0 and int(date) < 29: #to check the given date in a given month is correct
                        ttime = year + "-" + month + "-" + date
                        return ttime
                    else:
                        print("invalid date")
                elif int(year) % 4 == 0:
                    if int(date) > 0 and int(date) < 30: #to check the given date in a given month is correct
                        ttime = year + "-" + month + "-" + date
                        return ttime
                    else:
                        print("invalid date")
            else:
                print("invalid month")


#unique id in sequences
def gen_id(prefix):
    file = open("AllDataUser.txt","r") #open the file in read mode
    reclist = file.readlines() #reading lines from the text tile
    lastrec = reclist[len(reclist)-1] 
    idnum = lastrec[3:10] #idnum is the last 7 digit from the lastrec
    nextnum = str(int(idnum) + 1).zfill(7) 
    uniqueID = prefix + nextnum
    file.close() #close the file
    return uniqueID
        

#SuperAccount, for create admin account, edit admin account, show all admin profile
def super_account_menu(UserID): #to show the menu for super account
    print ("\n\n",80*"*","\n\n\t\t\t\tWELCOME SUPER USER\n\n")
    flag = True
    while flag == True:
        file1 = open("AllDataUser.txt","r") #open the file in read mode
        cnt =-1
        for rec in file1: #to read all the data in the file
            UserAccount = rec.split(" | ") #to data is split with " | "
            cnt += 1
            if UserAccount[0] == UserID:
                print("Select activity:\n 1. Create Admin Account\n 2. Edit Admin Account\n 3. Show all admin\n 4. Exit")
                option = int(input("Select option: ")) #enter the option
                if option == 1 :
                    create_admin_account(UserID)
                    break
                elif option == 2 :
                    edit_admin_account(UserID)
                    break
                elif option == 3 :
                    show_admin(UserID)
                    break
                elif option == 4 :
                    flag = False
                    break
        file1.close() #close the file


def create_admin_account(UserID): #to create admin account by super account
    print("\n\n",80*"*","\n\t\t\t\tCREATE ADMIN ACCOUNT\n", 80*"*","\n")
    file1 = open("AllDataUser.txt","a") #open file in append mode
    prefix = "AUA"
    AdminUserName = gen_id(prefix)
    AdminFullName = str(input("Enter Admin full name: "))
    AdminPassword =  "PasswordAdmin"
    AdminEmail = str(input("Enter Admin email: "))
    AdminPhone = int(input("Enter Admin phone number: "))
    AdminAddress = str(input("Enter Admin address: "))
    print("Birthday : ")
    BDay = date_checker()
    file1.write(AdminUserName + " | " + AdminPassword + " | " + AdminFullName + " | " + AdminEmail + " | " + str(AdminPhone) + " | " + AdminAddress + " | " + BDay + " | " + "Admin Account" + "\n")
    file1.close() #close file
    super_respond(UserID)

def edit_admin_account(UserID): #to check if the account is valid to be edited by the user
    print("\n\n",80*"*","\n\t\t\t\tEDIT ADMIN ACCOUNT\n", 80*"*","\n")
    file1 = open("AllDataUser.txt","r") #open file in read mode
    AdminUName = input("Enter Admin username to edit: ")
    AdminUPassword = input("Enter Admin password to edit: ")
    cnt = -1
    for rec in file1: #to read all the data in the file
        UserAccount  = rec.split(" | ")
        cnt += 1
        AdminUserName = UserAccount[0]
        AdminPassword = UserAccount[1]
        while AdminUName == AdminUserName and AdminUPassword == AdminPassword:
            if AdminUName == "SUC0000001" and AdminUPassword == "PasswordSuper": #to check if the input is the same as the condition
                print("Invalid Account!")
                break
            elif AdminUName[0:3] == "AUA" and AdminUName == UserAccount[0] and AdminUPassword == UserAccount[1]: #to check if the input is the same as the condition
                print("Admin data found!")
                edit_admin_detail(UserAccount, cnt)
                break
            elif AdminUName == UserAccount[0] and AdminUPassword == UserAccount[1]: #to check if the input is the same as the condition
                print("Invalid Account! Admin user only!")
                break
    file1.close() #close file
    super_respond(UserID)

def edit_admin_detail(UserAccount, cnt): #to edit the detail of the selected account
    file1 = open("AllDataUser.txt","r") #open the file in read mode
    firstFile = file1.readlines() #readlines from the file
    ModifyEmail = input("Enter Admin email: ")
    ModifyPhoneNumber = int(input("Enter Admin phone number: "))
    ModifyAddress = input("Enter Admin address: ")
    firstFile[cnt] = UserAccount[0] + " | " + UserAccount[1] + " | " + UserAccount[2] + " | " + ModifyEmail +  " | " + str(ModifyPhoneNumber) + " | " + ModifyAddress + " | " + UserAccount[6] + " | " + UserAccount[7]
    file1.close() #close the file
    file2 = open("AllDataUser.txt","w")
    file2.writelines(firstFile) #to overwrite the selected lines with the new variable list
    file2.close() #close file

def show_admin(UserID): #to show all of the admin account
    print("\n\n",80*"*","\n\t\t\t\tSHOW ADMIN ACCOUNT\n", 80*"*","\n")
    while True:
        file2 = open("AllDataUser.txt","r") #open file in read mode
        print("Admin List : ")
        for rec in file2: #to read all the data in the file
            UserAccount = rec.split(" | ") #to data is split with " | "
            if UserAccount[0][0:3] == "AUA":
                AdminList = UserAccount[0] + " | " + UserAccount[2] + " | " + UserAccount[3] + " | " + UserAccount[4] + " | " + UserAccount[5] + " | " + UserAccount[6]
                print(AdminList)
        file2.close() #close file
        break
    super_respond(UserID)



#AdminAccount. for add, modify, and show report customer account, show all saving and current customer
def admin_account_menu(UserID):
    print ("\n\n",80*"*","\n\n\t\t\t\tWELCOME" ,UserID, "USER\n\n")
    flag = True
    while flag == True:
        file1 = open("AllDataUser.txt","r") #open file in read mode
        cnt = -1
        for rec in file1: #to read all the data in the file
            UserAccount = rec.split(" | ") #to data is split with " | "
            cnt += 1
            if UserAccount[0] == UserID: 
                print("Select activity :\n 1. Create Customer Account\n 2. Edit Customer Account\n 3. Report\n 4. Exit")
                option = int(input ("Select options: "))
                if option == 1:
                    create_customer_account(UserAccount)
                    break            
                elif option == 2:
                    edit_customer_account(UserAccount)
                    break
                elif option == 3:
                    report_admin(UserAccount)
                    break
                elif option == 4:
                    flag = False
                    break
        file1.close() #close file


def create_customer_account(UserID):
    print("\n\n",80*"*","\n\t\t\t\tCREATE CUSTOMER ACCOUNT\n", 80*"*","\n")
    file1 = open("AllDataUser.txt","a") #open file in append mode
    print("Customer account type: \n 1. Saving Account \n 2. Current Account")
    flag = True
    while flag == True:
        option = int(input("Enter customer account type: "))
        if option == 1:
            CustomerType = "Saving Account"
            prefix = "SUA"
            CustomerUserName = gen_id(prefix)
            flag = False
        elif option == 2 :
            CustomerType = "Current Account"
            prefix = "CUA"
            CustomerUserName = gen_id(prefix)
            flag = False
        elif option != 1 or option != 2:
            print ("Enter valid option")
            flag = True

    CustomerFullName = str(input("Create Customer full name: "))
    CustomerPassword =  "PasswordUser"
    CustomerEmail = str(input("Enter Customer email: "))
    CustomerPhone = int(input("Enter Customer phone number: "))
    CustomerAddress = str(input("Enter Customer address: "))
    CustomerNationality = str(input("Enter Customer Nationality: "))
    print("Birthday : ")
    BDay = date_checker() 
    CustomerBalance = float(input("Enter your amount to deposit: RM "))
    file1.write(CustomerUserName + " | " + CustomerPassword + " | " + CustomerFullName + " | " + CustomerEmail + " | " + str(CustomerPhone) + " | " + CustomerAddress + " | " + BDay + " | " + CustomerType + " | " + str(CustomerBalance) + " | " + CustomerNationality + "\n")
    file1.close() #close file
    admin_respond(UserID)

def edit_customer_account(UserAccount):
    print("\n\n",80*"*","\n\t\t\tEDIT CUSTOMER ACCOUNT\n", 80*"*","\n")
    file1 = open("AllDataUser.txt","r") #open file in read mode
    CustomerUName = input("Enter Customer username to edit: ")
    CustomerUPassword = input("Enter Customer password to edit: ")
    cnt = -1
    for rec in file1: #to read all the data in the file
        UserAccount  = rec.split(" | ") #to data is split with " | "
        cnt += 1
        CustomerUserName = UserAccount[0]
        CustomerPassword = UserAccount[1]
        if CustomerUName == CustomerUserName and CustomerUPassword == CustomerPassword:
            if CustomerUName == "SUC0000001" and CustomerUPassword == "PasswordSuper":
                print("Invalid Account!")
                break
            elif CustomerUName[0:3] == "AUA" and CustomerUPassword == "PasswordAdmin":
                print("Invalid Account! Super Account only")
                break
            elif CustomerUName == UserAccount[0] and CustomerUPassword == UserAccount[1]:
                print("Customer data found!")
                edit_customer_detail(UserAccount, cnt)
                break
    file1.close() #close file
    admin_respond(UserAccount)

def edit_customer_detail(UserAccount, cnt):
    file1 = open("AllDataUser.txt","r") #open file in read mode
    firstFile = file1.readlines()
    ModifyEmail = str(input("Enter Customer email: "))
    ModifyPhoneNumber = int(input("Enter Customer Phone Number: "))
    ModifyAddress = str(input("Enter Customer Address: "))
    firstFile[cnt] = UserAccount[0] + " | " + UserAccount[1] + " | " + UserAccount[2] + " | " + ModifyEmail +  " | " + str(ModifyPhoneNumber) + " | " + ModifyAddress + " | " + UserAccount[6] + " | " + UserAccount[7]+ " | " + UserAccount[8] + " | " + UserAccount[9]
    file1.close() #close file
    file2 = open("AllDataUser.txt","w") #open file in write mode
    file2.writelines(firstFile) #to overwrite the selected lines with the new variable list
    file2.close() #close file
        
def report_admin(UserID):
    print("\n\n",80*"*","\n\t\t\t\tSHOW REPORT CUSTOMER\n", 80*"*","\n")
    trx = False
    while not trx:
        error = False
        print(" Start Date :    ")
        StartDay = str(date_checker())
        print(" End date :   ")
        EndDay = str(date_checker())
        useraccount = input("Enter Customer username: ")
        file1 = open("CustomerTransaction.txt","r") #open file in read mode
        for rec in file1: #to read all the data in the file
            UserTransaction = rec.split(" | ") #to data is split with " | "
            if useraccount == UserTransaction[0]:
                tdate = UserTransaction[6]
                try:
                    if int(StartDay.split("-")[0]) <= int(EndDay.split("-")[0]):
                        if (int(StartDay.split("-")[0]) == int(tdate.split("-")[0])) or int(EndDay.split("-")[0]) == int(tdate.split("-")[0]) :
                            if (int(StartDay.split("-")[1]) <= int(EndDay.split("-")[1])) and (int(StartDay.split("-")[1]) < 13) and (int(EndDay.split("-")[1]) < 13) :
                                if (int(StartDay.split("-")[1]) == int(tdate.split("-")[1])) or (int(EndDay.split("-")[1]) == int(tdate.split("-")[1])) :
                                    if (int(tdate.split("-")[2]) >= int(StartDay.split("-")[2])) and (int(tdate.split("-")[2]) <= int(EndDay.split("-")[2])) :
                                        report = UserTransaction[0] + " | "+ UserTransaction[1] + " | " + UserTransaction[2] + " | " + UserTransaction[3] + " | " + UserTransaction[4] + " | " + UserTransaction[5]
                                        print(report)
                                        trx = True
                                elif (int(tdate.split("-")[1]) > int(StartDay.split("-")[1])) and (int(tdate.split("-")[1]) < int(EndDay.split("-")[1])) :
                                    report = UserTransaction[0] + " | "+ UserTransaction[1] + " | " + UserTransaction[2] + " | " + UserTransaction[3] + " | " + UserTransaction[4] + " | " + UserTransaction[5]
                                    print(report)
                                    trx = True
                        elif (int(tdate.split("-")[0]) > int(StartDay.split("-")[0])) and (int(tdate.split("-")[0]) < int(EndDay.split("-")[0])) :
                            report = UserTransaction[0] + " | "+ UserTransaction[1] + " | " + UserTransaction[2] + " | " + UserTransaction[3] + " | " + UserTransaction[4] + " | " + UserTransaction[5]
                            print(report)
                            trx = True
                except IndexError:
                    print("Invalid date")
                    error = True
                    break
        if not trx and not error:
            print ("No record found")
            break
        file1.close()
    admin_respond(UserID)
        


#customer_account, option for deposit, withdraw, report, mod pw, and show balance
def customer_account_menu(UserID):
    print ("\n\n",80*"*","\n\n\t\t\t\tWELCOME",UserID ,"USER\n\n")
    flag = True
    while flag == True:
        file1 = open("AllDataUser.txt","r") #open file in read mode
        cnt = -1
        for rec in file1: #to read all the data in the file
            UserAccount = rec.split(" | ") #to data is split with " | "
            cnt += 1
            if UserAccount[0] == UserID:
                print("Select activity :\n 1. Balance\n 2. Deposit\n 3. Withdraw\n 4. Report\n 5. Modify Password\n 6. Exit")
                option = int(input ("Select options : "))
                if option == 1:
                    balance(UserAccount)
                    break            
                elif option == 2:
                    deposit(UserAccount, cnt)
                    break
                elif option == 3:
                    withdraw(UserAccount, cnt)
                    break
                elif option == 4:
                    report_customer(UserAccount)
                    break
                elif option == 5:
                    modify_password(UserAccount, cnt)
                    break
                elif option == 6:
                    flag = False
                    break
        file1.close() #close file


def balance(UserAccount):
    print("\n\n",80*"*","\n\t\t\t\tCUSTOMER ACCOUNT BALANCE\n", 80*"*","\n")
    file1 = open("AllDataUser.txt","r") #open file in read mode
    CustomerBalance = UserAccount[8]
    print( "RM " + CustomerBalance)
    file1.close() #close file
    customer_respond(UserAccount)

def deposit(UserAccount, cnt):
    print("\n\n",80*"*","\n\t\t\t\tCUSTOMER ACCOUNT DEPOSIT\n", 80*"*","\n")
    file1 = open("CustomerTransaction.txt","a") #open file in append mode
    AmountDeposit = float(input("Enter amount to deposit: RM "))
    nowbalance = float(UserAccount[8]) + AmountDeposit
    mydate = time()
    date = ttime()
    file1.write(UserAccount[0] + " | " + UserAccount[2] + " | " + UserAccount[8] + " | " + "+" + str(AmountDeposit) + " | " + str(nowbalance) + " | " + mydate + " | " + date + "\n" )
    file1.close() #close file
    file2 = open("AllDataUser.txt","r") #open file in read mode
    secondFile = file2.readlines() #reading lines from the text tile
    secondFile[cnt] = UserAccount[0] + " | " + UserAccount[1] + " | " + UserAccount[2] + " | " + UserAccount[3] +  " | " + UserAccount[4] + " | " + UserAccount[5] + " | " + UserAccount[6] + " | " + UserAccount[7] + " | " + str(nowbalance) + " | " + UserAccount[9] 
    file2.close() #close file
    file3 = open("AllDataUser.txt","w") #open file in write mode
    file3.writelines(secondFile)
    file3.close() #close file
    customer_respond(UserAccount)

def withdraw(UserAccount, cnt):
    print("\n\n",80*"*","\n\t\t\t\tCUSTOMER ACCOUNT WITHDRAW\n", 80*"*","\n")
    file1 = open("CustomerTransaction.txt","a") #open file in append mode
    AmountWithdraw = float(input("Enter amount to withdraw: RM "))
    nowbalance = float(UserAccount[8]) - AmountWithdraw
    mydate = time()
    date = ttime()
    if UserAccount[7] == "Saving Account":
        minbalance = 100
        if nowbalance >= minbalance:
            file1.write(UserAccount[0] + " | " + UserAccount[2] + " | " + UserAccount[8] + " | "+ "-" + str(AmountWithdraw) + " | " + str(nowbalance) + " | " + mydate + " | " + date + "\n" )
            file1.close() #close file
            file2 = open("AllDataUser.txt","r") #open file in read mode
            secondFile = file2.readlines() #reading lines from the text tile
            secondFile[cnt] = UserAccount[0] + " | " + UserAccount[1] + " | " + UserAccount[2] + " | " + UserAccount[3] +  " | " + UserAccount[4] + " | " + UserAccount[5] + " | " + UserAccount[6] + " | " + UserAccount[7] + " | " + str(nowbalance)+ " | " + UserAccount[9] 
            file2.close() #close file
            file3 = open("AllDataUser.txt","w") #open file in write mode
            file3.writelines(secondFile) #to overwrite the selected lines with the new variable list
            file3.close() #close file
            customer_respond(UserAccount)
        elif nowbalance < minbalance :
            print("Unsufficient balance")
            customer_respond(UserAccount)
    elif UserAccount[7] == "Current Account":
        minbalance = 500
        if nowbalance >= minbalance:
            file1.write(UserAccount[0] + " | " + UserAccount[2] + " | " + UserAccount[8] + " | "+ "-" + str(AmountWithdraw) + " | " + str(nowbalance) + " | " + mydate + " | " + date + "\n" )
            file1.close() #close file
            file2 = open("AllDataUser.txt","r") #open file in read mode
            secondFile = file2.readlines() #reading lines from the text tile
            secondFile[cnt] = UserAccount[0] + " | " + UserAccount[1] + " | " + UserAccount[2] + " | " + UserAccount[3] +  " | " + UserAccount[4] + " | " + UserAccount[5] + " | " + UserAccount[6] + " | " + UserAccount[7] + " | " + str(nowbalance) + " | " + UserAccount[9]
            file2.close() #close file
            file3 = open("AllDataUser.txt","w") #open file in append mode
            file3.writelines(secondFile) #to overwrite the selected lines with the new variable list
            file3.close() #close file
            customer_respond(UserAccount)
        elif nowbalance < minbalance :
            print("Unsufficient balance")
            customer_respond(UserAccount)
 
def report_customer(UserID):
    print("\n\n",80*"*","\n\t\t\t\tCUSTOMER ACCOUNT REPORT\n", 80*"*","\n")
    trx = False
    while not trx:
        error = False
        print(" Start Date :    ")
        StartDay = str(date_checker())
        print(" End date :   ")
        EndDay = str(date_checker())
        useraccount = UserID[0]
        file1 = open("CustomerTransaction.txt","r") #open file in read mode
        for rec in file1: #to read all the data in the file
            UserTransaction = rec.split(" | ") #to data is split with " | "
            if useraccount == UserTransaction[0]:
                tdate = UserTransaction[6]
                try:
                    if int(StartDay.split("-")[0]) <= int(EndDay.split("-")[0]):
                        if  int(EndDay.split("-")[0]) == int(tdate.split("-")[0]) or (int(StartDay.split("-")[0]) == int(tdate.split("-")[0])) :
                            if (int(StartDay.split("-")[1]) <= int(EndDay.split("-")[1])) and (int(StartDay.split("-")[1]) < 13) and (int(EndDay.split("-")[1]) < 13) :
                                if (int(StartDay.split("-")[1]) == int(tdate.split("-")[1])) or (int(EndDay.split("-")[1]) == int(tdate.split("-")[1])) :
                                    if (int(tdate.split("-")[2]) >= int(StartDay.split("-")[2])) and (int(tdate.split("-")[2]) <= int(EndDay.split("-")[2])) :
                                        report = UserTransaction[0] + " | "+ UserTransaction[1] + " | " + UserTransaction[2] + " | " + UserTransaction[3] + " | " + UserTransaction[4] + " | " + UserTransaction[5]
                                        print(report)
                                        trx = True
                                elif (int(tdate.split("-")[1]) > int(StartDay.split("-")[1])) and (int(tdate.split("-")[1]) < int(EndDay.split("-")[1])) :
                                    report = UserTransaction[0] + " | "+ UserTransaction[1] + " | " + UserTransaction[2] + " | " + UserTransaction[3] + " | " + UserTransaction[4] + " | " + UserTransaction[5]
                                    print(report)
                                    trx = True
                        elif (int(tdate.split("-")[0]) > int(StartDay.split("-")[0])) and (int(tdate.split("-")[0]) < int(EndDay.split("-")[0])) :
                            report = UserTransaction[0] + " | "+ UserTransaction[1] + " | " + UserTransaction[2] + " | " + UserTransaction[3] + " | " + UserTransaction[4] + " | " + UserTransaction[5]
                            print(report)
                            trx = True
                except IndexError:
                    print("Invalid date")
                    error = True
                    break
        if not trx and not error:
            print ("No record found")
            break
        file1.close() #close file
    customer_respond(UserID)

def modify_password(UserAccount, cnt):
    print("\n\n",80*"*","\n\t\t\t\tCUSTOMER ACCOUNT MODIFY PASSWORD\n", 80*"*","\n")
    file1 = open("AllDataUser.txt","r") #open file in read mode
    firstFile = file1.readlines() #reading lines from the text tile
    ModifyPassword = input("Enter Customer new password: ")
    firstFile[cnt] = UserAccount[0] + " | " + ModifyPassword + " | " + UserAccount[2] + " | " + UserAccount[3] +  " | " + UserAccount[4] + " | " + UserAccount[5] + " | " + UserAccount[6] + " | " + UserAccount[7] + " | " + UserAccount[8] + " | " + UserAccount[9]
    file1.close() #close file
    file2 = open("AllDataUser.txt","w") #open file in write mode
    file2.writelines(firstFile) #to overwrite the selected lines with the new variable list
    file2.close() #close file
    customer_respond(UserAccount)



#respond function
def customer_respond(UserAccount):
    print("Type any key to return to main menu ")
    respond = (input(" "))
    while respond == True:
        if respond == " ":
            customer_account_menu(UserAccount)
            break

def admin_respond(UserAccount):
    print("Type any key to return to main menu ")
    respond = (input(" "))
    while respond == True:
        if respond == " ":
            admin_account_menu(UserAccount)
            break

def super_respond(UserAccount):
    print("Type any key to return to main menu ")
    respond = (input(" "))
    while respond == True:
        if respond == " ":
            super_account_menu(UserAccount)
            break


def login_menu():
    while True :
        print ("\n\n",80*"*","\n\n\t\t\t\tWELCOME TO NEST BANK\n\n")
        UserName = input("Enter your account username   : ")
        UserPassword = input("Enter your password   : ")
        file1 = open("AllDataUser.txt","r") #open file in read mode
        for rec in file1: #to read all the data in the file
            UserAccount = rec.split(" | ") #to data is split with " | "
            username = UserAccount[0]
            userpassword = UserAccount[1]
            if UserName =="SUC0000001" and UserPassword == "PasswordSuper":
                print("Super Account login successful!")
                super_account_menu(UserName)
                break
            elif (UserName[0:3] == "AUA" and UserName == username) and UserPassword == "PasswordAdmin":
                print("Admin Account login successful!")
                admin_account_menu(UserName)
                break
            elif UserName == username and UserPassword == userpassword:
                print("Customer Account login successful!")
                customer_account_menu(UserName)
                break
        if UserName != username and UserPassword != userpassword :
            print("Invalid username or password! \nPlease try again!")
        file1.close() #close file
        




login_menu()

