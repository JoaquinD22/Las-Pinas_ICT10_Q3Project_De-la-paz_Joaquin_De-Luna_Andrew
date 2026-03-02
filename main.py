from js import document
import re

def check(event=None):
    reg = document.querySelector('input[name="reg"]:checked')
    med = document.querySelector('input[name="med"]:checked')
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    output_text = document.getElementById("output-text")
    output_img = document.getElementById("output-img")

    if reg is None or med is None:
        output_text.innerText = "Please answer all questions"
        output_img.src = ""

    elif reg.value != "yes" or med.value != "yes":
        output_text.innerText = "INELIGIBLE: Please make sure to register online and/or submit your medical clearance"
        output_img.src = "red.jpg"

    elif section == "sapphire":
        output_text.innerText = f"G{grade} - Sapphire: Blue Bears. Congratulations!"
        output_img.src = "blue.jpg"

    elif section == "ruby":
        output_text.innerText = f"G{grade} - Ruby: Red Bulldogs. Congratulations!"
        output_img.src = "red.jpg"

    elif section == "emerald":
        output_text.innerText = f"G{grade} - Emerald: Green Hornets. Congratulations!"
        output_img.src = "green.jpg"

    elif section == "topaz":
        output_text.innerText = f"G{grade} - Topaz: Yellow Tigers. Congratulations!"
        output_img.src = "yellow.jpg"

def sign_up(event=None):
    confirmation = document.getElementById("confirm")

    # Get username and password fields
    username = document.getElementById("username")
    password = document.getElementById("password")

    if confirmation is None or username is None or password is None:
        return 

    user_value = username.value
    pass_value = password.value

    # Requirement A: At least 10 characters
    if len(pass_value) < 10:
        confirmation.innerText = "❌ Password must be at least 10 characters long."
        return

    # Requirement B: At least one letter
    if not re.search("[A-Za-z]", pass_value):
        confirmation.innerText = "❌ Password must contain at least one letter."
        return

    # Requirement C: At least one number
    if not re.search("[0-9]", pass_value):
        confirmation.innerText = "❌ Password must contain at least one number."
        return

    # If all conditions are met
    confirmation.innerText = "✅ Account created. You may now log in using your credentials!"

def show_players(event=None):
    output_list = document.getElementById("output-list")

    if output_list is None:
        return

    people = [
        "Arevalo, Rhianna Mateo",
        "Atienza, Sebastian Caleb Bustamante",
        "Cubillas, Christian Emmanuel Lin",
        "David, Jolie Cassandra Marquez",
        "De Guzman, Stephanie Gaile",
        "De La Paz, Joaquin Matteo Altura",
        "De Leon, Marcus Theoden Catimpo",
        "De Luna, Andrew James Alipio",
        "Deinla, Brennan Shane Castillo",
        "Elevazo, John Rony Laurilla",
        "Francisco, Amber Ephesiah Manansala",
        "Ganal, Franceska Marie Salvador",
        "Lacerna, Atashya Khariz Coquilla",
        "Lavilla, Ava Samantha Gilo ",
        "Luna, Shantia Angelic Ayong",
        "Morishita, John Ken Gudito",
        "Ortega, Megan Jacinth Capili",
        "Pangilinan, Noleen Kelly Berdejo",
        "Salonga, Carmen Beatriz Francisco",
        "Santiaguel, Jasie Grace Dejucos",
        "Solis, Brooke Anika Zamora",
        "Sta. Maria, John Gabriel Sanchez",
        "Tubangi, Lyle Yumi U.",
        "Urrutia, Alexander Lucas Prospero",
        "Valeroso, Eyl Carl Rante",
        "Villanueva, Art Varon",
    ]

    text = ""
    for i in range(len(people)):
        text += f"{i+1}.) {people[i]}<br>"

    output_list.innerHTML = text

