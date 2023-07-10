"""
utils.py - Utility functions for common operations.

This module contains utility functions for performing common operations that are reusable
across different parts of the codebase. These functions provide convenient functionalities
to handle various tasks such as date manipulation, string formatting, mathematical calculations, etc.

List of functions:
- add_years_to_date(original_date, years_to_add): Adds a specified number of years to a given date.

Note: This module assumes the existence of the required dependencies and modules.

Author: xwshiba
Date: July 10, 2023
"""


def add_years_to_date(original_date, years_to_add):
    """
    Adds a specified number of years to a given date.

    Args:
        original_date (datetime.date): The original date.
        years_to_add (int): The number of years to add.

    Returns:
        datetime.date: The resulting date after adding the specified number of years.
    """
    result = original_date.replace(year=original_date.year + years_to_add)
    return result