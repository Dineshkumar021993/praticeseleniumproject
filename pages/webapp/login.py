import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    def __init__(self,driver):
        self.driver = driver
        self.username = (By.ID,"emailOrPhoneNum")
        self.password_locator = (By.XPATH, '//input[@id="password"]')
        self.login_button_locator = (By.ID, 'sign-in')


    def username_for_login(self):
        wait = WebDriverWait(self.driver, 10)
        username = wait.until(EC.presence_of_element_located(self.username))
        username.send_keys("thrinadharao@lotusinsights.in")

    def password_for_login(self):
        wait = WebDriverWait(self.driver, 10)
        password = wait.until(EC.presence_of_element_located(self.password_locator))
        password.send_keys("Dev@1234")

    def login(self):
        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(EC.presence_of_element_located(self.login_button_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(login_button).click().perform()
        time.sleep(10)