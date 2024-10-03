import requests
from django.conf import settings

def fetch_weather_data(city):
    """
    Function to fetch data from the external api.
    """
    url = f"{settings.WEATHER_API_URL}{city}?{settings.WEATHER_API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return None