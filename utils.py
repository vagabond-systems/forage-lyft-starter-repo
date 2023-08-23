from datetime import date

def add_years_to_date(original_date :date, years_to_add:int):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result