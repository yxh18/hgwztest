from pythoncode.calculator import Calculator
import pytest
import yaml


def get_datas():
    with open("./datas/calc.yml")as f:
        datas = yaml.safe_load(f)
        add_datas = datas['add']['datas']
        print(add_datas)
        return [add_datas]


class TestDatas:
    def setup_class(self):
        self.calc = Calculator()
        print("初始化数据")

    def teardown_class(self):
        print("关闭连接")

    @pytest.mark.parametrize('a,b,expect', get_datas()[0])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert expect == result
