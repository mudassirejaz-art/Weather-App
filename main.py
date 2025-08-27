import requests
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "City not found"))
            return

        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result_label.config(
            text=f"Weather: {weather}\nTemperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind} m/s"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")

city_entry = tk.Entry(root, width=25, font=("Arial", 14))
city_entry.pack(pady=20)
city_entry.focus()

search_btn = tk.Button(root, text="Get Weather", command=get_weather)
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
