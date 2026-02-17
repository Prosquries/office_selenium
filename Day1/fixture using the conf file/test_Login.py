import pytest

class TestLogin:

    def test_LoginByEmail(self,setup1):
        print("This is login by Email")
        assert True==True

    def test_LoginByTwitter(self,setup1):
        print("This is login bt Twitter")
        assert True == True

    def test_LoginByFacebook(self,setup1):
        print("This is login by Facebook")
        assert True == True
