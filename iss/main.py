import requests
from tkinter import *

# Získání počátečních údajů o poloze ISS
response_location = requests.get("http://api.open-notify.org/iss-now.json")
response_location.raise_for_status()
data_location = response_location.json()
longitude = data_location["iss_position"]["longitude"]
latitude = data_location["iss_position"]["latitude"]

# Získání počátečního počtu lidí ve vesmíru
response_people = requests.get("http://api.open-notify.org/astros.json")
response_people.raise_for_status()
data_people = response_people.json()
people = data_people["number"]

# Nastavení fontu a barev
bg_color = "#0c0c32"
fg_color = "#81dfc0"
main_font = ("Times New Roman", 12, "bold")

# Okno
window = Tk()
window.geometry("300x100+600+250")
window.title("Aktuální údaje o ISS")
window.config(bg=bg_color)
window.resizable(False, False)

# Popisky
Label(text="Zeměpisná délka:", bg=bg_color, fg=fg_color, font=main_font).grid(row=0, column=0, sticky=W, padx=10, pady=2)
Label(text="Zeměpisná šířka:", bg=bg_color, fg=fg_color, font=main_font).grid(row=1, column=0, sticky=W, padx=10, pady=2)
Label(text="Počet lidí ve Vesmíru: ", bg=bg_color, fg=fg_color, font=main_font).grid(row=2, column=0, padx=10, pady=2)

actual_longitude = Label(bg=bg_color, fg=fg_color, font=main_font)
actual_longitude.grid(row=0, column=1)

actual_latitude = Label(bg=bg_color, fg=fg_color, font=main_font)
actual_latitude.grid(row=1, column=1)

number_people = Label(bg=bg_color, fg=fg_color, font=main_font)
number_people.grid(row=2, column=1)

# Funkce pro aktualizaci polohy ISS
def update_iss_location():
    response_location = requests.get("http://api.open-notify.org/iss-now.json")
    response_location.raise_for_status()
    data_location = response_location.json()
    longitude = data_location["iss_position"]["longitude"]
    latitude = data_location["iss_position"]["latitude"]
    actual_longitude.config(text=longitude)
    actual_latitude.config(text=latitude)
    window.after(5000, update_iss_location)  # Aktualizace každých 5 sekund

# Funkce pro aktualizaci počtu lidí ve vesmíru
def update_iss_people():
    response_people = requests.get("http://api.open-notify.org/astros.json")
    response_people.raise_for_status()
    data_people = response_people.json()
    people = data_people["number"]
    number_people.config(text=people)
    window.after(10000, update_iss_people)  # Aktualizace každých 10 sekund

# Spuštění aktualizací
update_iss_location()
update_iss_people()

# Hlavní smyčka
window.mainloop()
