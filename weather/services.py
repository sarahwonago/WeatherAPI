import requests
from django.conf import settings
from django.core.cache import cache

def fetch_weather_data(city):
    """
    Fetch weather data from the external API (Visual Crossing).
    
    Args:
        city (str): The city for which weather data is requested.
    
    Returns:
        dict: The weather data if successful, None otherwise.
    """
     
    url = f"{settings.WEATHER_API_URL}{city}?key={settings.WEATHER_API_KEY}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log error in production
        print(f"Error fetching weather data: {e}")
        return None
    


def get_cached_weather_data(city):
    """
    Retrieve weather data from cache or fetch from API if not cached.
    
    Args:
        city (str): The city for which weather data is requested.
    
    Returns:
        dict: Weather data from cache or fetched from the external API.
    """
    cached_data = cache.get(city)
    if cached_data:
        return cached_data

    weather_data = fetch_weather_data(city)
    if weather_data:
        # Cache the result with an expiration time
        cache.set(city, weather_data, timeout=settings.CACHE_TTL)

    return weather_data



