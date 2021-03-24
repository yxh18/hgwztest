from pythoncode.calculator import Calculator
import yaml


def steps(addstepsfile, calc, a, b, expect):
    with open(addstepsfile) as f:
        steps = yaml.safe_load(f)

    for step in steps:
        if 'add' == step:
            result = calc.add(a, b)
            print("step add")
        elif 'add1' == step:
            result = calc.add(a, b)
            print("step add1")
        elif 'add4' == step:
            result = calc.add(a, b)
            print("step add4")
    return expect == result


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("初始化数据")

    def teardown_class(self):
        print("清理数据")

    # def test_add(self):
    #     result=self.calc.add(1,1)
    #     assert result == 2
    #
    # def test_add1(self):
    #     result=self.calc.add(100,100)
    #     assert result == 200

    def test_add_steps(self):
        a = 1
        b = 1
        expect = 2
        steps("./steps/add_steps.yml", self.calc, a, b, expect)
