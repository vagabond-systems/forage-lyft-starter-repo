from datetime import date


def add_years_to_date(date: date, years_to_add: int):
    result = date.replace(year=date.year + years_to_add)
    return result
