import datetime


def unix_to_datetime(unix):
    return datetime.datetime.fromtimestamp(
            int(unix)
        ).strftime('%Y-%m-%d %H:%M:%S')


def get_month_by_dt(unix):
    return datetime.datetime.fromtimestamp(
        int(unix)
    ).strftime('%m')
