import unittest

from split_nodes_image_or_link import split_nodes_link, split_nodes_image
from textnode import TextNode, TextType

class testSplitDelimiter(unittest.TestCase):
    
    def test_no_link(self):
        node = TextNode("This is text with a link", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("This is text with a link", TextType.TEXT,)], new_nodes)

    def test_no_image(self):
        node = TextNode("This is text with a link", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("This is text with a link", TextType.TEXT,)], new_nodes)
        
    def test_link_at_start(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) - that's your link",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
             TextNode(" - that's your link", TextType.TEXT,)
             ],
            new_nodes)

    def test_image_at_start(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) - that's your link",
            TextType.TEXT,
            )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
             TextNode(" - that's your link", TextType.TEXT,)
             ],
            new_nodes)
        
    def test_link_at_end(self):
        node = TextNode(
            "This is a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [TextNode("This is a link ", TextType.TEXT,),
             TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),         
             ],
            new_nodes)
        
    def test_image_at_end(self):
        node = TextNode(
            "This is a link ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [TextNode("This is a link ", TextType.TEXT,),
             TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),         
             ],
            new_nodes)        

  
    def test_multiple_links(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                          TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                          TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                          TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")],new_nodes)

    def test_multiple_images(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)![image](https://i.imgur.com/zjjcJKZ.png)![image](https://i.imgur.com/zjjcJKZ.png)![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                          TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                          TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                          TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")],new_nodes)

    def test_multiple_links_with_text_between(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) and [to boot dev](https://www.boot.dev) the [to boot dev](https://www.boot.dev) if [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                          TextNode(" and ", TextType.TEXT,),
                          TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                          TextNode(" the ", TextType.TEXT,),
                          TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                          TextNode(" if ", TextType.TEXT,),
                          TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")],new_nodes)

    def test_multiple_images_with_text_between(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and ![image](https://i.imgur.com/zjjcJKZ.png) the ![image](https://i.imgur.com/zjjcJKZ.png) if ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                          TextNode(" and ", TextType.TEXT,),
                          TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                          TextNode(" the ", TextType.TEXT,),
                          TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                          TextNode(" if ", TextType.TEXT,),
                          TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")],new_nodes)
            
    def test_only_link(self):
        node = TextNode("[to boot dev](https://www.boot.dev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")], new_nodes)

    def test_only_image(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")], new_nodes)
        
    def test_bold_node_in_split_link(self):
        node = TextNode("**to boot dev**", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual([TextNode("**to boot dev**", TextType.TEXT)], new_nodes)

    def test_bold_node_in_split_image(self):
        node = TextNode("**to boot dev**", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual([TextNode("**to boot dev**", TextType.TEXT)], new_nodes)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_split_images_with_image_and_link(self):
            node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another [a link to an image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_image([node])
            self.assertEqual([
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another [a link to an image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            ],new_nodes)

    def test_split_link_with_link_and_image(self):
            node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another [a link to an image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_link([node])
            self.assertEqual([
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ", TextType.TEXT),
                TextNode("a link to an image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],new_nodes)

if __name__ == "__main__":
    unittest.main()
