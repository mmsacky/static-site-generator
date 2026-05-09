import unittest
from source_to_destination import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        md = "# This is the Title of the page"
        extracted_title = extract_title(md)
        self.assertEqual(extracted_title, "This is the Title of the page")

    def test_title_with_space_at_end(self):
        md = "# This is the Title of the page "
        extracted_title = extract_title(md)
        self.assertEqual(extracted_title, "This is the Title of the page")
    
    def test_title_with_space_at_beginning(self):
        md = " # This is the Title of the page "
        extracted_title = extract_title(md)
        self.assertEqual(extracted_title, "This is the Title of the page")

    def test_no_title(self):
        md = " ## This is the Title of the page "
        with self.assertRaises(Exception):
             extract_title(md)

if __name__ == "__main__":
    unittest.main()