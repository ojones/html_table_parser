from bs4 import BeautifulSoup as bs
from html_table_parser import parser_functions as parse
from html_table_parser.tests import test_html_table_parser as test
import pprint
pp = pprint.PrettyPrinter(indent=4, width=120)

__author__ = 'oswaldjones'


if __name__ == '__main__':

    soup = bs(test.mock_html_table(), "html.parser")
    test_table = soup.find('table')

    twod = parse.make2d(test_table)

    # print 2D array
    pp.pprint(twod)

    # print column data by col heading name (case insensitive)
    pp.pprint(parse.twod_col_data(twod, 'first name'))
    pp.pprint(parse.twod_col_data(twod, 'lAst naMe'))
    pp.pprint(parse.twod_col_data(twod, 'POINTS'))

    # row data begins on first row after col headings
    # so rowstart is 1
    pp.pprint(parse.make_dict(test_table, 1))






