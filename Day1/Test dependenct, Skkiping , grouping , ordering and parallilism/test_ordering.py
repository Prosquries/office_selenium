import pytest

class Testclass:

    @pytest.mark.order(3)
    def test_methodC(self):
        print("Running Method C ..")

    @pytest.mark.order(4)
    def test_methodD(self):
        print("Running Method D ..")

    @pytest.mark.order(1)
    def test_methodA(self):
        print("Running Method A ..")

    @pytest.mark.order(2)
    def test_methodB(self):
        print("Running Method B ..")

    @pytest.mark.order(5)
    def test_methodE(self):
        print("Running Method E ..")