from dotenv import load_dotenv
import os
import requests
from pathlib import Path


def setup_environment():
    current_path = Path(__file__).parent
    env_path = current_path / '.env'

    if env_path.exists():
        load_dotenv(env_path)
    else:
        parent_path = current_path.parent
        env_path = parent_path / '.env'
        if env_path.exists():
            load_dotenv(env_path)
        else:
            raise FileNotFoundError("File .env tidak ditemukan")


def get_geocode(city):
    """
    Fungsi untuk mendapatkan koordinat (lat, lon) dari nama kota
    menggunakan Geocoding API OpenWeather
    """
    try:
        geo_url = "http://api.openweathermap.org/geo/1.0/direct"
        params = {
            'q': city,
            'limit': 1,  # Batasi hasil ke 1 kota
            'appid': os.getenv("API_KEY")
        }

        response = requests.get(geo_url, params=params)
        response.raise_for_status()

        geo_data = response.json()

        if not geo_data:
            return None

        location = geo_data[0]
        return {
            'lat': location['lat'],
            'lon': location['lon']
        }

    except requests.exceptions.RequestException:
        return None


def get_current_weather(city):
    """
    Mengambil data cuaca dari OpenWeather API berdasarkan nama kota
    """
    setup_environment()

    try:
        # Dapatkan koordinat kota terlebih dahulu
        location = get_geocode(city)
        if not location:
            return {
                "cod": "404",
                "message": "City not found"
            }

        weather_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'lat': location['lat'],
            'lon': location['lon'],
            'appid': os.getenv("API_KEY"),
            'units': 'metric'  # Gunakan unit metric (Celsius)
        }

        response = requests.get(weather_url, params=params)
        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "cod": "404",
            "message": f"Error: {str(e)}"
        }


if __name__ == "__main__":
    # Testing
    test_city = "London"
    weather = get_current_weather(test_city)
    print(weather)
