import calendar
from datetime import datetime
  
today_datetime = datetime.today() # 2022-04-13 18:14:34.796495


# 'datetime.date' object
td_date = today_datetime.date() # 2022-04-13
td_time = today_datetime.time() # 18:14:34.796495
td_time_am_pm = today_datetime.strftime("%I:%M %p") # 06:37 PM


year, month, day = [int(item) for item in str(td_date).split("-")] 


date_as_string = " ".join(str(today_datetime.date()).split("-"))
# 2022 04 13 <class 'str'>

day_code = datetime.strptime(date_as_string, "%Y %m %d").weekday()
weekday_as_string = calendar.day_name[day_code]
# Wednesday <class 'str'>

def add_time(start: str, duration:str, starting_day:str = None):
    converteStartParam = str(datetime.strptime(start, "%I:%M %p").time())
    starting = [int (item) for item in converteStartParam.split(":")[:2]] # [:2] ignore soconds

    print(starting)
    # 1900-01-01 19:35:00 <class 'datetime.datetime'>

    during = [int(item) for item in duration.split(":")]
    print(during)
    
    new_time = add_time_process(starting, during)
    print(new_time)
    return new_time


def add_time_process(start: list, duration:list) -> list:

    start_hour, start_minute = start
    duration_hour, duration_minute = duration
    
    hours_added = start_hour + duration_hour
    minutes_added = start_minute + duration_minute

    is_minute_over_60 = minutes_added / 60
    
    if is_minute_over_60 < 1:
        return [hours_added, minutes_added]
    elif is_minute_over_60 == 1.0:
        return [hours_added + 1, 0]
    elif is_minute_over_60 > 1:
        after_calculate_diff = [int(item) for item in str(round(is_minute_over_60, 2)).split(".")]
        # [hour_after_calcule, minute_after_calcule]
        # (158:60) + (19:13) -> (1, 22)
        
        new_h, new_m = after_calculate_diff
        return [hours_added + new_h , new_m]
    

add_time("07:35 PM", "24:20")