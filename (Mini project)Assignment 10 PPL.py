import tkinter as tk
from tkinter import messagebox

# Your existing functions
weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy", "Windy", "Foggy"]
city_weather_data = {
    "New York": (-5, 10),
    "London": (0, 15),
    "Mumbai": (20, 35),
    "Tokyo": (5, 20),
    "Sydney": (15, 30),
    "Cape Town": (10, 25),
    "Paris": (-2, 12),
    "Los Angeles": (10, 20),
    "Beijing": (-10, 5),
    "Dubai": (18, 25)
}

def get_weekday(day):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    base_day = 1
    return weekdays[(day - 1 + base_day) % 7]

def get_weather(city_name, day):
    if city_name in city_weather_data:
        temp_range = city_weather_data[city_name]
        temperature = temp_range[0] + (day % (temp_range[1] - temp_range[0] + 1))
        condition = weather_conditions[day % len(weather_conditions)]
        weekday = get_weekday(day)
        return {
            "city": city_name,
            "temperature": temperature,
            "condition": condition,
            "weekday": weekday
        }
    else:
        return {"error": "City not found in database."}

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

tk.Label(root, text="Enter City:").pack()
city_entry = tk.Entry(root)
city_entry.pack()

tk.Label(root, text="Enter Date (1-31):").pack()
date_entry = tk.Entry(root)
date_entry.pack()

def show_weather():
    city = city_entry.get()
    try:
        date = int(date_entry.get())
        if date < 1 or date > 31:
            raise ValueError("Invalid date range.")
        weather = get_weather(city, date)
        if "error" in weather:
            messagebox.showerror("Error", weather["error"])
        else:
            result = (
                f"Weather Forecast for {weather['city']} on {weather['weekday']}, January {date}:\n"
                f"Temperature: {weather['temperature']}°C\nCondition: {weather['condition']}"
            )
            result_label.config(text=result)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

tk.Button(root, text="Get Weather", command=show_weather).pack()
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack()

root.mainloop()