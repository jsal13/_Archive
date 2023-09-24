# import curses
from datetime import datetime
import fileinput
import json
import os
from typing import Any


def create_forecast_header() -> str:
    """Create a formatted string of column names for forecast."""
    headers = " Date |  Time |  Temp |  Wind    | Humid | Brief Forecast"
    seperator = "-" * len(headers)
    return f"{headers}\n{seperator}"


def format_line(row: dict[str, Any]):
    """
    Format a line for the piped-in data.

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

    def _format_datetime(val: str) -> str:
        """
        Format piped-in datetime to a pretty format.

        Input value is like this:
        "2023-06-28T15:00:00-05:00"
        """
        val = val[:-6]  # Strip off the timezone.
        parsed_dt = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S")
        formatted_dt = datetime.strftime(parsed_dt, "%m-%d | %I %p")
        return formatted_dt

    def _format_wind_direction(direction: str) -> str:
        """Return symbol for wind direction."""
        dir_map = {
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

        dir_symbol = dir_map.get(
            direction, direction
        )  # Return the str if not in the dict.
        return dir_symbol

    def _format_temperature_humidity_wind(
        temp: int, temp_unit: str, humidity: int, wind_speed: str, wind_dir: str
    ) -> str:
        """Format piped-in temp, humidity, and wind to a pretty format."""
        wind_speed, wind_speed_dims = wind_speed.split(" ")
        wind_dir_symbol = _format_wind_direction(wind_dir)
        return (
            f"{temp: >3}°{temp_unit} "
            + f"| {wind_speed: >2} {wind_speed_dims} {wind_dir_symbol} "
            + f"|{humidity: >4}% "
        )

    # MAIN PRINTING.
    # TODO: Precipitation?  Should I use this?
    print(_format_datetime(row["startTime"]), end=" | ")
    print(
        _format_temperature_humidity_wind(
            temp=row["temperature"],
            temp_unit=row["temperatureUnit"],
            humidity=row["relativeHumidity"],
            wind_speed=row["windSpeed"],
            wind_dir=row["windDirection"],
        ),
        end=" | ",
    )
    print(f'{row["shortForecast"]}')


def main(data: list[dict[str, Any]]) -> None:
    """Run the main fn loop."""
    # stdscr = curses.initscr()
    # stdscr.clear()  # Clear terminal
    clear_cmd = "cls" if os.name == "nt" else "clear"
    os.system(clear_cmd)

    print(create_forecast_header())
    for _row in data:
        format_line(row=_row)


if __name__ == "__main__":
    # This file is meant to receive piped-in input from `weather.sh`.

    json_data: str = ""
    for line in fileinput.input(encoding="utf-8"):
        json_data = json_data + line

    _data = json.loads(json_data)
    main(data=_data)
