import argparse
import sys

BS_CALENDAR_DATA = {
    '1975': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '1976': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '1977': [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 365],
    '1978': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '1979': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '1980': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '1981': [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30, 365],
    '1982': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '1983': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '1984': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '1985': [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30, 365],
    '1986': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '1987': [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '1988': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '1989': [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '1990': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '1991': [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '1992': [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 366],
    '1993': [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '1994': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '1995': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30, 365],
    '1996': [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 366],
    '1997': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '1998': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '1999': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2000': [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 365],
    '2001': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2002': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2003': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2004': [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 365],
    '2005': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2006': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2007': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2008': [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31, 365],
    '2009': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2010': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2011': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2012': [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30, 365],
    '2013': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2014': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2015': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2016': [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30, 365],
    '2017': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2018': [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2019': [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 366],
    '2020': [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2021': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2022': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30, 365],
    '2023': [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 366],
    '2024': [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2025': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2026': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2027': [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 365],
    '2028': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2029': [31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30, 365],
    '2030': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2031': [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 365],
    '2032': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2033': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2034': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2035': [30, 32, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31, 365],
    '2036': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2037': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2038': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2039': [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30, 365],
    '2040': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2041': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2042': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2043': [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30, 365],
    '2044': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2045': [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2046': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2047': [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2048': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2049': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30, 365],
    '2050': [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 366],
    '2051': [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2052': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2053': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30, 365],
    '2054': [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 366],
    '2055': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2056': [31, 31, 32, 31, 32, 30, 30, 29, 30, 29, 30, 30, 365],
    '2057': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2058': [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 365],
    '2059': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2060': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2061': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2062': [30, 32, 31, 32, 31, 31, 29, 30, 29, 30, 29, 31, 365],
    '2063': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2064': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2065': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2066': [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 29, 31, 365],
    '2067': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2068': [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2069': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2070': [31, 31, 31, 32, 31, 31, 29, 30, 30, 29, 30, 30, 365],
    '2071': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2072': [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2073': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366],
    '2074': [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2075': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2076': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30, 365],
    '2077': [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 366],
    '2078': [31, 31, 31, 32, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2079': [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30, 365],
    '2080': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 30, 365],
    '2081': [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31, 366],
    '2082': [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30, 365],
    '2083': [31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30, 365],
    '2084': [31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30, 365],
    '2085': [31, 32, 31, 32, 30, 31, 30, 30, 29, 30, 30, 30, 366],
    '2086': [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30, 365],
    '2087': [31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30, 366],
    '2088': [30, 31, 32, 32, 30, 31, 30, 30, 29, 30, 30, 30, 365],
    '2089': [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30, 365],
    '2090': [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30, 365],
    '2091': [31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30, 366],
    '2092': [31, 31, 32, 32, 31, 30, 30, 30, 29, 30, 30, 30, 366],
    '2093': [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30, 365],
    '2094': [31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30, 365],
    '2095': [31, 31, 32, 31, 31, 31, 30, 29, 30, 30, 30, 30, 366],
    '2096': [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30, 365],
    '2097': [31, 32, 31, 32, 31, 30, 30, 30, 29, 30, 30, 30, 366],
    '2098': [31, 31, 32, 31, 31, 31, 29, 30, 29, 30, 29, 31, 365],
    '2099': [31, 31, 32, 31, 31, 31, 30, 29, 29, 30, 30, 30, 365],
    '2100': [31, 32, 31, 32, 31, 30, 30, 30, 29, 29, 30, 31, 366]
}

BS_MONTHS = ["Baisakh", "Jestha", "Ashad", "Shrawan", "Bhadra", "Ashwin",
             "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]
AD_MONTHS = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]

LEAP_DAYS_LIST = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_LIST = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# very important
BASE_BS_YEAR = 1975
BASE_BS_MONTH = 1
BASE_BS_DATE = 1

BASE_AD_YEAR = 1918
BASE_AD_MONTH = 4
BASE_AD_DATE = 13

BASE_AD_OFFSET = 102


def is_leap_year(year):
    ''' checks whether given AD year is leap year or not '''
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def convert_bs_to_ad(bs_year, bs_month, bs_date):
    '''
        this function converts BS date to AD
        input: bs_year, bs_month, bs_date - int
        returns: tuple (ad_year, ad_month, ad_date)
    '''
    total_bs_days = 0

    ''' using num of days in each month '''
    # for year in range(BASE_BS_YEAR, bs_year):
    #     for month in range(0, 12):
    #         total_bs_days += BS_CALENDAR_DATA[str(year)][month]

    ''' using num of days in given year
        (last element of value in BS_CALENDAR_DATA) '''
    for year in range(BASE_BS_YEAR, bs_year):
        total_bs_days += BS_CALENDAR_DATA[str(year)][12]
    # print(total_bs_days)

    for month in range(0, bs_month - 1):
        total_bs_days += BS_CALENDAR_DATA[str(year)][month]
    # print(total_bs_days)

    total_bs_days += bs_date - 1
    # print(total_bs_days)

    res_ad_year = BASE_AD_YEAR
    res_ad_month = BASE_AD_MONTH
    res_ad_date = BASE_AD_DATE

    while(total_bs_days > 0):
        if(is_leap_year(res_ad_year)):
            if(res_ad_date < LEAP_DAYS_LIST[res_ad_month-1]):
                res_ad_date += 1
                total_bs_days -= 1
            else:
                res_ad_month += 1
                res_ad_date = 0
                if(res_ad_month > 12):
                    res_ad_year += 1
                    res_ad_month = 1
        else:
            if(res_ad_date < DAYS_LIST[res_ad_month-1]):
                res_ad_date += 1
                total_bs_days -= 1
            else:
                res_ad_month += 1
                res_ad_date = 0
                if(res_ad_month > 12):
                    res_ad_year += 1
                    res_ad_month = 1

    # print(total_bs_days)
    return (res_ad_year, res_ad_month, res_ad_date)


def convert_ad_to_bs(ad_year, ad_month, ad_date):
    '''
        this function converts AD date to BS
        input: ad_year, ad_month, ad_date - int
        returns: tuple (bs_year, bs_month, bs_date)
    '''
    total_ad_days = 0

    for year in range(BASE_AD_YEAR, ad_year):
        if(is_leap_year(year)):
            total_ad_days += 366
        else:
            total_ad_days += 365
    # print(total_ad_days)

    for month in range(0, ad_month - 1):
        if(is_leap_year(ad_year)):
            total_ad_days += LEAP_DAYS_LIST[month]
        else:
            total_ad_days += DAYS_LIST[month]
    # print(total_ad_days)

    total_ad_days += ad_date - 1
    total_ad_days -= BASE_AD_OFFSET
    # print(total_ad_days)

    res_bs_year = BASE_BS_YEAR
    res_bs_month = BASE_BS_MONTH
    res_bs_date = BASE_BS_DATE

    while(total_ad_days > 0):
        if(res_bs_date < BS_CALENDAR_DATA[str(res_bs_year)][res_bs_month-1]):
            res_bs_date += 1
            total_ad_days -= 1
        else:
            res_bs_month += 1
            res_bs_date = 0
            if(res_bs_month > 12):
                res_bs_year += 1
                res_bs_month = 1
    # print(total_ad_days)

    return (res_bs_year, res_bs_month, res_bs_date)


def is_valid_ad_date(year, month, date):
    ''' checks validity of AD Date '''
    if (year < BASE_AD_YEAR
            or (year == BASE_AD_YEAR and month < BASE_AD_MONTH)
            or (year == BASE_AD_YEAR
                and month == BASE_AD_MONTH
                and date < BASE_AD_DATE)):
        print("Supported date range " + str(BASE_AD_YEAR) + "-"
              + str(BASE_AD_MONTH) + "-" + str(BASE_AD_DATE) + " to 2044-4-15")
        return False

    if (year > 2044
            or (year == 2044 and month > 4)
            or (year == 2044 and month == 4 and date > 15)):
        print("Supported date range " + str(BASE_AD_YEAR) + "-"
              + str(BASE_AD_MONTH) + "-" + str(BASE_AD_DATE) + " to 2044-4-15")
        return False

    if month not in range(1, 13):
        print("Invalid Month")
        return False

    date_range = LEAP_DAYS_LIST[month-1] + 1 if is_leap_year(year) \
        else DAYS_LIST[month-1] + 1
    if date not in range(1, date_range):
        print(str(year) + " " + AD_MONTHS[month-1]
              + " does not have date " + str(date))
        return False

    return True


def is_valid_bs_date(year, month, date):
    ''' checks validity of BS Date '''
    if (year < BASE_BS_YEAR
            or (year == BASE_BS_YEAR and month < BASE_BS_MONTH)
            or (year == BASE_BS_YEAR
                and month == BASE_BS_MONTH
                and date < BASE_BS_DATE)):
        print("Supported date range " + str(BASE_BS_YEAR) + "-"
              + str(BASE_BS_MONTH) + "-" + str(BASE_BS_DATE)
              + " to 2100-12-31")
        return False

    if (year > 2100
            or (year == 2100 and month > 12)
            or (year == 2100 and month == 12 and date > 31)):
        print("Supported date range " + str(BASE_BS_YEAR) + "-"
              + str(BASE_BS_MONTH) + "-" + str(BASE_BS_DATE)
              + " to 2100-12-31")
        return False

    if month not in range(1, 13):
        print("Invalid Month")
        return False

    if date not in range(1, BS_CALENDAR_DATA[str(year)][month-1] + 1):
        print(str(year) + " " + BS_MONTHS[month-1]
              + " does not have date " + str(date))
        return False

    return True


def print_help():
    ''' show usage help '''
    print("usage: ad_bs_converter.py [type] [year] [month] [date]")
    print("")
    print("valid type [type]: to_bs | to_ad")
    print(("valid range [year] [month] [date]: 1978 1 1 to 2092 12 31 (to_bs),"
           " 1918 4 13 to 2044 4 14 (to_ad)"))
    print("")


def main():
    # print("func to call: ", sys.argv[1])
    func = sys.argv[1]
    year = int(sys.argv[2])
    month = int(sys.argv[3])
    date = int(sys.argv[4])

    if(func == "to_ad"):
        if is_valid_bs_date(year, month, date):
            print("converting BS to AD")
            print(convert_bs_to_ad(year, month, date))
    elif(func == "to_bs"):
        if is_valid_ad_date(year, month, date):
            print("converting AD to BS")
            print(convert_ad_to_bs(year, month, date))
    else:
        print("Unknown Type\n")
        print_help()
        return
    print("DONE")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    if len(sys.argv) != 5:
        print_help()
        sys.exit(1)
    main()
