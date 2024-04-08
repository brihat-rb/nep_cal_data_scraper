# -*- encoding: utf-8 -*-


import json

YEAR = 2081
IN_FILE_1 = "2081_detailed.json"
IN_FILE_2 = "events.json"
IN_FILE_3 = "bs_events.json"
OUT_FILE = "2081_detailed_w_events.json"


if __name__ == "__main__":
    in_file1 = open(IN_FILE_1, "r+")
    in_file2 = open(IN_FILE_2, "r")
    in_file3 = open(IN_FILE_3, "r")
    in_file1_data = json.load(in_file1)
    in_file2_data = json.load(in_file2)
    in_file3_data = json.load(in_file3)

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
                # print(in_file1_data)
                day_dict = in_file1_data["data"][month][day]
                day_date = day_dict["date"]
                bs_event_key = day_date[-5:]
                day_dict["lunar_month"] = in_file1_data["data"][month][day]["lunar_month"]
                day_dict["pakshya"] = in_file1_data["data"][month][day]["pakshya"]
                day_dict["tithi"] = in_file1_data["data"][month][day]["tithi"]
                day_dict["ns_year"] = in_file1_data["data"][month][day]["ns_year"]

                day_pakshya = day_dict["lunar_month"]
                day_tithi = day_dict["tithi"]
                day_event_list = in_file2_data[day_pakshya][day_tithi]
                try:
                    bs_event_list = in_file3_data["data"][bs_event_key]
                except:
                    bs_event_list = []
                day_event_list.extend(bs_event_list)
                # print(day_event_list)
                # print(len(day_event_list))

                day_event_list_length = len(day_event_list)
                if (day_event_list_length == 0):
                    continue
                elif (day_event_list_length == 1):
                    day_dict["lunar_event_one"] = day_event_list[0]
                elif (day_event_list_length == 2):
                    day_dict["lunar_event_one"] = day_event_list[0]
                    day_dict["lunar_event_two"] = day_event_list[1]
                elif (day_event_list_length == 3):
                    day_dict["lunar_event_one"] = day_event_list[0]
                    day_dict["lunar_event_two"] = day_event_list[1]
                    day_dict["lunar_event_three"] = day_event_list[2]
                elif (day_event_list_length == 4):
                    day_dict["lunar_event_one"] = day_event_list[0] + " / " + day_event_list[1]
                    day_dict["lunar_event_two"] = day_event_list[2]
                    day_dict["lunar_event_three"] = day_event_list[3]
                elif (day_event_list_length == 5):
                    day_dict["lunar_event_one"] = day_event_list[0] + " / " + day_event_list[1]
                    day_dict["lunar_event_two"] = day_event_list[2] + " / " + day_event_list[3]
                    day_dict["lunar_event_three"] = day_event_list[4]
                elif (day_event_list_length == 6):
                    day_dict["lunar_event_one"] = day_event_list[0] + " / " + day_event_list[1]
                    day_dict["lunar_event_two"] = day_event_list[2] + " / " + day_event_list[3]
                    day_dict["lunar_event_three"] = day_event_list[4] + " / " + day_event_list[5]
                elif (day_event_list_length == 7):
                    day_dict["lunar_event_one"] = day_event_list[0] + " / " + day_event_list[1] + " / " + day_event_list[2]
                    day_dict["lunar_event_two"] = day_event_list[3] + " / " + day_event_list[4]
                    day_dict["lunar_event_three"] = day_event_list[5] + " / " + day_event_list[6]
                elif (day_event_list_length == 8):
                    day_dict["lunar_event_one"] = day_event_list[0] + " / " + day_event_list[1] + " / " + day_event_list[2]
                    day_dict["lunar_event_two"] = day_event_list[3] + " / " + day_event_list[4] + " / " + day_event_list[5]
                    day_dict["lunar_event_three"] = day_event_list[6] + " / " + day_event_list[7]
                elif (day_event_list_length == 9):
                    day_dict["lunar_event_one"] = day_event_list[0] + " / " + day_event_list[1] + " / " + day_event_list[2]
                    day_dict["lunar_event_two"] = day_event_list[3] + " / " + day_event_list[4] + " / " + day_event_list[5]
                    day_dict["lunar_event_three"] = day_event_list[6] + " / " + day_event_list[7] + " / " + day_event_list[8]
                elif (day_event_list_length == 10):
                    day_dict["lunar_event_one"] = day_event_list[0] + " / " + day_event_list[1] + " / " + day_event_list[2]
                    day_dict["lunar_event_two"] = day_event_list[3] + " / " + day_event_list[4] + " / " + day_event_list[5]
                    day_dict["lunar_event_three"] = day_event_list[6] + " / " + day_event_list[7] + " / " + day_event_list[8] + " / " + day_event_list[9]
                else:
                    # print(day_event_list_length)
                    # print(day_event_list)
                    pass
                    
                out_data["data"][month].append(day_dict)
            except Exception as error:
                print("hereः", month, day)
                print(error)
                pass

    with open(OUT_FILE, 'w') as file:
        json.dump(in_file1_data, file)

# In Command Prompt
# json.load(open("2081_detailed.json","r"))
