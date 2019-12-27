import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

webURL = "https://copart.com"

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver", options=options)

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get(webURL)
        self.assertIn("Auto Auction - Copart USA - Salvage Cars for Sale in Online Car Auctions", self.driver.title)

    def popularList(self):
        self.driver.get(webURL)
        popularSearches = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]/div[2]//li/a")
        for popularList in popularSearches:
            print(popularList.text + " - " + popularList.get_attribute('href'))


if __name__ == '__main__':
    unittest.main()
