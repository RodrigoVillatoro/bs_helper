import bs4
import csv
import datetime
import os
import random
import requests
import sys
import time

res = ''
soup = ''
directory = ''
characters_to_remove = ['\n', ';', '"', '\r', '\t', '\xa0', '\x80']


class GeneralScraper:
    url = ''

    date_format = '%d_%b_%Y'
    today = datetime.datetime.today().strftime(date_format)

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:41.0) Gecko/20100101 Firefox/41.0",
        "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"
    }

    file_header = []  # First row of the csv file (table header)

    def __init__(self, url):
        self.url = url
        self.setup_scraper()

    def write_document(self, document_title, rows_to_write):
        """
        Helper function to write data to a csv file using the append option.
        :param document_title: The name we want the document to have.
        :type document_title: str
        :param rows_to_write: Data to be written to the file.
        :type rows_to_write: list
        """
        global directory
        doc_name = '{}_{}.csv'.format(document_title, self.today)

        if directory:
            os.makedirs(directory, exist_ok=True)
            path_and_doc_name = os.path.join(directory, os.path.basename(doc_name))
        else:
            path_and_doc_name = doc_name

        with open(path_and_doc_name, 'a', newline='') as csvfile:
            my_writer = csv.writer(csvfile, delimiter='\n')
            my_writer.writerow(rows_to_write)

    def setup_scraper(self):
        """
        Setups the scraper and saves the response and soup object to
        global variables that can later be referenced.
        """
        global res
        global soup

        if self.url:
            res = requests.get(self.url, headers=self.headers)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')


def clean_string(string):
    """
    Will clean a string by removing unwanted characters.
    :param string: The string we want to clean.
    :type string: str
    :return: string without unwanted characters.
    """
    global characters_to_remove
    string = string.strip()

    for character in characters_to_remove:
        string = string.replace(character, '')
    return string


def clean_string_list(data_list):
    """
    Will clean a list of strings by removing unwanted characters.
    :param data_list: List of strings that have to be cleaned.
    :type data_list: list
    :return: tuple with strings without unwanted characters.
    """
    temp_list = list(map(clean_string, data_list))
    return tuple(temp_list)


def sleep_range_in_seconds(num1, num2):
    """
    Will make the program wait for random number of seconds within
    the specified range.
    :param num1: Lower limit in seconds
    :type num1: int
    :param num2: Upper limit in seconds
    :type num2: int
    """
    random_seconds = random.randint(num1, num2)
    random_micro_seconds = random.randint(0, 9)
    wait_string = '{}.{}'.format(random_seconds, random_micro_seconds)
    time.sleep(float(wait_string))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('\n')
        print('PLEASE RUN THE SCRIPT WITH THE FOLLOWING COMMAND:')
        print('='*60)
        print("python -i general_scraper.py 'http://www.example.com'")
        print('='*60)
        print('\n')
    else:
        try:
            # User entered this command: python -i general_scraper.py 'http://www.example.com'
            scraper = GeneralScraper(str(sys.argv[1]))
        except ConnectionError:
            print('\n')
            print('='*60)
            sys.exit("Something went wrong. Check URL, connectivity, etc.")
        else:
            print("Use 'res' to view the response")
            print("Use 'soup' to view the BeautifulSoup object and parse HTML")
