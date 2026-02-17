import pytest
@pytest.fixture()
def setup1():
    print("Setup test")
    print("Opening the browser")
    yield
    print()
    print("Closing the browser")
