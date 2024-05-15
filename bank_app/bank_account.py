import json, os
from bank_methods import BankMethods

class BankAcc:
    def __init__(self, filename:str, user_name:str, user_pin:int, name:str = None):
        """
        Initializes a Bank Account object with necessary attributes.

        Args:
            - filename (str): The name of the file to store user data.
            - user_name (str): The username of the account holder.
            - user_pin (int): The PIN associated with the user account.
            - name (str, optional): The name of the account holder. Defaults to None.
        """
        self._name = name
        self.user_name = user_name
        self._user_pin = user_pin
        self.filename = filename
    
    def register(self):
        """
        Registers a new user account by storing account details in a JSON file.
        """
        if os.path.exists(self.filename) and os.stat(self.filename).st_size > 0:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = {}
        data[self.user_name] = {
            'name': self._name,
            'PIN': self._user_pin,
            'balance': 0,
        }

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
    def login(self):
        """
        Logs in an existing user by verifying username and PIN from stored data.

        Returns:
        - BankMethods object if login is successful, else returns False.
        """
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if self.user_name in data and data[self.user_name]['PIN'] == self._user_pin:
                    return BankMethods(self.filename, self.user_name)
        return False