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
        with open(cls.database, "w") as fs:
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
            "Pin": int(input("Create your 4 digit pin= ")),
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

    def depositmoney(self):
        accnumber = input("Enter your account number= ").strip()
        pin = int(input("Enter your pin number= "))

        # print(f"\nYou entered AccNo: '{accnumber}'")
        # print(f"You entered Pin: {pin}")
        # print(f"Bank data loaded: {bank.data}")

        userdata = [
            i for i in bank.data if i["AccountNo"] == accnumber and i["Pin"] == pin
        ]

        if not userdata:
            print("Sorry wrong account number! Please try again.")
        else:
            amount = int(input("Enter how much money you want to deposit= "))
            if amount > 10000 or amount < 0:
                print(
                    "Sorry amount is too high! You can only deposit below 10000 & above 0."
                )
            else:
                userdata[0]["Balance"] += amount
                bank._update()
                print("Amount deposited successfully! :)")


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
if check == 2:
    user.depositmoney()
