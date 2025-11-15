import tkinter as tk
from tkinter import messagebox
import requests

# --API KEY--
API = "6926b753a570eb6cf0dbdb917d7f1bc2"
url = "https://api.openweathermap.org/data/2.5/weather"

# function to get weather info
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name.")

    #query parameters
    parameters={
        'q': city,
        'appid': API,
        'units': 'metric'
    }

    try:
        response = requests.get(url, params=parameters)

        if response.status_code == 200:
            data = response.json()

            city_name = data['name']
            temp = data['main']['temp']
            weather_desc = data['weather'][0]['description']

            result_string = f"City : {city_name}\nTemperature : {temp}\nCondition : {weather_desc}"

            result_label.config(text=result_string)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("ERROR", f"Network error: {e}")

# --main window--
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# -- UI widgets --
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

city_entry = tk.Entry(input_frame, font=("Arial, 14"), width=20)
city_entry.pack(side=tk.LEFT, padx=1)

get_weather_button = tk.Button(root, text="Get Weather", font=('Arial', 14), command=get_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
result_label.pack(pady=20)

# Run the App
root.mainloop()