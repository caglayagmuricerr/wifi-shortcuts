import subprocess
import requests
import keyboard

def check_internet_access():
    try:
        requests.get("https://google.com")
        return True
    except requests.exceptions.ConnectionError:
        return False

def disconnect_wifi():
    if not check_internet_access():
        print("You are already disconnected.")
        return
    else:
        try:
            subprocess.run(["netsh", "wlan", "disconnect"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error disconnecting Wi-Fi: {str(e)}")

def connect_to_wifi(ssid):
    if check_internet_access():
        print("You are already connected.")
        return
    else:
        try:     
            subprocess.run(["netsh", "wlan", "connect", f"ssid={ssid}", f"name={ssid}"])
        except subprocess.CalledProcessError as e:
            print(f"Error connecting to Wi-Fi: {str(e)}")

# Set your WiFi SSID here
wifi_ssid = "TurkTelekom_ZTX6HF"

keyboard.add_hotkey('ctrl+alt+c', lambda: connect_to_wifi(wifi_ssid))
keyboard.add_hotkey('ctrl+alt+d', disconnect_wifi)

def main():
    keyboard.wait()

if __name__ == "__main__":
    main()