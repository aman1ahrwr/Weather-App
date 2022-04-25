import requests
from tkinter import*
import math

# Json -> {'coord': {'lon': 79.9744, 'lat': 23.1859}, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50d'}], 'base': 'stations', 'main': {'temp': 313.67, 'feels_like': 310.85, 'temp_min': 313.67, 'temp_max': 313.67, 'pressure': 1007, 'humidity': 11}, 'visibility': 5000, 'wind': {'speed': 4.12, 'deg': 0}, 'clouds': {'all': 0}, 'dt': 1650879968, 'sys': {'type': 1, 'id': 9066, 'country': 'IN', 'sunrise': 1650845481, 'sunset': 1650891875}, 'timezone': 19800, 'id': 1269633, 'name': 'Jabalpur', 'cod': 200}
lat = input("Enter the Latitude of the Region : ")
lon = input("Enter the Longitude of the Region : ")
apiKey = "de72c49dec153cb0a58e27e399370c05"



def getWeather(apiKey, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}"
    response = requests.get(url).json()

    # Name of the city 
    name = response['name']
    
    # Converting the temperature from Kelvin to Celsius
    temperature = math.floor(response['main']['temp'] - 273.15)


    feels_like = math.floor(response['main']['feels_like'] - 273.15)
    
    # Humidity of the city
    humidity = response['main']['humidity']
    
    return {
        'name': name,
        'temperature': temperature,
        'feels_like': feels_like,
        'humidity': humidity
    }


Weather = getWeather(apiKey, lat, lon)

print(Weather['name'])
print(Weather['temperature'])
print(Weather['feels_like'])
print(Weather['humidity'])

# Creating a Graphical User Interface (GUI)
root = Tk()
root.geometry("400x400")
root.title(f"{Weather['name']} Weather")

def displayCityName(city):
    cityLabel = Label(root, text=f"{Weather['name']}")
    cityLabel.config(font=("Palatino", 28))
    cityLabel.pack(side='top')

def displayStats(Weather):
    temperature = Label(root, text=f"Temperature: {Weather['temperature']} C")
    feels_like = Label(root, text=f"Feels Like: {Weather['feels_like']} C")
    humidity = Label(root, text=f"Humidity: {Weather['humidity']} %")

    temperature.config(font=("Palatino", 22))
    feels_like.config(font=("Palatino", 16))
    humidity.config(font=("Palatino", 16))

    temperature.pack(side='top')
    feels_like.pack(side='top')
    humidity.pack(side='top')


displayCityName(Weather['name'])
displayStats(Weather)

mainloop()