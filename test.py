import unittest
from app import roman_to_arabic

class TestRomanToArabic(unittest.TestCase):
    def test_basic_conversion(self):
        test_cases = [
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
            ('III', 3),
            ('IV', 4),
            ('IX', 9),
            ('LVIII', 58),
            ('MCMXCIV', 1994),
        ]

        for roman, arabic in test_cases:
            with self.subTest(roman=roman, arabic=arabic):
                self.assertEqual(roman_to_arabic(roman), arabic)

    def test_invalid_input(self):
        invalid_inputs = [
        '',
        'IIII',
        'VV',
        'XXXX',
        'LL',
        'CCCC',
        'DD',
        'MMMM',
        'A',
        '1',
    ]

        for roman in invalid_inputs:
            with self.subTest(roman=roman):
                with self.assertRaises(ValueError):
                    roman_to_arabic(roman)


if __name__ == '__main__':
    unittest.main()
