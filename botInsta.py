from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

class instaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        loginButton = driver.find_element_by_xpath("//input[@name='username']")
        loginButton.click()
        loginButton.clear()
        loginButton.send_keys(self.username)
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(8)
        self.seguir()

    def seguir(self):
        driver = self.driver
        driver.get('https://www.instagram.com/jadepicon/')
        time.sleep(5)
        followers = driver.find_element_by_xpath("//a[@href='/jadepicon/followers/']")
        followers.click()
        time.sleep(15)
        for i in range(1,100):
            buttonSeguir = driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
            buttonSeguir[i].click()
            time.sleep(3)

            
josevictormoreno_Bot = instaBot('josevictormoreno_', 'While04051751')
josevictormoreno_Bot.login()
