import itertools
import string
import time
import tkinter as tk
from tkinter import simpledialog, messagebox

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window


# Define the function to start cracking the password
def start_cracking(password):
    chars = string.printable
    max_length = 20
    start_time = time.time()

    for length in range(1, max_length + 1):
        for combination in itertools.product(chars, repeat=length):
            candidate = "".join(combination)
            print("Trying password:", candidate)
            if candidate == password:
                end_time = time.time()
                time_taken = end_time - start_time
                messagebox.showinfo(
                    "Password Found",
                    f"Password: {candidate}\nTime taken: {time_taken} seconds",
                )
                return


# Prompt the user to enter a password
password = simpledialog.askstring("Input", "Enter the password to be cracked:")

if password:
    start_cracking(password)
else:
    messagebox.showwarning("Input Error", "No password entered.")

# Close the main window
root.destroy()
