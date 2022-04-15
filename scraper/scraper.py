#-*- encoding: utf-8 -*-

import requests
import bs4

BASE_URL = "http://www.ashesh.com.np/nepali-calendar/"
MONTHS = ["Baishakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin", "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]
ENG_TITHIS = ["Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Sasthi", "Saptami", "Astami", "Nawami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Aaunsi", "Purnima"]
NEP_TITHIS = ["प्रतिपदा", "द्वितीया", "तृतिया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी", "अष्टमी", "नवमी", "दशमी", "एकादशी", "द्वादशी","त्रयोदशी", "चतुर्दशी", "औंसी", "पूर्णिमा"]


class Scraper:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.url = BASE_URL + "?year=" + str(self.year) + "&month=" + str(MONTHS[self.month])

        self.response = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(self.response.text, "html.parser")

    def get_nepali_calendar_data(self):
        all_days = self.soup.findAll('div', {"class": "date_np"})
        all_days_data = {}

        for day in all_days:
            tithi = day.parent.find('div', {"class": "tithi"}).text.strip()
            event_one = day.parent.find('div', {"class": "event_one"}).text.strip()
            event_two = day.parent.find('div', {"class": "rotate_left"}).text.strip()
            event_three = day.parent.find('div', {"class": "rotate_right"}).text.strip()
            if tithi in ENG_TITHIS:
                tithi = NEP_TITHIS[ENG_TITHIS.index(tithi)]
            all_days_data[int(day.get_text())] = [tithi, event_one, event_two, event_three]

        self.nepali_calendar_data = []
        for i in range(32):
            if (i+1) in all_days_data:
                day = all_days_data[i+1]
                date = (self.year, self.month+1, i+1)
                date_string = "%04d-%02d-%02d" % date
                self.nepali_calendar_data.append({
                    "date": date_string,
                    "tithi": day[0],
                    "lunar_event_one": day[1],
                    "lunar_event_two": day[2],
                    "lunar_event_three": day[3]
                })

        return self.nepali_calendar_data
