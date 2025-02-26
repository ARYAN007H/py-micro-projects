import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(data):
    if data.get('cod') != 200:
        print("City not found!")
        return

    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    weather = data['weather'][0]['description']

    print(f"Weather in {city}, {country}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather}")

def main():
    api_key = "5fd50cb91d2264559a8d7291c4623669"  # Replace with your actual API key
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()