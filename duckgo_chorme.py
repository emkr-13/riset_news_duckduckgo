import json
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import psutil

# Start time measurement
start_time = time.time()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

links = []
driver = webdriver.Chrome()

url = 'https://duckduckgo.com/?q=jokowi+site%3Akompas.com&t=h_&df=2024-02-01..2024-02-01&ia=web'

driver.get(url)

time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'html.parser')

articles = soup.find_all('article', {'data-testid': 'result'})

for article in articles:
    link = article.find('a', {'data-testid': 'result-title-a'})
    if link:
        href = link.get('href')
        links.append(href)

# Print the number of links
print("Number of links:", len(links))

# Print the time taken
print("Time taken: %s seconds" % (time.time() - start_time))

# Get memory usage
process = psutil.Process()
print("Memory usage:", process.memory_info().rss / (1024 * 1024), "MB")

# Quit the driver
driver.quit()
