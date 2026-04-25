from htmlnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from text_to_textnode import text_to_textnodes
from markdown_to_blocks import BlockType, markdown_to_blocks, block_to_block_type

def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    nodes = []


    for block in blocks:

        block_type = block_to_block_type(block)
               
        if block_type == BlockType.PARAGRAPH:
            clean_text = block.replace("\n"," ") 
            paragraph_node = ParentNode('p', text_to_children(clean_text))  
            nodes.append(paragraph_node)     
            
        elif block_type == BlockType.HEADING:
            clean_text = block.replace("\n"," ") 
            heading_node = ParentNode(get_heading_tag(clean_text), text_to_children(remove_heading_hash(clean_text)))           
            nodes.append(heading_node)                 
               
        elif block_type == BlockType.CODE:
            code_text_node = TextNode(remove_code_back_ticks(block),TextType.TEXT)            
            code_node = ParentNode('code', [text_node_to_html_node(code_text_node)])  
            pre_node = ParentNode('pre',[code_node]) 

            nodes.append(pre_node)
               
        elif block_type == BlockType.QUOTE:
            items = []
            lines = block.split("\n")
            
            for line in lines:
                 stripped = line.removeprefix("> ")
                 items.append(stripped)

            quote_node = ParentNode('blockquote', text_to_children(" ".join(items)))
            nodes.append(quote_node)
            
        elif block_type == BlockType.UNORDERED_LIST:
            items= []
            lines = block.split("\n")
            
            for line in lines:
                li_node = ParentNode('li', text_to_children(line.removeprefix("- ")))
                items.append(li_node)
            ul_node = ParentNode('ul', items)
        
            nodes.append(ul_node)
        
        elif block_type == BlockType.ORDERED_LIST:
            items= []
            lines = block.split("\n")
            
            for line in lines:
                li_node = ParentNode('li', text_to_children(line.split(". ", 1)[1]))
                items.append(li_node)
            ol_node = ParentNode('ol', items)
        
            nodes.append(ol_node)
        else:
            raise ValueError(f"unknown block type: {block_type}")
        
    return ParentNode("div", nodes)
    
    
def text_to_children(text):
    inline_markdown_nodes = []
    children = text_to_textnodes(text)

    for child in children:
        inline_markdown_nodes.append(text_node_to_html_node(child))  
    return inline_markdown_nodes      

def get_heading_tag(text):
    
    if text.startswith("# "):
        return "h1"  
    if text.startswith("## "):
        return "h2"
    if text.startswith("### "):
        return "h3" 
    if text.startswith("#### "):
        return "h4"
    if text.startswith("##### "):
        return "h5" 
    if text.startswith("###### "):
        return "h6"                      

def remove_heading_hash(text):
    
    if text.startswith("# "):
        return text.replace("# ","")
    elif text.startswith("## "):
        return text.replace("## ","")
    elif text.startswith("### "):
        return text.replace("### ","")
    elif text.startswith("#### "):
        return text.replace("#### ","")
    elif text.startswith("##### "):
        return text.replace("##### ","")
    elif text.startswith("###### "):
        return text.replace("###### ","")
    else:
        raise ValueError(f"invalid heading: {text}")

def remove_code_back_ticks(original_text):

    lines = original_text.split("\n")
    inner = "\n".join(lines[1:-1])
    return inner + "\n"