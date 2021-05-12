import unittest

from selenium import webdriver

from tpshop.PageOb import Mobile
from tpshop.PageOb.index import Index


class TestLogin2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.tpshop.com')

    def tearDown(self) -> None:
        self.driver.close()

    def test_turn_mobile(self):
        Index(self.driver).buy_mobile()
        self.assertTrue(Mobile.Mobile(self.driver).add_buycar(),'手机城')

    def test_turn_mobile2(self):
        Index(self.driver).buy_mobile2()
        self.assertTrue(Mobile.Mobile(self.driver).add_buycar(), '手机城')