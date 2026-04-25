import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )   

    def test_multiple_block_types(self):
        md = """# Heading

A paragraph of text.

- item one
- item two"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "# Heading",
            "A paragraph of text.",
            "- item one\n- item two",
            ])

    def test_multi_line_paragraph(self):
        md = """Hi! I'm your first Markdown file in **StackEdit**.
If you want to learn about StackEdit, you can read me. If you want to play with Markdown,
you can edit me. Once you have finished with me, you can create new files by opening the
**file explorer** on the left corner of the navigation bar."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Hi! I'm your first Markdown file in **StackEdit**.\nIf you want to learn about StackEdit, you can read me. If you want to play with Markdown,\nyou can edit me. Once you have finished with me, you can create new files by opening the\n**file explorer** on the left corner of the navigation bar."
            ],
        )

    def test_many_blocks(self):
        md = """# The Grand Adventure

Once upon a time in a land far away, there was a brave hero.

## Chapter 1: The Beginning

The hero set out on a journey to find the lost treasure.

- Pack supplies
- Study the map
- Say goodbye to family

## Chapter 2: The Journey

The road was long and treacherous, but the hero pressed on.

1. Cross the river
2. Climb the mountain
3. Enter the forest

## Chapter 3: The End

The hero found the treasure and returned home victorious."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(len(blocks), 10)
        
    def test_whitespace_only_blocks(self):
        md = "Real block\n\n   \n\nAnother block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Real block", "Another block"])
    
    def test_empty_string(self):
        blocks = markdown_to_blocks("")
        self.assertEqual(blocks, [])
 
    def test_code_markdown_to_blocks(self):
        md = """       
```python
def greet(name):
return f"Hello, {name}!"
print(greet("Michael"))
```
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,['```python\ndef greet(name):\nreturn f"Hello, {name}!"\nprint(greet("Michael"))\n```'])       
        
if __name__ == "__main__":
    unittest.main()