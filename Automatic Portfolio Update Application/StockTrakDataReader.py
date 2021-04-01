#!/Applications/miniconda3/envs/CQAChallenge/bin/python3
#Import os, glob, and pathlib (Provides access to file control)
import os
import glob
import time
from pathlib import Path
import config

#Import selenium webdriver+keys modules (Provides backend operation)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Designate path to chrome driver for current chrome version(May need to update)
PATH = "/Users/solbenishay/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)

#Open page on chrome
driver.get("https://www.stocktrak.com/login")
driver.implicitly_wait(100)

#Make sure on login page
assert "Login" in driver.title

#Find login+password inputs, fill them, and hit return
login = driver.find_element_by_id("tbLoginUserName")
password = driver.find_element_by_id("Password")
login.clear()
password.clear()
login.send_keys(config.STUSER)
password.send_keys(config.STPASSWORD)
password.send_keys(Keys.RETURN)

#Get portfolio value
time.sleep(10)
portfolio_value = driver.find_element_by_xpath('//*[@id="account-snapshot"]/div[1]/div[1]/div/div/span[1]/strong/span').text
print(portfolio_value)

#Access open positions page
time.sleep(15)
open_positions_link = driver.find_element_by_link_text('Open Positions')
open_positions_link.send_keys(Keys.RETURN)

#Access Download CSV Page
time.sleep(10)
downloadcsvbutton = driver.find_element_by_id('btnExportToExcel')
actions = ActionChains(driver)
actions.move_to_element(downloadcsvbutton)
actions.click(downloadcsvbutton)
actions.perform()

#Export CSV
time.sleep(5)
driver.switch_to_active_element
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnExport"))).click()

#Close Driver
time.sleep(10)
driver.quit()

#Find CSV and add to correct folder
downloadsfolder = glob.iglob("/Users/solbenishay/Downloads/*.csv")
downloadedfile = max(downloadsfolder, key=os.path.getctime)
Path(downloadedfile).rename(config.portfoliodatafolder[:-5]+downloadedfile[29:])







