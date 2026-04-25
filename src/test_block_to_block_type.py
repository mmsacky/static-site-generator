import unittest

from markdown_to_blocks import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_H1_heading(self):
        block = '# This is a H1 heading'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_H2_heading(self):
        block = '## This is a H2 heading'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
    
    def test_H3_heading(self):
        block = '### This is a H3 heading'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_H4_heading(self):
        block = '#### This is a H4 heading'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_H5_heading(self):
        block = '##### This is a H5 heading'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_H6_heading(self):
        block = '###### This is a H6 heading'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code_block(self):
        block = '```\npython\ndef hello_world():\nprint("Hello, world!")\n```'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_code_multi_line_block(self):
        block = '```python\ndef greet(name):\nreturn f"Hello, {name}!"\nprint(greet("Michael"))\n```'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
        
    def test_quote_block(self):
        block = '> This is the first paragraph of the quote.\n>\n> This is the second paragraph, separated by a blank line containing a ">".'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)       
        
    def test_unorded_list_block(self):
        block = '- This is a list\n- with items'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)       
        
    def test_ordered_block(self):
        block = '1. the\n2. quick\n3. fox'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)   
        
    def test_7_hashs_heading(self):
        block = '"####### not a heading"'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)          

    def test_not_code(self):
        block = "```code```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)         
    
    def test_not_quote(self):
        block = "> valid line\nnot a quote\n> valid line" 
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)  

    def test_not_unordered_list(self):
        block = "-no space\n- valid"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)          
    
    def test_not_ordered_list(self):
        block = "2. wrong start\n3. still wrong"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)  

    def test_not_ordered_list_2(self):
        block = "1. first\n3. skipped two"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)     
    
    def test_not_unordered_list(self):
        block = "- valid first\n line not a list item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)         
        
if __name__ == "__main__":
    unittest.main()
    
    