import pytest

class TestGropus:

    @pytest.mark.sanity
    def test_LoginByEmail(self):
        print("Testing the Login by email")
        assert 1 == 1

    @pytest.mark.sanity
    def test_LoginByTwitter(self):
        print("Testing the Login by Twitter")
        assert 1 == 1

    @pytest.mark.sanity
    def test_LogInByfacebook(self):
        print("Testing the Login by facebook")
        assert 1 == 1

    @pytest.mark.regression
    def test_SignInByEmail(self):
        print("Testing the Sign up by facebook")
        assert 1 == 1

    @pytest.mark.regression
    def test_SignInByTwitter(self):
        print("Testing the Sign up by twitter")
        assert 1 == 1

    @pytest.mark.regression
    def test_SignUpByFacebook(self):
        print("Testing the Sign up by facebook")

# To run this test we have to perform the command on the terminal
# python -m pytest -s -v -m  "regression" .\test_grouping.py # This is the command for the regression group
# python -m pytest -s -v -m  "sanity" .\test_grouping.py # This is the command for the sanity group
# and if we want both groups to run than we have to write # python -m pytest -s -v  .\test_grouping.py

