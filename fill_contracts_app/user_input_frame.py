import tkinter as tk
import datetime as dt

class UserInputFrame:
    """
    A class to create and manage user input fields.
    """
    def __init__(self, master):
        """
        Initializes the UserInputFrame with the master Tkinter widget.

        Args:
            - master (tk.Tk): The master Tkinter widget.
        """
        self.frame = tk.Frame(master)
        self.frame.grid(padx=20, pady=10, sticky='ew')
        self.entries = {}
        self.create_entries()

    def create_entries(self):
        """
        Creates entry widgets for user inputs.
        """
        entry_labels = {
            'first_name': 'Křestní jméno',
            'last_name': 'Příjmení',
            'birth': 'Datum narození',
            'residence': 'Bydliště',
            'type_of_work': 'Druh práce',
            'beginning_of_cooperation': 'Začátek spolupráce',
            'end_of_cooperation': 'Konec spolupráce',
            'work_location': 'Místo výkonu práce',
            'hourly_wage': 'Hodinová mzda'
        }

        for idx, (key, label) in enumerate(entry_labels.items()):
            self.create_entry(key, label, idx)
    
    def create_entry(self, key, label_text, row):
        """
        Creates a label and entry widget in the frame at the specified row.

        Args:
            - key (str): The key for the entry.
            - label_text (str): The text for the label.
            - row (int): The row number in the grid.
        """
        tk.Label(self.frame, text=label_text).grid(row=row, column=0, sticky='w')
        entry = tk.Entry(self.frame, width=70)
        entry.grid(row=row, column=1, sticky='ew')
        self.entries[key] = entry

    def get_data(self):
        """
        Collects data from the entry fields and returns it as a dictionary.

        Returns:
            - dict: A dictionary containing the user input data.
        """
        data = {f'[{key}]': entry.get() for key, entry in self.entries.items()}
        data['[current_date]'] = str(dt.date.today())
        return data
