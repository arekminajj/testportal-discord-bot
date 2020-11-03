from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def takeScreenshot(questionNumber):
    print("")
    #driver.save_screenshot('screenshots/screenshot' + str(questionNumber) + '.png')

async def getTest(url):
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    sleeptime = 5
    driver.get(url)

    firstName = driver.find_element_by_name("firstName")
    lastName = driver.find_element_by_name("lastName")
    Klasa_text = driver.find_element_by_name("Klasa_text")
    Nr_w_dzienniku_number = driver.find_element_by_name("Nr_w_dzienniku_number")

    firstName.send_keys("null")
    lastName.send_keys("null")
    Klasa_text.send_keys("null")
    Nr_w_dzienniku_number.send_keys("1")

    closeCookieAlertButton = driver.find_element_by_class_name("mdc-icon-button")
    closeCookieAlertButton.click()
    time.sleep(sleeptime)

    startButton = driver.find_element_by_id("start-form-submit")
    startButton.click()

    try:
        time.sleep(sleeptime)
        submitButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "mdc-button--outlined")))
        questions = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "question_header_content")))
        numberOfQuestions = int(questions.text[-1])
    finally:
        print("")

    driver.save_screenshot('screenshots/screenshot' + str(1) + '.png')

    submitButton.click()

    for x in range(numberOfQuestions-1):
        time.sleep(sleeptime)
        try:
            submitButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "mdc-button--outlined")))
            questions = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "question_header_content")))
        finally:
            print("") 
        driver.save_screenshot('screenshots/screenshot' + str(x+2) + '.png')
        submitButton.click()
    driver.quit()
    