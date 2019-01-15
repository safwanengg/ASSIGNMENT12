# Dependencies
import os
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
 
    news = {}
    # URL of page to be scraped
    url1 = 'https://mars.nasa.gov/news/'
    # Retrieve page with the requests module
    response = requests.get(url1)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup1 = bs(response.text, 'html.parser')
    # results are returned as an iterable list
    result = soup1.find('div', class_="content_title")
    news_title = result.a.text
    results = soup1.find('div', class_="rollover_description_inner")
    news_p = results.text   
    news["title"] = news_title
    news["body"] = news_p
    url2 = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url2)
    soup2 = bs(response.text, 'html.parser')
    result1 = soup2.find('div', class_="js-tweet-text-container")
    news["weather"] = result1.p.text
    url3 = 'http://space-facts.com/mars/'
    tables = pd.read_html(url3)
    df = tables[0]
    df.columns = ['Profile Parameter', 'Data']
    df.to_html('table.html')
    return news
