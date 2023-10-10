from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random


class Spotify: 
    mailTemp = "pigrefufrawou-7386@yopmail.com"
    password = "Prueba12345!"
    def sendMail(self):
        driver = webdriver.Chrome()
        
    def detectElementByXpath(self, driver, path):
        try:
            driver.find_element(By.XPATH, path)
            return True
        except NoSuchElementException:
            return False

    def sendTxtByXpath(self, driver, path, data):
        element = driver.find_element(By.XPATH, path)
        element.send_keys(data)

    def clickBtnByXpath(self, driver, path):
        element = driver.find_element(By.XPATH, path)
        element.click()


spotify = Spotify()
spotify.sendMail()