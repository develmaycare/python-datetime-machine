.. _getting-started:

***************
Getting Started
***************

System Requirements
===================

Python 3.6 or higher is required.

Install
=======

To install:

``pip install git+https://github.com/develmaycare/python-datetime-machine.git;``

Examples
========

Advancing a date forward in time.

.. code-block:: python

    from datetime_machine import DateTime

    # Defaults to the now.
    due = DateTime()
    print(due)

    # Increment by 30 business days.
    due.fast_forward(business_days=30)
    print(due) # 2016-06-06 14:35:58.805607+00:00

Moving a date backward in time.

.. code-block:: python

    from datetime_machine import DateTime

    start = DateTime()
    start.rewind(days=90)
    print(start)

FAQs
====

Have a question? `Just ask`_!

.. _Just ask: https://develmaycare.com/contact/?support=1&product=DateTime%20Machine