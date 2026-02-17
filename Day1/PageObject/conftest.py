import datetime

import pytest


@pytest.fixture()
def Setup(request):
    print()
    print("Opening the browser")
    yield
    print()
    print("Closing the browser")

def pytest_metadata(metadata):
    metadata["Project Name"] = "Dummy Ticket Automation"
    metadata["Tested By"] = "Aarav"
    metadata["Automation Tool"] = "Selenium"
    metadata["Framework"] = "Pytest"

