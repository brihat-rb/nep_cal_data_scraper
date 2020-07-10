#-*- encoding: utf-8 -*-

'''
    ONLY FOR 2076 BS
'''

import json
import copy

OUT_FILE = "2076_lunar_2.json"
OUT_FILE_2 = "2076_detailed_2.json"
YEAR = 2076


def get_nepal_sambat(date):
    ''' only valid  for 2076 BS '''
    date_split = date.split("-")
    date_month = int(date_split[1])
    date_day = int(date_split[2])

    ''' this is for 2077 '''
    # if date_month < 8:
    #     return "1140"
    # elif date_month >= 8:
    #     return "1141"
    # return " n/a "

    ''' this is for 2076 '''
    if date_month < 7:
        return "1139"
    elif date_month > 7:
        return "1140"
    elif date_month == 7:
        if date_day < 12:
            return "1139"
        elif date_day >= 12:
            return "1140"
    return " n/a "

if __name__ == "__main__":
    in_file = open("2076_detailed.json", "r+")
    prev_data = json.load(in_file)
    out_dict = {}

    for month in range(12):
        for day in range(32):
            try:
                day_dict = prev_data["data"][month][day]
                day_date = day_dict["date"]

                day_dict["ns_year"] = get_nepal_sambat(day_date)
                out_dict[day_date] = day_dict["ns_year"]

                # print(day_date),
                # print("\t"),
                # print(get_nepal_sambat(day_date))
            except:
                pass

    with open(OUT_FILE, 'w') as file:
        json.dump(out_dict, file)

    with open(OUT_FILE_2, 'w') as file2:
        json.dump(prev_data, file2)
