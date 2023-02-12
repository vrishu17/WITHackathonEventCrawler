# -*- coding: utf-8 -*-
import datetime
from bs4 import BeautifulSoup
import requests

def get_all_meetups():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    # url = 'https://www.meetup.com/women-who-code-mumbai/events/'
    url = 'https://www.meetup.com/pune-developers-community/events/'
    # url = 'https://www.meetup.com/pune-tech-community/events/'
    # url = 'https://www.meetup.com/find/?location=in--Pune&source=EVENTS'

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
            print('----------------------------------------')
            eventTitle = item.select('.eventCardHead--title')[0].get_text()
            #print(eventTitle)
            li["eventTitle"] = eventTitle
        except Exception as e:
            # raise e
            eventTitle = ''

        try:
            eventDesc = item.select('.description-markdown--p')[0].get_text()
            #print(eventDesc)
            li["eventDesc"] = eventDesc
        except Exception as e:
            # raise e
            eventDesc = ''

        try:
            eventType = item.select('.networkEventCardHead--title')[0].get_text()
            #print(eventType)
            li["eventType"] = eventType
        except Exception as e:
            # raise e
            eventType = ''

        try:
            # eventDateTime = item.select('.eventTimeDisplay-startDate')[0].get_text()
            # # print(eventDateTime)
            # li["eventDateTime"] = eventDateTime

            datetime_val = item.select("time")[0]
            if datetime_val and 'datetime' in datetime_val.attrs:
                datetime_num = datetime_val['datetime']
                datetimeobj = datetime.datetime.fromtimestamp(int(datetime_num) / 1e3)
                print(datetimeobj)

                dt_timezone = datetimeobj.astimezone().tzname()
                dt_day = datetimeobj.strftime('%A')
                dt_month = datetimeobj.strftime('%b')
                dt_date = datetimeobj.strftime('%d')
                dt_year = datetimeobj.strftime('%Y')
                dt_time = datetimeobj.strftime('%H:%M')

                # print(dt_timezone)
                # print(dt_day)
                # print(dt_month)
                # print(dt_date)
                # print(dt_year)
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
            #print(eventLink)
            li["eventLink"] = eventLink
        except Exception as e:
            # raise e
            eventType = ''

        try:
            eventVenue = item.select('.venueDisplay')[0].get_text()
            #print(eventVenue)
            li["eventVenue"] = eventVenue
        except Exception as e:
            # raise e
            eventType = ''

        lo.append(li)

    # print(lo)
    #print(eventTitle)
    #print(eventDesc)
    #print(eventType)
    #print(eventDateTime)
    #print(eventLink)
    #print(eventVenue)
    return lo

# print(get_all_meetups())
