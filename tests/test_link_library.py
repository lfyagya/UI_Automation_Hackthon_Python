from selenium import webdriver
from login import Login_page
from pom.events import events
from pom.link_library import Link_library
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_crud_link_library():
    driver = webdriver.Chrome()
    login = Login_page(driver)
    login.login_setup()
    link_library= Link_library(driver)
    link_library.navigate_leapfrogger()
    link_library.click_view_events()
    link_library.click_link_library_tab()
    link_library.click_add_new_category()
    link_library.enter_new_category("test category")
    link_library.add_close_category()
    success_message = link_library.link_library_added_success_message()
    assert success_message == "Category created successfully."