# -*- coding: utf-8 -*-
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
            evenDateTime = item.select('.eventTimeDisplay-startDate')[0].get_text()
            #print(evenDateTime)
            li["evenDateTime"] = evenDateTime
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
    #print(evenDateTime)
    #print(eventLink)
    #print(eventVenue)
    return lo

print(get_all_meetups())

