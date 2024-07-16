from weather_detail_getter import get_weather_detail, process_response
from send_email import send_info_to_user
from scheduler import time_is_up
from config import min_buffer
import time


if __name__ == "__main__":
    while True:
        result = time_is_up(8, 0)
        if result:
            body_info = get_weather_detail()
            summary = process_response(body_info)
            subject_component = ""
            if "rain" in summary:
                subject_component = "-Rain"
            elif "snow" in summary:
                subject_component = "-Snow"
            weather_prediction = ""
            weather_prediction += f"WEATHER PREDICTION (coming 24hrs):\n\n" + summary
            send_info_to_user(weather_prediction, subject_component)
            print("The warm weather reminder has been sent to the user!\n")
        print("Waiting till the moment.")
        time.sleep(min_buffer * 60)
