# Contoh aplikasi weather dengan Synchronous
# this is bad practice for Data Fetching or Data Streaming
# hanya mencontohkan penggunaan external library pada python dengan pip install -r requirements.txt
# library akan disimpan pada folder .venv/Lib daripada root project

import requests
from dotenv import load_dotenv
import os
from pathlib import Path


def setup_environment():
    # Mencari .env di folder yang sama dengan script
    current_path = Path(__file__).parent
    env_path = current_path / '.env'

    if env_path.exists():
        load_dotenv(env_path)
    else:
        # Jika tidak ada, cari di folder parent
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
        # Base URL untuk Geocoding API
        geo_url = "http://api.openweathermap.org/geo/1.0/direct"

        # Parameter untuk request
        params = {
            'q': city,
            'limit': 5,  # Batasi hasil ke 5 kota
            'appid': os.getenv("API_KEY")
        }

        # Melakukan request ke Geocoding API
        response = requests.get(geo_url, params=params)
        # - urllib3 menangani koneksi
        # - certifi memverifikasi sertifikat HTTPS
        # - charset-normalizer menangani encoding response
        # - idna menangani domain jika ada karakter internasional

        response.raise_for_status()

        # Mengambil data hasil geocoding
        geo_data = response.json()

        if not geo_data:
            print(f"\nKota '{city}' tidak ditemukan!")
            return None

        # Ambil data kota pertama dari hasil pencarian
        location = geo_data[0]
        return {
            'lat': location['lat'],
            'lon': location['lon'],
            'name': location['name'],
            'country': location['country'],
            'state': location.get('state', '')
        }

    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil data geocode: {e}")
        return None


def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nMasukkan nama kota:\n")

    # Dapatkan koordinat kota
    location = get_geocode(city)
    if not location:
        return

    try:
        # Base URL untuk Weather API
        weather_url = "https://api.openweathermap.org/data/2.5/weather"

        # Parameter untuk request
        params = {
            'lat': location['lat'],
            'lon': location['lon'],
            'appid': os.getenv("API_KEY"),
            'units': 'metric'  # Gunakan unit metric (Celsius)
        }

        # Melakukan request ke Weather API
        response = requests.get(weather_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        # test update commit git
        # Tampilkan informasi cuaca
        print(f"\nCuaca saat ini di {location['name']}, {location['country']} {location['state']}:")
        print(f"Suhu: {weather_data['main']['temp']:.1f}°C")
        print(f"Terasa seperti: {weather_data['main']['feels_like']:.1f}°C")
        print(f"Kondisi: {weather_data['weather'][0]['description'].capitalize()}")
        print(f"Kelembaban: {weather_data['main']['humidity']}%")
        print(f"Kecepatan Angin: {weather_data['wind']['speed']} m/s\n")

    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil data cuaca: {e}")

if __name__ == "__main__":
    setup_environment()

    while True :
        get_current_weather()

        # Tanya user apakah ingin mencari kota lain
        lanjut = input("Cari kota lain? (y/n): ").lower()
        if lanjut != 'y':
            break