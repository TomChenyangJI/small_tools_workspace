from registerAttendance import register_attendance
import datetime
import time


"""
research center location：(
        *, # latitude 
        * # longitude
        )
"""


if __name__ == "__main__":
    while True:
        current_hr = datetime.datetime.now().hour
        current_day = datetime.datetime.now().day
        # if current_hr == 22 and current_day == 18:
        if current_hr == 22 or current_hr == 19 or current_hr == 7:
            print(datetime.datetime.now())
            register_attendance()
            time.sleep(60 * 60)
            # break
        else:
            print("Sleeping for 30 minutes...")
            time.sleep(60 * 30)
