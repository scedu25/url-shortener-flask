from app import generate_short_url_path
import unittest

class TestApp(unittest.TestCase):
    def test(self):
        test_url = generate_short_url_path('https://www.google.com')
        self.assertEqual(len(test_url), 6)
        self.assertRegex(test_url, '[a-f0-9]{6}$')
        self.assertEqual(test_url, '06dd0b')

        test_url = generate_short_url_path('instagram.com', 10)
        self.assertEqual(len(test_url), 10)
        self.assertRegex(test_url, '[a-f0-9]{10}$')

if __name__ == '__main__':
    unittest.main()