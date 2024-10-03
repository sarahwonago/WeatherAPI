from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import get_cached_weather_data


class WeatherAPIView(APIView):
    """
    API View to handle weather data requests.
    """
    def get(self, request, city):
        """
        Handles GET requests to retrieve weather data for a given city.
        
        Args:
            city (str): The city for which weather data is requested.
        
        Returns:
            Response: JSON response containing weather data or error message.
        """
        weather_data = get_cached_weather_data(city)
        if weather_data:
            return Response(weather_data, status=status.HTTP_200_OK)
        return Response(
            {"error": "Could not fetch weather data"},
            status=status.HTTP_400_BAD_REQUEST
        )
