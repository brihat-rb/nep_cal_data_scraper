from scraper.scraper import Scraper
import json

OUT_FILE = "2080.json"
YEAR = 2080

if __name__ == "__main__":
    all_data = []
    year = YEAR

    for month in range(12):
        print(str(year) + " - " + str(month+1))
        s = Scraper(year, month)
        all_data.append(s.get_nepali_calendar_data())

    nep_cal_json = {
        "year": YEAR,
        "author": "Brihat Ratna Bajracharya (brihatbajracharya@gmail.com)", 
        "data": all_data
    }

    with open(OUT_FILE, 'w') as file:
        json.dump(nep_cal_json, file)
