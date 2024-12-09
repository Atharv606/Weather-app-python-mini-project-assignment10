import tkinter as tk
from tkinter import messagebox

# Predefined weather conditions and data for cities
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

# Function to determine the weekday based on the day number
def get_weekday(day):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[(day - 1) % 7]

# Function to get the weather data for the city and day
def get_weather(city_name, day):
    if city_name in city_weather_data:
        temp_range = city_weather_data[city_name]
        # Calculate the temperature within the range for the given day
        temperature = temp_range[0] + (day % (temp_range[1] - temp_range[0] + 1))
        # Choose weather condition based on the day
        condition = weather_conditions[day % len(weather_conditions)]
        # Get the weekday
        weekday = get_weekday(day)
        return {
            "city": city_name,
            "temperature": temperature,
            "condition": condition,
            "weekday": weekday
        }
    else:
        return {"error": "City not found."}

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# User input for city
tk.Label(root, text="Enter City:").pack()
city_entry = tk.Entry(root)
city_entry.pack()

# User input for date
tk.Label(root, text="Enter Date (1-31):").pack()
date_entry = tk.Entry(root)
date_entry.pack()

# Function to show the weather when the button is pressed
def show_weather():
    city = city_entry.get()  # Get city name from input
    try:
        date = int(date_entry.get())  # Get date from input
        if date < 1 or date > 31:
            raise ValueError("Please enter a valid date (1-31).")

        weather = get_weather(city, date)  # Get weather based on input
        if "error" in weather:
            messagebox.showerror("Error", weather["error"])  # Show error if city not found
        else:
            # Display the weather information
            result = (
                f"Weather in {weather['city']} on {weather['weekday']}, January {date}:\n"
                f"Temperature: {weather['temperature']}°C\nCondition: {weather['condition']}"
            )
            result_label.config(text=result)  # Update the result label

    except ValueError as e:
        messagebox.showerror("Error", str(e))  # Show error if invalid date is entered

# Button to trigger the weather display
tk.Button(root, text="Get Weather", command=show_weather).pack()

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack()

root.mainloop()  # Start the GUI
