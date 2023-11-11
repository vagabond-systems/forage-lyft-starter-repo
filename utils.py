def battery_needs_service(last_service_date, current_date, service_years):
    if last_service_date + service_years < current_date:
        return True
    else:
        return False