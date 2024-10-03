# Weather API Wrapper Service

A Django Rest Framework (DRF) based backend service that integrates with an external weather API to provide real-time weather information. The service includes caching using Redis to optimize performance and reduce external API calls.



## Features

- Fetches weather data from an external API (e.g., Visual Crossing).
- Implements in-memory caching with Redis to store API responses for a defined period (12 hours by default).
- Provides a REST API endpoint to retrieve weather data based on the city.
- Easily configurable using environment variables.
- Production-ready with PEP8 compliance, and error handling.


## **Table of Contents**
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Caching](#caching)
- [Testing](#testing)
- [Security](#security)


# Requirements
1. Python 3.8+
2. Django 3.0+
3. Django Rest Framework(resta_framework)
4. Redis
5. Requests library(requests)
6. Visual Crossing (or any weather API with free tier)

# Installation
1. Clone the repository
`git clone https://github.com/sarahwonago/WeatherAPI/`
`cd WeatherAPI`

2. Create and activate a virtual environment
`python3 -m venv weather_env`
`source weather_env/bin/activate`

3. Install the dependencies
`pip install -r requirements.txt`

4. Install Redis on your machine
`sudo apt-get install redis-server`

5. Start the Redis server
`redis-server`

6. Run the development server 
`python manage.py runserver`

7. The API will be accessible at http://127.0.0.1:8000/api/weather/{city}/


# Configuration
1. Create a .env file in the project root and add the following variables

```
# .env

# Weather API Configuration
WEATHER_API_KEY=your_visual_crossing_api_key
WEATHER_API_URL=https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/

# Redis Cache TTL (optional)
CACHE_TTL=43200  # Time-to-live in seconds (12 hours)

```
2. Update the settings.py file to configure cache

```
from decouple import config

WEATHER_API_KEY = config('WEATHER_API_KEY')
WEATHER_API_URL = config('WEATHER_API_URL')
CACHE_TTL = int(config('CACHE_TTL', default=12 * 60 * 60))

```

# Usage
1. Run the development server

```
python manage.py runserver

```

# API Endpoints
1. GET /api/weather/{city}/- retrieves the current weather data for a city.

**Parameters**:
city: The name of the city (string).

Example request:
```
GET http://127.0.0.1:8000/api/weather/london/

```

Response example:
```
{
    "city": "London",
    "temperature": 18.3,
    "condition": "Cloudy"
    ...
}

```

# Caching
The service uses Redis to cache weather data for cities. Cached data is stored with a TTL (time-to-live) of 12 hours (default), which can be configured in the .env file or the settings.py file. After the TTL expires, the data will be fetched from the external weather API again and re-cached.

Redis caching ensures faster responses and reduced reliance on the external weather API, which may have rate limits.

# Testing
You can test the API using tools like Postman or curl.

# Security
1. Secure API Key
Ensure that your weather API key is stored securely and never hard-coded in your codebase. Use environment variables or secret management systems like AWS Secrets Manager.
