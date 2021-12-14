#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


event_list = []
event_no = 0
source_urls = { 'Pitt Academic Calendar': 'https://calendar.pitt.edu/calendar',
                'Pitt Academic Calendar- Engineering': 'https://calendar.pitt.edu/engineering',
                'Pitt Academic Calendar-2021/1': 'https://calendar.pitt.edu/calendar/month/2021/1',
                'Pitt Academic Calendar-2021/2': 'https://calendar.pitt.edu/calendar/month/2021/2',
                'Pitt Academic Calendar-2021/3': 'https://calendar.pitt.edu/calendar/month/2021/3',
                'Pitt Academic Calendar-2021/4': 'https://calendar.pitt.edu/calendar/month/2021/4',
                'Pitt Academic Calendar-2021/5': 'https://calendar.pitt.edu/calendar/month/2021/5',
                'Pitt Academic Calendar-2021/6': 'https://calendar.pitt.edu/calendar/month/2021/6',
                'Pitt Academic Calendar-2021/7': 'https://calendar.pitt.edu/calendar/month/2021/7',
                'Pitt Academic Calendar-2021/8': 'https://calendar.pitt.edu/calendar/month/2021/8',
                'Pitt Academic Calendar-2021/9': 'https://calendar.pitt.edu/calendar/month/2021/9',
                'Pitt Academic Calendar-2021/10': 'https://calendar.pitt.edu/calendar/month/2021/10',
                'Pitt Academic Calendar-2021/11': 'https://calendar.pitt.edu/calendar/month/2021/11',
                'Pitt Academic Calendar-2021/12': 'https://calendar.pitt.edu/calendar/month/2021/12',
                'Pitt Academic Calendar-2022/1':   'https://calendar.pitt.edu/calendar/month/2022/1',
                'Pitt Academic Calendar-2022/2':   'https://calendar.pitt.edu/calendar/month/2022/2',
                'Pitt Academic Calendar-2022/3':   'https://calendar.pitt.edu/calendar/month/2022/3',
                'Pitt Academic Calendar-2022/4':  'https://calendar.pitt.edu/calendar/month/2022/4',
                'Pitt Academic Calendar-2022/5':  'https://calendar.pitt.edu/calendar/month/2022/5',
                'Pitt Academic Calendar-2022/6':  'https://calendar.pitt.edu/calendar/month/2022/6',
                'Pitt Academic Calendar-2022/7':  'https://calendar.pitt.edu/calendar/month/2022/7',
                'Pitt Academic Calendar-2022/8':  'https://calendar.pitt.edu/calendar/month/2022/8',
                'Pitt Academic Calendar-2022/9':  'https://calendar.pitt.edu/calendar/month/2022/9',
                'Pitt Academic Calendar-2022/10':  'https://calendar.pitt.edu/calendar/month/2022/10',
                'Pitt Academic Calendar-2022/11':  'https://calendar.pitt.edu/calendar/month/2022/11',
                'Pitt Academic Calendar-2022/12':  'https://calendar.pitt.edu/calendar/month/2022/12',
                'Pitt Academic Calendar- Arts and Sciences': 'https://calendar.pitt.edu/arts-and-sciences',
                'Pitt Academic Calendar- School of Computing and Information': 'https://calendar.pitt.edu/school_of_computing_and_information/calendar'}

title_set = set()

for source, url in source_urls.items():
    with urlopen(url) as response:
        soup = BeautifulSoup(response, 'html.parser')

    for event in soup.find_all('div', class_='item event_item vevent'):
        for heading in event.find_all('div', class_='item_content_medium'):
            title = heading.find('a').get_text().strip()
            link = heading.find('a').get('href').strip()
            if title not in title_set:
                eventDetails = {}
                event_no += 1
                eventDetails['id'] = event_no
                eventDetails['title'] = title
                eventDetails['link'] = link
                title_set.add(title)
                eventDetails['recurring'] = heading.find('div', id='recurringmessage').get_text().strip()
                content = heading.find('div', class_='item_separator')
                eventDetails['description'] = content.find('h4', class_='description').get_text().strip()
                event_info = heading.find('div', class_='event_info').find('div', class_='actionbar grid_container')
                eventDetails['date'] = event_info.find('div', class_='dateright grid_12').find('abbr', class_='dtstart').get_text().strip()
                location = event_info.find('div', class_='location grid_12')
                if location == None:
                    eventDetails['location'] = 'Virtual Event'
                else:
                    eventDetails['location'] = location.get_text().strip()
                eventDetails['source'] = source
                event_list.append(eventDetails)

print(event_list)
with open('data.json', 'w') as outfile:
    json.dump(event_list, outfile)













