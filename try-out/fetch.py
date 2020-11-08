from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

# import requests

url = "https://www.mfarm.co.ke/posts"

# Start the WebDriver and load the page
wd = webdriver.Chrome(executable_path="./driver/chromedriver")
wd.get(url)

# Wait for the dynamically loaded elements to show up

# WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "anti-spin-nested-loading")))
wait = WebDriverWait(wd, 10)
# wait.until(wd.find_elements_by_class_name('row'))
wait.until(lambda w:  w.find_elements_by_class_name('description'))

# And grab the page HTML source
html_page = wd.page_source
wd.close()

soup = BeautifulSoup(html_page, "lxml")
file = open("page_data.txt",'w')
l = soup.prettify()
for items in l:
    file.write(items)

file.close()
# print(soup.prettify())