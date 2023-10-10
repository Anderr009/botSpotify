from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random


class mailRandom:
    mailGeneratedXpth = "/html/body/div/div[2]/main/div/div[2]/div/div[1]/div[1]/div/span[1]"
    domainXpth = "/html/body/div/div[2]/main/div/div[2]/div/div[1]/div[1]/div/span[2]"
    page = "https://yopmail.com/es/email-generator"
    options = Options()
    def __init__(self) :
        self.options.add_argument('--headless') 
    def sendMail(self):
        driver = webdriver.Edge(options=self.options)
        driver.get(self.page)
        mail = f"{self.extractTxt(driver,self.mailGeneratedXpth)}@{self.extractTxt(driver,self.domainXpth)}"
        driver.close()
        return mail

    def extractTxt(self,driver,path):
        txt = driver.find_element(By.XPATH,path)
        return txt.text
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

#test area
mail = mailRandom()
print(mail.sendMail())