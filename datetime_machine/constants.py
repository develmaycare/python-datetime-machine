"""
The constants module provides some common tokens that Prevent the need to
*remember* various time-related values and formulas, while helping to eliminate
unnamed numerical constants (i.e. `magic numbers`_).

.. _magic numbers: https://en.wikipedia.org/wiki/Magic_number_(programming)

**Days of the Week*

The ISO weekday numbers are available as the following constants: ``MONDAY``,
``TUESDAY``, ``WEDNESDAY``, ``THURSDAY``, ``FRIDAY``, ``SATURDAY``, ``SUNDAY``.

**Intervals and Measurements**

``DAYS_PER_WEEK`` is the number of days in a week (7).

``HOURS_PER_DAY`` is the number of hours in a day (24).

``LAST_HOUR`` represents the last hour of the day in 24 hour format (i.e. 23).

``LAST_MINUTE`` represents the last minute of the day (59).

``LAST_SECOND`` represents the last second of the day (59).

``MICROSECONDS_PER_SECOND`` is the number if microseconds in a second.

``MINUTES_PER_DAY`` is the number of minutes in a 24 hour day.

``MINUTES_PER_HOUR`` is the number of minutes in an hour.

``MONTHS_PER_YEAR`` is the number of months in a year.

``MONTHS`` is a tuple of tuples containing the month number and (English) month
name.

``NINETY_DAYS`` is self-explanatory.

``QUARTERS`` is a dictionary with 4 elements. Each key is a quarter number and
the values are a tuple containing the month numbers for each quarter.

``SECONDS_PER_DAY`` is the number of seconds in a 24 hour day.

``SECONDS_PER_HOUR`` is the number of seconds in an hour.

``SECONDS_PER_MINUTE`` is the number of seconds in a minute.

``SECONDS_PER_WEEK`` is the number of seconds in a 7 day week.

``SIXTY_DAYS`` is self-explanatory.

``THIRTY_DAYS`` is self-explanatory.

**UTC Timezone**

``UTC`` from ``pytz`` is made available a convenience.

"""
# Imports

import pytz

# Exports

# Be sure to update this if adding new constants. Also, it's good form to do
# this. Also, if you don't do this, modules used here might be imported by other
# modules and very hard-to-troubleshoot things will happen.
__all__ = (
    "DAYS_PER_YEAR",
    "DAYS_PER_WEEK",
    "FRIDAY",
    "HOURS_PER_DAY",
    "LAST_HOUR",
    "LAST_MINUTE",
    "LAST_SECOND",
    "MICROSECONDS_PER_SECOND",
    "MINUTES_PER_DAY",
    "MINUTES_PER_HOUR",
    "MONDAY",
    "MONTHS",
    "MONTHS_PER_YEAR",
    "NINETY_DAYS",
    "QUARTERS",
    "SATURDAY",
    "SECONDS_PER_DAY",
    "SECONDS_PER_HOUR",
    "SECONDS_PER_MINUTE",
    "SECONDS_PER_WEEK",
    "SIXTY_DAYS",
    "SUNDAY",
    "THIRTY_DAYS",
    "THURSDAY",
    "TUESDAY",
    "WEDNESDAY",
    "UTC",
)

# These constants exist purely for the elimination of magic numbers.
DAYS_PER_YEAR = 365
DAYS_PER_WEEK = 7
HOURS_PER_DAY = 24
LAST_HOUR = 23
LAST_MINUTE = 59
LAST_SECOND = 59
MICROSECONDS_PER_SECOND = 1000000
MINUTES_PER_DAY = 24 * 60
MINUTES_PER_HOUR = 60
MONTHS_PER_YEAR = 12
SECONDS_PER_DAY = 24 * 60 * 60
SECONDS_PER_HOUR = 60 * 60
SECONDS_PER_MINUTE = 60
SECONDS_PER_WEEK = SECONDS_PER_DAY * 7

# Time periods. Also to eliminate some common magic numbers.
THIRTY_DAYS = 30
SIXTY_DAYS = 60
NINETY_DAYS = 90

# Use constants equivalent to isoweekday().
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

# Quarters dividing the year.
QUARTERS = {
    1: (1, 2, 3),
    2: (4, 5, 6),
    3: (7, 8, 9),
    4: (10, 11, 12),
}

# Months (untranslated) in a "choices" format.
MONTHS = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
)

# Make UTC available.
UTC = pytz.UTC
