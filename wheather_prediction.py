import tkinter as tk
import requests  
from datetime import datetime
from tkinter import messagebox

def weather_data():
    city = city_entry.get()
    api_key = "4fa79db51da312055c3954f5d844e54f"  # Replace with your OpenWeatherMap API key
    api_link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        api_get_link = requests.get(api_link)
        api_data = api_get_link.json()

        if api_data['cod'] == '404':
            messagebox.showerror("Weather Prediction", "City not found. Please check spelling!")
        else:
            temp_city = api_data['main']['temp'] - 273.15  # Convert temperature to Celsius
            format_temp_city = "{:.2f}".format(temp_city)
            weather_description = api_data['weather'][0]['description']
            humidity = api_data['main']['humidity']
            wind_speed = api_data['wind']['speed']
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            # Update labels with fetched data
            temp_city_lbl.config(text=f"Temperature: {format_temp_city} °C")
            weather_descriptions_lbl.config(text=f"Weather: {weather_description}")
            humidity_lbl.config(text=f"Humidity: {humidity}")
            wind_speed_lbl.config(text=f"Wind: {wind_speed} km/h")
            date_time_lbl.config(text=f"Date & Time: {date_time}")

    except Exception as e:
        messagebox.showerror("Exception", f"Error fetching data: {str(e)}")

# GUI setup
window = tk.Tk()
window.title("Weather Report")
window.minsize(500, 500)

city_label = tk.Label(window, text="Enter City Name", font="Times 30 bold", bg='black', fg='white')
city_label.grid(row=0, column=0, pady=10)

city_entry = tk.Entry(window, width=30, font=("Arial", 25, "bold"))
city_entry.grid(row=1, column=0, padx=10, pady=10)

submit_btn = tk.Button(window, text="Get Weather Data", bd=3, bg='black', fg='white', command=weather_data)
submit_btn.grid(row=2, column=0, pady=10)

# Labels for displaying weather data
temp_city_lbl = tk.Label(window, font="Times 20 bold")
temp_city_lbl.grid(row=3, column=0, pady=5)

weather_descriptions_lbl = tk.Label(window, font="Times 20 bold")
weather_descriptions_lbl.grid(row=4, column=0, pady=5)

humidity_lbl = tk.Label(window, font="Times 20 bold")
humidity_lbl.grid(row=5, column=0, pady=5)

wind_speed_lbl = tk.Label(window, font="Times 20 bold")
wind_speed_lbl.grid(row=6, column=0, pady=5)

date_time_lbl = tk.Label(window, font="Times 20 bold")
date_time_lbl.grid(row=7, column=0, pady=5)

window.mainloop()
