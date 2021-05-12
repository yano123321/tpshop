import unittest
from datetime import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tpshop.PageOb.index import Index


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.tpshop.com')

    def tearDown(self) -> None:
        self.driver.close()

    def test_login(self):
        Index(self.driver).login().login()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='安全退出']")))
        self.assertEqual(Index(self.driver).login_success(), '安全退出')

    def test_logup(self):
        Index(self.driver).logup().logup_mobile('18800411115', '191192', '191192', '18800411164')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='安全退出']")))
        self.assertEqual(Index(self.driver).login_success(), '安全退出')



