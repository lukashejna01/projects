import os
import time
import json

class bankMethods:
    """
    Tato třída poskytuje metody pro manipulaci s bankovními účty uloženými v JSON souboru.

    Atributy:
    - acc (str): Uživatelské jméno bankovního účtu, se kterým se provádějí operace.
    - amt (float): Aktuální zůstatek na bankovním účtu pro zadané uživatelské jméno.
    """
    
    def __init__(self, account):
        self.acc = account
        self.amt = self.get_current_balance()
    
    def get_current_balance(self):
        """
        Získá aktuální zůstatek bankovního účtu z JSON souboru
        """
        with open("users.json", "r", encoding="utf-8") as file:
            user_data = json.load(file)
            for user in user_data:
                for username, data in user.items():
                    if username == self.acc:
                        return data["balance"]
            print("Účet nenalezen.")
            return None
    
    def vklad(self):
        """
        Metoda pro vložení peněz na bankovní účet
        """
        deposit = float(input("Zadejte částku k vložení: "))
        self.amt += deposit
        self.update_amount_in_users()
        self.print_current_balance()
    
    def vyber(self):
        """
        Metoda pro výběr peněz z bankovního účtu
        """
        withdrawal = float(input("Zadejte částku k výběru: "))
        if withdrawal <= self.amt:
            self.amt -= withdrawal
            self.update_amount_in_users()
            self.print_current_balance()
        else:
            print("Nedostatečné prostředky na účtu.")
    
    def aktual(self):
        """
        Metoda pro zjištění aktuálního zůstatku na bankovním účtu.
        """
        self.print_current_balance()
    
    def update_amount_in_users(self):
        """
        Aktualizuje zůstatek na bankovním účtu v JSON souboru.
        """
        with open("users.json", "r+", encoding="utf-8") as file:
            user_data = json.load(file)
            for user in user_data:
                for username, data in user.items():
                    if username == self.acc:
                        data["balance"] = self.amt
                        break
            file.seek(0)
            json.dump(user_data, file, indent=4, ensure_ascii=False)
    
    def print_current_balance(self):
        """
        Vypíše aktuální zůstatek na bankovním účtu.
        """
        print(f"Váš aktuální zůstatek je: {self.amt} Kč.")
