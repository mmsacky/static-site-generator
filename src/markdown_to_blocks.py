from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    filtered = []
    
    blocks = markdown.split("\n\n")
    
    for block in blocks:
        block = block.strip()
        if block:
            filtered.append(block)
    
    return filtered

def block_to_block_type(block):
    
    heading_prefix = ("# ","## ","### ","#### ","##### ","###### ")
    num = 1
  
    if block.startswith(heading_prefix):       
        return BlockType.HEADING
    
    elif block.startswith("```"):
        lines  =  block.split("\n")
        if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"): 
            return BlockType.CODE
        return BlockType.PARAGRAPH  
    
    elif block.startswith(">"):
        for line in block.split("\n"):
            if not line.startswith(">"):
                return BlockType.PARAGRAPH 
        return BlockType.QUOTE
    
    elif block.startswith("- "):  
        for line in block.split("\n"): 

            if not line.startswith("- "):
                return BlockType.PARAGRAPH         
        return BlockType.UNORDERED_LIST
    
    elif block.startswith(f"{num}. "):   
        for line in block.split('\n'):
            if not line.startswith(f"{num}. "):
                return BlockType.PARAGRAPH 
            num+=1
        return BlockType.ORDERED_LIST   
    
    else:
        return BlockType.PARAGRAPH     