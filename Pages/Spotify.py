from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import Select
import pyautogui
from datetime import date


class Spotify:
    # para configurarlo pon el modo configuracion en True exactamente con la mayuscula y False si ya lo modificaste
    modoConfig = False
    # para cambiar la contrase;a de los correos modifica esta variable
    password = "Prueba12345!"
    # ---------- NO TOCAR Debajo de esto
    extension_path = './Extensiones/Buster.crx'
    urlSpotify = "https://open.spotify.com/"

    # - COMPROBando de que este registrado
    explorePremiumXpth = '/html/body/div[4]/div/div[2]/div[1]/header/button[1]/span'
    # ---- buttons
    btnSignupXpth = "/html/body/div[3]/div/div[2]/div[1]/header/div[5]/button[1]"
    btnSendMail = '/html/body/div[1]/main/div/main/section/div/div/form/button/span[1]'
    btnSendPassw = '/html/body/div[1]/main/div/main/section/div/div/section/form/div[2]/button/span[1]'
    btnSendBirthXpth = '/html/body/div[1]/main/div/main/section/div/div/section/form/div[2]/button'
    btnSendCaptchaXpth = '/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/button/span[1]'
    btnTermsXpth = '/html/body/div[1]/main/div/main/section/div/div/section/form/div[2]/button/span[1]'
    # ----- inputs
    inpMailXpth = '//*[@id="username"]'
    inpPasswordXpth = '//*[@id="new-password"]'
    inpName = '//*[@id="displayName"]'
    inpDay = '//*[@id="day"]'
    inpYear = '//*[@id="year"]'
    # ----- Select
    selectMonthXpth = '//*[@id="month"]'
    options = Options()
    # ----- Radio Button
    radioGenderXpth = '//*[@id="gender_option_prefer_not_to_say"]'
    termsButtonXpth1 = '//*[@id="checkbox-marketing"]'
    termsButtonXpth2 = '//*[@id="checkbox-privacy"]'
    # ----- Captcha
    btnCaptchaXpth = '/html/body/div[1]/div/div[2]/main/div/div/div/div/div/div/button/span[1]'

    def __init__(self):
        self.options.add_extension(self.extension_path)

    def sendMail(self, mail):
        driver = webdriver.Edge(options=self.options)
        driver.maximize_window()
        driver.get("https://open.spotify.com/")
        sleep(6)
        self.clickBtnByXpath(driver, self.btnSignupXpth)
        sleep(3)
        self.sendTxtByXpath(driver, self.inpMailXpth, mail)
        sleep(2)
        self.clickBtnByXpath(driver, self.btnSendMail)
        sleep(5)
        self.sendTxtByXpath(driver, self.inpPasswordXpth, self.password)
        sleep(3)
        self.clickBtnByXpath(driver, self.btnSendPassw)
        sleep(4)
        # --- Reactorizar
        select = Select(self.detectElementByXpath(
            driver, self.selectMonthXpth))
        select.select_by_index(4)
        sleep(1)
        # ------------------
        self.sendTxtByXpath(driver, self.inpDay, "8")
        sleep(1)
        self.sendTxtByXpath(driver, self.inpYear, "1980")
        sleep(1)
        self.sendTxtByXpath(driver, self.inpName, "Juanito alimaña")
        sleep(1)
        # -- Refactorizar
        element = self.detectElementByXpath(driver, self.radioGenderXpth)
        driver.execute_script("arguments[0].click();", element)
        sleep(3)
        element = self.detectElementByXpath(driver, self.btnSendBirthXpth)
        driver.execute_script("arguments[0].click();", element)
        sleep(4)
        element = self.detectElementByXpath(driver, self.termsButtonXpth1)
        driver.execute_script("arguments[0].click();", element)

        sleep(1.5)
        element = self.detectElementByXpath(driver, self.termsButtonXpth1)
        driver.execute_script("arguments[0].click();", element)
        sleep(2)
        element = self.detectElementByXpath(driver, self.btnTermsXpth)
        driver.execute_script("arguments[0].click();", element)
        sleep(14)

        # modo configuracion
        while self.modoConfig == True:
            print(pyautogui.position())
        # ----------- clicks
        while self.detectElementByXpath(driver, self.explorePremiumXpth) == None:
            sleep(4)
            # click en el primer captcha
            pyautogui.click(744, 522)
            sleep(5)
            # click en el segundo, "dibujito"
            pyautogui.click(967, 1020)
            sleep(7)
            # click en caso de que no se haya resuelto
            pyautogui.click(967, 700)
            sleep(6)
            try:
                element = self.detectElementByXpath(
                    driver, self.btnCaptchaXpth)
                driver.execute_script("arguments[0].click();", element)
            except:
                pass
            if self.detectElementByXpath(driver, self.explorePremiumXpth) == None:
                driver.refresh()
        self.WriteOutput(f"Correo: {mail} contraseña: {self.password}")

    def detectElementByXpath(self, driver, path):
        try:
            element = driver.find_element(By.XPATH, path)
            return element
        except NoSuchElementException:
            return None

    def sendTxtByXpath(self, driver, path, data):
        element = driver.find_element(By.XPATH, path)
        element.send_keys(data)

    def clickBtnByXpath(self, driver, path):
        element = driver.find_element(By.XPATH, path)
        element.click()

    # refactorizar y sacar fuera de la clase
    def WriteOutput(data):
        today = date.today()
        file = open(f"./output/{today}", "a")
        file.write("\n" + data)
        file.close()
