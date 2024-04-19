from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class teams():
    def __init__(self, driver):
        self.driver = driver
        self.release_note = (By.CLASS_NAME, 'releaseNote_module_releaseNoteModal__header_Close__7943ddf4')
        #Locator to navigate to teams page
        self.teams_navbar = (By.XPATH, '//div[@class="nav_module_nav__37ad822e flex-fix"]/div[@class="navLink_module_nav__node__92c07ff2"]/a[@class="navLink_module_nav__link__92c07ff2" and @href="/teams"]')
        #Locator to add project
        self.add_project_button = (By.XPATH, '//button[@class="btn btn--primary"]')
        #Locator of add project page 1
        self.project_name_textfield = (By.XPATH, '//input[@placeholder="Enter Project Name"]')
        self.category_dropdown = (By.XPATH, '//div[@id="react-select-2-placeholder"]')
        self.status_dropdown = (By.XPATH, '//div[@id="react-select-3-placeholder"]')
        self.industry_dropdown = (By.XPATH, '//div[@id="react-select-4-placeholder"]')
        self.account_manager_input = (By.XPATH, '//input[@id="react-select-5-input"]')
        self.relation_manager_input = (By.XPATH, '//input[@id="react-select-6-input"]')
        self.project_leader_input = (By.XPATH, '//input[@id="react-select-7-input"]')
        self.work_shift_dropdown = (By.XPATH, '//div[@id="react-select-8-placeholder"]')
        self.team_model_dropdown = (By.XPATH, 'react-select-9-placeholder')
        self.project_description_textarea = (By.XPATH, '//body[@data-mce-placeholder="Add Project Description Here"]')
        self.business_goal_textarea = (By.XPATH, '//body[@data-mce-placeholder="Add Business Goal Here"]')
        self.next_button = (By.XPATH, '//button[@type="submit" and contains(text(), "Next")]')
        #Locator of add project page 2
        self.add_button = (By.XPATH, '//button[@type="submit" and contains(text(), "Add Project")]')

        #Locator of search project
        self.search_project_input = (By.XPATH, '//input[@placeholder="Search by project name"]')
        self.teams_apply_filter_button = (By.XPATH, '//button[@type="button" and contains(text(), "Apply Filter")]')
        #Add locator to find the project
        #Locator of edit
        self.edit_button = (By.XPATH, '//span[@class="edit-text"]')
        #Locator of status new
        self.status_dropdown = (By.XPATH, '//input[@id="react-select-13-input"]')
        # Locator of add project page 2
        self.next_button = (By.XPATH, '//button[@type="submit" and contains(text(), "Save")]')


    def close_release_note(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.release_note))
        self.driver.find_element(*self.release_note).click()

    def click_teams(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.teams_navbar))
        self.driver.find_element(*self.teams_navbar).click()

    def click_add_project(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.add_project_button))
        self.driver.find_element(*self.add_project_button).click()

    def enter_project_name(self, pname):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.project_name_textfield))
        self.driver.find_element(*self.project_name_textfield).send_keys(pname)

    def select_category(self, category):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.category_dropdown))
        dropdown = Select(self.driver.find_element(*self.category_dropdown))
        dropdown.select_by_visible_text(category)

    def select_status(self, status):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.status_dropdown))
        dropdown = Select(self.driver.find_element(*self.status_dropdown))
        dropdown.select_by_visible_text(status)

    def select_industry(self, industry):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.industry_dropdown))
        dropdown = Select(self.driver.find_element(*self.industry_dropdown))
        dropdown.select_by_visible_text(industry)

    def add_account_manager(self, am):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.account_manager_input))
        self.driver.find_element(*self.account_manager_input).send_keys(am)
        dropdown = Select(self.driver.find_element(*self.account_manager_input))
        dropdown.select_by_visible_text(am)

    def add_relation_manager(self, rm):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.relation_manager_input))
        self.driver.find_element(*self.relation_manager_input).send_keys(rm)
        dropdown = Select(self.driver.find_element(*self.relation_manager_input))
        dropdown.select_by_visible_text(rm)

    def add_project_leader(self, pl):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.project_leader_input))
        self.driver.find_element(*self.project_leader_input).send_keys(pl)
        dropdown = Select(self.driver.find_element(*self.project_leader_input))
        dropdown.select_by_visible_text(pl)

    def select_shift(self, shift):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.work_shift_dropdown))
        dropdown = Select(self.driver.find_element(*self.work_shift_dropdown))
        dropdown.select_by_visible_text(shift)

    def select_team_model(self, model):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.team_model_dropdown))
        dropdown = Select(self.driver.find_element(*self.team_model_dropdown))
        dropdown.select_by_visible_text(model)

    def enter_project_description(self, desc):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.project_description_textarea))
        self.driver.find_element(*self.project_name_textfield).send_keys(desc)


    def enter_business_goal(self, desc2):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.business_goal_textarea))
        self.driver.find_element(*self.project_name_textfield).send_keys(desc2)


    def click_next(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.next_button))
        self.driver.find_element(*self.next_button).click()

    def click_add(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.add_button))
        self.driver.find_element(*self.add_button).click()


    def enter_project_name_search(self, project):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.search_project_input))
        self.driver.find_element(*self.search_project_input).send_keys(project)


    def click_apply_filter(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.teams_apply_filter_button))
        self.driver.find_element(*self.teams_apply_filter_button).click()