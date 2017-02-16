from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import time
import os
from mputil.mplogger import MPLogger
import xmltodict


logger = MPLogger(__name__)
settingFile = "settings.xml"

@pytest.fixture(scope="module", params = ["FIREFOX", "CHROME"])
def setup(request):
    #setting up browser webdriver locations
    loc = os.environ["MPHOME"] + settingFile
    with open(loc, "r") as f:
        setting = xmltodict.parse(f.read())
        chromedriver = os.environ["MPHOME"] + setting["mpSettings"]["selenium"]["chromedriver"]
        geckodriver  = os.environ["MPHOME"] + setting["mpSettings"]["selenium"]["geckodriver"]

    #setting up webdriver fixture
    if request.param == "FIREFOX":
        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        caps["binary"] = geckodriver
        driver = webdriver.Firefox(capabilities=caps)
    elif request.param == "CHROME":
        #caps = DesiredCapabilities.CHROME
        #caps["binary"] = "/usr/bin/chrome"
        driver = webdriver.Chrome(chromedriver)

    logger.info("Starting " + request.param + " WebDriver.")
    yield driver
    #tearing down webdriver fixture
    print("\nTearing down {} webdriver setup".format(request.param) )
    logger.info("Tearing down {} driver handle.".format(request.param) )
    driver.quit()

def test_pycon(setup):
    logger.info("testing pycon site")
    setup.get("http://www.python.org")
    assert "Python" in setup.title
    elem = setup.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in setup.page_source
    time.sleep(2)
    

def test_google(setup):
    logger.info("testing google.com") 
    setup.get("https://google.com")
    assert "Google" in setup.title
    time.sleep(2)

