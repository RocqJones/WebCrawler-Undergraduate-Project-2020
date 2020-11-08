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

if __name__=='__main__':
    web_driver = driver_configs()
    url = "https://www.mfarm.co.ke/posts"
    crawler(web_driver, url)

    # close chrome driver
    web_driver.close()