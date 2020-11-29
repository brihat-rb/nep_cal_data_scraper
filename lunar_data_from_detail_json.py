# -*- encoding: utf-8 -*-

import json

OUT_FILE = "2076_lunar_data.json"

if __name__ == "__main__":
    in_file = open("2076_detailed.json", "r+")
    prev_data = json.load(in_file)
    day_dict = {}

    for month in range(12):
        for day in range(32):
            try:
                day_date = prev_data["data"][month][day]["date"]
                lunar_month = prev_data["data"][month][day]["lunar_month"]
                pakshya = prev_data["data"][month][day]["pakshya"]
                tithi = prev_data["data"][month][day]["tithi"]
                ns_year = prev_data["data"][month][day]["ns_year"]

                day_dict[day_date] = [lunar_month, pakshya, tithi, ns_year]
            except:
                pass

    with open(OUT_FILE, 'w') as file:
        json.dump(day_dict, file)
