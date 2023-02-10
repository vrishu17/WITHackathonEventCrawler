# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
# from models import Event

def get_all_meetups():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    url = 'https://www.meetup.com/women-who-code-mumbai/events/'
    # url = 'https://www.meetup.com/pune-developers-community/events/'
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
    l_eventTitle = []
    l_eventDesc = []
    l_evenDateTime = []
    l_eventType = []
    l_eventLink = []
    l_eventVenue = []
    lo = []
    counter = 0
    for item in soup.select('.card'):
        li = []
        #counter += 1
        #ll.append(counter)

        try:
            print('----------------------------------------')
            # print(item)
            eventTitle = item.select('.eventCardHead--title')[0].get_text()
            #print(eventTitle)
            #l_eventTitle.append(eventTitle)
            li.append(eventTitle)
        except Exception as e:
            # raise e
            eventTitle = ''

        try:
            eventDesc = item.select('.description-markdown--p')[0].get_text()
            #print(eventDesc)
            li.append(eventDesc)
        except Exception as e:
            # raise e
            eventDesc = ''

        try:
            eventType = item.select('.networkEventCardHead--title')[0].get_text()
            #print(eventType)
            li.append(eventType)
        except Exception as e:
            # raise e
            eventType = ''

        try:
            evenDateTime = item.select('.eventTimeDisplay-startDate')[0].get_text()
            #print(evenDateTime)
            li.append(evenDateTime)
        except Exception as e:
            # raise e
            eventType = ''

        try:
            eventLink = base_url + item.select('.eventCard--link')[0]['href']
            #print(eventLink)
            li.append(eventLink)
        except Exception as e:
            # raise e
            eventType = ''

        try:
            eventVenue = item.select('.venueDisplay')[0].get_text()
            #print(eventVenue)
            li.append(eventVenue)
        except Exception as e:
            # raise e
            eventType = ''

    lo.append(li)
    print(lo)
    #print(eventTitle)
        #print(eventDesc)
    #print(eventType)
    #print(evenDateTime)
    #print(eventLink)
    #print(eventVenue)
        #l_eventTitle.append(eventTitle)

    #event = l_eventTitle(eventTitle, eventDesc, eventVenue, 'city', evenDateTime, "time", "price", eventLink, eventType,
     #              'tech')
    #print(l_eventTitle)
    #print(l_eventTitle)

get_all_meetups()

