import unittest

class demo(unittest.TestCase):
    def setUp(self) -> None:
        print("setup")
    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("test01")
        self.assertEqual(1,1,"相等")
        self.assertIn('t','tzh')

    def test_case02(self):
        print("test02")
        self.assertEqual(1,1,"相等")
        self.assertIn('t','tzh')

    @unittest.skip
    def test_case03(self):
        print("test03")
        self.assertEqual(1,1,"相等")
        self.assertIn('t','tzh')

if __name__ == '__main__':
    unittest.main()