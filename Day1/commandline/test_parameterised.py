import pytest

class TestClass:

    @pytest.mark.parametrize('num1,num2',[(10,15),(5,20),(20,20),(2,2),(45,25)])
    def test_clauculations(self,num1,num2):
        assert num1 == num2