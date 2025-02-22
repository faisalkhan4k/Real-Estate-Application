import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://www.realestateindia.com/')
time.sleep(2)

driver.find_element(by = By.XPATH, value='/html/body/section[2]/div/ul/li[9]/a').click()
time.sleep(5)

user_input1 = driver.find_element(by=By.XPATH,value='//*[@id="index_search_buy_rent"]/div[1]/div[2]/div/div[1]/span/input')
user_input1.send_keys('Plots')
time.sleep(2)
# user_input1.send_keys(Keys.ENTER) for working for realestateindia.com instead use XPATH of search button
user_input1.find_element(by=By.XPATH,value='//*[@id="index_search_buy_rent"]/div[1]/button').click()
time.sleep(2)


driver.find_element(by=By.XPATH,value='//*[@id="pscfBudget"]').click()

time.sleep(5)
driver.find_element(by=By.XPATH,value='//*[@id="frm_refine"]/div[1]/div/div/ul/li[2]/div/div[1]/div[2]/ul/li[1]/div/label').click()

time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')


while True:

    driver.find_element(by=By.XPATH,value='//*[@id="load_more_button"]').click()
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')
    
    time.sleep(1)
    print(old_height)
    print(new_height)


    if(old_height ==  new_height):
        break
    old_height=new_height
time.sleep(1)
html = driver.page_source

with open('./web-scraping/hyd-plot-data.html','w',encoding='utf-8') as f:
    f.write(html)
