from datetime import datetime

def string_to_datetime(date, time):
    return datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')

def calculate_delay_minutes(date, planned_time, departure_time):
    planned = string_to_datetime(date, planned_time)
    departure = string_to_datetime(date, departure_time)

    time_delta = (departure - planned).total_seconds()

    return int(time_delta / 60)

def calculate_time_on_station(date, arrival_time, departure_time):
    arrival = string_to_datetime(date, arrival_time)
    departure = string_to_datetime(date, departure_time)

    time_delta = (departure - arrival).total_seconds()

    return int(time_delta / 60)

def get_output_filename(input_filename, suffix):
    return input_filename.replace('.csv', '_' + suffix + '.csv')
