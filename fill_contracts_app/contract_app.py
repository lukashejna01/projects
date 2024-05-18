import tkinter as tk
from tkinter import messagebox
from user_input_frame import UserInputFrame
from contract_manager import ContractManager

class ContractApp:
    """
    The main application class to initialize the Tkinter window and manage the workflow.
    """
    def __init__(self, root):
        """
        Initializes the ContractApp with the root Tkinter widget.

        Args:
            - root (tk.Tk): The root Tkinter widget.
        """
        self.root = root
        self.root.title('Vyplnění smluv')
        self.root.geometry('600x500+600+300')
        self.create_widgets()

    def create_widgets(self):
        """
        Creates all necessary widgets for the application.
        """
        self.create_header()
        self.user_input_frame = UserInputFrame(self.root)
        self.create_checkboxes()
        self.create_fill_button()

    def create_header(self):
        """
        Creates the header label.
        """
        header_frame = tk.Frame(self.root)
        header_frame.grid(padx=20, pady=10, sticky='ew')
        header_label = tk.Label(header_frame, text='Základní údaje', font=('Arial', 16))
        header_label.grid(sticky='ew')

    def create_checkboxes(self):
        """
        Creates checkboxes for selecting which contracts to fill.
        """
        checkbox_frame = tk.Frame(self.root)
        checkbox_frame.grid(padx=20, pady=10, sticky='ew')

        checkbox_label = tk.Label(checkbox_frame, text='Vyberte smlouvy k vyplnění', font=('Arial', 12))
        checkbox_label.grid(row=0, columnspan=2, sticky='w')

        self.dpc_var = tk.BooleanVar()
        self.dpp_var = tk.BooleanVar()

        dpc_checkbox = tk.Checkbutton(checkbox_frame, text='DPČ', variable=self.dpc_var)
        dpp_checkbox = tk.Checkbutton(checkbox_frame, text='DPP', variable=self.dpp_var)

        dpc_checkbox.grid(row=1, column=0, sticky='w')
        dpp_checkbox.grid(row=1, column=1, sticky='w')

    def create_fill_button(self):
        """
        Creates the fill button to trigger the contract filling process.
        """
        button_frame = tk.Frame(self.root)
        button_frame.grid(padx=20, pady=10, sticky='ew')

        fill_button = tk.Button(button_frame, text='Vyplnit smlouvy', command=self.on_fill_button_click)
        fill_button.grid(sticky='ew')

    def on_fill_button_click(self):
        """
        Handles the fill button click event.
        """
        data = self.user_input_frame.get_data()
        contract_manager = ContractManager(data, 'vyplnene-smlouvy'
)
        contract_manager.fill_selected_contracts(self.dpc_var.get(), self.dpp_var.get())
        messagebox.showinfo("Info", "Smlouvy byly vyplněny a uloženy.")
