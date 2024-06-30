import pytest
import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from webdriver_manager.firefox import GeckoDriverManager
os.environ['GH_TOKEN']= "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"
"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"


@pytest.fixture(params=['Chrome', 'FireFox'])
def fixtureSetup(request):
    driver = None
    if request.param == "Chrome":
        options = Options()
        #options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
    elif request.param == "FireFox":
        ff_options = FireFoxOptions()
        ff_options.add_argument("--headless")
        driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()), options=ff_options)
    return driver
        
