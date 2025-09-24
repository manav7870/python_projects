# print("ATM Machine")
# bal=15000
# num=int(input("Enter your card number: "))
# if num == 1234:
#     pin=int(input("Enter the your pin number: "))
#     if pin ==6622:
#         while True:
#             print("Welcome to ATM")
#             print(f"Total Balance: {bal}")
#             print("Press 1 to check balance")
#             print("Press 2 to withdraw money")
#             print("Press 3 to deposit money")
#             print("Press 4 to exit")
#             choice=int(input("Enter your choice: " ))
#             if choice == 1:
#                 print(f"Your total balance is: {bal}")
#             elif choice == 2:
#                 wid = int(input("Enter the withdrawal amount:  "))
#                 if wid<=bal:
#                     bal-=wid
#                     print(f"Your current balance is: {bal}")
#                 else:
#                     print("Insufficient balance")    
#             elif choice == 3:
#                 dep=int(input("Enter the deposit amount: "))
#                 bal+=dep
#                 print(f"Your current balance is: {bal}")
#             elif choice == 4:
#                 print("You have been logged out")
#                 break
#             else:
#                 print("Invalid Number")
#     else:
#         print("Pin is Incorrect")
# else:
#     print("Invalid card Number")

#ATM Machine by single class
class A:
    def displayA(self):
        print("ATM Machine")
        bal=15000
        num=int(input("Enter your card number: "))
        if num == 1234:
            pin=int(input("Enter the your pin number: "))
            if pin ==6622:
                while True:
                    print("Welcome to ATM")
                    print(f"Total Balance: {bal}")
                    print("Press 1 to check balance")
                    print("Press 2 to withdraw money")
                    print("Press 3 to deposit money")
                    print("Press 4 to exit")
                    choice=int(input("Enter your choice: " ))
                    if choice == 1:
                        print(f"Your total balance is: {bal}")
                    elif choice == 2:
                        wid = int(input("Enter the withdrawal amount:  "))
                        if wid<=bal:
                            bal-=wid
                            print(f"Your current balance is: {bal}")
                        else:
                            print("Insufficient balance")    
                    elif choice == 3:
                        dep=int(input("Enter the deposit amount: "))
                        bal+=dep
                        print(f"Your current balance is: {bal}")
                    elif choice == 4:
                        print("You have been logged out")
                        break
                    else:
                        print("Invalid Number")
            else:
                print("Pin is Incorrect")
        else:
            print("Invalid card Number")
a1=A()
a1.displayA()