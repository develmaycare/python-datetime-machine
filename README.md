# Python Datetime Machine

Working with dates and times in any programming language is always painful and
often non-intuitive. Python has a great tool set for dates and times, but there
is a useful layer that's missing – the ability to easily manipulate datetimes
in way that is contextual and obvious.

## Disclaimer

We *are* using this package in various projects, but it is still experimental
and there are no unit tests. Use at your own risks.

Feedback is welcomed.

## Installation

Install using PIP:

    pip install https://bitbucket.org/bogeymin/python-datetime-machine/get/master.zip;

## Examples

Incrementing a datetime::

        from datetime_machine import DateTime

        # Defaults to the now.
        due = DateTime()
        print(due) # 2016-04-25 14:35:58.805607+00:00

        # Increment by 30 business days.
        due.increment(business_days=30)
        print(due) # 2016-06-06 14:35:58.805607+00:00

Testing a range::

    from datetime_machine import DateTime, DateTimeRange
    
    # Assume you have a bunch of datetimes to check.
    # datetimes = [..., ..., ...]
    
    # DateTimeRange accepts a datetime or DateTime instance.
    start = DateTime()
    
    # We can use the datetime from start to initialize and then increment a due 
    # date.
    due = DateTime(start.dt)
    due.increment(days=30)
    
    # Now create a range.
    dt_range = DateTimeRange(start, due)
    
    # Interate through the datetimes to check.
    for dt in datetimes:
        if dt_range.includes(dt):
            print("datetime is in range: %s" % dt)
    