from textnode import TextNode, TextType
from extract_links import extract_markdown_links, extract_markdown_images

def split_nodes_link(old_nodes):
    
    new_nodes = []
    
    for old_node in old_nodes:

        extracted_achor_text_and_link = extract_markdown_links(old_node.text)
        
        if not len(extracted_achor_text_and_link):
            new_nodes.append(old_node)
        else:
     
            remaining_text = old_node.text 
            
            for items in extracted_achor_text_and_link:
                
                link_text = items[0]
                link = items[1]
                    
                sections = (remaining_text.split(f'[{link_text}]({link})',1))
                
                if sections[0] != "":               
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))           
                new_nodes.append(TextNode(link_text, TextType.LINK, link))
                remaining_text = sections[1]
                    
            if remaining_text != "":
                new_nodes.append(TextNode(sections[1], TextType.TEXT))
 
    return new_nodes 



def split_nodes_image(old_nodes):
    
    new_nodes = []
    
    for old_node in old_nodes:

        extracted_alt_text_and_link = extract_markdown_images(old_node.text)
        
        if not len(extracted_alt_text_and_link):
            new_nodes.append(old_node)
        else:
     
            remaining_text = old_node.text 
            
            for items in extracted_alt_text_and_link:
                
                alt_text = items[0]
                link = items[1]
                    
                sections = (remaining_text.split(f'![{alt_text}]({link})',1))
                
                if sections[0] != "":               
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))           
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, link))
                remaining_text = sections[1]
                    
            if remaining_text != "":
                new_nodes.append(TextNode(sections[1], TextType.TEXT))
 
    return new_nodes 