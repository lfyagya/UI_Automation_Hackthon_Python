
import requests
from dotenv import dotenv_values
from selenium.webdriver.common.by import By

class Login_page:
    def __init__(self,driver):
        self.webdriver= driver
        self.config = dotenv_values("config.env")

    def login_setup(self):
        params = {
            "clientId": self.config['client_id'],
            "token": self.config['token']
        }
        response = requests.get(self.config['authorization_url'], params=params).json()
        access_token = response['data']['accessToken']
        refresh_token = response['data']['refreshToken']

        driver=self.webdriver
        if access_token:
            driver.get(self.config['base_url'])
            cookie = [
                {
                    'name': 'accessToken',
                    'value': access_token,
                },
                {
                    'name': 'refreshToken',
                    'value': refresh_token,
                }
            ]
            for cookies in cookie:
                driver.add_cookie(cookies)
            driver.refresh()