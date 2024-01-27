def add_yearTodate(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result