import pytest

class TestClass:

    def test_LoginByEmail(self):
        print("Testing the login by email")

    def test_LoginByFacebook(self):
        print("Testing the login by facebook")

    def test_LoginByTwitter(self):
        print("Testing login by twitter")

    @pytest.mark.skip("Testing the Login first")
    def test_SignupByEmail(self):
        print("The Signup by Email")
        assert 1 == 1

    @pytest.mark.skip("Testing the Login first")  # To Skip the testcase to be executed
    def test_SignupByFacebook(self):
        print("The Signup by Facebook")
        assert 1 == 1

    @pytest.mark.skip("Testing the Login first")  # To Skip the testcase to be executed
    def test_SignUpByTwitter(self):
        print("The Sign Up by Twitter")
        assert 1 == 1