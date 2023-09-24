import os
from collections import OrderedDict
from datetime import datetime
from typing import Any

import pandas as pd
import requests
import tabulate

tabulate.WIDE_CHARS_MODE = True
KEYWORDS_TO_SYMBOLS_LIST = [
    ["smoke", "🔥"],
    ["rain", "🌧️"],
    ["partly sunny", "🌥️"],
    ["partly cloudy", "⛅"],
    ["sunny", "☀️"],
    ["cloudy", "☁️"],
    ["clear", "🟦"],
]


FORECAST_SYMBOL_MAP: dict[str, str] = OrderedDict(KEYWORDS_TO_SYMBOLS_LIST)


DIRECTION_SYMBOL_MAP = {
    "N": "↑",
    "NNE": "↗",
    "NE": "↗",
    "ENE": "↗",
    "E": "→",
    "ESE": "↘",
    "SE": "↘",
    "SSE": "↘",
    "S": "↓",
    "SSW": "↙",
    "SW": "↙",
    "WSW": "↙",
    "W": "←",
    "WNW": "↖",
    "NW": "↖",
    "NNW": "↖",
}


class Forecast:
    """Manipulate Weather.gov's API to get forecast data."""

    def __init__(self, lat: float = 41.9328, lng: float = -87.6427) -> None:
        self.lat = lat
        self.lng = lng
        self.station_data = self._get_closest_station()
        self.forecast = self._get_18_hours_of_forecast_data()
        self.clean_forecast = self._clean_data()
        self.daily_forecast_list = self._create_daily_dfs()

    def _get_closest_station(self) -> dict[str, Any]:
        """Return closest weather station and grid values (Defaults to Chicago)."""
        resp = requests.get(
            f"https://api.weather.gov/points/{self.lat},{self.lng}", timeout=60
        )
        data = resp.json().get("properties")

        station_data = {
            "cwa": data.get("cwa"),
            "gridX": data.get("gridX"),
            "gridY": data.get("gridY"),
        }
        return station_data

    def _get_18_hours_of_forecast_data(self) -> list[dict[str, Any]]:
        url = (
            "https://api.weather.gov/gridpoints/"
            + f"{self.station_data['cwa']}/"
            + f"{self.station_data['gridX']},{self.station_data['gridX']}"
            + "/forecast/hourly"
            + "?units=us"
        )
        resp = requests.get(url, timeout=60).json().get("properties").get("periods")
        resp_first_18 = resp[:18]

        data = [
            {
                "startTime": row.get("startTime"),
                "temperature": row.get("temperature"),
                "temperatureUnit": row.get("temperatureUnit"),
                "probabilityOfPrecipitation": row.get("probabilityOfPrecipitation").get(
                    "value"
                ),
                "relativeHumidity": row.get("relativeHumidity").get("value"),
                "windSpeed": row.get("windSpeed"),
                "windDirection": row.get("windDirection"),
                "shortForecast": row.get("shortForecast"),
            }
            for row in resp_first_18
        ]

        return data

    def _clean_data(self) -> list[dict[str, Any]]:
        """
        Clean up data to make it look nice.

        Each row in `data` should look like:
        {
            'startTime': '2023-06-28T23:00:00-05:00',
            'temperature': 67,
            'temperatureUnit': 'F',
            'probabilityOfPrecipitation': 31,
            'relativeHumidity': 75,
            'windSpeed': '5 mph',
            'windDirection': 'SE',
            'shortForecast': 'Chance Showers And Thunderstorms'
        }
        """

        def _format_datetime(val: str) -> tuple[str, str]:
            """
            Format piped-in datetime to a pretty format.

            Input value is like this:
            "2023-06-28T15:00:00-05:00"
            """
            val = val[:-6]  # Strip off the timezone.
            parsed_dt = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S")

            date = datetime.strftime(parsed_dt, "%a, %b %d")
            time = datetime.strftime(parsed_dt, "%-I %p")
            return date, time

        def _format_temperature(temp: int, temp_unit: str) -> str:
            """Format temp to a pretty format."""
            temp_str: str = ""
            if temp >= 80:
                temp_str = "🌡️ "
            elif temp <= 0:
                temp_str = "❄️ "

            temp_str += f"{temp}°{temp_unit}"

            return temp_str

        def _format_humidity(humidity: int) -> str:
            """Format humidity to a pretty format."""
            return f"{humidity}%"

        def _format_wind(wind_speed: str, wind_dir: str) -> str:
            """Format wind to a pretty format."""
            wind_speed, wind_speed_dims = wind_speed.split(" ")

            wind_str: str = ""
            if int(wind_speed) >= 20:
                wind_str = "💨 "

            wind_dir_symbol = DIRECTION_SYMBOL_MAP.get(wind_dir, wind_dir)
            wind_str += f"{wind_speed} {wind_speed_dims} {wind_dir_symbol}"
            return wind_str

        def _format_forecast(forecast: str) -> str:
            """Format forecast to a pretty format."""
            forecast_lower = forecast.lower()
            forecast_str: str = ""
            for key, symbol in FORECAST_SYMBOL_MAP.items():
                if key in forecast_lower:
                    forecast_str = symbol + " "
                    break

            forecast_str += f"{forecast}"
            return forecast_str

        # Main part of `_clean_data`.
        clean_data = []
        for row in self.forecast:
            date, time = _format_datetime(row["startTime"])
            temperature = _format_temperature(
                temp=row["temperature"],
                temp_unit=row["temperatureUnit"],
            )
            humidity = _format_humidity(
                humidity=row["relativeHumidity"],
            )
            wind = _format_wind(
                wind_speed=row["windSpeed"],
                wind_dir=row["windDirection"],
            )

            forecast = _format_forecast(forecast=row["shortForecast"])
            formatted_row = {
                "date": date,
                "time": time,
                "temp": temperature,
                "humid": humidity,
                "wind": wind,
                "forecast": forecast,
            }
            clean_data.append(formatted_row)
        return clean_data

    def _create_daily_dfs(self) -> list[tuple[str, pd.DataFrame]]:
        """Create a list of dataframes grouped by date."""
        df = pd.DataFrame(self.clean_forecast)
        keys = df["date"].unique()

        df_groups = []
        for key in keys:
            _df = df[df["date"] == key]
            _df_slimmed = _df.drop("date", axis=1)
            df_groups.append((key, _df_slimmed))

        return df_groups

    def create_tables_forecast(self) -> list[tuple[str, pd.DataFrame]]:
        """Create a table forecast to print."""
        dfs = self.daily_forecast_list
        dfs_str = []

        for df in dfs:
            # time, temp, humid, wind, forecast
            colalign = ("right", "right", "right", "right", "left")
            df_str = tabulate.tabulate(
                df[1],
                showindex=False,
                headers=df[1].columns,
                tablefmt="fancy_outline",
                colalign=colalign,
            )
            dfs_str.append((df[0], df_str))
        return dfs_str

    def print_daily_forecasts(self) -> None:
        """Pretty print the daily forecasts."""

        def _clear_screen() -> None:
            """Clear the screen on the terminal."""
            clear_cmd = "cls" if os.name == "nt" else "clear"
            os.system(clear_cmd)

        _clear_screen()

        dfs_str = self.create_tables_forecast()
        for df_str in dfs_str:
            print(df_str[0], df_str[1], sep="\n", end="\n\n")


def main() -> None:
    """Call to print daily forecasts."""
    Forecast().print_daily_forecasts()
