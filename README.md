# Python-Scraper
Web scraper made with Python

The goal of this file is to quickly setup a scraper to understand how a webpage is organized. It uses the **_requests_** and **_bs4_** python modules. 

## How to use: 

1) Import the **GeneralScraper** class:
```python
>>> from general_scraper import GeneralScraper
```

2) Make an instance of **GeneralScraper**, and assign the url that you want to scraper: 
```python
>>> scraper = GeneralScraper()
>>> scraper.url = 'http://httpbin.org/get'
```

3) Call the setup_scraper() method. This sets makes a get request and sets up BeautifulSoup. 
```python
>>> scraper.setup_scraper()
```

4) The response is stored in the *res* attribute and the BeautifulSoup object is stored in the *soup* object. For example: 
```python
>>> scraper.res.ok
True
```

If you need to review another page, just update the url and call **setup_scraper()** again:
```python
>>> scraper.url = 'http://github.com'
>>> scraper.setup_scraper()
>>> scraper.soup.find('h1').string
'Where software is built'
```
