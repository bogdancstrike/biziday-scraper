import datetime as datetime
from datetime import datetime, timedelta
import re


def convert_time_string_to_date(time_string):
    time_string = time_string.lower()

    current_time = datetime.now()

    if "acum" not in time_string:
        raise ValueError("Invalid time string format")

    if "minut" in time_string:
        time_unit = "minutes"
    elif "oră" in time_string or "ore" in time_string or "ora" in time_string:
        time_unit = "hours"
    elif "zi" in time_string or "zile" in time_string:
        time_unit = "days"
    elif "lună" in time_string or "luni" in time_string or "luna" in time_string:
        time_unit = "months"
    else:
        raise ValueError("Invalid time unit in the time string")

    number_pattern = r"\d+"
    match = re.search(number_pattern, time_string)
    if match:
        value = int(match.group())
    else:
        value = 1

    if time_unit == "minutes":
        date = current_time - timedelta(minutes=value)
    elif time_unit == "hours":
        date = current_time - timedelta(hours=value)
    elif time_unit == "days":
        date = current_time - timedelta(days=value)
    elif time_unit == "months":
        date = current_time - timedelta(days=value * 30)

    return date


def todayDate():
    today = datetime.today()
    date_only = today.date()
    return date_only
