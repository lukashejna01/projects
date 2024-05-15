from bank_account import BankAcc
import os
import time

def clear():
    time.sleep(2)
    os.system('clear')

def main():
    """
    Main function of the bank system.
    """
    while True:
        print("Vítejte v bankovním systému!")
        choice = input("Chcete se přihlásit (p), registrovat (r) nebo vypnout systém (v)? ").lower()
        if choice not in {'p', 'r', 'v'}:
            print("Neplatná volba!")
            clear()
            continue
        if choice == 'p':
            message = "Neplatné uživatelské jméno nebo PIN!"
            register = False
            clear()
        elif choice == 'r':
            name = input("Zadejte vaše jméno: ")
            message = "Registrace proběhla úspěšně!"
            register = True
        else:
            clear()
            exit()

        username = input("Zadejte uživatelské jméno: ")
        pin = int(input("Zadejte PIN: "))
        bank_acc = BankAcc("data.json", username, pin, name if register else None)
        if register:
            bank_acc.register()
        logged_user = bank_acc.login()
        if logged_user:
            handle_user(logged_user)
        else:
            print(message)

def handle_user(user):
    """
    Handles user actions after successful login or register.
    """
    while True:
        print("""
    Vyberte akci:
        1. Zobrazit aktuální zůstatek
        2. Vložit peníze na účet
        3. Vybrat peníze z účtu
        4. Převést peníze na jiný účet
        5. Odhlásit se
        """)

        choice = input("Zadejte číslo akce: ")

        match choice:
            case '1':
                print(f"Aktuální zůstatek: {user.get_current_balance()} Kč")
                clear()
            case '2':
                amount = float(input("Zadejte částku k vložení: "))
                user.deposit(amount)
                print("Částka byla vložena na účet.")
                clear()
            case '3':
                amount = float(input("Zadejte částku k výběru: "))
                if user.withdraw(amount):
                    print("Částka byla vybrána z účtu.")
                else:
                    print("Nedostatečné prostředky na účtu.")
                clear()
            case '4':
                recipient_username = input("Zadejte uživatelské jméno příjemce: ")
                amount = float(input("Zadejte částku k převodu: "))
                if user.transfer(recipient_username, amount):
                    print("Převod proběhl úspěšně.")
                else:
                    print("Nedostatečné prostředky na účtu nebo neplatné uživatelské jméno příjemce.")
                clear()
            case '5':
                clear()
                print("Odhlášení proběhlo úspěšně.")
                break
            case _:
                print('Neplatná volba')
                clear()

if __name__ == "__main__":
    main()
