# test code
# @author: Fiona; @date: Oct 19, 2020
import pytest
import yaml

from FuncToBeTested.Calculator import Calculator


def setup_function():
    print("setup function")


def teardown_function():
    print("teardown")


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']

    print(add_datas)
    print(add_ids)

    return [add_datas, add_ids]


def get_steps(addstepfiles, calc, a, b, expect):
    with open(addstepfiles) as f:
        steps = yaml.safe_load(f)

    for step in steps:
        if step == 'add':
            print("step: add")
            result = calc.add(a, b)
        elif step == 'add1':
            print("step: add1")
            result = calc.add1(a, b)
        assert result == expect

@pytest.fixture(autouse=True, scope="class")
def get_calc():
    print("start calculation")
    yield
    print("end calculation")

class TestCalc:
    calc = Calculator()

    @pytest.mark.parametrize('a, b, expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [2, 1, 2], [100, 2, 50]
    ])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [
        [1, 0, 1], [0.1, 0, 0.3], [100, 0, 300]
    ])
    def test_div_zero_b(self, a, b, expect):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)

    def test_add_steps(self):
        a = 1
        b = 2
        expect = 3
        get_steps("./datas/steps.yml", self.calc, a, b, expect)

    def test_case1(self, login):
        print(login)
        print("test cases 1")

    @pytest.mark.usefixtures("login")
    def test_case2(self):
        print("test cases 2")
        # print(login)
