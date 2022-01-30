import sys
import pandas as pd
from .validators import is_valid_station_number, is_valid_line_number, is_valid_vehicle_mumber, is_valid_time, is_valid_date
from .helpers import calculate_delay_minutes, calculate_time_on_station, string_to_datetime, get_output_filename

def filter_correct_data(filename_in):
    data = pd.read_csv(filename_in, sep=',')

    data_incorrect = data[
        ~(data['NrPrzystanku'].apply(is_valid_station_number)
        & data['NrLinii'].apply(is_valid_line_number)
        & data['NrPojazdu'].apply(is_valid_vehicle_mumber)
        & data['Data'].apply(is_valid_date)
        & data['CzasRozkladowy'].apply(is_valid_time)
        & data['CzasPrzyjazdu'].apply(is_valid_time)
        & data['CzasOdjazdu'].apply(is_valid_time))
    ]
    data_correct = data[
        data['NrPrzystanku'].apply(is_valid_station_number)
        & data['NrLinii'].apply(is_valid_line_number)
        & data['NrPojazdu'].apply(is_valid_vehicle_mumber)
        & data['Data'].apply(is_valid_date)
        & data['CzasRozkladowy'].apply(is_valid_time)
        & data['CzasPrzyjazdu'].apply(is_valid_time)
        & data['CzasOdjazdu'].apply(is_valid_time)
    ]

    data_correct['Opoznienie(min)'] = data_correct.apply(lambda row: calculate_delay_minutes(row['Data'], row['CzasRozkladowy'], row['CzasOdjazdu']), axis=1)
    data_correct['CzasNaStacji(min)'] = data_correct.apply(lambda row: calculate_delay_minutes(row['Data'], row['CzasPrzyjazdu'], row['CzasOdjazdu']), axis=1)

    with open(get_output_filename(filename_in, 'nieprawidlowe'), mode='w', newline="") as file:
        file.write(data_incorrect.to_csv(index=False))

    with open(get_output_filename(filename_in, 'prawidlowe'), mode='w', newline="") as file:
        file.write(data_correct.to_csv(index=False))
