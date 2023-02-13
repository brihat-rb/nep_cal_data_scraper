# -*- encoding: utf-8 -*-


import json

YEAR = 2080
IN_FILE_1 = "2080.json"
IN_FILE_2 = "2080_lunar_data.json"
OUT_FILE = "2080_detailed.json"


if __name__ == "__main__":
    in_file1 = open(IN_FILE_1, "r+")
    in_file2 = open(IN_FILE_2, "r")
    in_file1_data = json.load(in_file1)
    in_file2_data = json.load(in_file2)

    out_data = {
        "year": YEAR,
        "author": "Brihat Ratna Bajracharya (brihatbajracharya@gmail.com)",
        "data": [[] for i in range(12)]
        }

    # print(out_data)
    day_dict = {}

    for month in range(12):
        for day in range(32):
            try:
                day_dict = in_file1_data["data"][month][day]
                day_date = day_dict["date"]
                day_dict["lunar_month"] = in_file2_data["2080-" + str(month + 1).zfill(2) + "-" + str(day + 1).zfill(2)][0]
                day_dict["pakshya"] = in_file2_data["2080-" + str(month + 1).zfill(2) + "-" + str(day + 1).zfill(2)][1]
                day_dict["tithi"] = in_file2_data["2080-" + str(month + 1).zfill(2) + "-" + str(day + 1).zfill(2)][2]
                day_dict["ns_year"] = in_file2_data["2080-" + str(month + 1).zfill(2) + "-" + str(day + 1).zfill(2)][3]

                out_data["data"][month].append(day_dict)
                # print(out_data)
            except:
                pass

    with open(OUT_FILE, 'w') as file:
        json.dump(out_data, file)

# In Command Prompt
# json.load(open("2080_detailed.json","r"))
