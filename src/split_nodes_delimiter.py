from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for old_node in old_nodes:
        
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
 
        elif delimiter in old_node.text:

            if old_node.text.count(delimiter) % 2 == 0:

                split_text = (old_node.text.split(delimiter))
                for index, text in enumerate(split_text):
                        if text == "":
                            continue
                        if index % 2 == 0:
                            new_nodes.append(TextNode(text, TextType.TEXT))
                        else:
                            new_nodes.append(TextNode(text, text_type))               
            else:
                raise SyntaxError("invalid Markdown syntax")
        else: 
            new_nodes.append(old_node)

    return new_nodes