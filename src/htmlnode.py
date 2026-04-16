
class HTMLNode:
    def __init__(self, tag = None, value= None, children= None, props= None):
        self.tag = tag 
        self.value = value
        self.children = children
        self.props = props 

    def to_html(self):
        raise NotImplementedError("Method not yet written")
    
    def props_to_html(self):
        
        if not self.props:
            return ""
        
        return "".join(f' {key}="{value}"' for key, value in self.props.items())
            
    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        
        # If something later on doest work change this back to if not self.value
        if self.value is None:
            raise ValueError("There is no value")

        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):

        if not self.tag:
            raise ValueError("No HTML tag found")
        
        if not self.children:
            raise ValueError("No child node found")
        
        # If string conversion happens later on remove it here
        children_html = "".join(str(child.to_html()) for child in self.children)
        
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
    