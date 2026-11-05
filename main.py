import tkinter as tk

# Color palette
BG = "#FFFDE8" 
ACCENT = "#FF8C81"
TEXT = "#000000"
INPUT_BG = "#EDEBD4"

# creating main window
root = tk.Tk()

# window settings
root.title("HelpMEType")
root.geometry("850x550")
root.configure(bg = BG)

# Title
title = tk.Label(

    root, 
    text="HelpMEType", 
    font=("Consolas", 18, "bold"), 
    fg=TEXT, 
    bg=BG

    )

title.pack(pady = 30)

# Sample passage
passage = "Hello! This is an example passage that would be used to demonstrate the typing test. This will be updated later..."

# Passage label
passage_label = tk.Label(

    root, 
    text=passage, 
    font=("Consolas", 14), 
    fg=TEXT, 
    bg=BG, 
    wraplength=650

    )

passage_label.pack(pady=20)

# input container 
input_container = tk.Frame(

    root,
    bg = INPUT_BG,
    padx=15
)

input_container.pack(pady=25)

# Input field 
typing_input = tk.Entry(

    input_container, 
    font=("Consolas", 13), 
    width=70, 
    bg=INPUT_BG, 
    fg=TEXT, 
    insertbackground=ACCENT,
    relief="flat",
    bd = 0

    )

typing_input.pack(ipady=12)

# Results display
results_label = tk.Label(
    root, 
    text="WPM: 0 | Accuracy: 0% | Time: 0s", 
    font=("Consolas", 12, "bold"), 
    fg=TEXT, 
    bg=BG

    )

results_label.pack(pady=20)

root.mainloop()