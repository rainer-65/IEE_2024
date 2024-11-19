import requests
import matplotlib.pyplot as plt
import seaborn as sns

from config import API_KEY

# Simple weather forecast application with Python

# Constants
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Fetches weather information for a given city.

    Args:
    city (str): Name of the city

    Returns:
    dict: Parsed weather data or error message
    """
    try:
        # Construct the request URL
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Parse and return the data
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def visualize_weather_data(weather_data_list):
    """
    Visualizes weather data for multiple cities.

    Args:
    weather_data_list (list): List of weather data dictionaries
    """
    # Prepare data for visualization
    cities = [data["city"] for data in weather_data_list]
    temperatures = [data["temperature"] for data in weather_data_list]
    humidities = [data["humidity"] for data in weather_data_list]
    wind_speeds = [data["wind_speed"] for data in weather_data_list]

    # Set up the plot style
    sns.set(style="whitegrid")

    # Plot temperature
    plt.figure(figsize=(12, 6))
    plt.bar(cities, temperatures, color="skyblue")
    plt.title("Temperature in Cities (°C)")
    plt.ylabel("Temperature (°C)")
    plt.xlabel("City")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot humidity
    plt.figure(figsize=(12, 6))
    plt.bar(cities, humidities, color="lightgreen")
    plt.title("Humidity in Cities (%)")
    plt.ylabel("Humidity (%)")
    plt.xlabel("City")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot wind speed
    plt.figure(figsize=(12, 6))
    plt.bar(cities, wind_speeds, color="lightcoral")
    plt.title("Wind Speed in Cities (m/s)")
    plt.ylabel("Wind Speed (m/s)")
    plt.xlabel("City")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    print("Welcome to the Weather Visualization App!")
    cities = input("Enter city names separated by commas: ").split(",")

    weather_data_list = []
    for city in cities:
        city = city.strip()  # Remove extra spaces
        weather_data = get_weather(city)
        if "error" in weather_data:
            print(f"Error fetching data for {city}: {weather_data['error']}")
        else:
            weather_data_list.append(weather_data)
            print(f"Retrieved data for {weather_data['city']}")

    if weather_data_list:
        visualize_weather_data(weather_data_list)


if __name__ == "__main__":
    main()
