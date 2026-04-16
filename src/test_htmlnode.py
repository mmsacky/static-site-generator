import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_not_implemented(self):
        node = HTMLNode("H1", "Baraka", None, {"href" : "https://baraka.media"})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode("H1", "Baraka", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_props_to_html_none(self):
        node = HTMLNode("H1", "Baraka", None, None)
        self.assertEqual("", node.props_to_html())

    def test_repr(self):
        node = HTMLNode("H1", "Baraka", None, {"href": "https://baraka.media", "target":"_blank"})
        self.assertEqual("HtmlNode(H1, Baraka, children: None, {'href': 'https://baraka.media', 'target': '_blank'})", repr(node))


if __name__ == "__main__":
    
    unittest.main()

