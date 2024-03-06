from selenium import webdriver

# Set the path where you want to store the profile
profile_directory = "../../lat_python/riset_news_duckduckgo/cek"

# Set Chrome options to specify the profile directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=" + profile_directory)

# Launch Chrome with the specified profile
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://github.com/emkr-13/scraping-berita-indo")
