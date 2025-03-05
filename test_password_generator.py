import unittest
import string
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.default_length = 12
        self.max_length = sum(map(len, PasswordGenerator.CHARACTER_GROUPS)) - len(PasswordGenerator.EXCLUDED_CHARACTERS)

    def test_password_length(self):
        gen = PasswordGenerator(8)  # Below min length
        self.assertEqual(len(gen.generate()), 12)  # Should be at least 12

        gen = PasswordGenerator(20)
        self.assertEqual(len(gen.generate()), 20)

        gen = PasswordGenerator(200)  # Above max length
        self.assertEqual(len(gen.generate()), self.max_length)

    def test_password_character_types(self):
        gen = PasswordGenerator(16)
        password = gen.generate()

        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_excluded_characters(self):
        gen = PasswordGenerator(16)
        password = gen.generate()
        for char in PasswordGenerator.EXCLUDED_CHARACTERS:
            self.assertNotIn(char, password)

    def test_minimum_punctuation_and_uppercase(self):
        gen = PasswordGenerator(16)
        password = gen.generate()
        punctuation_count = sum(1 for c in password if c in string.punctuation)
        uppercase_count = sum(1 for c in password if c.isupper())
        self.assertGreaterEqual(punctuation_count, 2)
        self.assertGreaterEqual(uppercase_count, 2)

    def test_invalid_length_type(self):
        with self.assertRaises(TypeError):
            PasswordGenerator("invalid")

if __name__ == "__main__":
    unittest.main()
