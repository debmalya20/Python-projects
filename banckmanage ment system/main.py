import json
import random
import string
from pathlib import Path


class bank:
    database = "data.json"
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                content = fs.read()
                data = json.loads(content) if content.strip() else []
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An exception occurred: {err}")

    @classmethod
    def _update(cls):                   
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def _accountgenerate(cls):          
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info = {
            "Name": input("Enter your name= "),
            "Age": int(input("Enter your age= ")),
            "Email": input("Enter your email= "),
            "Pin": int(input("Enter your 4 digit pin= ")),
            "AccountNo": bank._accountgenerate(),  
            "Balance": 0,
        }
        if info["Age"] < 18 or len(str(info["Pin"])) != 4:
            print("Sorry! You are not eligible for creating account.")
        else:
            print("Account created successfully!")
            for i in info:
                print(f"{i} = {info[i]}")
            print("Please note down your account number!")
            bank.data.append(info)
            bank._update()                         


user = bank()
print("Press 1 for creating new account.")
print("Press 2 for deposit money")
print("Press 3 for withdrawal money")
print("Press 4 for account details")
print("Press 5 for updating details")
print("Press 6 for deleting account")

check = int(input("Tell your response= "))

if check == 1:
    user.createaccount()