from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Logup:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def logup_mobile(self, mobilenumber, pwd, pwd2, mobile2, verify='8888'):
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(mobilenumber)
        self.driver.find_element(By.XPATH, "//input[@name='verify_code']").send_keys(verify)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//input[@id='password2']").send_keys(pwd2)
        self.driver.find_element(By.XPATH, "//input[@name='invite']").send_keys(mobile2)
        self.driver.find_element(By.XPATH, "//a[text()='同意协议并注册']").click()
