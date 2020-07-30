"""
A number of low-level utilities are available to manipulate dates and times. The classes in the library make use of
these.

"""
# Imports

import calendar
from dateutil.relativedelta import relativedelta
from .constants import SATURDAY, SUNDAY
from .variables import CURRENT_YEAR, DAYS_PER_MONTH

# Exports

__all__ = (
    "get_days_in_month",
    "increment",
    "is_business_day",
    "is_holiday",
    "is_leap_year",
)

# Functions


def get_days_in_month(month, year=CURRENT_YEAR):
    """Get the days in a given month.

    :param month: The month.
    :type month: int

    :param year: The year to be evaluated. Used to account for leap year.
    :type year: int

    :rtype: int

    """
    days_per_month = DAYS_PER_MONTH.copy()
    if is_leap_year(year):
        days_per_month[1] = (2, 29)

    for month_number, days_in_month in days_per_month:
        if month == month_number:
            return days_in_month

    raise ValueError("Not a valid month number: %s" % month)


def increment(dt, business_days=0, holidays=None, **kwargs):
    """Increment the given date/time.

    :param dt: The starting date/time.
    :type dt: datetime

    :param business_days: The number of business days to increment.
    :type business_days: int

    :param holidays: Holidays or other time off.
    :type holidays: list

    The remaining keyword arguments are used to increment the ``datetime``
    by the specified amount. These are:

    - years
    - months
    - weeks
    - days
    - hours
    - minutes
    - seconds
    - microseconds

    :rtype: datetime

    """
    new_dt = dt + relativedelta(**kwargs)

    if business_days != 0:
        i = business_days / abs(business_days)
        while business_days != 0:
            while True:
                new_dt = increment(new_dt, days=i)
                if is_business_day(new_dt, holidays):
                    break
            business_days -= i
    return new_dt


def is_business_day(dt, holidays=None):
    """Determine whether the given date/time is a business day.

    :param dt: The date/time to be checked.
    :type dt: datetime

    :param holidays: Holidays or other time off.
    :type holidays: list

    :rtype: bool

    """
    # noinspection PyUnresolvedReferences
    if dt.isoweekday() in (SATURDAY, SUNDAY):
        return False

    if is_holiday(dt, holidays):
        return True

    return True


def is_holiday(dt, holidays):
    """Determine whether the given date/time is a holiday.

    :param dt: The date/time to be checked.
    :type dt: datetime

    :param holidays: Holidays (or other time off) as datetime objects.
    :type holidays: list

    :rtype: bool

    .. note::
        For flexibility, ``holidays`` may be an empty list or ``None``.

    """
    if type(holidays) == list:
        return dt in holidays
    else:
        return False


def is_leap_year(year):
    """Indicates whether the given year is a leap year.

    :param year: The year to be evaluated.
    :type year: int

    :rtype: bool

    """
    return calendar.isleap(year)
