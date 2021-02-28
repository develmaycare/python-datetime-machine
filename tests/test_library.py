from datetime import datetime
from datetime_machine.library import *
import pytest
import pytz


class TestDateTime(object):

    def test_current(self):
        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)
        assert timing.current == dt

    def test_dt(self):
        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)
        assert timing.dt == dt

    def test_end_of_day_dt(self):
        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)

        end_dt = datetime(2021, 2, 28, 23, 59)
        assert timing.end_of_day_dt() == end_dt

    def test_end_of_month_dt(self):
        dt = datetime(2021, 1, 1, 11, 30)
        timing = DateTime(dt)

        end_dt = datetime(2021, 1, 31, 23, 59)
        assert timing.end_of_month_dt() == end_dt

    def test_fast_forward(self):
        dt = datetime(2021, 2, 28, 11, 30)
        # print(dt)

        timing = DateTime(dt)
        timing.fast_forward(months=1)
        assert timing.dt.month == 3

    def test_from_date(self):
        dt = datetime(2021, 1, 31, tzinfo=pytz.UTC)
        test_date = dt.date()
        timing = DateTime.from_date(test_date)
        assert timing.dt == dt

    def test_from_string(self):
        dt = datetime(2021, 1, 1, 0, 0)

        timing = DateTime.from_string("2021-01-01", input_format="%Y-%m-%d")
        assert timing.dt == dt

        timing = DateTime.from_string("2021-01-01")
        assert timing.dt == dt

    def test_get_day_of_week(self):
        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)

        assert timing.get_day_of_week() == 0
        assert timing.get_day_of_week(offset=True) == 1

    def test_test_init(self):
        timing = DateTime()
        assert timing.dt is not None

        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)
        assert timing.dt == dt

        timing.fast_forward(days=1)
        new_dt = timing.dt

        new_timing = DateTime(timing)
        assert new_timing.dt == new_dt

    def test_in_range(self):
        dt = datetime(2021, 1, 15, 11, 30)
        timing = DateTime(dt)

        start_dt = datetime(2021, 1, 1, 0, 0)
        end_dt = datetime(2021, 1, 31, 23, 59)
        assert timing.in_range(start_dt, end_dt) is True

        start_dt = datetime(2021, 2, 1, 0, 0)
        end_dt = datetime(2021, 2, 28, 23, 59)
        assert timing.in_range(start_dt, end_dt) is False

    def test_is_business_day(self):
        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)
        assert timing.is_business_day() is False

        dt = datetime(2021, 1, 1, 11, 30)
        timing = DateTime(dt)

        holidays = [
            datetime(2020, 12, 25).date(),
            datetime(2021, 1, 1).date(),
        ]
        assert timing.is_business_day(holidays=holidays) is False

        dt = datetime(2021, 3, 1)
        timing = DateTime(dt)
        assert timing.is_business_day() is True

    def test_original(self):
        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)
        assert timing.original == dt

        timing.fast_forward(days=10)
        assert timing.original == dt

    def test_replace(self):
        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)

        with pytest.raises(TypeError):
            timing.replace("invalid", 1)

        timing.replace("tz", "US/Eastern")
        assert str(timing.timezone) == "US/Eastern"

        timing.replace("day", 27)
        assert timing.dt.day == 27

    def test_rewind(self):
        dt = datetime(2021, 2, 28, 11, 30)
        # print(dt)

        timing = DateTime(dt)
        timing.rewind(days=1)

        assert timing.dt.day == 27

        timing = DateTime(dt)
        timing.rewind(business_days=5)
        assert timing.dt.day == 22

    def test_start_of_day_dt(self):
        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)

        end_dt = datetime(2021, 2, 28, 0, 1)
        assert timing.start_of_day_dt() == end_dt

    def test_start_of_month(self):
        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)

        end_dt = datetime(2021, 2, 1, 0, 1)
        assert timing.start_of_month_dt() == end_dt

    def test_str(self):
        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)
        assert str(timing) == "2021-02-28 11:30:00"

    def test_to_date(self):
        dt = datetime(2021, 2, 28, 11, 30)
        timing = DateTime(dt)
        assert str(timing.to_date()) == "2021-02-28"
