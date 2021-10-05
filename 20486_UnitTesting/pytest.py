import unittest
from login import login_up


class validtest(unittest.TestCase):
    def test1(self):
        self.assertEqual(login_up('Avichal', 'AvichalSriv'), True)

    def test2(self):
        self.assertEqual(login_up('AvicH', 'Avichal@123'), True)

    def test3(self):
        self.assertEqual(login_up('AvIcHaL', '@#$%AVICHAL'), True)

    def test4(self):
        self.assertEqual(login_up('Avichal', 'qwerty'), False)

    def test5(self):
        self.assertEqual(login_up(9999, 'Qwerty@#$'), False)

    def test6(self):
        self.assertEqual(login_up('Avichal', 123456), False)

    def setUp(self):
        print("Setup")

    def tearDown(self):
        print("Teardown")

    @classmethod
    def setUpClass(self) \
            -> print("setup class"):
        pass

    @classmethod
    def tearDownClass(self) \
            -> print("teardown"):
        pass

    if __name__ == '__main__':
        unittest.main()
