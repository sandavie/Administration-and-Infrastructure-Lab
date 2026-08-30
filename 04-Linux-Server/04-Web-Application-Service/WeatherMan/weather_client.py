from dotenv import load_dotenv
import os
import requests

load_dotenv()


def get_forecast_data(location="new york city"):
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "q": location,
            "appid": os.getenv("API_KEY"),
            "units": "imperial",
        },
        timeout=10,
    )
    forecast_data = response.json()
    if forecast_data.get("cod") == "404":
        return get_forecast_data()
    else:
        forecast = {
            "title": forecast_data["name"],
            "temp": f"{forecast_data['main']['temp']:.1f}",
            "forecast": forecast_data["weather"][0]["description"].capitalize(),
            "feels": f"{forecast_data['main']['feels_like']:.1f}",
            "high": f"{forecast_data['main']['temp_max']:.1f}",
            "low": f"{forecast_data['main']['temp_min']:.1f}",
            "wind": forecast_data["wind"]["speed"],
        }
        return forecast
