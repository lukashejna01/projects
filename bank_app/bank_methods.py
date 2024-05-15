import json

class BankMethods:
    def __init__(self, filename:str, username:str):
        """
        Initializes BankMethods object with necessary attributes.

        Args:
            - filename (str): The name of the file containing user data.
            - username (str): The username associated with the account.
        """
        self.user_name = username
        self.file_name = filename
        self._balance = self.get_current_balance()

    def get_current_balance(self):
        """
        Gets the current balance of the user.

        Returns:
            - int or False: The current balance if user exists, False otherwise.
        """
        with open(self.file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if self.user_name in data:
                return data[self.user_name]["balance"]
            return False
    
    def update_balance(self):
        """
        Updates the balance of the user in the file.
        """
        with open(self.file_name, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            if self.user_name in data:
                data[self.user_name]['balance'] = self._balance
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

    def deposit(self, amount):
        """
        Deposits the specified amount into the user's account.
        """
        self._balance += amount
        self.update_balance()

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the user's account.

        Returns:
            - bool: True if withdrawal is successful, False otherwise.
        """
        if amount > self._balance:
            return False
        self._balance -= amount
        self.update_balance()
        return True

    def transfer(self, recipient_username, amount):
        """
        Transfers the specified amount from the user's account to the recipient's account.

        Args:
            - recipient_username (str): The username of the recipient.
            - amount (int): The amount to transfer.

        Returns:
            - bool: True if transfer is successful, False otherwise.
        """
        if self._balance >= amount:
            self.withdraw(amount)
            self.update_balance()

            recipient_account = BankMethods(self.file_name, recipient_username)
            recipient_account.deposit(amount)
            recipient_account.update_balance()
            return True
        return False
        
    def __str__(self):
        return self._balance