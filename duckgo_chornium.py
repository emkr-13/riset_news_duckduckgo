import asyncio
import json
import psutil
from bs4 import BeautifulSoup
from pyppeteer import launch
import time

# Start time measurement
start_time = time.time()

links = []

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    
    url = 'https://duckduckgo.com/?q=jokowi+site%3Akompas.com&t=h_&df=2024-02-01..2024-02-01&ia=web'
    await page.goto(url)
    
    # Wait for page content to load
    await page.waitForSelector('article[data-testid="result"]')
    
    # Get page content
    page_content = await page.content()
    
    soup = BeautifulSoup(page_content, 'html.parser')
    
    articles = soup.find_all('article', {'data-testid': 'result'})
    
    for article in articles:
        link = article.find('a', {'data-testid': 'result-title-a'})
        if link:
            href = link.get('href')
            links.append(href)
    
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

# Print the number of links
print("Number of links:", len(links))

# Print the time taken
print("Time taken: %s seconds" % (time.time() - start_time))

# Get memory usage
process = psutil.Process()
print("Memory usage:", process.memory_info().rss / (1024 * 1024), "MB")
