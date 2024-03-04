import json
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import psutil

# Start time measurement
import time
start_time = time.time()

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        page = await browser.new_page()
        await page.goto('https://duckduckgo.com/?q=jokowi+site%3Akompas.com&t=h_&df=2024-02-01..2024-02-01&ia=web')
        await page.wait_for_load_state('networkidle')

        # Get the page content
        page_content = await page.content()

        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(page_content, 'html.parser')

        links = []
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

        await browser.close()

asyncio.run(main())
