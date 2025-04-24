import typing as t
from datetime import datetime, timedelta


def get_all_days_this_month() -> t.List[datetime]:
    today: datetime = datetime.today()
    year: int = today.year
    month: int = today.month

    # First day of the current month
    start_date: datetime = datetime(year, month, 1)

    # First day of the next month
    if month == 12:
        next_month: datetime = datetime(year + 1, 1, 1)
    else:
        next_month: datetime = datetime(year, month + 1, 1)

    # Number of days in the month
    num_days: int = (next_month - start_date).days

    # Generate all dates
    return [start_date + timedelta(days=i) for i in range(num_days)]
