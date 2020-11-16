"""
    testowanie kalkulatora
"""

import unittest


class Calculator:

    CALCULATORS = 0

    def __init__(self):
        print("Rozpoczynam prace...")

    def subtract(self, a, b):
        return a-b

    def divide(self, a, b):
        return a / b

    @classmethod
    def klasowa_metoda(sda):
        sda.CALCULATORS += 1


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # RUN SERVER
        print("Startuje serwer")

    def setUp(self):
        self.calc = Calculator()
        # self.file = open('asdasds.txt')

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 4),
                         1)
        self.assertTrue(1)
        self.assertFalse(0)
        self.assertIn(3, [1,2,3])
        self.assertIsNot({1: 'a'}, {1: 'a'})
        # self.assertIsNone({1: 'a'})

    @unittest.skipIf(1> 2, "Dlatego bo mi sie nie podoba")
    def test_divide_nominal(self):
        self.assertEqual(self.calc.divide(4, 2),
                         2)

    def test_divide_by_zero(self):
        # try:
        #     self.calc.divide(4, 0)
        # except ZeroDivisionError:
        #     return
        # self.fail()
        with self.assertRaises(ZeroDivisionError) as err:
            self.calc.divide(4, 0)
        print(err.exception)

    def tearDown(self):
        print("Koncze test.")
        # self.file.close()
        # SHUTDOWN SERVER

    @classmethod
    def tearDownClass(cls):
        # SHUTDOWN SERVER
        print("Zamykam serwer")

    def zwykla_metoda(self):
        ...

    @staticmethod
    def statyczna_metoda():
        ...

    @classmethod
    def klasowa_metoda(cls):
        ...

# x = Calculator()
# x.subtract()
#
# Calculator.klasowa_metoda()
