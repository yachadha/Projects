import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


print("Auto GIRM upload program for San Martin c/r")
passw = input("Enter your CRM password - ")

tickets = os.listdir(r"C:\Users\sanmartin\Pictures\Auto upload")
i=1
print(tickets)
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)
driver.get('http://crpprda3.igl.co.in:8010/sap(bD1lbiZjPTMwMCZkPW1pbg==)/bc/bsp/sap/crm_ui_start/default.htm')
try:
    element_present = EC.presence_of_element_located((By.NAME, 'sap-user'))
    WebDriverWait(driver, 15).until(element_present)
    elem = driver.find_element(By.NAME, 'sap-user')
    elem.clear()
    elem.send_keys('cjitender670')
    password = driver.find_element(By.NAME, 'sap-password').send_keys(passw) #feb@2022
    login = driver.find_element(By.LINK_TEXT, 'Log On').click()
    time.sleep(1)
    onm = driver.find_element(By.ID, 'ZOPERTIONREP50005474').click()
    time.sleep(2)
except NoSuchElementException:
    driver.find_element(By.ID, "SESSION_QUERY_CONTINUE_BUTTON").click()
    time.sleep(1.6)
    onm = driver.find_element(By.ID, 'ZOPERTIONREP50005474').click()
finally:
    time.sleep(2)
    driver.switch_to.frame('CRMApplicationFrame')
    driver.switch_to.frame('WorkAreaFrame1')
    for GIRM in tickets:
        print("Code has run {} times".format(i))
        driver.find_element(By.ID, "C4_W16_V17_ZIGL-SRV").click()
        element_present = EC.presence_of_element_located((By.XPATH, "//input[@id='C15_W50_V51_V52_search_parameters[1].VALUE1']"))
        WebDriverWait(driver, 25).until(element_present)
        driver.find_element(By.XPATH, "//input[@id='C15_W50_V51_V52_search_parameters[1].VALUE1']").clear()
        element_present = EC.presence_of_element_located((By.XPATH, "//input[@id='C15_W50_V51_V52_search_parameters[12].VALUE1']"))
        WebDriverWait(driver, 25).until(element_present)
        num1 = driver.find_element(By.XPATH, "//input[@id='C15_W50_V51_V52_search_parameters[12].VALUE1']")
        num1.clear()
        time.sleep(0.8)
        num1.send_keys(GIRM)
        time.sleep(0.2)
        driver.find_element(By.ID, "C15_W50_V51_Searchbtn").click()
        element_present = EC.presence_of_element_located((By.XPATH, "//a[@id='C15_W50_V51_V53_searchresult_table[1].object_id']"))
        WebDriverWait(driver, 40).until(element_present)
        driver.find_element(By.XPATH, "//a[@id='C15_W50_V51_V53_searchresult_table[1].object_id']").click()
        try:
            element_present = EC.presence_of_element_located((By.XPATH, "//span[@id='0013_nl8_8_mid']"))
            WebDriverWait(driver, 12).until(element_present)
            driver.find_element(By.XPATH, "//span[@id='0013_nl8_8_mid']").click()
        except TimeoutException:
            element_present = EC.presence_of_element_located((By.XPATH, "//span[@id='0015_nl5_5_mid']"))
            WebDriverWait(driver, 15).until(element_present)
            driver.find_element(By.XPATH, "//span[@id='0015_nl5_5_mid']").click()
        try:
            element_present = EC.presence_of_element_located((By.XPATH, "//img[@title='New Create (Ctrl+N)']"))
            WebDriverWait(driver, 20).until(element_present)
            driver.find_element(By.XPATH, "//img[@title='New Create (Ctrl+N)']").click()
        except (NoSuchElementException, TimeoutException):
            time.sleep(1)
        finally:
            element_present = EC.presence_of_element_located((By.XPATH, "//span[@class='icon icon-toolbarAdd']"))
            WebDriverWait(driver, 200).until(element_present)
            driver.find_element(By.XPATH, "//span[@class='icon icon-toolbarAdd']").click()
            element_present = EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Document']"))
            WebDriverWait(driver, 30).until(element_present)
            driver.find_element(By.XPATH, "//a[normalize-space()='Document']").click()
            time.sleep(4)
            file_path = "C:\\Users\\sanmartin\\Pictures\\Auto upload\\{}".format(GIRM)
            pyautogui.write(file_path)
            time.sleep(1.5)
            pyautogui.press('enter')
            time.sleep(1.5)
            try:
                element_present = EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Cancel'])[1]"))
                WebDriverWait(driver, 20).until(element_present)
                driver.find_element(By.XPATH, "(//button[normalize-space()='Cancel'])[1]").click()
                print("{} was already uploaded".format(GIRM))
            except (NoSuchElementException, TimeoutException):
                element_present = EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='{}']".format(GIRM)))
                WebDriverWait(driver, 180).until(element_present)
                print("{} uploaded successfully".format(GIRM))
            i=i+1
            continue
print("This program has been written by Yash.")
