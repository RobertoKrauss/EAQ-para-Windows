#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pip.exe install selenium
#pip install webdriver-manager
# https://www.reddit.com/r/selenium/comments/7341wt/success_how_to_run_selenium_chrome_webdriver_on/
#---------------------------------------------------------------------------------------


import os
#from selenium import webdriver
import datetime
import time
from selenium import webdriver
#driver = webdriver.Chrome("C:\SPB_Data\.wdm\drivers\chromedriver\80.0.3987.106\win32\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors. 

print ("abrindo janela")
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)

print ("abrindo a pagina")
driver.get("https://www.brasilbandalarga.com.br/bbl")

print ("clinado o botão")
button = driver.find_element_by_id('btnIniciar')
button.click()

print ("Inicio do teste")
#--------------------------------------------------
#wait a minute
#import time

print("This prints once a minute.")
time.sleep(60) # Delay for 1 minute (60 seconds).
print("This prints once a minute.")
x = datetime.datetime.now()
#-------------------------------------------


data = driver.find_elements_by_class_name("textao")
i=1
for data in data:
    print(data.text.strip())
    if i==1:
        download=data.text.strip()
        i+=1
    elif i==2:
        upload=data.text.strip()
        i+=1
print ("download= ", download, " / upload= ", upload)

#data = driver.find_elements_by_class_name("col-xs-6 col-md-6 text-center")
#for data in data:
#    print(data.text.strip())

print("Tempo computador= ", x)

driver.quit() 
