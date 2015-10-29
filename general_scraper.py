import bs4
import re
import requests
import sys


class GeneralScraper:

    def __init__(self, url, web=True):
        self.url = url
        self.res = ''
        self.soup = ''

        web_agent =  ("Mozilla/5.0 (Macintosh Intel Mac OS X 10.11; rv:41.0) "
                      "Gecko/20100101 Firefox/41.0")
        mobile_agent = ("Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) "
                        "AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
        accepts = "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"

        if web:
            self.headers = {
                "User-Agent": web_agent,
                "Accept": accepts
            }
        else:
            self.headers = {
                "User-Agent": mobile_agent,
                "Accept": accepts
            }

        self.setup_scraper()

    def setup_scraper(self):
        self.url = GeneralScraper.processed_url(self.url)
        self.res = requests.get(self.url, headers=self.headers)
        self.soup = bs4.BeautifulSoup(self.res.text, 'html.parser')

    @staticmethod
    def processed_url(url):
        if re.match(r'^https?://.*', url):
            return url
        elif re.match(r'^www\..*', url):
            return 'http://{}'.format(url)
        else:
            print('Warning: your URL does not start with HTTP or WWW')
            return url


if __name__ == '__main__':
    global scraper
    if len(sys.argv) == 1:
        print('PLEASE RUN THE SCRIPT WITH THE FOLLOWING COMMAND:')
        print('='*60)
        print("python -i general_scraper.py 'http://www.example.com")
        print('='*60)
        print('exit() and try again.')
    else:
        try:
            # User entered this command: python -i general_scraper.py 'http://www.example.com'
            scraper = GeneralScraper(str(sys.argv[1]))
        except requests.exceptions.ConnectionError:
            print('='*60)
            print('Check your Connection or URL.')
            print('exit() and try again.')
        except requests.exceptions.MissingSchema:
            print('='*60)
            print('Check your URL.')
            print('exit() and try again.')
        else:
            print("scraper.res: {}".format(scraper.res))
            print("Use 'scraper.soup' to view the BeautifulSoup object and parse HTML")
