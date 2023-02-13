import unittest
import main


class SayNumTestCase(unittest.TestCase):
    def test_numberToWord(self):
        self.assertEqual(main.say_num(293892389), "two hundred ninetythree million eight hundred ninetytwo thousand three hundred eightynine")  # add assertion here


if __name__ == '__main__':
    unittest.main()
