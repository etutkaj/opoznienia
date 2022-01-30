import re

def is_valid_station_number(value):
    return value.isdigit()

def is_valid_line_number(value):
    return is_valid_station_number(value)

def is_valid_vehicle_mumber(value):
    if (len(value) < 5 or not value.isdecimal()):
        return False
    return True

def is_valid_date(value):
    return re.match("^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$", value)

def is_valid_time(value):
    return re.match("^(0[1-9]|1[0-9]|2[0-3]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])$", value)
