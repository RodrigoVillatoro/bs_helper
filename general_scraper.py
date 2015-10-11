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
        string = string.strip()
        for character in self.characters_to_remove:
            string = string.replace(character, '')
        return string

    def clean_string_list(self, data_list):
        temp_list = []
        for item in data_list:
            self.clean_string(item)
            temp_list.append(item)
        return tuple(temp_list)

    def sleep_range_in_seconds(self, num1, num2):
        random_seconds = random.randint(num1, num2)
        random_micro_seconds = random.randint(0, 9)
        wait_string = '{}.{}'.format(random_seconds, random_micro_seconds)
        time.sleep(float(wait_string))

    def setup_scraper(self):
        if self.url:
            self.res = requests.get(self.url, headers=self.headers)
            self.soup = bs4.BeautifulSoup(self.res.text, 'html.parser')
