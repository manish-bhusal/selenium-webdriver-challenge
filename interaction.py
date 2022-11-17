from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys, ActionChains

chrome_driver_path = Service(
    "C:\Development\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
driver.maximize_window()
# ----------Keyboard Actions Start------------
URL = "https://www.facebook.com"
driver.get(URL)
driver.find_element(By.ID, "email").send_keys("manish@gmail.com")

act = ActionChains(driver)
# Long Form
# act.key_down(Keys.CONTROL).send_keys(
#     "a").key_up(Keys.CONTROL).perform()
# act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# act.send_keys(Keys.TAB).perform()
# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# act.send_keys(Keys.ENTER).perform()

# Short Form
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)\
    .key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL)\
    .send_keys(Keys.TAB)\
    .key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL)\
    .send_keys(Keys.ENTER).perform()

# ------------Keyboard Actions End----------------
