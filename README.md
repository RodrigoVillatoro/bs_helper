# Python BeautifulSoup Helper
Simple BeautifulSoup object creator for web scraping

The goal of this file is to quickly setup a scraper to understand how a webpage is organized. It uses the **_requests_** and **_bs4_** python modules. 

## How to use: 

For quick inspection:
1) For quick inspection, just run the following command:
```bash
python -i general_scraper.py 'http://www.example.com'
```

If you need to dive in or check multiple pages:
1) Import the module
```python
>>> from general_scraper import GeneralScraper
```

2) Make an instance of **GeneralScraper**, and assign the url that you want to scrape: 
```python
>>> scraper = GeneralScraper(''http://httpbin.org/get'')
```

3) The response is stored in the *res* attribute and the BeautifulSoup object is stored in the *soup* object. For example: 
```python
>>> scraper.res.ok
True
```

4) If you need to review another page, just update the url and call **setup_scraper()** again:
```python
>>> scraper.url = 'http://github.com'
>>> scraper.setup_scraper()
>>> scraper.soup.find('h1').string
'Where software is built'
```
