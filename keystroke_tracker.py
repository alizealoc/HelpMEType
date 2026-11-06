import time

keystrokes = []
last_key_time = None

def record_keystroke(key, expected, position):

    global last_key_time
    currentTime = time.perf_counter()

    if last_key_time is None:

        interval = 0

    else: 

        interval = currentTime - last_key_time

    # store keystroke
    keystrokes.append({
        "key": key,
        "expected": expected,
        "position": position,
        "correct": key == expected if expected is not None else None,        "timestamp": currentTime,
        "interval": round(interval * 1000, 2)
    })

    last_key_time = currentTime

def reset_keystrokes():

    global last_key_time
    keystrokes.clear()
    last_key_time = None

