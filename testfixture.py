import pytest


@pytest.mark.login
def test_case01(login):
    print("这是test01，需要登录")

@pytest.mark.search

def test_case02():
    print("这是test02，不需要登录")
@pytest.mark.search
def test_case03(login):
    print("这是test03，需要登录")

if __name__ == '__main__':
    pytest.main('-m','login')