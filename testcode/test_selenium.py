import selenium
from selenium import webdriver

def test_selenium():
    driver=webdriver.chrome()
    driver.get("https://www.baidu.com")