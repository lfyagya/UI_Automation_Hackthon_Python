
# from config.config import Config
from pom.leapfrogs import Leapfrogger
from tests.login import Login
import time

# test_config = Config()
test_login = Login()
leapfroggers = Leapfrogger()

class TestLeapfrog:

    def test_search_leapfrogs(self):
        driver = test_login.run()
        search_name = 'yagya'
        # time.sleep(50)
        leapfroggers.release_note(driver)
        leapfroggers.search_leapfrogger(driver, search_name)
        time.sleep(10)
    

