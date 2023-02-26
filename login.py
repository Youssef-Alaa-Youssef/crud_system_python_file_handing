import datetime
import re
import os
import time


EREGEX = r"[^@]+@[^@]+\.[^@]+"
PASSREGEX = r"(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

def validationEmail():
    while True:
        email = input("Enter Your Email  : ").lower()
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


def projecttitle(title):
    while True:
        if title.isalpha():
            return title
        else:
            print(f"{title} must consist only of String. Please try again.")


def totalTarget(targetAmount):
    while True:
        if targetAmount.isdigit():
            return targetAmount
        else:
            print(f"{targetAmount} must consist only of numbers. Please try again.")


def setDates(start_date, end_date):
    try:
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        if start > end:
            print("Error: The start date cannot be after the end date.")
        else:
                return f"{start.strftime('%B %d, %Y')}:{end.strftime('%B %d, %Y')}"
    except ValueError:
        print("Error: Please enter the dates in the format 'YYYY-MM-DD'.")


def Menu():
    projectName = input("Enter The name of your project : ")
    fileName = input(f"Enter Your file Name in {projectName} :")
    if not os.path.isdir(projectName):
        os.system(f"mkdir {projectName};cd {projectName};touch {fileName}")
    else:
        Menu()
    title = input("Enter your project title : ")
    while title =="":
            title = input("Enter your project title : ")
    protitle = projecttitle(title)
    details = input("Enter your project details : ")
    target = input("Enter Your target : ")
    while target =="" or  target.isalpha():
            target = input("Enter Your target : ")
    startDate = input("Enter Your Start Date :")
    endDate = input("Enter Your End Date : ")
    dates = setDates(startDate, endDate)
    with open(f"{projectName}/{fileName}", "a") as userInfo:
        userInfo.write(f"{round(time.time())}:{protitle}:{details}:{target}:{dates}\n")


user = ""


def Login():
    email = validationEmail()

    password = validationPassword()

    with open('Database.txt', 'r') as file:
        for line in file:
            stored_email = line.split(':')[3]
            stored_password = line.split(':')[4]
            global user
            user_name = line.split(':')[1]
            user = user_name
            if email == stored_email and password == stored_password:
                os.system("clear")
                print(f"Welcome {user} :)")
                options()
        else:
            print("Invalid email or password")


def mainOptions():
    while True:
        print("Main Menu:")
        print("1. Registeration ")
        print("2. Login ")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            import validation
        elif choice == "2":
            Login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def edit():
    projectName = input("Enter The name of your project : ")
    fileEdit = input("Enter The name of your file will be edit : ")
    if os.path.isdir(projectName):
        print("welcome")
        os.system(f"cd {projectName};")
        try:      
            with open(f"{projectName}/{fileEdit}", 'r') as file:
                content = file.readlines()
                print(content)
                Name = input("Enter ID in this file : ")
                print(type(Name))
                for line in content:
                    print(type(line.split(":")[0] ))
                    if line.split(":")[0] == Name:
                        print(line)
                        parts = list(line.strip().split(":"))
                        for part in range(len(parts)):
                            while True:
                                print("Menu:")
                                print("1. Change Title ")
                                print("2. Change Details ")
                                print("3. Change Target ")
                                print("4. Change Date ")
                                print("5. Exit")
                                choice = input("Enter your choice : ")
                                if choice == "1":
                                    title = input("Enter your project title : ")
                                    parts[1] = projecttitle(title)
                                    break
                                elif choice == "2":
                                    parts[2] = input(
                                        "Enter your project details : ")
                                    break

                                elif choice == "3":
                                    target = input("Enter Your target : ")
                                    parts[3] = totalTarget(target)
                                    break
                                elif choice == "4":
                                    startDate = input("Enter Your Start Date :")
                                    endDate = input("Enter Your End Date : ")
                                    parts[4] = setDates(startDate, endDate)
                                    break
                                elif choice == "5":
                                    os.system("clear")
                                    break
                                else:
                                    print("Invalid choice. Please try again.")
                            print(parts)
                            break
                    else:
                        parts =content
        except Exception as err:
                print(f"{err}")
        try:
            with open(f"{projectName}/{fileEdit}", 'w') as file:
                line =':'.join(parts)+'\n'
                file.writelines(line)
        except Exception as err:
            print("File Must Be Entered Before Edit")
       

    else:
        print(f"{projectName} Not Found")


def addContent():
    projectName = input("Enter The name of your project : ")
    addContent = input(
        "Enter The name of your file will be add content in it : ")
    if os.path.isdir(projectName):
        os.system(f"cd {projectName};")
        title = input("Enter your project title : ")
        while title =="":
            title = input("Enter your project title : ")
        protitle = projecttitle(title)
        details = input("Enter your project details : ")
        target = input("Enter Your target : ")
        while target =="" or  target.isalpha():
            target = input("Enter Your target : ")
        totlaltarget = totalTarget(target)
        startDate = input("Enter Your Start Date :")
        endDate = input("Enter Your End Date : ")
        dates = setDates(startDate, endDate)
        try:
            with open(f"{projectName}/{addContent}", "a") as userInfo:
                userInfo.write(f"{round(time.time())}:{protitle}:{details}:{totlaltarget}:{dates}\n")
        except Exception as err:
            print("File Must Be Entered")

    else:
        print(f"{projectName} Not Found")


def delete():
    projectName = input("Enter The name of your project : ")
    fileDelete = input("Enter The name of your file will be Delete : ")
    if fileDelete =="":
       fileDelete = input("Enter The name of your file will be Delete : ")       
    if os.path.isdir(projectName):
            os.system(f"cd {projectName};rm {fileDelete}")
            print("Your project Deleted Successfully.")

    else:
        print(f"{projectName} Not Found")


def add():
    projectName = input("Enter The name of your project : ")
    AddFile = input("Enter The name of your file will be add : ")
    if os.path.isdir(projectName):
        os.system(f"cd {projectName};touch {AddFile}")
        title = input("Enter your project title : ")
        while title =="":
            title = input("Enter your project title : ")
        protitle = projecttitle(title)
        details = input("Enter your project details : ")
        target = input("Enter Your target : ")
        while target =="" or  target.isalpha():
            target = input("Enter Your target : ")

        startDate = input("Enter Your Start Date :")
        endDate = input("Enter Your End Date : ")
        dates = setDates(startDate, endDate)
        try:
            with open(f"{projectName}/{AddFile}", "a") as userInfo:
                userInfo.write(f"{round(time.time())}:{protitle}:{details}:{target}:{dates}\n")
        except Exception as err:
            print("File Must Be Entered")

    else:
        print(f"{projectName} Not found")
    


def DeleteAllProject():
    projectName = input("Enter The name of your project : ")
    if os.path.isdir(projectName):
        os.system(f"rm -rf {projectName}")
    else:
        print(f"{projectName} Not found")


def options():
    while True:
        print("Menu:")
        print("1. Create Project ")
        print("2. Edit Your Proect ")
        print("3. Delete Your project ")
        print("4. add File ")
        print("5. Delete All Project ")
        print("6. Add content to exist project ")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Menu()
        elif choice == "2":
            edit()
        elif choice == "3":
            delete()
        elif choice == "4":
            add()
        elif choice == "5":
            DeleteAllProject()
        elif choice == "6":
            addContent()
        elif choice == "7":
            os.system("clear")
            break
        else:
            print("Invalid choice. Please try again.")


mainOptions()
