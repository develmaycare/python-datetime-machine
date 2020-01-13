# Imports

from datetime import date, datetime
from dateutil import parser as datetime_parser
import pytz
from .utils import get_days_in_month, increment, is_business_day
from .variables import CURRENT_DT

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

    # TODO: Implement is_in_quarter() or in_quarter() method.

    # TODO: Implement is_same(self, dt) or is_same_as()

    def __init__(self, dt=None):
        """Initialize a new date time instance.

        :param dt: A Python datetime. If omitted ``CURRENT_DT`` is used.
        :type dt: datetime | DateTime

        .. versionchanged:: 0.6.0-d
            Removed support for input other than datetime or DateTime objects. Also removed ``input_format`` argument.
            See ``from_date()`` and ``from_string()`` class methods.

        .. note::
            The ``dt`` parameter may be given as a ``datetime``, which is generally preferred. However, it may also be
            given as a another ``DateTime`` instance:

        """
        if isinstance(dt, DateTime):
            dt = dt.dt
        elif type(dt) == datetime:
            dt = dt
        else:
            dt = CURRENT_DT

        self._current_dt = dt
        self._ending_dt = dt
        self._starting_dt = dt

    def __str__(self):
        return str(self.dt)

    @property
    def current(self):
        """Always returns the date and time as currently represented by the
        object, and as effected by ``increment()``, etc.

        :rtype: datetime

        """
        return self._current_dt

    def decrement(self, business_days=0, holidays=None, **kwargs):
        """Reverse the date and time using the given parameters.

        :param business_days: The number of business days to increment.
        :type business_days: int

        :param holidays: Holidays or other time off.
        :type holidays: list

        The remaining keyword arguments are used to increment the ``datetime`` by the specified amount. These are:

        - years
        - months
        - weeks
        - days
        - hours
        - minutes
        - seconds
        - microseconds

        :rtype: datetime

        .. versionadded: 0.5.2-d

        """
        if business_days:
            reverse_business_days = business_days - business_days * 2
        else:
            reverse_business_days = 0

        reverse_kwargs = dict()
        for key, value in kwargs.items():
            reverse_value = value - value * 2
            reverse_kwargs[key] = reverse_value

        return self.increment(business_days=reverse_business_days, holidays=holidays, **reverse_kwargs)

    @property
    def dt(self):
        """See ``current``."""
        return self._current_dt

    def end_of_day_dt(self):
        """Get the date/time for the end of the current date/time.

        :rtype: datetime

        """
        dt = self._current_dt
        dt = dt.replace(hour=23, minute=59)
        return dt

    def end_of_month_dt(self):
        """Get the date/time for the end of the month for the current date/time.

        :rtype: datetime

        """
        dt = self._current_dt

        day = get_days_in_month(dt.month, year=dt.year)

        dt = dt.replace(day=day, hour=23, minute=59)

        return dt

    @classmethod
    def from_date(cls, value):
        """Create a new ``DateTime`` instance from a date object.

        :param value: The date to be converted.
        :type value: date

        :rtype: DateTime

        """
        return cls(datetime(value.year, value.month, value.day, tzinfo=pytz.UTC))

    @classmethod
    def from_string(cls, value, input_format=None):
        """Create a new ``DateTime`` instance from a string object.

        :param value: The value to be converted.
        :type value: str

        :param input_format: The format of the datetime when given as a string. See `strptime behavior`_.
                             If omitted, an attempt will be made to automatically parse the string, which may not be
                             ideal.
        :type input_format: str

        .. _strptime behavior: https://docs.python.org/3.7/library/datetime.html#strftime-strptime-behavior

        :rtype: DateTime

        """
        # https://stackoverflow.com/a/18706449
        if input_format is not None:
            return cls(datetime.strptime(value, input_format))
        else:
            return cls(datetime_parser.parse(value))

    def get_day_of_week(self, offset=False):
        """Get the day of the week for the current date/time.

        :param offset: Sunday in Python is ``0``. Use offset to increase they day of the week by ``1``.
        :type offset: bool

        :rtype: int

        """
        dow = int(self._current_dt.strftime("%w"))

        if offset:
            dow += 1

        return dow

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

    def set_day(self, value):
        """Set the day of the current date/time.

        :param value: The day.
        :type value: int

        """
        self._current_dt = self._current_dt.replace(day=value)

    def set_hour(self, value):
        """Set the hour of the current date/time.

        :param value: The hour.
        :type value: int

        """
        self._current_dt = self._current_dt.replace(hour=value)

    def set_minute(self, value):
        """Set the minute of the current date/time.

        :param value: The minute.
        :type value: int

        """
        self._current_dt = self._current_dt.replace(minute=value)

    def set_timezone(self, timezone='utc'):
        """Set (reset) the timezone for the current date/time.

        :param timezone: The timezone to add. This is UTC by default.
        :type timezone: str

        :rtype: datetime

        """
        timezone = pytz.timezone(timezone)
        self._current_dt = self._current_dt.replace(tzinfo=timezone)
        return self.dt

    def start_of_day_dt(self):
        """Get the date/time for the beginning of the current date/time.

        :rtype: datetime

        """
        dt = self._current_dt
        dt = dt.replace(hour=0, minute=1)
        return dt

    def start_of_month_dt(self):
        """Get the date/time for the beginning of the month for the current date/time.

        :rtype: datetime

        """
        dt = self._current_dt
        dt = dt.replace(day=1, hour=0, minute=1)
        return dt

    @property
    def timezone(self):
        return self.dt.tzinfo

    def to_date(self):
        """Get the current date/time as a date.

        :rtype: date

        .. versionadded: 0.5.3-d

        """
        return self._current_dt.date()


class DateTimeRange(object):
    """Represents a starting point and ending point, and (potentially) all the
    dates and times in between.
    """

    def __init__(self, start_dt, end_dt):
        """Create a new range of dates.

        :param start_dt: The starting datetime.
        :type start_dt: datetime || date

        :param end_dt: The ending datetime.
        :type end_dt: datetime || date

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
        :type dt: datetime || DateTime

        :rtype: bool

        .. note::
            A :class:`DateTime` instance is also accepted as input.

        """
        if isinstance(dt, DateTime):
            dt = dt.dt

        return self.start.dt <= dt <= self.end.dt
