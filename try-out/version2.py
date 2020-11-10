import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def driver_configs():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    web_driver = webdriver.Chrome(executable_path="./driver/chromedriver", options = chrome_options)
    return web_driver

def crawler(web_driver, url):
    web_driver.get(url)
    try:
        wait = WebDriverWait(web_driver, 15)
        wait.until(lambda w:  w.find_elements_by_class_name('col-lg-9'))

    except TimeoutException:
        print("TimeoutException: Element not found")
        return None

    soup = BeautifulSoup(web_driver.page_source, "lxml")
    for products_col in soup.select('div.row'):
        for products in products_col.select('div.col-md-4'):
            product_name = 'div.post div.description a'
            date_posted = 'div.post small.post-info'
            
            print({
                "Product Name" : products.select_one(product_name).text,
                "Date Posted" : products.select_one(date_posted).text.replace("\n","").replace("\xa0","").replace(" ",""),
            })

            dictionary_data = {
                "Product Name" : products.select_one(product_name).text,
                "Date Posted" : products.select_one(date_posted).text.replace("\n","").replace("\xa0","").replace(" ",""),
            } 
            # Serializing json
            json_object = json.dumps(dictionary_data, indent=2)
            # write to json  file
            with open("sample_data.json", 'a+') as outfile:
                outfile.write(json_object)

            # d = products.select_one(product_name).text
            # with open("sample_data.txt", 'a+') as outfile:
            #     outfile.write(d)

if __name__=='__main__':
    web_driver = driver_configs()

    # paging - Range 1 - 100/200
    pages = []
    base_url = 'https://www.mfarm.co.ke/posts'
    pages.append(base_url)
    for i in range(2, 10):
        other_pages = 'https://www.mfarm.co.ke/posts?page=' + str(i)
        pages.append(other_pages)

    for w_links in pages: 
        crawler(web_driver, w_links)

    # close chrome driver
    web_driver.close()


"""
Writting data in .json file
- dictionary – name of dictionary which should be converted to JSON object.
- indent – defines the number of units for indentation
"""