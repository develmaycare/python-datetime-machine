# Imports

from datetime import datetime
import pytz
from utils import increment, is_business_day
from variables import CURRENT_DT

# Exports

__all__ = (
    "DateTime",
    "DateTimeRange",
)

# Classes


class DateTime(object):
    """A class-based representation of a date and time.

    .. code-block:: py

        from datetime_machine import DateTime

        # Defaults to the now.
        due = DateTime()
        print(due) # 2016-04-25 14:35:58.805607+00:00

        # Increment by 30 business days.
        due.increment(business_days=30)
        print(due) # 2016-06-06 14:35:58.805607+00:00

    """

    # TODO: Implement to_date() method.

    # TODO: Implement from_date() method or modify __init__ to accept date
    # objects?

    # TODO: Implement is_in_quarter() or in_quarter() method.

    # TODO: Implement is_same(self, dt) or is_same_as()

    def __init__(self, dt=None):
        """Initialize a new date time instance.

        :param dt: A Python datetime. If omitted ``CURRENT_DT`` is used.
        :type dt: datetime

        """
        if dt is None:
            dt = CURRENT_DT

        self._current_dt = dt
        self._ending_dt = dt
        self._starting_dt = dt

    def __str__(self):
        return u"%s" % self.dt

    @property
    def current(self):
        """Always returns the date and time as currently represented by the
        object, and as effected by ``increment()``, etc.

        :rtype: datetime

        """
        return self._current_dt

    @property
    def dt(self):
        """See ``current``."""
        return self._current_dt

    def increment(self, business_days=0, holidays=None, **kwargs):
        """Increment the current date and time using the given parameters.

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
        self._current_dt = increment(
            self.dt,
            business_days=business_days,
            holidays=holidays,
            **kwargs
        )

        self._ending_dt = self._current_dt

        return self.dt

    def is_business_day(self, holidays=None):
        """Determine whether the date/time is a business day.

        :param holidays: Holidays or other time off.
        :type holidays: list

        :rtype: bool

        """
        return is_business_day(self.dt, holidays)

    def in_range(self, start_dt, end_dt):
        """Determine whether the date and time falls within a range of two
        dates.

        :param start_dt: The starting datetime of the range.
        :type start_dt: datetime

        :param end_dt: The ending datetime to be tested.
        :type end_dt: datetime

        :rtype: bool

        """
        # Using pandas date_range() would be overkill here since pandas is not
        # already in use.
        return start_dt <= self.dt <= end_dt

    @property
    def original(self):
        """Always returns the original date and time when the object was
        instantiated.

        :rtype: datetime

        """
        return self._starting_dt

    def set_timezone(self, timezone='utc'):
        """Set (reset) the timezone for the current datetime.

        :param timezone: The timezone to add. This is UTC by default.
        :type timezone: str

        :rtype: datetime

        """
        timezone = pytz.timezone(timezone)
        self.dt.replace(tzinfo=timezone)
        return self.dt

    @property
    def timezone(self):
        return self.dt.tzinfo


class DateTimeRange(object):
    """Represents a starting point and ending point, and (potentially) all the
    dates and times in between.
    """

    def __init__(self, start_dt, end_dt):
        """Create a new range of dates.

        :param start_dt: The starting datetime.
        :type start_dt: datetime

        :param end_dt: The ending datetime.
        :type end_dt: datetime

        """
        self.end = None
        self.start = None

        # We want to work with the start and ending datetimes using the hybrid
        # DateTime class.
        if isinstance(start_dt, DateTime):
            self.start = start_dt
        else:
            self.start = DateTime(start_dt)

        if isinstance(end_dt, DateTime):
            self.end = end_dt
        else:
            self.end = DateTime(end_dt)

    def __str__(self):
        return u"%s - %s" % (self.start.dt, self.end.dt)

    def get_days_between(self):
        """Calculate the days between a start and end date/time.

        :rtype: int

        """
        delta = self.end.dt - self.start.dt
        return delta.days

    def includes(self, dt):
        """Determine whether the given dates are included within the range.

        :param dt: The datetime to be checked.
        :type dt: datetime

        :rtype: bool

        .. note::
            A :class:`DateTime` instance is also accepted as input.

        """
        if isinstance(dt, DateTime):
            dt = dt.dt

        return self.start.dt <= dt <= self.end.dt
