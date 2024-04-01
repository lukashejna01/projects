import os
import time
import json

class bankMethods:
    
    def __init__(self, account):
        self.acc = account
        self.amt = self.get_current_balance()
    
    def get_current_balance(self):
        with open("users.json", "r", encoding="utf-8") as file:
            user_data = json.load(file)
            for user in user_data:
                for username, data in user.items():
                    if username == self.acc:
                        return data["balance"]
            print("Účet nenalezen.")
            return None
    
    def vklad(self):
        deposit = float(input("Zadejte částku k vložení: "))
        self.amt += deposit
        self.update_amount_in_users()
        self.print_current_balance()
    
    def vyber(self):
        withdrawal = float(input("Zadejte částku k výběru: "))
        if withdrawal <= self.amt:
            self.amt -= withdrawal
            self.update_amount_in_users()
            self.print_current_balance()
        else:
            print("Nedostatečné prostředky na účtu.")
    
    def aktual(self):
        self.print_current_balance()
    
    def update_amount_in_users(self):
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
        print(f"Váš aktuální zůstatek je: {self.amt} Kč.")