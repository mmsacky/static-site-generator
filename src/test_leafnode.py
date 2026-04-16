import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me!</a>')

    def test_leaf_to_html_class(self):
        node = LeafNode("h2", "Hello Word", {"class": "secondary-title"})
        self.assertEqual(node.to_html(), '<h2 class="secondary-title">Hello Word</h2>')

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello World!")
        self.assertEqual("Hello World!", node.to_html())

    def test_leaf_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_int(self):
        node = LeafNode(None, 0)
        self.assertEqual(0, node.to_html())


if __name__ == "__main__":
    
    unittest.main()