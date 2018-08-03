from selenium.webdriver.common.by import By

from base import BaseAction


class MorePage(BaseAction):

    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"


    def click_more(self):
        self.click(self.more_button)

    def click_mobile_network(self):
        self.click(self.mobile_network_button)
