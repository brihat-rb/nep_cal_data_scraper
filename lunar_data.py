#-*- encoding: utf-8 -*-

'''
    ONLY FOR 2077 BS
'''

import json
import copy

OUT_FILE = "2077_lunar.json"
OUT_FILE_2 = "2077_detailed.json"
YEAR = 2077


lunar_month_list = ["चौलागा","बछलागा","बछलाथ्व","तछलागा","तछलाथ्व","दिल्लागा","दिल्लाथ्व","गुँलागा","गुँलाथ्व","ञलागा","ञलाथ्व","अनलागा","अनलाथ्व","कौलागा","कौलाथ्व","कछलागा","कछलाथ्व","थिल्लागा","थिल्लाथ्व","पोहेलागा","पोहेलाथ्व","सिल्लागा","सिल्लाथ्व","चिल्लागा","चिल्लाथ्व","चौलागा"]
pakshya_list = ["वैशाख कृष्णपक्ष", "वैशाख शुक्लपक्ष", "ज्येष्ठ कृष्णपक्ष", "ज्येष्ठ शुक्लपक्ष", "आषाढ कृष्णपक्ष", "आषाढ शुक्लपक्ष", "श्रावण कृष्णपक्ष", "श्रावण शुक्लपक्ष", "भाद्र कृष्णपक्ष", "भाद्र शुक्लपक्ष", "आश्विन कृष्णपक्ष", "अधिक आश्विन शुक्लपक्ष", "अधिक आश्विन कृष्णपक्ष", "आश्विन शुक्लपक्ष", "कार्तिक कृष्णपक्ष", "कार्तिक शुक्लपक्ष", "मंसिर कृष्णपक्ष", "मंसिर शुक्लपक्ष", "पौष कृष्णपक्ष", "पौष शुक्लपक्ष", "माघ कृष्णपक्ष", "माघ शुक्लपक्ष", "फाल्गुण कृष्णपक्ष", "फाल्गुण शुक्लपक्ष", "चैत्र कृष्णपक्ष", "चैत्र शुक्लपक्ष"]


def get_lunar_month(date):
    ''' only valid  for 2077 BS '''
    date_split = date.split("-")
    date_month = int(date_split[1])
    date_day = int(date_split[2])

    if date_month == 1 and (date_day >= 1 and date_day <= 11):
        return lunar_month_list[0]
    elif date_month == 1 and (date_day >= 12 and date_day <= 25):
        return lunar_month_list[1]
    elif (date_month == 1 and (date_day >= 26 and date_day <= 32)) or (date_month == 2 and (date_day >= 1 and date_day <= 9)):
        return lunar_month_list[2]
    elif date_month == 2 and (date_day >= 10 and date_day <= 23):
        return lunar_month_list[3]
    elif date_month == 2 and (date_day >= 24 and date_day <= 32) or (date_month == 3 and (date_day >= 1 and date_day <= 7)):
        return lunar_month_list[4]
    elif date_month == 3 and (date_day >= 8 and date_day <= 21):
        return lunar_month_list[5]
    elif date_month == 3 and (date_day >= 22 and date_day <= 32) or (date_month == 4 and (date_day >= 1 and date_day <= 5)):
        return lunar_month_list[6]
    elif date_month == 4 and (date_day >= 6 and date_day <= 19):
        return lunar_month_list[7]
    elif date_month == 4 and (date_day >= 20 and date_day <= 32) or (date_month == 5 and (date_day >= 1 and date_day <= 3)):
        return lunar_month_list[8]
    elif date_month == 5 and (date_day >= 4 and date_day <= 17):
        return lunar_month_list[9]
    elif date_month == 5 and (date_day >= 18 and date_day <= 32) or (date_month == 6 and (date_day >= 1 and date_day <= 1)):
        return lunar_month_list[10]
    elif date_month == 6 and (date_day >= 2 and date_day <= 15):
        return lunar_month_list[11]
    elif date_month == 6 and (date_day >= 16 and date_day <= 30):
        return lunar_month_list[12]
    elif date_month == 7 and (date_day >= 1 and date_day <= 15):
        return lunar_month_list[13]
    elif date_month == 7 and (date_day >= 16 and date_day <= 30):
        return lunar_month_list[14]
    elif date_month == 8 and (date_day >= 1 and date_day <= 15):
        return lunar_month_list[15]
    elif date_month == 8 and (date_day >= 16 and date_day <= 29):
        return lunar_month_list[16]
    elif date_month == 8 and (date_day >= 30 and date_day <= 32) or (date_month == 9 and (date_day >= 1 and date_day <= 15)):
        return lunar_month_list[17]
    elif date_month == 9 and (date_day >= 16 and date_day <= 29):
        return lunar_month_list[18]
    elif date_month == 10 and (date_day >= 1 and date_day <= 15):
        return lunar_month_list[19]
    elif date_month == 10 and (date_day >= 16 and date_day <= 29):
        return lunar_month_list[20]
    elif date_month == 10 and (date_day >= 30 and date_day <= 32) or (date_month == 11 and (date_day >= 1 and date_day <= 15)):
        return lunar_month_list[21]
    elif date_month == 11 and (date_day >= 16 and date_day <= 29):
        return lunar_month_list[22]
    elif date_month == 12 and (date_day >= 1 and date_day <= 15):
        return lunar_month_list[23]
    elif date_month == 12 and (date_day >= 16 and date_day <= 30):
        return lunar_month_list[24]
    elif date_month == 12 and (date_day >= 31 and date_day <= 32):
        return lunar_month_list[25]
    return date + " undefined lunar month"


