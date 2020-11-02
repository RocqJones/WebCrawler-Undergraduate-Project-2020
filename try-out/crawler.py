from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def configure_driver():
    """
    - Add additional Options to the webdriver.
    - Add the argument and make the browser Headless.
    - Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="./driver/chromedriver", options = chrome_options)
    return driver


def crawler(driver, filter_keyword):
    """
    Step 1: Go to mkulimayoung.com, market section with selected filter keyword
          - Then wait for the element to load with try and catch...
    Step 2: Create a parse tree of page sources after filtering with BeautifulSoup
    Step 3: Iterate over the filtered results and fetch the data
    """
    driver.get(f"https://www.mkulimayoung.com/market?tags={filter_keyword}")
    try:
        # WebDriverWait(driver, 5).until(lambda s: s.find_element_by_id("app").is_displayed())
        WebDriverWait(driver, 15).until(lambda s: s.find_elements_by_class_name("ant-spin-nested-loading"))
    except TimeoutException:
        print("TimeoutException: Element not found")
        return None

    soup = BeautifulSoup(driver.page_source, "lxml")
    
    for market_page in soup.select("div.col-lg-3"):
        for product in market_page.select("div.item"):
            product_name = "a div.description p"
            location = "a div.description address p"
            
            print({
                "Product Name": product.select_one(product_name).text,
                "Location": product.select_one(location).text,
            })

# create the driver object.
driver = configure_driver()
filter_keyword = "Cereals"
crawler(driver, filter_keyword)
# close the driver.
driver.close()