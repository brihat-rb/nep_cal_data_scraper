# -*- encoding: utf-8 -*-

import json

OUT_FILE = "2070_lunar_data.json"

if __name__ == "__main__":
    in_file = open("2070.json", "r+")
    prev_data = json.load(in_file)
    day_dict = {}

    for month in range(12):
        for day in range(32):
            try:
                day_date = prev_data["data"][month][day]["date"]
                try:
                    lunar_month = prev_data["data"][month][day]["lunar_month"]
                except:
                    lunar_month = ""
                try:
                    pakshya = prev_data["data"][month][day]["pakshya"]
                except:
                    pakshya = ""
                try:
                    tithi = prev_data["data"][month][day]["tithi"]
                except:
                    tithi = ""
                try:
                    ns_year = prev_data["data"][month][day]["ns_year"]
                except:
                    ns_year = ""

                day_dict[day_date] = [lunar_month, pakshya, tithi, ns_year]
            except:
                pass

    with open(OUT_FILE, 'w') as file:
        json.dump(day_dict, file)
