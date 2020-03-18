from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import username as user, password as pw
from info import name

class FaceBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Firefox()
        self.username = username
        self.driver.get("https://www.facebook.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"email\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"pass\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("//input[@type=\"submit\"]")\
            .click()
        sleep(4)

    # Already Logged
    def send_message(self):
        self.driver.find_element_by_xpath("//input[@class='_58al']")\
            .send_keys(name)
        sleep(4)
        self.driver.find_element_by_xpath("//input[@class='_58al']")\
            .send_keys(Keys.ENTER)
        sleep(3)

        elem = self.driver.switch_to.active_element
        elem.send_keys('Hey There!' + Keys.ENTER)

my_bot = FaceBot(user, pw)
my_bot.send_message()
