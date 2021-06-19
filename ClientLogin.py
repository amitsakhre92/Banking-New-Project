from controller import logincontroller
from controller import customerdetailcontroller
from controller import credit_amountcontrol
from controller import withdraw_amountcontrol
from controller import accountcreationcontrolller
from controller import mini_statement_control
from getpass import getpass
from controller import close_account_controller
from controller import kyc_controller
from datetime import datetime
from controller import yearlymonthlycontroll
from controller import balancecheckcontroller


def cust_info(username):
    global response
    response = customerdetailcontroller.customerdetail(username)

    if response is not None:
        print("\n\t\t\t\tHello", response[1])
        print("\n\t\t\t\tCUSTOMER_ID :", response[0])
        print("\n\t\t\t\tAccount Number :", response[2])
        print("\n\t\t\t\tIFSC CODE:", response[4])
        print("\n\t\t\t\tBranch_name: ", response[3])

    while True:
        print("\nWhat would you like to do:")
        print('''
                1. CREDIT
                2. DEBIT
                3. Balance check
                4. Mini Statement
                5. Yearly/Monthly Statement
                6. logout''')
        enter = int(input("Choose the option: "))

        if enter == 1:
            amount_credit(username)
        if enter == 2:
            amount_withdrawal(username)
        if enter == 3:
            balancecheck(username)
        if enter == 4:
            mini_statement(username)
        if enter == 5:
            wisestatement(username)
        if enter == 6:
            break


def checkforlogin():
    print("Please enter credential to verify yourself:")

    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    global response

    response = logincontroller.login(username, password)

    if response is None:
        print("You are not authorised to perform required activity !! ")
    else:
        print("You have successfully logged in !! Welcome : ")

        cust_info(response[0])


def addinformation():
    global response

    print("\n\t\t\t\tPlease enter your Personal Detail:")

    customer_name = input("\n\t\t\t\tPlease enter your name (Ex. Amit Sakhare): ").title().strip()

    address = input("\n\t\t\t\tPlease enter Address (Ex. plot no.2369 ravi pune): ").capitalize().strip()

    mobile_number = input("\n\t\t\t\tPlease enter MobileNumber(Ex. 99999999): ")

    email_id = input("\n\t\t\t\tPlease enter Email_ID: (Ex. xyz@yahoo.com): ").strip()

    date_of_birth_s = input("\n\t\t\t\tEnter the date of birth in format: dd-mon-yyyy: ")

    date_of_birth = datetime.strptime(date_of_birth_s, "%d-%b-%Y")

    aadhar_number = input("\n\t\t\t\tPlease Enter your aadhar Number(Ex.1234-1234-1234-1475): ")

    pan_number = input("\n\t\t\t\tPlease Enter your PAN Number(Ex.yu041865): ").strip()

    gender = input("\n\t\t\t\tPlease Enter your Gender(Ex. M or F): ").upper().strip()

    city = input("\n\t\t\t\tPlease Enter your City(Ex. Pune): ").capitalize().strip()

    pin_code = input("\n\t\t\t\tPlease Enter your Pin Code(Ex.400000)").strip()

    response = accountcreationcontrolller.accountcreate(customer_name, address, mobile_number, email_id,
                                                        date_of_birth, pan_number, aadhar_number, gender, city,
                                                        pin_code)


def amount_credit(username):
    global response
    print("How much amount would you like to deposit")
    amount = int(input("Enter the amount: "))
    response = credit_amountcontrol.credit_amountcontroll(username)
    account_balance = response[0] + amount
    account_number = response[1]
    credit_amountcontrol.updatebalances(account_balance, account_number, amount)
    print(f"Rs.{amount}/- amount is successfully credited in your account.")
    balancecheck(username)


