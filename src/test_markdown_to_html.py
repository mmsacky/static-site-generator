import unittest

from markdown_to_html import markdown_to_html_node

class TestMarkDownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headings(self):
        md = """
# This is a h1 Heading

## This is a h2 Heading

### This is a h3 Heading

#### This is a h4 Heading

##### This is a h5 Heading

###### This is a h6 Heading

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a h1 Heading</h1><h2>This is a h2 Heading</h2><h3>This is a h3 Heading</h3><h4>This is a h4 Heading</h4><h5>This is a h5 Heading</h5><h6>This is a h6 Heading</h6><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_code(self): 
        md = """   
## Mixed Example

Here’s a quick example combining text and code:

```
python
numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers]
print(squared)
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><h2>Mixed Example</h2><p>Here’s a quick example combining text and code:</p><pre><code>python\nnumbers = [1, 2, 3, 4, 5]\nsquared = [n**2 for n in numbers]\nprint(squared)\n</code></pre></div>")

    def test_code_preserve(self): 
        md = """   
```
**not bold** and _not italic_
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><pre><code>**not bold** and _not italic_\n</code></pre></div>")

    def test_quote(self): 
        md = """   
> Quoted Heading
> **Tip:** You can include _formatting_ inside a quote.
> You can even include headings and other elements inside a blockquote.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
                         "<div><blockquote>Quoted Heading <b>Tip:</b> You can include <i>formatting</i> inside a quote. You can even include headings and other elements inside a blockquote.</blockquote></div>"
                         )

    def test_unordered_list(self): 
        md = """   
- Item one
- Item two
- Item three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><ul><li>Item one</li><li>Item two</li><li>Item three</li></ul></div>")

    def test_unordered_list(self): 
        md = """   
1. Item one
2. Item two
3. Item three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><ol><li>Item one</li><li>Item two</li><li>Item three</li></ol></div>")

    def test_unordered_list_with_inline_formating(self): 
        md = """   
1. First **item**
2. Second _item_
3. Third `item`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><ol><li>First <b>item</b></li><li>Second <i>item</i></li><li>Third <code>item</code></li></ol></div>")
     
    def test_inline_markdown_inside_headings(self): 
        md = "# Hello **world**"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><h1>Hello <b>world</b></h1></div>")
        
#~~~~~~~~~~~~~~~~~~~~
    def test_mixed_blocks(self):
        md = """
# Heading

This is a paragraph with **bold** text.

- list item one
- list item two

> a quoted line
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading</h1><p>This is a paragraph with <b>bold</b> text.</p><ul><li>list item one</li><li>list item two</li></ul><blockquote>a quoted line</blockquote></div>",
            )
        
    def test_all_heading_levels(self):
        md = """
# h1

## h2

### h3

#### h4

##### h5

###### h6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>h1</h1><h2>h2</h2><h3>h3</h3><h4>h4</h4><h5>h5</h5><h6>h6</h6></div>",
            )    
        
    def test_heading_with_inline(self):
        md = "# Hello **world** and _friends_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Hello <b>world</b> and <i>friends</i></h1></div>",
            )    
    
    def test_links_and_images(self):
        md = "Click [here](https://boot.dev) or see ![pic](https://img.com/x.png)"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>Click <a href="https://boot.dev">here</a> or see <img src="https://img.com/x.png" alt="pic"></img></p></div>',
            )
    
    def test_ordered_list_inline(self):
        md = """
1. First **item**
2. Second _item_
3. Third `item`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First <b>item</b></li><li>Second <i>item</i></li><li>Third <code>item</code></li></ol></div>",
            )

    def test_multiline_quote(self):
        md = """
> Line one of the quote
> Line two of the quote
> Line three with **bold**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Line one of the quote Line two of the quote Line three with <b>bold</b></blockquote></div>",
            )
    
    def test_unordered_list_inline(self):
        md = """
- apple **pie**
- banana _split_
- cherry `cobbler`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>apple <b>pie</b></li><li>banana <i>split</i></li><li>cherry <code>cobbler</code></li></ul></div>",
            )   
    
if __name__ == "__main__":
    unittest.main()        
