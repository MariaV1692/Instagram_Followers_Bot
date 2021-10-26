import os
import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("window-size=1400,1200")


class InstaFollower:
    INSTAGRAM_URL = "https://www.instagram.com/"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=os.environ["CHROME_DRIVER_PATH"], options=options)

    def login_to_instagram(self, email, password):
        self.driver.get(url=self.INSTAGRAM_URL)
        time.sleep(1)
        self.driver.find_element_by_css_selector("input[name='username']").send_keys(email)
        self.driver.find_element_by_css_selector("input[name='password']").send_keys(password)
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        time.sleep(4)

    def find_followers(self, account_to_find):
        xpath_search_input = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
        expected_condition = ExpectedConditions.element_to_be_clickable((By.XPATH, xpath_search_input))
        search_input = WebDriverWait(self.driver, 20).until(expected_condition)
        search_input.send_keys(account_to_find)
        time.sleep(2)
        self.driver.find_element_by_class_name("-qQT3").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(1)
        followers_number = int(self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header'
                                                                 '/section/ul/li[2]/a/span').get_attribute(
            "title").replace(",", ""))
        element_inside_popup = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for n in range(int(followers_number / 700)):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element_inside_popup)
            time.sleep(2)

    def follow(self):
        followers_list = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]'). \
            find_elements_by_tag_name("li")
        for follower in followers_list:
            try:
                follower.find_element_by_tag_name("button").click()
                time.sleep(2)
            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]').click()
