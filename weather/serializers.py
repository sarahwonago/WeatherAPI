from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    """
    Serializer for the weather data.
    """
    city = serializers.CharField(max_length=100)
    condition = serializers.CharField()
    temperature = serializers.FloatField(max_length=100)