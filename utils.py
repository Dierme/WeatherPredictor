import datetime


def unix_to_datetime(unix):
    return datetime.datetime.fromtimestamp(
            int(unix)
        ).strftime('%Y-%m-%d %H:%M:%S')