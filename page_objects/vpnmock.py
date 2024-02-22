from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



# Create an Options object
op = Options()

# Set the .crx file path of the extension using raw string (prefix with r)
op.add_extension(r'C:\Users\Nerwadi.Shashikala\PycharmProjects\pythonProject4\ModHeader - Modify HTTP headers 6.0.2.0.crx')

# Set the path to the chromedriver executable
chromedriver_path = r'C:\Users\Nerwadi.Shashikala\PycharmProjects\driverss\chromedriver-win32\chromedriver'

# Update to use the ChromeOptions class directly
op.add_argument("executable_path=" + chromedriver_path)

op.add_argument("--auto-open-devtools-for-tabs")

extension_url = "chrome-extension://idgpnmonknjnojddfkpgkljpfnnfcklj/popup.html"








# Create a Chrome webdriver object
driver = webdriver.Chrome(options=op)

# Maximize the window
driver.maximize_window()

# Launch the browser and navigate to a website
driver.get("https://www.dazn.com/en-IN/welcome")
driver.get(extension_url)
driver.switch_to.window(driver.window_handles[0])



# Locate the fields
#name_input = '//input[@name="header-name" and @placeholder="Name"]'
#value_input = '//input[@name="header-value" and @placeholder="Value"]'



name_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@name="header-name" and @placeholder="Name"]'))
)
name_input.send_keys("X-Forwarded-For")

value_input = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@name="header-value" and @placeholder="Value"]'))
)
# Input values into the fields
value_input.send_keys("92.251.255.11")
sleep(60)




