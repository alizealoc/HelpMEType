import time

start_time = None

def start_timer():
    global start_time

    if start_time is None:
        start_time = time.perf_counter()

def get_elapsed_time():
    
    if start_time is None:
        return 0

    return time.perf_counter() - start_time

def calculate_wpm(typed_text):
    elapsed_time = get_elapsed_time()

    if elapsed_time <= 0:
        return 0

    # standard definition for WPM is one word = 5 characters
    words = len(typed_text) / 5
    minutes = elapsed_time / 60

    return round(words / minutes, 2)

def calculate_accuracy(typed_text, passage):

    if len(typed_text) == 0:
        return 0

    correct_chars = 0

    for i in range(len(typed_text)):

        if i < len(passage) and typed_text[i] == passage [i]:
            
            correct_chars += 1

    return round((correct_chars / len(typed_text)) * 100, 2)


