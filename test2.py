import asyncio
import time
from pyppeteer import launch

async def main():
    # Define the path where you want to store the profile
    profile_directory = "/kit"

    # Launch Pyppeteer
    browser = await launch(
        headless=False,  # Set to True if you want to hide the browser window
        userDataDir=profile_directory  # Specify the profile directory
    )

    # Create a new page
    page = await browser.newPage()

    # Navigate to a website to verify the profile is working
    await page.goto("https://www.youtube.com/")

    # Perform any actions with the page as needed

    # Wait for 60 seconds (1 minute)
    await asyncio.sleep(600)

    # Close the browser
    await browser.close()

# Run the main function
asyncio.get_event_loop().run_until_complete(main())
