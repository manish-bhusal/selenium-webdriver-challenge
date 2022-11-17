from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# The following two lines of code solves 'browser closing immediately' type of problem.
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_driver_path = Service(
    "C:\Development\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(options=options, service=chrome_driver_path)
URL = "https://techstepacademy.com/trial-of-the-stones"
driver.maximize_window()
driver.get(URL)
input_first = driver.find_element(By.NAME, "r1Input")
input_first.send_keys("rock")
button_1 = driver.find_element(By.NAME, "r1Btn")
button_1.click()

first_ans_password = driver.find_element(
    By.CSS_SELECTOR, "#passwordBanner h4").text

input_2 = driver.find_element(By.NAME, "r2Input")
input_2.send_keys(first_ans_password)
button_2 = driver.find_element(By.NAME, "r2Butn")
button_2.click()

name_jessica = driver.find_element(
    By.XPATH, '//*[@id="block-05ea3afedc551e378bdc"]/div/div[3]/span/b').text
wealth_jessica = int(driver.find_element(
    By.XPATH, '//*[@id="block-05ea3afedc551e378bdc"]/div/div[3]/p').text)
name_bernard = driver.find_element(
    By.XPATH, '//*[@id="block-05ea3afedc551e378bdc"]/div/div[4]/span/b').text
wealth_bernard = int(driver.find_element(
    By.XPATH, '//*[@id="block-05ea3afedc551e378bdc"]/div/div[4]/p').text)

input_3 = driver.find_element(By.NAME, "r3Input")
if wealth_jessica > wealth_bernard:
    input_3.send_keys(name_jessica)
else:
    input_3.send_keys(name_bernard)

button_3 = driver.find_element(By.NAME, "r3Butn")
button_3.click()

check_ans_button = driver.find_element(By.NAME, "checkButn")
check_ans_button.click()
