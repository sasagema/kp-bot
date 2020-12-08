import time
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select




#os.system(os.getcwd() + '\script.exe')

subprocess.Popen([os.getcwd() + '\script.exe'])

driver = webdriver.Chrome('./driver/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.kupujemprodajem.com/oglasi.php?action=new')
time.sleep(5) # Let the user actually see something!

email = driver.find_element_by_xpath("//*[@id='email']")
password = driver.find_element_by_xpath("//*[@id='password']")
#element.send_keys("some text")
email.send_keys(EMAIL)
password.send_keys(PASSWORD, Keys.ENTER)
time.sleep(5) # Let the user actually see something!

radio = driver.find_element_by_xpath("//*[@id='data[ad_kind]goods']")
radio.click()
time.sleep(5)

#category_menu = driver.find_element_by_xpath("//*[@id='categorySelection']/div/div[1]/div/span[4]")
#category_menu.click()

#time.sleep(5)

category = driver.find_element_by_xpath("//div[text()='{}']".format(CATEGORY))
category.click()
time.sleep(5)

group = driver.find_element_by_xpath("//div[text()='{}']".format(GROUP))
group.click()
time.sleep(5)



name = driver.find_element_by_xpath("//*[@id='data[name]']").send_keys(NAME)
time.sleep(2)

driver.find_element_by_xpath("//*[contains(text(), '{}')]".format(CONDITION)).click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='price_number']").send_keys(PRICE)
time.sleep(2)

driver.find_element_by_xpath("//*[@id='currency_{}']".format(CURRENCY.lower())).click()
time.sleep(2)

if FIXED:
    driver.find_element_by_xpath("//*[@id='data[price_fixed]']").click()
time.sleep(2)

if INSTEAD_OF_PRICE:
    driver.find_element_by_xpath("//*[@id='sellPanel']/div[2]/div[7]/div").click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[text()='{}']".format(INSTEAD_OF_PRICE)).click()

    #driver.find_element_by_xpath("//*[contains(text(), '{}')]".format(INSTEAD_OF_PRICE)).click()

time.sleep(2)

if EXCHANGE:
    driver.find_element_by_xpath("//*[@id='exchangeForm']").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='adPhotosHolder']").click()
time.sleep(5)

iframe = driver.find_elements_by_tag_name('iframe')[2]

driver.switch_to.frame(iframe)
element = driver.find_element_by_xpath("//*[@id='tinymce']")
driver.execute_script("arguments[0].innerText = '{}'".format(TEXT), element)
#driver.execute_script("document.querySelector('#tinymce').innerHTML = '200';")
time.sleep(2)

driver.switch_to.default_content()

owner_input = driver.find_element_by_xpath("//*[@id='data[owner]']")
driver.execute_script("arguments[0].innerText = '{}'".format(OWNER), owner_input)
time.sleep(2)

# driver.find_element_by_xpath("//*[@id='data[owner]']").send_keys(OWNER)
# time.sleep(2)

#driver.find_element_by_xpath("//*[@id='phone_number']").text(PHONE)

#driver.find_element_by_xpath("//*[@id='phone_number']").send_keys(PHONE)
phone_input = driver.find_element_by_xpath("//*[@id='phone_number']")
driver.execute_script("arguments[0].innerText = '{}'".format(PHONE), phone_input)
time.sleep(2)

driver.find_element_by_xpath("//*[@id='locationSelection']/div/div[1]/div/span[4]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='locationSelection']/div/div[2]/div/div[2]/input").send_keys(CITY)

#driver.find_element_by_xpath("//div[text()='{}']".format(CITY)).click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='adFormInfo']/div[2]/div[20]/div/input").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='data[promo_type]none']").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='adFormProgressHolderInner']/div[5]/div[4]/div/input").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='accept_yes']").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='adFormDeclaration']/div[8]/div/input").click()
time.sleep(2)





time.sleep(5) 
driver.quit()