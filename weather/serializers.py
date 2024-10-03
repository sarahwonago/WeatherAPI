from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    """
    Serializer for the weather data.
    """
    city = serializers.CharField()
    condition = serializers.CharField()
    temperature = serializers.FloatField()