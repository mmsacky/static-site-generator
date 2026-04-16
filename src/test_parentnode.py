import unittest

from htmlnode import LeafNode, ParentNode

class testParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )    

    def test_to_html_assignment_example(self):
         bold_node = LeafNode("b", "Bold text")
         italic_node = LeafNode("i", "italic text")        
         normal_text_node = LeafNode(None, "Normal text")
         normal_text_node2 = LeafNode(None, "Normal text")  
         parent_node = ParentNode("p",[bold_node, normal_text_node, italic_node, normal_text_node2])
         self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_deep_nesting(self):
        node = LeafNode("span", "end")
        for _ in range(3):
            node = ParentNode("div", [node])
        self.assertEqual(
            node.to_html(),
            "<div><div><div><span>end</span></div></div></div>"
        )

    def test_to_html_mixed_children(self):
        parent_node = ParentNode("p", [
            LeafNode(None, "Hello "),
            LeafNode("b", "world"),
            LeafNode(None, "!")
        ])
        self.assertEqual(
            parent_node.to_html(),
            "<p>Hello <b>world</b>!</p>"
        )

    def test_to_html_empty_text_nodes(self):
        parent_node = ParentNode("p", [
            LeafNode("b", ""),
            LeafNode(None, "")
        ])
        self.assertEqual(
            parent_node.to_html(),
            "<p><b></b></p>"
        )

    def test_to_html_numbers_only(self):
        parent_node = ParentNode("p", [
            LeafNode(None, 0),
            LeafNode(None, 1),
            LeafNode(None, 2)
        ])
        self.assertEqual(
            parent_node.to_html(),
            "<p>012</p>"
        )

    def test_to_html_nested_mixed(self):
        parent_node = ParentNode("div", [
            LeafNode(None, "Start "),
            ParentNode("span", [
                LeafNode("b", "bold"),
                LeafNode(None, " and normal")
            ]),
            LeafNode(None, " end")
        ])
        self.assertEqual(
            parent_node.to_html(),
            "<div>Start <span><b>bold</b> and normal</span> end</div>"
        )

    def test_to_html_many_children(self):
        children = [LeafNode(None, "x") for _ in range(5)]
        parent_node = ParentNode("p", children)
        self.assertEqual(
            parent_node.to_html(),
            "<p>xxxxx</p>"
        )

    def test_to_html_text_only_children(self):
        parent_node = ParentNode("p", [
            LeafNode(None, "Just "),
            LeafNode(None, "text")
        ])
        self.assertEqual(
            parent_node.to_html(),
            "<p>Just text</p>"
        )

    def test_repr(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("H1", child_node, {"href": "https://baraka.media", "target":"_blank"})
        self.assertEqual("ParentNode(H1, LeafNode(span, child, None), {'href': 'https://baraka.media', 'target': '_blank'})", repr(parent_node))

if __name__ == "__main__":
    unittest.main()
