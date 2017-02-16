from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import time
from mputil.mplogger import MPLogger

'''
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("/tmp/"+ __name__ + ".log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
'''
logger = MPLogger(__name__)

@pytest.fixture(scope="module")
def setup():
    import sys
    geckodriverPath = "Users/suibin/Projects/mptest/selenium"
    geckodriverPath = "/Users/suibin/Projects/mptest/mputil/selenium"
    sys.path.append(geckodriverPath)
    logger.info(sys.path)

    #setting up webdriver fixture
    print("Starting up Webdriver.\n")
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    caps["binary"] = "/usr/bin/firefox"
    logger.info("Starting Firefox geckodriver.")
    driver = webdriver.Firefox(capabilities=caps)
    yield driver
    #tearing down webdriver fixture
    print("\nTearing down setup")
    logger.info("Tear down driver handle.")
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

