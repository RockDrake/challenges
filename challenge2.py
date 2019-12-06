# import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")

def challenge2():
    driver = webdriver.Chrome("./chromedriver", options=options)
    driver.get("https://copart.com")
    element = driver.find_element_by_id("input-search")
    element.send_keys(('exotics'), Keys.ENTER)
    time.sleep(5)
    resultsTotal = len(driver.find_elements(By.XPATH, "//*[@id=\"serverSideDataTable\"]/tbody/tr//td[5]/span"))
    results = []
    porsche = 0
    for i in range(resultsTotal):
        result = driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]/tbody/tr[" + str(i + 1) + "]/td[5]/span")
        if result.text.upper() == "PORSCHE":
            porsche += 1
        results.append(result.text)
    print(results)

    print("Found Porsche " + str(porsche) + " times in the list.")
    driver.close()

challenge2()