def get_pakshya(date):
    ''' only valid  for 2077 BS '''
    date_split = date.split("-")
    date_month = int(date_split[1])
    date_day = int(date_split[2])

    if date_month == 1 and (date_day >= 1 and date_day <= 11):
        return pakshya_list[0]
    elif date_month == 1 and (date_day >= 12 and date_day <= 25):
        return pakshya_list[1]
    elif (date_month == 1 and (date_day >= 26 and date_day <= 32)) or (date_month == 2 and (date_day >= 1 and date_day <= 9)):
        return pakshya_list[2]
    elif date_month == 2 and (date_day >= 10 and date_day <= 23):
        return pakshya_list[3]
    elif date_month == 2 and (date_day >= 24 and date_day <= 32) or (date_month == 3 and (date_day >= 1 and date_day <= 7)):
        return pakshya_list[4]
    elif date_month == 3 and (date_day >= 8 and date_day <= 21):
        return pakshya_list[5]
    elif date_month == 3 and (date_day >= 22 and date_day <= 32) or (date_month == 4 and (date_day >= 1 and date_day <= 5)):
        return pakshya_list[6]
    elif date_month == 4 and (date_day >= 6 and date_day <= 19):
        return pakshya_list[7]
    elif date_month == 4 and (date_day >= 20 and date_day <= 32) or (date_month == 5 and (date_day >= 1 and date_day <= 3)):
        return pakshya_list[8]
    elif date_month == 5 and (date_day >= 4 and date_day <= 17):
        return pakshya_list[9]
    elif date_month == 5 and (date_day >= 18 and date_day <= 32) or (date_month == 6 and (date_day >= 1 and date_day <= 1)):
        return pakshya_list[10]
    elif date_month == 6 and (date_day >= 2 and date_day <= 15):
        return pakshya_list[11]
    elif date_month == 6 and (date_day >= 16 and date_day <= 30):
        return pakshya_list[12]
    elif date_month == 7 and (date_day >= 1 and date_day <= 15):
        return pakshya_list[13]
    elif date_month == 7 and (date_day >= 16 and date_day <= 30):
        return pakshya_list[14]
    elif date_month == 8 and (date_day >= 1 and date_day <= 15):
        return pakshya_list[15]
    elif date_month == 8 and (date_day >= 16 and date_day <= 29):
        return pakshya_list[16]
    elif date_month == 8 and (date_day >= 30 and date_day <= 32) or (date_month == 9 and (date_day >= 1 and date_day <= 15)):
        return pakshya_list[17]
    elif date_month == 9 and (date_day >= 16 and date_day <= 29):
        return pakshya_list[18]
    elif date_month == 10 and (date_day >= 1 and date_day <= 15):
        return pakshya_list[19]
    elif date_month == 10 and (date_day >= 16 and date_day <= 29):
        return pakshya_list[20]
    elif date_month == 10 and (date_day >= 30 and date_day <= 32) or (date_month == 11 and (date_day >= 1 and date_day <= 15)):
        return pakshya_list[21]
    elif date_month == 11 and (date_day >= 16 and date_day <= 29):
        return pakshya_list[22]
    elif date_month == 12 and (date_day >= 1 and date_day <= 15):
        return pakshya_list[23]
    elif date_month == 12 and (date_day >= 16 and date_day <= 30):
        return pakshya_list[24]
    elif date_month == 12 and (date_day >= 31 and date_day <= 32):
        return pakshya_list[25]
    return date + " undefined pakshya"

if __name__ == "__main__":
    in_file = open("2077.json", "r+")
    prev_data = json.load(in_file)
    out_dict = {}

    for month in range(12):
        for day in range(32):
            try:
                day_dict = prev_data["data"][month][day]
                day_date = day_dict["date"]

                day_dict["lunar_month"] = get_lunar_month(day_date)
                day_dict["pakshya"] = get_pakshya(day_date)
                out_dict[day_date] = [day_dict["lunar_month"], day_dict["pakshya"]]

                # print(day_date),
                # print("\t"),
                # print(get_lunar_month(day_date))
            except:
                pass

    with open(OUT_FILE, 'w') as file:
        json.dump(out_dict, file)

    with open(OUT_FILE_2, 'w') as file2:
        json.dump(prev_data, file2)