def amount_withdrawal(username):
    global response
    print("How much amount would you like to withdraw")
    amount = int(input("Enter the Amount: "))
    response = withdraw_amountcontrol.withdraw_amountcontroll(username)
    if (response[0]) >= amount:
        account_balance = response[0] - amount
        account_number = response[1]
        withdraw_amountcontrol.updatebalance(account_balance, account_number, amount)
        print(f"Rs.{amount}/- amount is debited from your account successfully.")
        balancecheck(username)
    else:
        print("Insufficient amount")


def balancecheck(username):
    global response
    response = balancecheckcontroller.balancecheckcontroll(username)
    print(f"This is your current account balance: Rs.{response}/-")


def mini_statement(username):
    global response
    print(" This is your last 5 Transaction: ")
    response = mini_statement_control.mini_statementcontroll(username)
    # print(response)
    for responses in response:
        x = (responses[1].strftime("%d-%m-%Y"))
        statement = list(responses)
        statement.insert(1, x)
        statement.pop(2)
        print(statement)


def wisestatement(username):
    global response
    print('''
    1. Monthly Statement
    2. yearly statement
    ''')
    option = int(input("Enter your option:  "))
    if option == 1:
        response = yearlymonthlycontroll.monthlystate(username)
        for responses in response:
            x = (responses[1].strftime("%d-%m-%Y"))
            statement = list(responses)
            statement.insert(1, x)
            statement.pop(2)
            print(statement)

    elif option == 2:
        response = yearlymonthlycontroll.yearlystate(username)
        for responses in response:
            x = (responses[1].strftime("%d-%m-%Y"))
            statement = list(responses)
            statement.insert(1, x)
            statement.pop(2)
            print(statement)
    else:
        print("Choose correct option")


def close_account():
    print("Do you want to close account")
    print("1. yes \n2.NO")
    user_input = int("Please select one option")
    if user_input == 1:
        print("Please Enter User Name")
        username = input("Username")
        response = close_account_controller.closeaccountcontroll(username)
        print(response)
        print("Your account is close successfully")
    else:
        print("Thank You")


def kycverification():
    print("Please enter your user_name")
    username = input("USER_ID: ")
    print("Please enter Aadhar_number")
    addhar_number = input("Aadhar_number:")
    response2 = kyc_controller.kycincontroll(username)
    print(response2[0])
    if response2[0] == addhar_number:
        print("Your KYC Verification is completed successfully")
    else:
        print("Your KYC Verification is Fail")


def checkforadminlogin():
    print("Please enter credential to verify yourself:")

    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    global response

    response = logincontroller.adminlogin(username, password)

    if response is None:
        print("You are not authorised to perform required activity !! ")
    else:
        print("You have successfully logged in !! Welcome : ")

        while True:
            print("\nWhat would you like to do:")
            print('''
                    
                    1. CREDIT Amount
                    2. DEBIT Amount
                    3. Balance check
                    3. Mini Statement
                    4. Monthly/ yearly statement
                    5. KYC verification
                    6. Close Account
                    7. logout''')
            enter = int(input("Choose the option: "))
            username = input("Enter the username")

            if enter == 1:
                amount_credit(username)
            if enter == 2:
                amount_withdrawal(username)
            if enter == 3:
                balancecheck(username)
            if enter == 4:
                mini_statement(username)
            if enter == 5:
                wisestatement(username)
            if enter == 6:
                kycverification()
            if enter == 7:
                close_account()
            if enter == 8:
                break


while True:
    print("\n\t\t\t\tWELCOME TO ROYAL BANK")
    print("\t\t\t=============================")

    print("\nIt is our pleasure to serve you. kindly tell us what you want to do")
    print("\n(A)ccount Creation\n(C)ustomer Login\n(Ad)min login\n(Q)uit\n")

    Choice = input("Provide Input Here >>>>").lower().strip()

    if Choice == "a":
        addinformation()

    elif Choice == "c":
        checkforlogin()

    elif Choice == "ad":
        checkforadminlogin()

    elif Choice == "q":
        break

    else:
        print("Invalid Choice, Please Choose again\n")
