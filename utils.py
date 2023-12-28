def add_years_to_date(original_date, years):
    result = original_date.replace(year= original_date.year + years)
    return result