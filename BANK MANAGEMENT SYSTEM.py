class bank:
    def __init__(self,amount=0,withdraw=0,name='',type='',address='',phone=0,accno=1000,balance=0,deposit=0):
        self.name=name
        self.address=address
        self.phone=phone
        self.balance=balance
        self.deposit=deposit
        self.accno=accno
        self.type=type
        self.amount=amount
    
class accdetails(bank):
    def createAccount(self):
        self.name=input("enter the name:")
        self.phone=int(input("enter the phone no:"))
        self.address=input("enter the address:")
        self.type = input("Ente the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
        print("\n\n\nAccount Created")
        self.accno+=1
    def showAccount(self):
        print("Account Numer:",self.accno)
        print("Account Holder Name:",self.name)
        print("Account Holder Phone Number:",self.phone)
        print("Account Holder Address:",self.address)
        print("Account Type:",self.type)
        print("Balance:",self.deposit)
    def modifyAccount(self):
        print("Account Number : ",self.accno)
        self.name = input("Modify Account Holder Name :")
        self.phone=int(input("Modify Account Holder phone no:"))
        self.address=input("Modify Account Holder address:")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))

    def depositAmount(self):
        self.amount=int(input("Enter Your Deposit Amount:"))
        self.deposit += self.amount
        print("The Total Balance is:",self.deposit)
    
    def withdrawAmount(self):
        self.amount=int(input("Enter Your Withdraw Amount:"))
        self.deposit -= self.amount
        print("The Total Balance is:",self.deposit)

    def balance(self):
        print(self.deposit) 
        

class transact(accdetails):
    def loans(self):
        print("1.educational loan")
        print("2.agriculture loan")
        print("3.bussiness loan")
        d=int(input("enter the option:"))
        if d==1:
            print("1.college fees or school fees")
            print("2.educational support")
            e=int(input("enter your choice:"))
            if e==1:
                f=int(input("enter the fees amount:"))
                t=int(input("enter time duration:"))
                interest=((0.2*f*t)/100)
                print("fees amount and added interest",interest)
            elif e==2:
                f=int(input("enter the educational support amount:"))
                t=int(input("enter time duration:"))
                interest=((0.2*f*t)/100)
                print("fees amount and added interest",interest)
            else:
                print("enter the valid option")
        elif d==2:
            print("1.crop cultivation")
            print("2.agriculture support")
            p=int(input("enter your choice:"))
            if p==1:
                f=int(input("enter the amount:"))
                t=int(input("enter time duration:"))
                interest=((0.2*f*t)/100)
                print("fees amount and added interest",interest)
            elif p==2:
                f=int(input("enter the agriculture support amount:"))
                t=int(input("enter time duration:"))
                interest=((0.2*f*t)/100)
                print("fees amount and added interest",interest)
            else:
                print("enter the valid option")
        elif d==3:
            print("1.start up loan")
            print("2.personal loan")
            w=int(input("enter your choice:"))
            if w==1:
                f=int(input("enter the  amount:"))
                t=int(input("enter time duration:"))
                interest=((0.2*f*t)/100)
                print("fees amount and added interest",interest)
            elif w==2:
                f=int(input("enter the personal support amount:"))
                t=int(input("enter time duration:"))
                interest=((0.2*f*t)/100)
                print("fees amount and added interest",interest)
            else:
                print("enter the valid option")
        else:
            print("enter the valid option")
            
class over(transact):
    def bb(self):
        print("visit us again :)")
z=over()

while True:

     print("\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$$\n\t\t\t-------WELCOME YOUR BANK-------\n\t\t\t\t$$$$$$$$$$$$$$$$$$$$$$$$")
     print("\t1. NEW ACCOUNT OPEN")
     print("\t2. ALL ACCOUNT HOLDER LIST")
     print("\t3. MODIFY ACCOUNT DETAILS")
     print("\t4. CHECK BALANCE")
     print("\t5. DEPOSIT AMOUNT")
     print("\t6. WITHDRAW AMOUNT")
     print("\t7. LOAN AMOUNT")
     print("\t8. EXIT")

     ch=int(input("Select Your Option From Above Box Menu:"))

     if ch==1:
         z.createAccount()

     elif ch==2:
         z.showAccount()

     elif ch==3:
         z.modifyAccount()

     elif ch==4:
         z.balance()

     elif ch==5:
         z.depositAmount()

     elif ch==6:
         z.withdrawAmount()

     elif ch==7:
         z.loans()

     elif ch==8:
         quit()

     else:
         print("Enter Valid Option")
         
         
                
                    
                
                
