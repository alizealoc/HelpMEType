import tkinter as tk
from typing_test import start_timer, get_elapsed_time, calculate_wpn, calculate_accuracy

# Color palette
BG = "#FFFDE8" 
ACCENT = "#2323F0"
TEXT = "#000000"
INPUT_BG = "#EDEBD4"
CORRECT = "#268F2C"
INCORRECT = "#D12313"

# creating main window
root = tk.Tk()

# window settings
root.title("HelpMEType")
root.geometry("850x500")
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

# Passage display
passage_display = tk.Text(

    root, 
    font=("Consolas", 14), 
    fg=TEXT, 
    bg=BG, 
    wrap="word",
    width=65,
    height=4,
    relief="flat",
    bd=0,
    highlightthickness=0,
    cursor="arrow"
    
    )

passage_display.pack(pady=20)
passage_display.insert("1.0", passage)

# character colors
passage_display.tag_configure("correct", foreground=CORRECT)
passage_display.tag_configure("incorrect", foreground=INCORRECT)

# current index
passage_display.tag_configure(
    "current",
    underline=True,
    foreground=ACCENT

)

# prevent user from editing te passage
passage_display.config(state="disabled")

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

# Results container
results_container = tk.Frame(

    root,
    bg = BG,
    width=600,
    height=50,

)

results_container.pack(pady=20)
results_container.pack_propagate(False)

# columns for the results
for i in range(3):
    results_container.columnconfigure(i, minsize = 200)

# WPM results
wpm_label = tk.Label(
    results_container, 
    text="WPM: 0", 
    font=("Consolas", 12, "bold"), 
    fg=TEXT, 
    bg=BG,
    width=20,
    anchor="center"

    )

wpm_label.grid(row=0, column=0)

# Accuracy results
accuracy_label = tk.Label(
    results_container, 
    text="Accuracy: 0%", 
    font=("Consolas", 12, "bold"), 
    fg=TEXT, 
    bg=BG,
    width=20,
    anchor="center"

    )

accuracy_label.grid(row=0, column=1)

# Time results
time_label = tk.Label(
    results_container, 
    text="Time: 0s", 
    font=("Consolas", 12, "bold"), 
    fg=TEXT, 
    bg=BG,
    width=20,
    anchor="center"

    )

time_label.grid(row=0, column=2)

# incorrect vs correct characters
def passage_update_colors():

    typed_text = typing_input.get()

    # temporarily allow editing to update colors
    passage_display.config(state="normal")

    # remove previous colors
    passage_display.tag_remove("correct", "1.0", "end")
    passage_display.tag_remove("incorrect", "1.0", "end")
    passage_display.tag_remove("current", "1.0", "end")

    # compare typed text & update colors accordingly
    for i in range(min(len(typed_text), len(passage))):

        # text widget character position
        start = f"1.0 + {i} chars"
        end = f"1.0 + {i+1} chars"

        if typed_text[i] == passage [i]:

            passage_display.tag_add("correct", start, end)

        else:

            passage_display.tag_add("incorrect", start, end)

    # underline next character
    current_index = len(typed_text)
    if current_index < len(passage):

        start = f"1.0 + {current_index} chars"
        end = f"1.0 + {current_index + 1} chars"

        passage_display.tag_add("current", start, end)

    # disable editing again
    passage_display.config(state="disabled")

    
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
    wpm_label.config(text=f"WPM: {wpm}")
    accuracy_label.config(text=f"Accuracy: {accuracy}%")
    time_label.config(text=f"Time: {elapsed:.1f}s")

    # call func to update colors
    passage_update_colors()

# update results when the user types
typing_input.bind("<KeyRelease>", update_results)

# restart timer & results
def restart_timer():

    if get_elapsed_time() > 0:
        update_results()

    root.after(100, restart_timer)

restart_timer() 
passage_update_colors()

root.mainloop()