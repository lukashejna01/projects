import os
from docx import Document

class ContractManager:
    """
    A class to manage filling and saving contracts.
    """
    def __init__(self, data, directory):
        """
        Initializes the ContractManager with data and directory.

        Args:
            - data (dict): The data to fill into the contracts.
            - directory (str): The directory to save the filled contracts.
        """
        self.data = data
        self.directory = directory
        os.makedirs(directory, exist_ok=True)
    
    def fill_contract(self, template_path, output_path):
        """
        Fills the contract template with provided data and saves it to the output path.

        Args:
            - template_path (str): The path to the contract template.
            - output_path (str): The path to save the filled contract.
        """
        try:
            doc = Document(template_path)
            for paragraph in doc.paragraphs:
                for key, value in self.data.items():
                    if key in paragraph.text:
                        paragraph.text = paragraph.text.replace(key, value)
            doc.save(output_path)
            print(f"Contract saved successfully at {output_path}")
        except Exception as e:
            print(f"An error occurred while filling the contract: {e}")

    def fill_selected_contracts(self, fill_dpc, fill_dpp):
        """
        Fills and saves the selected contracts based on user choice.

        Args:
            - fill_dpc (bool): Whether to fill the DPC contract.
            - fill_dpp (bool): Whether to fill the DPP contract.
        """
        if fill_dpc:
            dpc_path = os.path.join(self.directory, 'dpc.docx')
            self.fill_contract('dpc_nero_2024.docx', dpc_path)
        
        if fill_dpp:
            dpp_path = os.path.join(self.directory, 'dpp.docx')
            self.fill_contract('dpp_nero_2024.docx', dpp_path)
