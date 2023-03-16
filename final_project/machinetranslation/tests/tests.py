import unittest
from ..translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("dog"), "Bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "dog")


if __name__ == '__main__':
    unittest.main()
