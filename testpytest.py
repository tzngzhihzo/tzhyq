import pytest
def login():
    print("这是登录方法")
class TestDemo():
    def test_one(self):
        print("开始执行testone")
        x = "this"
        assert 'h' in x

    def test_two(self):
        print("开始执行testtwo")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行testthree")
        a = 'hello'
        x = 'hello world'
        assert a in x
if __name__ == '__main__':
    pytest.main("-v -x TestDemo")
    pytest.main(['-v', '-x', 'TestDemo'])