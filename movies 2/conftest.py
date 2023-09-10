import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def setup(request):
    if request.param == "Chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        service_obj = ChromeService(executable_path="path/to/chromedriver")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        return driver
    elif request.param == "Firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_capability("moz:firefoxOptions", {"detach": True})
        service_obj = FirefoxService(executable_path="path/to/geckodriver")
        driver = webdriver.Firefox(service=service_obj, options=firefox_options)
        return driver
    elif request.param == "Edge":
        edge_options = EdgeOptions()
        edge_options.set_capability("edgeOptions", {"detach": True})
        service_obj = EdgeService(executable_path="path/to/msedgedriver")
        driver = webdriver.Edge(service=service_obj, options=edge_options)
        return driver
