class bankAcc:
    """
    Tato třída slouží k uchování základních údajů uživatele bankovního účtu.

    Parametry:
    - name (str): Jméno vlastníka bankovního účtu.
    - user_name (str): Uživatelské jméno pro přihlášení k účtu.
    - user_pin (str): PIN kód pro přihlášení k účtu.
    """
    def __init__(self, name, user_name, user_pin):
        self.name = name
        self.u_name = user_name
        self.u_pin = user_pin
