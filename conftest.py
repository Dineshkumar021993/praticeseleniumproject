import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(scope="module")
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome()
    url ="https://d3ldvcrr82x82a.cloudfront.net/"
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()



