class Pencil:
        """
        Pencil is a device that will allow us to write text on paper. 
        Text will represent a string that is written on paper.
        
        lead_durability = the current lead durability of the pencil tip.
        """
        
        def __init__(self, lead_durability):
            self.lead_durability = lead_durability
            self.inital_lead_durability = lead_durability
            
        def write(self, input, paper):
            post_degradation_input = self.lead_durability(input)
            page_text = paper.write(post_degradation_input)
            return page_text
        
        def degradation_cost(self, character):
            if character.isupper():
                return 2
            elif character.islower():
                return 1
            else:
                return 0
            
        def sharpen(self):
            self.lead_durability = self.inital_lead_durability