import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Link_library():
    def __init__(self, driver):
         self.driver = driver
         self.view_events= (By.XPATH,'//a[text()="Events and Notices"]')
         self.link_library_tab = (By.XPATH,'//a[@href="/events-notices/link-library"]')
         self.add_new_category = ((By.XPATH,'//*[text()="Add new category"]'))
         self.category_name = ((By.XPATH,'//input[@placeholder="Write the name of the category"]'))
         self.add_close_new_category = ((By.XPATH,'//input[@placeholder="Add & close"]'))
         self.Success_message = ((By.CLASS_NAME,'lf-toast__message"]'))


    def navigate_leapfrogger(self):
        self.driver.get("https://qa.vyaguta.lftechnology.com.np/leapfroggers")

    def click_view_events(self):
        wait= WebDriverWait(self.driver,10)
        wait.until(EC.visibility_of_element_located(self.view_events))
        self.driver.find_element(*self.view_events).click()

    def click_link_library_tab(self):
        wait= WebDriverWait(self.driver,10)
        wait.until(EC.visibility_of_element_located(self.link_library_tab))
        self.driver.find_element(*self.link_library_tab).click()

    def click_add_new_category(self):
        wait= WebDriverWait(self.driver,10)
        wait.until(EC.visibility_of_element_located(self.add_new_category))
        self.driver.find_element(*self.add_new_category).click()
 
    def enter_new_category(self):
        wait= WebDriverWait(self.driver,10)
        wait.until(EC.visibility_of_element_located(self.category_name))
        self.driver.find_element(*self.category_name)

    def add_close_category(self):
        wait= WebDriverWait(self.driver,10)
        wait.until(EC.visibility_of_element_located(self.add_close_new_category))
        self.driver.find_element(*self.add_close_new_category).click()

    def link_library_added_success_message(self):
        wait= WebDriverWait(self.driver,10)
        wait.until(EC.visibility_of_element_located(self.Success_message))
        self.driver.find_element(*self.Success_message)