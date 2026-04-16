import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a plain text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false_2(self):
        node = TextNode("This is a plain text node", TextType.TEXT)
        node2 = TextNode("This is a p text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a plain text node", TextType.ITALIC, "https://google.com")
        node2 = TextNode("This is a plain text node", TextType.ITALIC, "https://google.com")
        self.assertEqual(node, node2)

    def test_eq_url_false(self):
        node = TextNode("This is a plain text node", TextType.ITALIC, "https://gogle.com")
        node2 = TextNode("This is a plain text node", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a plain text node", TextType.ITALIC, "https://google.com")
        self.assertEqual("TextNode(This is a plain text node, ITALIC, https://google.com)", repr(node))

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is a text node", "invalid_type")
            text_node_to_html_node(node)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_text_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text node")

    def test_text_code(self):
        node = TextNode("def function(self)", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "def function(self)")

    def test_text_link(self):
        node = TextNode("click here!", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "click here!")
        self.assertEqual(html_node.props, {'href':'https://google.com'})

    def test_text_image(self):
        node = TextNode('the offcial google logo', TextType.IMAGE, "https://google.com/google-logo")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {'src':'https://google.com/google-logo', 'alt':'the offcial google logo'})


if __name__ == "__main__":
    unittest.main()
