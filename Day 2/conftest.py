import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from SighnupZipangApp_PageObject import ZipangLogin

# ---------------- METADATA ----------------
def pytest_metadata(metadata):
    metadata["Project Name"] = "Zipang application Preview test cases"
    metadata["Tested By"] = "Aarav Mathur"
    metadata["Automation tool"] = "Selenium"
    metadata["Framework"] = "Pytest"
    metadata["URL"] = "https://zipang.myauctionstech.in/en/preview/products/69942ffe140afa28e18adfcd/sdfh/2026-02-21%2009%3A08"

# ---------------- DRIVER SETUP ----------------
@pytest.fixture(scope="session")
def driver():
    download_path = r"D:\Aarav\Selenium\Day 2\Downloads"
    ops = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    ops.add_experimental_option("prefs", prefs)
    serv_obj = Service()
    driver = webdriver.Chrome(service=serv_obj,options=ops)

    driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # ---------------- LOGIN ----------------
    login = ZipangLogin(driver)
    login.set_HomePage()
    login.set_Login()
    login.set_Email("aarav.2mathur@outlook.com")
    login.set_password("password")
    login.set_LoginButton()
    login.set_Accept_buttons()

    # ---------------- CLOSE DRIVER ----------------
    yield driver
    driver.quit()

# ---------------- REFRESH AFTER EACH TEST ----------------
@pytest.fixture(autouse=True)
def refresh_AfterEachTest(driver):
    yield
    driver.refresh()
