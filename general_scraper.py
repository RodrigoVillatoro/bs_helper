import bs4
import re
import requests
import sys


class GeneralScraper:

    def __init__(self, url, web=True):
        web_agent =  ("Mozilla/5.0 (Macintosh Intel Mac OS X 10.11; rv:41.0) "
                      "Gecko/20100101 Firefox/41.0")
        mobile_agent = ("Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) "
                        "AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
        accepts = "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"

        self.url = GeneralScraper.processed_url(url)
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


def main():
    if len(sys.argv) == 1:
        print('PLEASE RUN THE SCRIPT WITH THE FOLLOWING COMMAND:')
        print('='*60)
        print("python -i general_scraper.py 'http://www.example.com")
        print('='*60)
    else:
        try:
            # User entered this command: python -i general_scraper.py 'http://www.example.com'
            scraper = GeneralScraper(str(sys.argv[1]))
        except ConnectionError:
            print('='*60)
            sys.exit("Something went wrong. Check URL, connectivity, etc.")
        else:
            print("scraper.res: {}".format(scraper.res))
            print("Use 'scraper.soup' to view the BeautifulSoup object and parse HTML")


if __name__ == '__main__':
    main()
    # if len(sys.argv) == 1:
    #     print('\n')
    #     print('PLEASE RUN THE SCRIPT WITH THE FOLLOWING COMMAND:')
    #     print('='*60)
    #     print("python -i general_scraper.py 'http://www.example.com")
    #     print('='*60)
    #     print('\n')
    #     sys.exit()
    # else:
    #     try:
    #         # User entered this command: python -i general_scraper.py 'http://www.example.com'
    #         scraper = GeneralScraper(str(sys.argv[1]))
    #     except ConnectionError:
    #         print('\n')
    #         print('='*60)
    #         sys.exit("Something went wrong. Check URL, connectivity, etc.")
    #     else:
    #         print("Use 'res' to view the response")
    #         print("Use 'soup' to view the BeautifulSoup object and parse HTML")
