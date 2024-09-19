from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def highest_checker(store):
    a = []
    for i in range(len(store)):
        if "grayed" not in store[i].get_attribute('class'):
            a.append(store[i])
    return a


WEBSITE_URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(WEBSITE_URL)  

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5
stop = time.time() + 5 * 60
while time.time() < stop:
    cookie.click()

    if time.time() > timeout:
        # getting value of the money we have from the website and turn it into int
        money_selenium = driver.find_element(By.ID, "money")
        money = int(money_selenium.text.replace(',', ''))

        # make a list of prices of all the items in the store and turn into int by removing commas and also
        # seperating words from it
        store_div = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        store_limit_list = [(s.text.split(" ")[-1]) for s in store_div if s.text != ""]
        store_price = [int(i.replace(',', '')) for i in
                       store_limit_list]  # getting the price for the items in the store

        # the div where you click the items in order to purchase them
        store_class = driver.find_elements(By.CSS_SELECTOR, "#store div")

        # using the function in order to get the list of usable items 
        unlocked = highest_checker(store_class)
        # as the list of usable items we get are in ascending order I use the last items here as it will be the most
        # expensive one
        unlocked[-1].click()

        timeout = time.time() + 5

# driver.quit()
