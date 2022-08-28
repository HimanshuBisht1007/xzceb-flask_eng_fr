import unittest
from translator import englishtofrench, frenchtoenglish

class TestMyModule(unittest.TestCase):
        def test_englishToFrench(self):
            self.assertEqual(englishtofrench("Hello"),"Bonjour")
            self.assertEqual(englishtofrench("Hi"),"Salut")

        def test_frenchToEnglish(self):
            self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
            self.assertEqual(frenchtoenglish("Salut"),"Hi")


if __name__ == "__main__":
        unittest.main()