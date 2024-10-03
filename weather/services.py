import requests
from django.conf import settings
from django.core.cache import cache

def fetch_weather_data(city):
    """
    Function to fetch data from the external api.
    """
    url = f"{settings.WEATHER_API_URL}{city}?{settings.WEATHER_API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return None


def get_cached_weather_data(city):
    """
    Function to fetch cached data.
    """

    cached_data = cache.get(city)

    if cached_data:
        return cached_data
    
    weather_data = fetch_weather_data(city)

    if weather_data:
        cache.set(city, weather_data, timeout=12*60*60)
    return weather_data