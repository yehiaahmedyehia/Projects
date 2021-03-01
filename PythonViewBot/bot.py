#Selenium Webdriver must be installed for this to work

import time;
from selenium import webdriver;

#time to refresh page (minute)
Timer = 1:45

#youtube link
link = 'https://www.youtube.com/watch?v=hW_WFUs3hfQ&t=2s'

#number of views
views = 10

driver = webdriver.Chrome('webdrivers\chromedriver.exe')
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
  
