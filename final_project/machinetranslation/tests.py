import unittest
from translator import englishtofrench, frenchtoenglish

class TestMyModule(unittest.TestCase):
        def test_englishToFrench(self):
            self.assertEqual(englishtofrench("Hello"),"Bonjour")
            self.assertNotEqual(englishtofrench("hello"),"Hello", "failed")
            self.assertEqual(englishtofrench(""),"")

        def test_frenchToEnglish(self):
            self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
            self.assertNotEqual(frenchtoenglish("Bonjour"),"Bonjour", "failed")
            self.assertEqual(frenchtoenglish(""),"")
        


if __name__ == "__main__":
        unittest.main()