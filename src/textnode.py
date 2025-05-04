from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url 

    def __eq__(self, other):
        #checks if other is a TextNode
        if not isinstance(other, TextNode):
            return NotImplemented
        
        #if self = other return True
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    #reports what the TextNode is
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"