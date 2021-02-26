from datetime import datetime
from datetime_machine.variables import CURRENT_YEAR
from datetime_machine.utils import *
import pytest


def test_get_days_in_month():
    days = get_days_in_month(1)
    assert days == 31

    days = get_days_in_month(2, 2020)
    assert days == 29

    with pytest.raises(ValueError):
        get_days_in_month(13)


def test_get_year_range():
    a = get_year_range(2015)
    assert a[0] == 2015
    assert a[-1] == CURRENT_YEAR

    a = get_year_range(2000, 2019)
    assert a[0] == 2000
    assert a[-1] == 2019


def test_increment():
    pass


def test_is_business_day():
    dt = datetime.strptime("2021-02-26 13:14:00", "%Y-%m-%d %H:%M:%S")
    assert is_business_day(dt) is True

    dt = datetime.strptime("2021-02-27 13:14:00", "%Y-%m-%d %H:%M:%S")
    assert is_business_day(dt) is False

    holidays = [
        datetime.strptime("2021-12-25 13:14:00", "%Y-%m-%d %H:%M:%S"),
    ]
    dt = datetime.strptime("2021-12-24 13:14:00", "%Y-%m-%d %H:%M:%S")
    assert is_business_day(dt, holidays=holidays) is True

    dt = datetime.strptime("2021-12-25 13:14:00", "%Y-%m-%d %H:%M:%S")
    assert is_business_day(dt, holidays=holidays) is False


def test_is_holiday():
    pass


def test_is_leap_year():
    assert is_leap_year(2019) is False
    assert is_leap_year(2020) is True
