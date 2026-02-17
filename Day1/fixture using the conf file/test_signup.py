import pytest

class TestSighnup:

    def test_sighnup_email(self,setup1):
        print("Sighnup by a email and password")
        assert True

    def test_sighnup_phone(self,setup1):
        print("Sighnup by a phone number and OTP")

    def test_sighnup_google(self,setup1):
        print("Sighnup by a google ID")

    def test_sighnup_facebook(self,setup1):
        print("Sighnup by a facebook ID")


#  python -m pytest -v -s test_Login.py # To run single test case at a time
#  python -m pytest -v -s # To run all the test cases at once
#  python -m pytest -v -s test_Login.py::TestLogin::test_LoginByEmail # to run a specific method.