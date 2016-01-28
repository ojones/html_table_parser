# import urllib.request
import requests
from bs4 import BeautifulSoup as bs
from html_table_parser import parser_functions as parse
import pprint
pp = pprint.PrettyPrinter(indent=4, width=100)

__author__ = 'oswaldjones'
URL = 'https://apm.activecommunities.com/santamonicarecreation/Activity_Search'


def event_dict(name, first_date, number, category, days, time, location, open, action):

    event = dict()

    event['name'] = name.text
    event['first_date'] = first_date.text
    event['number'] = number.text
    event['category'] = category.text
    event['days'] = days.text
    event['time'] = time.text
    event['location'] = location.text
    event['open'] = open.text
    # url key is computed from href in name cell
    event['url'] = name.find('a').get('href')
    # action value is not interesting so we ignore
    # event['action'] = action.text

    return event


def fetch_html():

    html = ""

    page = requests.get(URL)
    html = page.content

    return html


if __name__ == '__main__':

    events = []

    soup = bs(fetch_html(), "html.parser")
    event_table = soup.find_all('table')[1]

    # using text_only false because we want soup cells in order to reference href attr
    twod = parse.make2d(event_table, text_only=False)

    for row in twod[2:]:
        # using event_dict to explicitly set custom column keys
        events.append(event_dict(*row))

    pp.pprint(events)





