import tkinter as tk
from typing_test import start_timer, get_elapsed_time, calculate_wpn, calculate_accuracy

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

# update results
def update_results(event = None):

    typed_text = typing_input.get()

    # start counting when first character is typed
    if typed_text:
        start_timer()

    # calculate results
    elapsed = get_elapsed_time()
    wpm = calculate_wpn(typed_text)
    accuracy = calculate_accuracy(typed_text, passage)
    
    # update results label
    results_label.config(
        text=f"WPM: {wpm} | Accuracy: {accuracy}% | Time: {elapsed:.1f}s")

# update results when the user types
typing_input.bind("<KeyRelease>", update_results)

# restart timer & results
def restart_timer():

    if get_elapsed_time() > 0:
        update_results()

    root.after(100, restart_timer)

restart_timer()

root.mainloop()