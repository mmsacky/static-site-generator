import unittest

from extract_links import extract_markdown_images, extract_markdown_links


class testSplitDelimiter(unittest.TestCase):

    def test_assignment_example_01(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        
    def test_assignment_example_02(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    
    # Basic image extraction
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    # Multiple images
    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches,
        )

    # No images returns empty list
    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images("This is plain text with no images.")
        self.assertListEqual([], matches)

    # Basic link extraction
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://wikipedia.org"),
            ],
            matches,
        )

    # No links returns empty list
    def test_extract_markdown_links_none(self):
        matches = extract_markdown_links("No links here.")
        self.assertListEqual([], matches)

    # Images should NOT be captured by extract_markdown_links
    def test_extract_markdown_links_ignores_images(self):
        matches = extract_markdown_links(
            "![an image](https://example.com/img.png) and [a link](https://example.com)"
        )
        self.assertListEqual([("a link", "https://example.com")], matches)

if __name__ == "__main__":
    unittest.main()
