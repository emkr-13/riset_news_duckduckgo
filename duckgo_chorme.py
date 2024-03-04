import json
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import psutil

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

links = []
driver = webdriver.Chrome()

url = 'https://duckduckgo.com/?q=anies+site%3Akompas.com&t=h_&df=2024-02-02..2024-02-02&ia=web'

driver.get(url)

time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

articles = soup.find_all('article', {'data-testid': 'result'})

for article in articles:
    link = article.find('a', {'data-testid': 'result-title-a'})
    if link:
        href = link.get('href')
        links.append(href)

print(links)
