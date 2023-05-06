from sitewisecrawlers import AllMeetups
from constants import sitenames

# Read URLs from constants
def read_urls():
    with open('constants/urls.constant', 'r') as f:
        urls = [convert_to_dict(url.strip().split(' :: ')) for url in f.readlines() if url[0]!='#']
    return urls

# Utility function to convert list to dict
def convert_to_dict(lst):
    res_dct = {lst[0] : lst[1]}
    return res_dct

# tech events list
def get_all_tech_meetups():
    all_tech_events = []
    for i in read_urls():
        for k, v in i.items():
            if k == 'tech' and v.startswith(sitenames.meetup):
                all_tech_events.extend(AllMeetups.get_all_meetups_from_one_url(v))
    return all_tech_events

# sports events list
def get_all_sports_meetups():
    all_tech_events = []
    for i in read_urls():
        for k, v in i.items():
            if k == 'sports' and v.startswith(sitenames.meetup):
                all_tech_events.extend(AllMeetups.get_all_meetups_from_one_url(v))
    return all_tech_events

# all events list 
def get_all_meetups():
    all_events = get_all_tech_meetups() + get_all_sports_meetups()
    # print(all_events)
    all_events = sorted(all_events, key=lambda d: d['datetimeobj'])  #, reverse=True
    return all_events[0:2]

def get_all():
    return get_all_meetups()

def get_all_techs():
    return get_all_tech_meetups()

def get_all_sports():
    return get_all_sports_meetups()

# print(get_all())
