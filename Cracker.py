import customtkinter as ctk
import tkinter as tk
import hashlib  # Corrected import for hashlib
from pytbangla import computer
import time
# Global variables to control the cracking process
current_guess_index = 0
guesses = []

def crack_password():
    global current_guess_index, guesses
    
    if current_guess_index < len(guesses):
        guess = guesses[current_guess_index]
        hashedGuess = ""
        
        if selected_option.get() == "SHA1":
            hashedGuess = hashlib.sha1(bytes(guess.strip(), 'utf-8')).hexdigest()
        elif selected_option.get() == "MD5":
            hashedGuess = hashlib.md5(bytes(guess.strip(), 'utf-8')).hexdigest()

        # Check if the guess matches the hash
        if hashedGuess.upper() == input_field.get().upper():
            result_label.configure(bg_color="green")  # Set background to green
            result_label.configure(text="The Password is: " + str(guess.strip()))
            computer.bolo("Password Found")
        else:
            result_label.configure(text="Trying: " + guess.strip())
            current_guess_index += 1  # Move to the next guess
            # Schedule the next guess
            root.after(100, crack_password)  # Call the function again after 100ms
    else:
        computer.bolo("Password Not Found")
        result_label.configure(text="Password not in database", text_color="white")
        result_label.configure(bg_color="red")  # Set background to red

def start_cracking():
    global current_guess_index, guesses
    current_guess_index = 0  # Reset the index
    result_label.configure(text="Decrypting, Please Wait", text_color="black", bg_color="yellow")  # Indicate processing
    with open("Wordlists.txt", "r") as file:
        guesses = file.readlines()  # Read all guesses from the wordlist
    crack_password()  # Start the cracking process

def on_select(choice):
    if choice:
        input_field.pack(pady=10)  # Show the input field
        activate_button.pack(pady=10)

# Initialize the customtkinter window
root = ctk.CTk()
root.title("Password Cracker")
root.geometry("300x900")
root.iconbitmap("logo.ico")
# Center the window on the screen
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create tabs
tabview = ctk.CTkTabview(root)
tabview.pack(expand=True, fill="both")

# Add Crack Tab
tab_crack = tabview.add("Crack")

# Create a dropdown menu
options = ["SHA1", "MD5"]  # Define your options here
selected_option = tk.StringVar(value=options[0])  # Set the default value

# Create the dropdown menu
dropdown = ctk.CTkOptionMenu(tab_crack, variable=selected_option, values=options, command=on_select)
dropdown.pack(pady=20)

# Create an input field
input_field = ctk.CTkEntry(tab_crack, placeholder_text="Enter your input here...", width=250)
input_field.pack_forget()  # Hide the input field initially

# Label to display the result
result_label = ctk.CTkLabel(tab_crack, text="Results Will Be Shown Here", width=250)
result_label.pack(pady=20)

# Create a Crack button in the Crack tab
activate_button = ctk.CTkButton(tab_crack, text="Crack", command=start_cracking)
activate_button.pack_forget()

# Add Developer Info Tab
tab_developer_info = tabview.add("Developer Info")

# Add developer info in the Developer Info tab
developer_info = """
Developer: Mohammad Mahfuz Rahman
Company: Dexcorp Softwares Limited
Version: 1.0.0
Contact: 01876891680
Email: mahfuzrahman0712@gmail.com
"""
developer_label = ctk.CTkLabel(tab_developer_info, text=developer_info, justify=tk.LEFT)
developer_label.pack(pady=20)

# Start the main loop
root.mainloop()
