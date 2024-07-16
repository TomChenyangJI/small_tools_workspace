import datetime
from config import min_buffer


# design the schedule
def time_is_up(hr=6, m=0):
    delta = datetime.timedelta(minutes=min_buffer)
    datetime_obj_lower_bound = datetime.datetime.now() - delta
    datetime_obj_upper_bound = datetime.datetime.now() + delta
    desired_time = datetime.datetime.now().replace(hour=hr, minute=m)
    if datetime_obj_lower_bound < desired_time < datetime_obj_upper_bound:
        return True
    else:
        return False
