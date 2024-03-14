from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
# Set up proxy
proxy_ip = "103.155.116.239"
proxy_port = "8085"

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = f"{proxy_ip}:{proxy_port}"
proxy.ssl_proxy = f"{proxy_ip}:{proxy_port}"

# Create a new instance of the Chrome driver using the desired proxy
options = webdriver.ChromeOptions()
options.add_argument(f"--proxy-server={proxy.http_proxy}")

driver = webdriver.Chrome(options=options)

# Now you can use the driver as usual
driver.get("https://www.youtube.com/")

time.sleep(1000)

# Remember to close the driver when done
driver.quit()
