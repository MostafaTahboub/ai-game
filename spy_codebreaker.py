import random
import tkinter as tk
from tkinter import messagebox, ttk

# Generate a 4-digit secret code with unique digits
secret_code = ''.join(random.sample('0123456789', 4))

# Create the main window
root = tk.Tk()
root.title("Spy Codebreaker Game")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="#1e1e2f")

# Title label
title_label = tk.Label(
    root,
    text="Spy Codebreaker",
    font=("Helvetica", 24, "bold"),
    fg="#f5f5f5",
    bg="#1e1e2f"
)
title_label.pack(pady=10)

# Frame for user input and button
input_frame = tk.Frame(root, bg="#1e1e2f")
input_frame.pack(pady=10)

# Instruction label
instructions = tk.Label(
    input_frame,
    text="Enter your 4-digit guess:",
    font=("Helvetica", 14),
    fg="#f5f5f5",
    bg="#1e1e2f"
)
instructions.grid(row=0, column=0, columnspan=2, pady=5)

# Entry field for the user's guess
entry = ttk.Entry(input_frame, font=("Helvetica", 14), width=10)
entry.grid(row=1, column=0, padx=5)

# Function to check the guess
def check_guess():
    guess = entry.get()

    # Validate the guess
    if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
        messagebox.showerror("Invalid Input", "Enter a 4-digit number with unique digits.")
        return

    # Calculate right digits in the right place
    right_place = sum(1 for i in range(4) if guess[i] == secret_code[i])

    # Calculate right digits in the wrong place
    right_digit_wrong_place = sum(1 for digit in guess if digit in secret_code) - right_place

    # Display feedback
    feedback_text = f"Digits in the correct place: {right_place}\n"
    feedback_text += f"Correct digits in the wrong place: {right_digit_wrong_place}"
    feedback_label.config(text=feedback_text)

    # Check if the user has guessed the code correctly
    if right_place == 4:
        messagebox.showinfo("Congratulations!", "You've guessed the secret code!")
        root.quit()

# Button to submit the guess
submit_button = ttk.Button(input_frame, text="Submit", command=check_guess)
submit_button.grid(row=1, column=1, padx=5)

# Frame for feedback
feedback_frame = tk.Frame(root, bg="#1e1e2f")
feedback_frame.pack(pady=10)

# Feedback label
feedback_label = tk.Label(
    feedback_frame,
    text="",
    font=("Helvetica", 14),
    fg="#f5f5f5",
    bg="#1e1e2f",
    justify="left"
)
feedback_label.pack()

# Start the Tkinter main loop
root.mainloop()
