import pytest

class TestDependencies:

    @pytest.mark.dependency(name ="OpenApp")
    def test_Openapp(self):
        assert True == True

    @pytest.mark.dependency(name = "Login", depends = ["OpenApp"])
    def test_Login(self):
        assert True == True

    @pytest.mark.dependency(name = "Search", depends = ["Login"])
    def test_Search(self):
        assert True == False

    @pytest.mark.dependency(name = "AdvanceSearch",depends = ["Search"])
    def test_AdvancedSearch(self):
        assert True == True

    @pytest.mark.dependency(name = "Logout", depends = ["Login"])
    def test_logout(self):
        assert True == True