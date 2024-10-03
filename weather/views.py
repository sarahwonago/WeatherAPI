from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import get_cached_weather_data


class WeatherAPIView(APIView):
    def get(self, request, city):
        weather_data = get_cached_weather_data(city)

        if weather_data:
            return Response(weather_data, status=status.HTTP_200_OK)
        
        return Response({"message":"Sorry, could not fetch weather data."}, status=status.HTTP_400_BAD_REQUEST)