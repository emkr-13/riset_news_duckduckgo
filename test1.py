from playwright.sync_api import sync_playwright
import time

# Define the path where you want to store the profile
profile_directory = "~/custom_profile"

# Launch Playwright
with sync_playwright() as p:
    # Launch a browser context with a custom profile
    browser = p.chromium.launch_persistent_context(user_data_dir=profile_directory, headless=False)

    # Open a new page
    page = browser.new_page()

    # Navigate to a website to verify the profile is working
    page.goto("https://www.youtube.com/")

    time.sleep(600000)
    # Perform any actions with the page as needed

    # Close the browser

