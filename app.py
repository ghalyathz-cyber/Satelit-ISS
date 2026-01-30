import requests
import time
from datetime import datetime

API_URL = "http://api.open-notify.org/iss-now.json"

def get_iss_position():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        latitude = float(data["iss_position"]["latitude"])
        longitude = float(data["iss_position"]["longitude"])
        timestamp = data["timestamp"]
        waktu = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S UTC")

        return latitude, longitude, waktu

    except Exception as e:
        print("Gagal mengambil data:", e)
        return None, None, None


if __name__ == "__main__":
    print("Tracking posisi ISS (CTRL + C untuk berhenti)\n")

    try:
        while True:
            lat, lon, waktu = get_iss_position()
            if lat is not None:
                print(f"Waktu     : {waktu}")
                print(f"Latitude  : {lat}")
                print(f"Longitude : {lon}")
                print("-" * 40)

            time.sleep(5)  # update tiap 5 detik

    except KeyboardInterrupt:
        print("\nTracking dihentikan.")
