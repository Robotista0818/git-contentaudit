import logging
import requests
from bs4 import BeautifulSoup

def url_scraper(url):
    logging.info(f"Downloading the URL content");
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    body = soup.find('body')
    text_body = '\n'.join(line.strip() for line in body.get_text().split('\n') if line.strip())

    return text_body