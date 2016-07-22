from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import Select 
import time

#Navigate to chrome
options = webdriver.ChromeOptions() 
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options) 

#Goto to browser 
browser.get("https://www.facebook.com") 

username = browser.find_element_by_id( "email" )
password = browser.find_element_by_id( "pass" )
submit   = browser.find_element_by_id("u_0_x")
 
# Input text in username and password inputboxes
username.send_keys("santosh.immortal@gmail.com")
password.send_keys("1234567890")
 
# Click on the submit button
submit.click()

print("Successfully completed Finding a bug in www.facebook.com")