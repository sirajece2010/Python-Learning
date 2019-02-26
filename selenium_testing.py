from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('/home/innominds firefox binay')

geckoPath = '/home/innominds/PycharmProjects/Safe/venv/Python_Learning/geckodriver'
driver = webdriver.Firefox(executable_path=geckoPath)
driver.get('http://google.com')
assert 'Google' in driver.title
elem = driver.find_element