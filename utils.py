import datetime


def get_dt():
    dt = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(dt, "%m-%d-%Y %H:%M:%S")
    return timestamp