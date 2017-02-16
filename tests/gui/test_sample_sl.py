from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import time
'''
@pytest.fixture
def setupSel():
    geckodriverPath = "Users/suibin/Projects/mptest/selenium"
    import sys
    
    ### if selenium standalone server needs to start before calling webdriver
    import subprocess
    print("Starting selenium server with log at /tmp/selenium.log")
    selProc = subprocess.Popen((["java", "-jar", \
        "/Users/suibin/Projects/venv/selenium/selenium-server-standalone-3.0.1.jar", \
        "-log", "/tmp/selenium.log"]))
    print("Started selenium server with pid: %d; log at /tmp/selenium.log", selProc.pid)
    yield selProc
    print("Tearing down selenium server")
    selProc.terminate()
    
    import sys
    geckodriverPath = "/Users/suibin/Projects/mptest/mputil/selenium"
    sys.path.append(geckodriverPath)
    print(sys.path)
'''

def test_pycon():
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    caps["binary"] = "/usr/bin/firefox"

    driver = webdriver.Firefox(capabilities=caps)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    try:
        assert "No results found." in driver.page_source
    except AssertionError:
        time.sleep(15)
        driver.quit()
        assert 0
    #assert 0

def test_google():
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    caps["binary"] = "/usr/bin/firefox"

    driver = webdriver.Firefox(capabilities=caps)
    driver.get("https://google.com")
    assert "Google" in driver.title
    time.sleep(15)
    driver.quit()
    #assert 0

#test_pycon()
#test_google()
