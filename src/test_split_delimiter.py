import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class testSplitDelimiter(unittest.TestCase):

    def test_assignment_example(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)  
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ])         
            
    def test_invalid_markdown_syntax_code(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(SyntaxError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_invalid_markdown_syntax_bold(self):
        node = TextNode("This is text with a **code block word", TextType.TEXT)
        with self.assertRaises(SyntaxError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_invalid_markdown_syntax_italic(self):
        node = TextNode("This is text with a _code block word", TextType.TEXT)
        with self.assertRaises(SyntaxError):
            split_nodes_delimiter([node], "_", TextType.ITALIC)
    
    def test_text_type_not_text(self):
        node = TextNode("This is text with a **bold text** word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a **bold text** word", TextType.BOLD)])

    def test_delimiter_italic(self):
        node = TextNode("This is text with a _italic text_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
            ])    

    def test_multiple_delimiters(self):
        node = TextNode("A `code1` and `code2` here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("A ", TextType.TEXT),
                TextNode("code1", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("code2", TextType.CODE),
                TextNode(" here", TextType.TEXT),
            ],
        )

    def test_no_delimiter(self):
        node = TextNode("Just plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("Just plain text", TextType.TEXT)])

    def test_non_text_node_passthrough(self):
        node = TextNode("already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("already bold", TextType.BOLD)])

    def test_delimiter_at_start(self):
        node = TextNode("**bold** at the start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" at the start", TextType.TEXT),
            ],
        )

    def test_unmatched_delimiter_raises(self):
        node = TextNode("This has a `broken delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_bold_with_spaces(self):
        node = TextNode("This is **bold words here** end", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold words here", TextType.BOLD),
                TextNode(" end", TextType.TEXT),
            ],
        )

    def test_no_spaces_around_delimiter(self):
        node = TextNode("x**bold**y", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("x", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode("y", TextType.TEXT),
            ],
        )

if __name__ == "__main__":
    unittest.main()
