from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tpshop.PageOb import logup, login
from tpshop.PageOb.Mobile import Mobile


class Index:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self):
        self.driver.find_element(By.XPATH, "//div//a[@class='red']").click()
        return login.Login(self.driver)

    def logup(self):
        self.driver.find_element(By.XPATH, "//a[text()='注册']").click()
        return logup.Logup(self.driver)

    def login_success(self):
        flag = self.driver.find_element(By.XPATH, "//a[text()='安全退出']")
        if flag:
            return flag.text
        else:
            raise

    def buy_mobile(self):
        self.driver.find_element(By.XPATH, "//a[text()='手机城']").click()

    def buy_mobile2(self):
        self.driver.find_element(By.XPATH, "//a[text()='手机']").click()
