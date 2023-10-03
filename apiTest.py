import requests        # Imported request module from Python

# Created a function to fetch weather data from API
def get_weather_data(city, api_key):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:  # Added the IF condition with HTTP status code, To check the request is sucessful or not.
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

# Created a function to get temperature at a specific date and time.
def get_temperature(data, date_time):
    for item in data['list']:
        if item['dt_txt'] == date_time:
            return item['main']['temp']
    return None

# Created a function to get wind speed at a specific date and time.
def get_wind_speed(data, date_time):
    for item in data['list']:
        if item['dt_txt'] == date_time:
            return item['wind']['speed']
    return None

# Created a function to get pressure at a specific date and time.
def get_pressure(data, date_time):
    for item in data['list']:
        if item['dt_txt'] == date_time:
            return item['main']['pressure']
    return None

# Here is the main program loop to evalute.
if __name__ == "__main__":
    city = "London,us"
    api_key = "b6907d289e10d714a6e88b30761fae22"
    weather_data = get_weather_data(city, api_key)

    if weather_data is not None:
        while True:
            print("Options:")
            print("1. Get Temperature")
            print("2. Get Wind Speed")
            print("3. Get Pressure")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                date_time = input("Enter the date with time (yyyy-mm-dd hh:mm:ss): ")
                temperature = get_temperature(weather_data, date_time)
                if temperature is not None:
                    print(f"Temperature at {date_time}: {temperature} K")
                else:
                    print("Data not found for the given date and time.")
            elif choice == "2":
                date_time = input("Enter the date with time (yyyy-mm-dd hh:mm:ss): ")
                wind_speed = get_wind_speed(weather_data, date_time)
                if wind_speed is not None:
                    print(f"Wind Speed at {date_time}: {wind_speed} m/s")
                else:
                    print("Data not found for the given date and time.")
            elif choice == "3":
                date_time = input("Enter the date with time (yyyy-mm-dd hh:mm:ss): ")
                pressure = get_pressure(weather_data, date_time)
                if pressure is not None:
                    print(f"Pressure at {date_time}: {pressure} hPa")
                else:
                    print("Data not found for the given date and time.")
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please select a valid option.")
