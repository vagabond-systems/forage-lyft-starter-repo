def battery_service_year(actual_date, duration):

    year_sum = actual_date.replace(year = actual_date.year + duration)
    return year_sum