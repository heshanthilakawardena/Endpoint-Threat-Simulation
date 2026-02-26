import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# The file we know the attacker (our keylogger) uses
SUSPICIOUS_FILE = ".system_audit.log"

class SecurityMonitor(FileSystemEventHandler):
    # This triggers when a new file is created
    def on_created(self, event):
        if event.is_directory:
            return
        print(f"\n[WARNING] New file detected: {event.src_path}")
        self.check_threat(event.src_path)

    # This triggers when an existing file is modified/written to
    def on_modified(self, event):
        if event.is_directory:
            return
        self.check_threat(event.src_path)

    def check_threat(self, filepath):
        # We check if the file being messed with is our known bad file
        filename = os.path.basename(filepath)
        if filename == SUSPICIOUS_FILE:
            print(f"[CRITICAL ALERT] Unauthorized keystroke logging detected in: {filename}!")
            print(">>> Action Recommended: Isolate the machine and investigate running processes.\n")

if __name__ == "__main__":
    # We will monitor the current folder (represented by ".")
    path_to_watch = "."
    
    print(f"🛡️  Blue Team FIM started. Monitoring directory: {os.path.abspath(path_to_watch)}")
    print("Waiting for suspicious activity... (Press Ctrl+C to stop)")

    # Set up the watchdog observer
    event_handler = SecurityMonitor()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            # Keep the script running
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping FIM monitor...")
        observer.stop()
    observer.join()