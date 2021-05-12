from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Login:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self):
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys('18800411164')
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys('191192')
        self.driver.find_element(By.XPATH, "//input[@id='verify_code']").send_keys('8888')
        self.driver.find_element(By.XPATH, "//a[@name='sbtbutton']").click()
