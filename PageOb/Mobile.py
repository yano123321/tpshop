from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tpshop.PageOb.login import Login


class Mobile():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_buycar(self):
        ele = self.driver.find_element(By.XPATH, "//li[@class='selected']//a")
        if ele:
            return ele.text
        else:
            return False
