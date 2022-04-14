from datetime import datetime as dt, timedelta
# first weekdays date in 2000/01
# I ised it as a refree
# example first monday in 2000/01 the date was 2000/01/*3*
DaysOfTheWeek = {
    "Monday": 3, 
    "Tuesday": 4,
    "Wednesday": 5, 
    "Thursday": 6, 
    "Friday": 7, 
    "Saturday": 1, 
    "Sunday": 2
}


def add_time(start: str, period: str, start_from: str= "No"):
    start_from = start_from.capitalize()
    
    # used first of 2000 as a refree
    current_year, current_month, current_day = 2000, 1, 1
    in_dt = dt.strptime(start, "%I:%M %p").strftime("%H:%M").split(":")
    user_hour, user_minute = [int(item) for item in in_dt]

    hours_toBe_added, minutes_toBe_added = [int(item) for item in period.split(":")]

    if start_from not in DaysOfTheWeek:
        day_as_dt = dt(year=current_year, month=current_month, day=current_day, hour=user_hour, minute=user_minute)
        time_after_added = day_as_dt + timedelta(hours=hours_toBe_added, minutes=minutes_toBe_added)
        
    else:
        starting_day_code = DaysOfTheWeek[start_from]
        day_as_dt = dt(year=current_year, month=current_month, day=starting_day_code, hour=user_hour, minute=user_minute)
        time_after_added = day_as_dt + timedelta(hours=hours_toBe_added, minutes=minutes_toBe_added)


    nDays = time_after_added.date().day - day_as_dt.date().day
    weekday_name = time_after_added.strftime("%A")
    
    goal_time = time_after_added.strftime("%I:%M %p")
    
    # check if the time contain a 0 at the begining
    # if so remove it
    if goal_time.split(":")[0][:1] == "0":
        goal_time = goal_time[1:]

    
    if start_from in DaysOfTheWeek:
        if nDays == 0:
            return f"{goal_time}, {weekday_name}"
        elif nDays == 1:
            return f"{goal_time}, {weekday_name} (next day)"
        else:
            return f"{goal_time}, {weekday_name} ({nDays} days later)"
    else:
        if nDays == 0:
            return f"{goal_time}"
        if nDays == 1:
            return f"{goal_time} (next day)"
        else:
            return f"{goal_time} ({nDays} days later)"