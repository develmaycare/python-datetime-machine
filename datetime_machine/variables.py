"""
Similar to constants, tokens in the variables module provide values that change depending upon the current date and
time.

- ``CURRENT_DT`` is the current datetime with UTC for the timezone.
- ``CURRENT_MONTH`` is the current month number.
- ``CURRENT_YEAR`` is the current year.
- ``DAYS_IN_MONTH`` is the number of days in the current month. This is adjusted for leap year.
- ``DAYS_PER_MONTH`` is a list of tuples containing the month number and the number of days in that month. This is
  adjusted for leap year.
- ``IS_LEAP_YEAR`` indicates whether the current year is a leap year.
- ``TODAY`` is the current date.

"""

# Imports

import calendar
from datetime import datetime
# noinspection PyProtectedMember
from pytz import UTC

# Exports

# Be sure to update this if adding new variables. Also, it's good form to do
# this. Also, if you don't do this, modules used here might be imported by other
# modules and very hard-to-troubleshoot things will happen.
__all__ = (
    "CURRENT_DT",
    "CURRENT_MONTH",
    "CURRENT_YEAR",
    "DAYS_IN_MONTH",
    "DAYS_PER_MONTH",
    "IS_LEAP_YEAR",
    "TODAY",
)

# The current datetime, month, year, and today's date. Timezone must always default to UTC.
CURRENT_DT = datetime.utcnow().replace(tzinfo=UTC)
CURRENT_MONTH = CURRENT_DT.month
CURRENT_YEAR = CURRENT_DT.year
TODAY = CURRENT_DT.date()

# Reference for finding the days in a given month.
DAYS_PER_MONTH = [
    (1, 31),
    (2, 28),
    (3, 31),
    (4, 30),
    (5, 31),
    (6, 30),
    (7, 31),
    (8, 31),
    (9, 30),
    (10, 31),
    (11, 30),
    (12, 31),
]

# Note leap year and update DAYS_IN_MONTH as needed.
IS_LEAP_YEAR = calendar.isleap(CURRENT_YEAR)

# This causes problems when the current year is not the year to be evaluated.
# if IS_LEAP_YEAR:
#     DAYS_PER_MONTH[1] = (2, 29)

# Define the number of days in the current month.
DAYS_IN_MONTH = DAYS_PER_MONTH[CURRENT_MONTH - 1][1]
