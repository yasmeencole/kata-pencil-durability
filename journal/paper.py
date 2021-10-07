class Paper:
        """
        Paper represents an item that text can be written on. 
        Text will represent a string that is written on paper.
        """
        
        def __init__(self):
            self.text = ""
            
        def write(self, text):
            self.text = text