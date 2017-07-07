import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
#episodeName="gamr of thrones s06e05"
 
fp = webdriver.FirefoxProfile()
 
#to automatically download zip files without download prompt
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","/home/amit/Downloads/")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")
 
def login():
    #log in to filestream
    driver.get("https://filestream.me/members/user/login")
    elem = driver.find_element_by_name("username")
    elem.send_keys("your email-id")
    elem = driver.find_element_by_name("password")
    elem.send_keys("password")
    elem.send_keys(Keys.RETURN)
    try:
        wait = WebDriverWait(driver, 30)
        #wait until you are logged in
        element = wait.until(EC.presence_of_element_located((By.ID,'header-upload-link')))
    except:
         print "Login failed or internet too slow"
         driver.quit()
         exit()
 
def getUrlFromPirateBay():
    driver.get("https://thepiratebay.org/")
    elem = driver.find_element_by_name("q")
    elem.send_keys(episodeName)
    elem.send_keys(Keys.RETURN)
 
    try:
        wait = WebDriverWait(driver, 50)
        #wait and check if any results
        element= wait.until(EC.presence_of_element_located((By.XPATH,"//table[@id='searchResult']/tbody/tr[1]/td[2]/a")))
    except:
        print "NO results or internet too slow"
        driver.quit()
        exit()
 
    #return magnet url for the first result
    return element.get_attribute("href")
 
def download(url):
    driver.get("https://filestream.me/members/user/login")
     #wait for pop up and close it
    try:
        wait = WebDriverWait(driver, 10)
        element=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='filesPopup']/a")))
        element.click()
    except:
        print "failed..."
        driver.quit()
        exit()
 
    time.sleep(2)
    driver.find_element_by_id("main-menu-downloading-link").click()
    time.sleep(2)
    elem = driver.find_element_by_name("uploadLinks")
    elem.send_keys(url)
    driver.find_element_by_id("header-upload-link").click()
    try:
        #wait until torrent is cached
        wait = WebDriverWait(driver, 1000)
        element= wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='icons download']")))
    except:
        print "failed..."
        driver.quit()
        exit()
    element.click()
 
if __name__=="__main__":
    driver = webdriver.Firefox(fp)
    #login to filestream
    login()
    url=getUrlFromPirateBay()
    download(url)