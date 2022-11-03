from datetime import datetime, timedelta
from typing import List
import re

# Fancy regex to compile db text
PATTERN = re.compile(
    r"-\s?(\d\d?) (\w+)[:\s]+(\w+)[,\s&]*(\w+)?[,\s&]*(\w+)?[,\s&]*(\w+)?[,\s&]*(\w+)?"
)

TIME_FORMAT_DB = "%m-%-d"

# Valid month names
MONTHS = [
    "januari",
    "februari",
    "maart",
    "april",
    "mei",
    "juni",
    "juli",
    "augustus",
    "september",
    "oktober",
    "november",
    "december",
]

def get_content(data):
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    
    birthday_boys = data.get(today.strftime(TIME_FORMAT_DB), None)
    if birthday_boys is not None:
        birthday_boys_str, pronoun = parse_names_with_verb(birthday_boys)
        today_str = f"🥳 Jaa! Vandaag {birthday_boys_str} jarig! 🎉"
        extra_str = f"Vergeet {pronoun} niet te feliciteren!"
    else:
        today_str = f"😔 Helaas! Er geen Thijs jarig!"

        tomorrow_birthday_boys = data.get(tomorrow.strftime(TIME_FORMAT_DB), None)
        if tomorrow_birthday_boys is not None:
            birthday_boys_str, _ = parse_names_with_verb(tomorrow_birthday_boys)
            extra_str = f"Maar... morgen {birthday_boys_str} jarig!"
        else:
            next_date = get_next_birthday_boys_date(list(data.keys()))
            birthday_boys_str, _ = parse_names_with_verb(data[next_date])
            extra_str = f"Nog even geduld, op {date_to_str(next_date)} is er weer een Thijs jarig!"
    return today_str, extra_str


def parse_line(db_line: str):
    m = PATTERN.match(db_line)
    assert m, f"{db_line} did not match pattern"

    day, month = m.groups()[:2]
    names = m.groups()[2:]

    # Checks if days and months are in desired format and range
    assert int(day) < 32, f"{day} is not a valid day number"
    assert month.lower() in MONTHS, f"{month} is not a valid month name"

    # Remove None names
    names = [name for name in names if name != None]
    return day, month, names


def get_data(datafile: str):
    data = {}
    with open(datafile) as tf:
        for line in tf.readlines():
            day, month, names = parse_line(line)
            data[f"{MONTHS.index(month.lower()) + 1}-{int(day)}"] = names

    return data


def parse_names_with_verb(names: List[str]):
    if len(names) == 1:
        return f"is {names[0]}", "hem"
    else:
        return "zijn " + ", ".join(names[:-1]) + f" en {names[-1]}", "ze"


def get_next_birthday_boys_date(dates: List[str]):
    today = datetime.now().strftime(TIME_FORMAT_DB)
    dates.append(today)
    sorted_dates = list(sorted(dates, key=lambda d: datetime.strptime(d, "%m-%d")))
    today_index = sorted_dates.index(today)

    if today_index == len(sorted_dates) - 1:
        # If today is the last day, return the first day
        return sorted_dates[0]
    else:
        # Return the next day
        return sorted_dates[today_index + 1]

def date_to_str(date_str):
    month, day = date_str.split("-")
    return f"{day} {MONTHS[int(month)-1]}"