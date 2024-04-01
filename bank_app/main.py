from bank_methods import bankMethods
from bank_account import bankAcc
import os
import time
import json

def create_acc():
    # Přidání nového uživatele
    new_name = input("Zadejte jméno a příjmení: ")
    new_user_name = input("Zadejte uživatelské jméno, kterým se budete přihlašovat: ")
    new_user_pin = input("Zadejte váš PIN: ")
    new_balance = 0
    new_user = {new_user_name: {"name": new_name, "PIN": new_user_pin, "balance": new_balance}}

    # Kontrola existence souboru
    if os.path.exists("users.json") and os.stat("users.json").st_size > 0:
        # Načtení existujících dat
        with open("users.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = []

    # Přidání nového uživatele k existujícím datům
    data.append(new_user)

    # Zápis dat zpět do souboru
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    print("Váš účet byl úspěšně vytvořen.")
    
    # Po vytvoření účtu spustit metody pro provádění operací
    metody(bankMethods(new_user_name))

def login():
    user_name = input("Zadejte uživatelské jméno: ")
    with open("users.json", "r", encoding="utf-8") as file:
        user_data = json.load(file)
        for user in user_data:
            for username, data in user.items():
                if user_name == username:
                    pin_input = input("Zadejte PIN: ")
                    if pin_input == data["PIN"]:
                        print("Přihlášení proběhlo úspěšně.")
                        return bankMethods(username)
                    else:
                        print("Nesprávný PIN kód.")
                        return False
        print("Účet nenalezen.")
        return False

def metody(user_account):
    while True:
        operation = input("Jakou operaci chcete provést? (w - výběr, d - vklad, a - aktuální zůstatek, q - pro odhlášení):\n")
        if operation == "w":
            user_account.vyber()
        elif operation == "d":
            user_account.vklad()
        elif operation == "a":
            user_account.aktual()
        elif operation == "q":
            print("Byli jste odhlášeni.")
            time.sleep(2)
            os.system("cls")
            break
        else:
            print("Neplatná volba. Zkuste to znovu")

lets_continue = True

while lets_continue:
    print("Vítejte v bankovním systému!")
    log_or_new = input("Chcete se přihlásit (l) nebo založit nový účet (n)?\n").lower()
    if log_or_new == "l":
        user_account = login()
        if user_account == False:
            print("Nepodařilo se přihlásit. Zkuste to znovu.")
            time.sleep(2)
            os.system('cls')
            continue  
        metody(user_account)
    elif log_or_new == "n":
        create_acc()
    elif log_or_new == "k":
        lets_continue = False