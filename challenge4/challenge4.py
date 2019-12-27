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



if __name__ == '__main__':
    unittest.main()