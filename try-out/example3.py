import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def correct_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    return url

def crawler(url):
    service = Service('driver/chromedriver')
    service.start()

    # pass url to check if it's correct
    url = correct_url(url)
    driver = webdriver.Remote(service.service_url)
    driver.get(url)

    # crawler starts here
    # s = driver.find_element_by_css_selector("p").text
    # print(s)
    all_hover_elements = driver.find_elements_by_class_name('container')
    # p_elements = driver.find_elements_by_class_name
    # print(p_elements)
    
    for hover_element in all_hover_elements:
        # hover_element = driver
        p_element = hover_element.find_element_by_css_selector('p').text
        # product_name = p_element.get_attribute("body")
        print(p_element)

    # sleep after 15 seconds
    time.sleep(10)
    driver.quit()

if __name__=='__main__':
    url = "http://www.mkulimayoung.com/market"
    crawler(url)