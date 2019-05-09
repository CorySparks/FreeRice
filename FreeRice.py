from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time

driver = webdriver.Firefox()
driver.get("http://freerice.com/user/login")

amount = 0

driver.find_element_by_xpath("//input[@class='watermarkPluginCustomClass']").click()
driver.find_element_by_xpath("//input[@class='form-text required']").send_keys("username")
driver.find_element_by_xpath("//input[@id='edit-pass']").click()
driver.find_element_by_xpath("//input[@name='pass']").send_keys("password")
driver.find_element_by_xpath("//input[@class='form-submit']").click()
driver.find_element_by_xpath("//li[@class='leaf']/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[contains(text(), 'Multiplication Table')]").click()
time.sleep(1)

while True:
    elem = driver.find_element_by_xpath("//a[@class='question-link']/b").text
    numbers = re.findall('\d+', elem)
    if numbers[1]:
        answer = int(numbers[0]) * int(numbers[1])
        #print "answer pick: " + str(driver.find_element_by_xpath("//a[contains(text(), " + str(answer) + ")]").text)
        driver.find_element_by_xpath("//a[contains(text(), " + str(answer) + ")]").click()
        amount += 1
        print "amount: " + str(amount)
        #print "math: " + str(int(numbers[0])) + " * " + str(int(numbers[1]))
        #print "answer: " + str(answer)
        time.sleep(0.8)
    else:
        print "refresh"
        driver.refresh()
        driver.find_element_by_xpath("//li[@class='leaf']/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[contains(text(), 'Multiplication Table')]").click()
        time.sleep(1)
