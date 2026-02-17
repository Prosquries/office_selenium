from XLUtils import *

class TestLogin:
    @pytest.fixture() # This is the decorator
    def Setup(self):
        print()
        print("Launching the browser")
        yield # It prints something very important
        print("Opening the application")

    def test_Login(self,Setup):
        print("Testing the app login by a email and password")
        assert True
    def test_Login2(self,Setup):
        print("Testing the app login by Google")

    def test_Login3(self,Setup):
        print("Testing the app login by Twitter")

    def test_Login4(self,Setup):
        print("Testing the app login by Facebook")