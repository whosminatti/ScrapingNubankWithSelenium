from selenium import webdriver
from bs4 import BeautifulSoup as soup
import requests
import time

cpf = '00000000000'
senha = 'XXXXXXXXXXXXXXX'
#set webdriver
driver = webdriver.Firefox()

#set URL
driver.get('https://app.nubank.com.br/#/login')

#wait 5 seconds
time.sleep(5)

#get inputs
user_box = driver.find_element_by_id('username')
pass_box = driver.find_element_by_id('input_001')

#get button
login_button = driver.find_element_by_tag_name('button')

#set credentials
user_box.send_keys(cpf)
pass_box.send_keys(senha)

#sleep2
time.sleep(2)

#login
login_button.click()

#sleep2
time.sleep(10)

#
page_html = driver.page_source
#item_elements = page_html.find_all("div", class_="event-card")
itens = driver.find_elements_by_xpath("//div[contains(@class,'event-card transaction')]")

print(len(itens ))

print(itens[0].text)
list_of_itens = []
for item in itens:
    #list_of_itens = item.text
    list_of_itens = item.get_attribute("h4")
    print(list_of_itens)
