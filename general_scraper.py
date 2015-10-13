import bs4
import csv
import datetime
import os
import random
import requests
import time


class GeneralScraper:
    url = ''
    res = ''
    soup = ''
    directory = ''

    date_format = '%d_%b_%Y'
    today = datetime.datetime.today().strftime(date_format)

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:41.0) Gecko/20100101 Firefox/41.0",
        "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"
    }

    file_header = []  # First row of the csv file (table header)
    characters_to_remove = ['\n', ';', '"', '\r', '\t', '\xa0', '\x80']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def write_document(self, document_title, rows_to_write):
        """
        Helper function to write data to a csv file using the append option.
        :param document_title: The name we want the document to have.
        :type document_title: str
        :param rows_to_write: Data to be written to the file.
        :type rows_to_write: list
        """

        doc_name = '{}_{}.csv'.format(document_title, self.today)

        if self.directory:
            os.makedirs(self.directory, exist_ok=True)
            path_and_doc_name = os.path.join(self.directory, os.path.basename(doc_name))
        else:
            path_and_doc_name = doc_name

        with open(path_and_doc_name, 'a', newline='') as csvfile:
            my_writer = csv.writer(csvfile, delimiter='\n')
            my_writer.writerow(rows_to_write)

    def clean_string(self, string):
        """
        Will clean a string by removing unwanted characters.
        :param string: The string we want to clean.
        :type string: str
        :return: clean string
        """
        string = string.strip()
        for character in self.characters_to_remove:
            string = string.replace(character, '')
        return string

    def clean_string_list(self, data_list):
        """
        Will clean a list of string by removing unwanted characters.
        :param data_list: List of strings that have to be cleaned.
        :type data_list: list
        :return: tuple with clean strings
        """
        temp_list = []
        for item in data_list:
            self.clean_string(item)
            temp_list.append(item)
        return tuple(temp_list)

    def sleep_range_in_seconds(self, num1, num2):
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

    def setup_scraper(self):
        """
        Setups the scraper and saves the response and soup object to
        global variables that can later be referenced.
        """
        if self.url:
            self.res = requests.get(self.url, headers=self.headers)
            self.soup = bs4.BeautifulSoup(self.res.text, 'html.parser')
