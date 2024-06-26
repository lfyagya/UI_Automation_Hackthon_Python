import time
from selenium import webdriver
from login import Login_page
from POM.add_project import teams
from POM.events import events
from POM.leapfroggers import Leapfroggers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestProject:

    def test_add_project(self):
        driver = webdriver.Chrome()
        login = Login_page(driver)
        login.login_setup()
        Teams = teams(driver)
        Teams.click_teams()
        pname = 'Selenium Heroes'
        category = 'Services'
        status = 'Lead'
        industry = 'Data'
        am = 'Cal Vokins'
        rm = 'Cal Vokins'
        pl = 'Cal Vokins'
        shift = 'Day Shift'
        model = 'Augmented Team'
        desc = 'This is generated by selenium'
        desc2 = 'The goal is to learn'
        # time.sleep(50)
        Teams.click_add_project()
        Teams.enter_project_name(pname)
        Teams.select_category(category)
        Teams.select_status(status)
        Teams.select_industry(industry)
        Teams.add_account_manager(am)
        Teams.add_relation_manager(rm)
        Teams.add_project_leader(pl)
        Teams.select_shift(shift)
        Teams.select_team_model(model)
        Teams.enter_project_description(desc)
        Teams.enter_business_goal(desc2)
        Teams.click_next()
        Teams.click_add()
        time.sleep(10)