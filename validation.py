

import re
import time

PREGEX = r"^01[0-9]{9}$"
EREGEX = r"[^@]+@[^@]+\.[^@]+"
PASSREGEX = r"(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"


def validationFirstName():
    while True:
        first_name = input("Enter Your First Name : ").lower()
        if first_name.isalpha():
            return first_name
        else:
            print(f"{first_name} must consist only of String. Please try again.")


def validationLastName():
    while True:
        last_name = input("Enter Your Last Name : ").lower()
        if last_name.isalpha():
            return last_name
        else:
            print(f"{last_name} must consist only of String. Please try again.")


def validationEmail():
    while True:
        email = input("Enter Your Email  : ")
        if re.match(EREGEX, email):
            return email
        else:
            print("Invalid email format.")


def validationPassword():
    while True:
        password = input("Enter Your Password : ")

        if re.match(PASSREGEX, password) and len(password) >= 8:
            return password
        else:
            print("Invalid Password format. and must be greater or equal 8")


def validationConfirm(password):
    while True:
        ConfirmPassword = input("Enter Confirm Password ")
        if password == ConfirmPassword:
            return ConfirmPassword
        else:
            print("Confirm Password must be identical Password")


def validationPhone():
    while True:
        mobile_phone = input("Enter Your Phone Number : ")
        if re.match(PREGEX, mobile_phone):
            return mobile_phone
        else:
            print("Invalid Phone")


id = round(time.time())
firstName = validationFirstName()
lastName = validationLastName()
email = validationEmail()
password = validationPassword()
confromPassword = validationConfirm(password)
phoneNumber = validationPhone()


with open("Database.txt", "a") as userInfo:
    userInfo.write(
        f"{id}:{firstName}:{lastName}:{email}:{password}:{phoneNumber}\n")

# print("You entered:", firstName)
# print("You entered:", lastName)
# print("You entered:", email)
# print("You entered:", password)
# print("You entered:", confromPassword)
# print("You entered:", phoneNumber)
# print("Id", id)
