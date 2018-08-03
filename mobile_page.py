from selenium.webdriver.common.by import By

from base import BaseAction

class Mobile_page(BaseAction):

    first_network_button = By.XPATH, "//*[contains(@text,'首选')]"
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def click_first_network(self):
        self.click(self.first_network_button)

    def click_2g(self):
        self.click(self.network_2g_button)

    def click_3g(self):
        self.click(self.network_3g_button)