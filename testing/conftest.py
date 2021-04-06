import pytest


@pytest.fixture(scope='session')
def func():
    print('初始化环境')
    yield '返回数据111111'
    print('关闭连接')
