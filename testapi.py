import requests

API_KEY = '18d63821e3598b53d8b4f415871c71a3'
city = 'London'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

response = requests.get(url)
print(response.json())