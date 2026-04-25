import unittest

from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType

class testTextToTextNode(unittest.TestCase):
    
    def test_in_order(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ],new_nodes)
    
    def test_just_bold(self):
        text = "This is **text**"
        new_nodes = text_to_textnodes(text)
        self.assertEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD)],new_nodes)

    def test_just_italic(self):
        text = "with an _italic_ word"
        new_nodes = text_to_textnodes(text)
        self.assertEqual([
            TextNode("with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            ],new_nodes)
        
    def test_just_code(self):
        text = "and a `code block`"
        new_nodes = text_to_textnodes(text)
        self.assertEqual([
            TextNode("and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            ],new_nodes)

    def test_just_image(self):
        text = "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        new_nodes = text_to_textnodes(text)
        self.assertEqual([
            TextNode("and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],new_nodes)

    def test_just_link(self):
        text = "and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertEqual([
            TextNode("and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ],new_nodes)
        
    def test_plain_text(self):
        text = "This is just a text node"
        new_nodes = text_to_textnodes(text)
        self.assertEqual([TextNode("This is just a text node", TextType.TEXT),],new_nodes)

    def test_all_types_back_to_back(self):
        text = "**text**_italic_`code block`![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertEqual([
            TextNode("text", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode("code block", TextType.CODE),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ],new_nodes)
        
    def test_multiple_same_types(self):
        text = "**bold****text**_italic__text_`code``block` this is the test **text**_bold_`italic`"
        new_nodes = text_to_textnodes(text)
        self.assertEqual([
            TextNode("bold", TextType.BOLD),
            TextNode("text", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode("text", TextType.ITALIC),
            TextNode("code", TextType.CODE),
            TextNode("block", TextType.CODE),
            TextNode(" this is the test ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode("bold", TextType.ITALIC),
            TextNode("italic", TextType.CODE),
            ],new_nodes)
        
    def test_bold_italic_same_word(self):
        text = "**_bold italic_** this is the test _**bold italic**_"
        with self.assertRaises(SyntaxError):
            text_to_textnodes(text)
            
    def test_type_at_start(self):
        text = "**bold** this is the test [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertEqual([
            TextNode("bold", TextType.BOLD),
            TextNode(" this is the test ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ],new_nodes)
    
    def unclosed_delimiter(self):
        text = "**bold this _is the test [link](https://boot.dev)"
        with self.assertRaises(ValueError):
            text_to_textnodes(text)
            
    def empty_string(self):
        text = ""
        new_nodes = text_to_textnodes(text)
        self.assertEqual([], new_nodes)

        
if __name__ == "__main__":
    unittest.main()
