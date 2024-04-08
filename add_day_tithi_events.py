# -*- encoding: utf-8 -*-

import json
import datetime
import re
from ad_bs_converter import convert_bs_to_ad

YEAR = 2081
IN_FILE_1 = "2081_detailed_w_events.json"
OUT_FILE = "2081_detailed_final.json"


if __name__ == "__main__":
    in_file1 = open(IN_FILE_1, "r+")
    in_file1_data = json.load(in_file1)
    
    out_data = {
        "year": YEAR,
        "author": "Brihat Ratna Bajracharya (brihatbajracharya@gmail.com)",
        "data": [[] for i in range(12)]
    }
    
    for month in range(12):
        for day in range(32):
            try:
                day_dict = in_file1_data["data"][month][day]
                day_date = day_dict["date"]
                bs_event_key = day_date[-5:]

                (ad_year, ad_month, ad_date) = convert_bs_to_ad(YEAR, month + 1, day + 1)
                ad_weekday = datetime.date(ad_year, ad_month, ad_date).weekday()

                all_lunar_events = []
                event1 = re.sub(r' / ', ',', day_dict["lunar_event_one"]).split(",")
                event2 = re.sub(r' / ', ',', day_dict["lunar_event_two"]).split(",")
                event3 = re.sub(r' / ', ',', day_dict["lunar_event_three"]).split(",")
                
                all_lunar_events.extend(event1)
                all_lunar_events.extend(event2)
                all_lunar_events.extend(event3)

                all_lunar_events = [i for i in all_lunar_events if i]
                lunar_events_length = len(all_lunar_events)

                wkday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                # print("2081-", month + 1, day + 1, wkday[ad_weekday], end=": ")
                # print(all_lunar_events)

                tithi = in_file1_data["data"][month][day]["tithi"]

                if tithi == "अष्टमी" and "गोरखकाली पूजा" not in all_lunar_events:
                    if lunar_events_length == 0:
                        if day_dict["lunar_event_one"] == "":
                            day_dict["lunar_event_one"] = "गोरखकाली पूजा"
                        else:
                            day_dict["lunar_event_one"] += " / गोरखकाली पूजा"
                        lunar_events_length += 1
                    elif lunar_events_length == 1:
                        if day_dict["lunar_event_two"] == "":
                            day_dict["lunar_event_two"] = "गोरखकाली पूजा"
                        else:
                            day_dict["lunar_event_two"] += " / गोरखकाली पूजा"
                        lunar_events_length += 1
                    elif lunar_events_length == 2:
                        if day_dict["lunar_event_two"] == "":
                            day_dict["lunar_event_three"] = "गोरखकाली पूजा"
                        else:
                            day_dict["lunar_event_three"] += " / गोरखकाली पूजा"
                        lunar_events_length += 1
                    else:
                        day_dict["lunar_event_three"] += " / गोरखकाली पूजा"
                        lunar_events_length += 1

                if tithi == "औंसी" and ad_weekday == 0 and "सोमबारे औंसी" not in all_lunar_events:
                    if lunar_events_length == 0:
                        if day_dict["lunar_event_one"] == "":
                            day_dict["lunar_event_one"] = "सोमबारे औंसी"
                        else:
                            day_dict["lunar_event_one"] += " / सोमबारे औंसी"
                        lunar_events_length += 1
                    elif lunar_events_length == 1:
                        if day_dict["lunar_event_two"] == "":
                            day_dict["lunar_event_two"] = "सोमबारे औंसी"
                        else:
                            day_dict["lunar_event_two"] += " / सोमबारे औंसी"
                        lunar_events_length += 1
                    elif lunar_events_length == 2:
                        if day_dict["lunar_event_two"] == "":
                            day_dict["lunar_event_three"] = "सोमबारे औंसी"
                        else:
                            day_dict["lunar_event_three"] += " / सोमबारे औंसी"
                        lunar_events_length += 1
                    else:
                        day_dict["lunar_event_three"] += " / सोमबारे औंसी"
                        lunar_events_length += 1
                    
                if tithi == "चतुर्थी" and ad_weekday == 1 and "मङ्गल चौथी" not in all_lunar_events:
                    if lunar_events_length == 0:
                        if day_dict["lunar_event_one"] == "":
                            day_dict["lunar_event_one"] = "मङ्गल चौथी"
                        else:
                            day_dict["lunar_event_one"] += " / मङ्गल चौथी"
                        lunar_events_length += 1
                    elif lunar_events_length == 1:
                        if day_dict["lunar_event_two"] == "":
                            day_dict["lunar_event_two"] = "मङ्गल चौथी"
                        else:
                            day_dict["lunar_event_two"] += " / मङ्गल चौथी"
                        lunar_events_length += 1
                    elif lunar_events_length == 2:
                        if day_dict["lunar_event_two"] == "":
                            day_dict["lunar_event_three"] = "मङ्गल चौथी"
                        else:
                            day_dict["lunar_event_three"] += " / मङ्गल चौथी"
                        lunar_events_length += 1
                    else:
                        day_dict["lunar_event_three"] += " / मङ्गल चौथी"
                        lunar_events_length += 1
                
                out_data["data"][month].append(day_dict)
            except:
                # print("here", month, day)
                pass

    with open(OUT_FILE, 'w') as file:
        json.dump(out_data, file)

# In Command Prompt
# json.load(open("2081_detailed.json","r"))
