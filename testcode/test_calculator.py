# test code
# @author: Fiona; @date: Oct 19, 2020
import pytest
import yaml

from FuncToBeTested.Calculator import Calculator

def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)

    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']

    min_datas = datas['min']['datas']
    min_ids = datas['min']['ids']

    multi_datas = datas['multi']['datas']
    multi_ids = datas['multi']['ids']

    div_datas = datas['div']['datas']
    div_ids = datas['div']['ids']

    div_zero_exception_datas = datas['div_zero_exception']['datas']
    div_zero_exception_ids = datas['div_zero_exception']['ids']

    exception_non_numeric_datas = datas['exception_non_numeric']['datas']
    exception_non_numeric_ids = datas['exception_non_numeric']['ids']

    return [add_datas, add_ids, min_datas, min_ids, multi_datas, multi_ids, div_datas, div_ids,
            div_zero_exception_datas, div_zero_exception_ids,
            exception_non_numeric_datas, exception_non_numeric_ids]


def is_number(a, b):
    try:
        float(a)
        float(b) # for int, long and float
    except ValueError:
        try:
            complex(a)
            complex(b) # for complex
        except ValueError:
            return False

    return True

class TestCalc:
    calc = Calculator()

    # test add
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    # test min
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, expect', get_datas()[2], ids=get_datas()[3])
    def test_min(self, a, b, expect):
        result = self.calc.min(a, b)
        assert round(result, 3) == expect

    # test multi
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a, b, expect', get_datas()[4], ids=get_datas()[5])
    def test_multi(self, a, b, expect):
        result = self.calc.multi(a, b)
        assert result == expect

    # test div
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a, b, expect', get_datas()[6], ids=get_datas()[7])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect

    # test zero divider exception by div
    @pytest.mark.run(order=-2)
    @pytest.mark.parametrize('a, b, expect', get_datas()[8], ids=get_datas()[9])
    def test_div_zero_b(self, a, b, expect):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)