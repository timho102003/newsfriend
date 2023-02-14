import pytz
from datetime import datetime
from config import TIMEZONE

def convert_timezone(time=None, format="%Y-%m-%dT%H:%M:%SZ", ori_timezone=None, desire_timezone=TIMEZONE):
    date_time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    ori_timezone = pytz.timezone(ori_timezone)
    date_time = ori_timezone.localize(date_time)
    desired_timezone = pytz.timezone(desire_timezone)
    desire_time = pytz.utc.normalize(date_time).astimezone(desired_timezone)
    return desire_time
