
def add_years_to_date(last_service_date, delta_year):
    return last_service_date.replace(year=last_service_date.year + delta_year)