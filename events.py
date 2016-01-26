import urllib.request
from bs4 import BeautifulSoup as bs
import html_table_parser as parser
import ssl

__author__ = 'oswaldjones'
URL = 'https://apm.activecommunities.com/santamonicarecreation/Activity_Search'


def event_list():

    events = []

    soup = bs(fetch_html(), "html.parser")
    event_table = soup.find_all('table')[1]

    twod = parser.make2d(event_table)

    for row in twod[2:]:
        events.append(event(*row))

    return events


def event(name, first_date, number, category, days, time, location, open, action):

    event = dict()

    event['name'] = name.text
    event['first_date'] = first_date.text
    event['number'] = number.text
    event['category'] = category.text
    event['days'] = days.text
    event['time'] = time.text
    event['location'] = location.text
    event['open'] = open.text
    # event['action'] = action.text
    event['url'] = name.find('a').get('href')

    return event


def fetch_html():

    html = ""

    # bypass ssl cert error
    context = ssl._create_unverified_context()

    with urllib.request.urlopen(URL, context=context) as response:
       html = response.read()

    return html


if __name__ == '__main__':

    import pprint
    pp = pprint.PrettyPrinter(indent=4, width=100)

    pp.pprint(event_list())





