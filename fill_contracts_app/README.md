## ContractFillerApp
ContractFillerApp is a desktop application built using Python and Tkinter, designed to automate the filling of contract documents. The application allows users to input personal and job-related information, select the types of contracts they need, and generate personalized contract documents.

### Key Features:
- **User Input Management:** Collects user data through a graphical interface with various input fields.
- **Contract Selection:** Users can select which contracts to fill from the available options.
- **Automated Document Filling:** Automatically fills the selected contract templates with the user’s data.
- **Personalized Output:** Saves the filled contracts in a user-specific folder, named after the user, for easy access and organization.
- **Notification:** Informs the user once the contracts are successfully filled and saved.

### Technologies Used:
- Python
- Tkinter (for the graphical user interface)
- python-docx (for handling Word documents)
- os (for file and directory operations)
- datetime (for handling date information)

### Project Structure:
- `main.py`: The main script that initializes the application and handles the workflow.
- `user_input_frame.py`: Contains the `UserInputFrame` class responsible for creating and managing user input fields.
- `contract_manager.py`: Contains the `ContractManager` class responsible for filling and saving the contract documents.

### Getting Started:
To get started with ContractFillerApp, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the application.
