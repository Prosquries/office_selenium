import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser name: chrome or edge"
    )


@pytest.fixture()
def Setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service as ChromeService
        service = ChromeService()
        driver = webdriver.Chrome(service=service)

    elif browser == "edge":
        from selenium.webdriver.edge.service import Service as EdgeService
        service = EdgeService()
        driver = webdriver.Edge(service=service)

    else:
        print("Browser not supported!")

    driver.implicitly_wait(10)
    driver.maximize_window()

    return driver

    driver.quit()