# -*- coding: utf-8 -*-
import datetime
from bs4 import BeautifulSoup
import requests

def get_all_meetups_from_one_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

    base_url = 'https://www.meetup.com'

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    # print(soup)

    eventTitle = ''
    eventDesc = ''
    evenDateTime = ''
    eventType = ''
    eventLink = ''
    eventVenue = ''

    # empty list
    lo = []
    li = {}

    for item in soup.select('.card'):
        li = {}
        # print(item)

        try:
            # print('----------------------------------------')
            eventTitle = item.select('.eventCardHead--title')[0].get_text()
            li["eventTitle"] = eventTitle
        except Exception as e:
            # raise e
            eventTitle = ''

        try:
            eventDesc = item.select('.description-markdown--p')[0].get_text()
            li["eventDesc"] = eventDesc
            li["eventDescShort"] = eventDesc[0:200] + '...'
        except Exception as e:
            # raise e
            eventDesc = ''

        try:
            eventType = item.select('.networkEventCardHead--title')[0].get_text()
            li["eventType"] = eventType
        except Exception as e:
            # raise e
            eventType = ''

        try:
            datetime_val = item.select("time")[0]
            if datetime_val and 'datetime' in datetime_val.attrs:
                datetime_num = datetime_val['datetime']
                datetimeobj = datetime.datetime.fromtimestamp(int(datetime_num) / 1e3)

                dt_timezone = datetimeobj.astimezone().tzname()
                dt_day = datetimeobj.strftime('%A')
                dt_month = datetimeobj.strftime('%b')
                dt_date = datetimeobj.strftime('%d')
                dt_year = datetimeobj.strftime('%Y')
                dt_time = datetimeobj.strftime('%H:%M')

                li["datetimeobj"] = datetimeobj
                li["eventTimezone"] = dt_timezone
                li["eventDay"] = dt_day
                li["eventMonth"] = dt_month
                li["eventDate"] = dt_date
                li["eventYear"] = dt_year
                li["eventTime"] = dt_time
        except Exception as e:
            # raise e
            eventType = ''

        try:
            eventLink = base_url + item.select('.eventCard--link')[0]['href']
            li["eventLink"] = eventLink
        except Exception as e:
            # raise e
            eventType = ''

        try:
            eventVenue = item.select('.venueDisplay')[0].get_text()
            li["eventVenue"] = eventVenue
        except Exception as e:
            # raise e
            eventType = ''

        lo.append(li)

    return lo

# print(get_all_meetups_from_one_url('https://www.meetup.com/women-who-code-mumbai/events/'))
