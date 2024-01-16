from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


def openAndLogin():
    global wait
    driver.get(f"http://instagram.com")  # Open page.
    wait.until(EC.visibility_of_element_located((By.NAME, "username")))  # Wait till username will show up at login screen.
    driver.find_element_by_name("username").send_keys("reuven.itz")  # Type the username.
    driver.find_element_by_name("password").send_keys("@Re3228559093", Keys.ENTER)  # Type the password and then press enter.
    # driver.find_element_by_name("username").send_keys("nisui_hevrati")  # Type the username.
    # driver.find_element_by_name("password").send_keys("@Re3228559092", Keys.ENTER)  # Type the password and then press enter.


def closeNotifications():
    global wait
    wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="_a9-- _a9_1"]')))  # Wait till notifications message will show up.
    driver.find_element_by_xpath('//button[@class="_a9-- _a9_1"]').click()  # Click on "Not Now" at the notification message.


def sendFollow(user):
    global wait
    try:
        driver.find_element_by_xpath('//div[@class="_aaw9"]').click()  # Press on Search
        sleep(1)
    except exceptions as e:
        print(e)
        print("Search button not found.")
        if driver.find_element_by_xpath('//div[@class="_aaw9"]').is_displayed():
            driver.find_element_by_xpath('//div[@class="_aaw9"]').click()
        else:
            print("RIP - can't find search button.")
            return 0
    try:
        driver.find_element_by_xpath('//input[@aria-label="Search input"]').send_keys(open("instagram users.txt", "r").readlines()[user])  # Type the username
        sleep(1)
    except exceptions as e:
        print(e)
        print("can't type username.")
        if driver.find_element_by_xpath('//input[@aria-label="Search input"]').is_displayed():
            driver.find_element_by_xpath('//input[@aria-label="Search input"]').send_keys(open("instagram users.txt", "r").readlines()[user])
        else:
            return 0
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="/{a}/"]'.format(a=open("instagram users.txt", "r").readlines()[user].replace("\n", "")))))  # Wait till the user will show up at search bar.
        sleep(1)
    except exceptions as e:
        print(e)
        print("Waited to much time to find the username at the search bar.")
        return 0
    try:
        driver.find_element_by_xpath(('//a[@href="/{a}/"]'.format(a=open("instagram users.txt", "r").readlines()[user].replace("\n", "")))).click()  # Click on the username.
        sleep(1)
    except exceptions as e:
        print(e)
        print("Cannot click on the username at the search bar.")
        if driver.find_element_by_xpath(('//a[@href="/{a}/"]'.format(a=open("instagram users.txt", "r").readlines()[user].replace("\n", "")))).is_displayed():
            driver.find_element_by_xpath(('//a[@href="/{a}/"]'.format(a=open("instagram users.txt", "r").readlines()[user].replace("\n", "")))).click()
        else:
            return 0
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Follow")]')))  # Wait till follow button will show up.
        sleep(1)
    except exceptions as e:
        print(e)
        print("No follow button.")
        if not driver.find_element_by_xpath('//div[contains(text(), "Follow")]').is_displayed():  # check if follow button is showing up.
            return 0
    try:
        driver.find_element_by_xpath('//div[contains(text(), "Follow")]').click()  # click on follow button.
        sleep(1)
    except exceptions as e:
        print(e)
        print("Can't click on the follow button.")


driver = webdriver.Chrome(r"C:\Drivers\chromedriver.exe")  # Set the webdriver.
wait = WebDriverWait(driver, 10)  # Command - Wait.
openAndLogin()
closeNotifications()
for user in range(90):
    print(f"{user+1}. ", open("instagram users.txt", "r").readlines()[user].replace("\n", ""))  # Print the first line from this txt.
    sendFollow(user)




