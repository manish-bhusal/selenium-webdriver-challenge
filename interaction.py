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
# URL = "https://www.facebook.com"
URL = "https://selenium.dev/selenium/web/mouse_interaction.html"
driver.get(URL)
# driver.find_element(By.ID, "email").send_keys("manish@gmail.com")

act = ActionChains(driver)
# Long Form
# act.key_down(Keys.CONTROL).send_keys(
#     "a").key_up(Keys.CONTROL).perform()
# act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# act.send_keys(Keys.TAB).perform()
# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# act.send_keys(Keys.ENTER).perform()

# Short Form
# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)\
#     .key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL)\
#     .send_keys(Keys.TAB)\
#     .key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL)\
#     .send_keys(Keys.ENTER).perform()

# ------------Keyboard Actions End----------------

# -----------Copy Paste--------------
# act.key_down(Keys.CONTROL).key_down(
#     Keys.SHIFT).send_keys(Keys.ARROW_LEFT).send_keys(Keys.ARROW_LEFT).perform()

# ---------Mouse Actions Start---------------
# clickable = driver.find_element(By.ID, "clickable")
# clickable = driver.find_element(By.ID, "click")
#Click and Hold
# act.click_and_hold(clickable).perform()
# Click(Left Click)
# act.click(clickable).perform()
# Right Click
# act.context_click(clickable).perform()

# Double Click
# act.double_click(clickable).perform()

# Hovering
# hoverable = driver.find_element(By.ID, "hover")
# act.move_to_element(hoverable).perform()

# Drag and Drop
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")
act.drag_and_drop(draggable, droppable).perform()

# -----------Mouse Actions End----------
