class Outfit:

    def __init__(self, top, bottom, shoes):
        self.top = top
        self.bottom = bottom
        self.shoes = shoes

#The inputs will be colours so that we test if the outfit is coordinated by colour

    def matching(self):
        if self.top == self.bottom == self.shoes:
            print("I love your outfit!")
        elif self.top == self.bottom:
            print("Hmm, maybe try different shoes")
        elif self.top == self.shoes:
            print("Hmm, maybe try different bottoms")
        elif self.bottom == self.shoes:
            print("Hmm, maybe try a different top")
        else: print("Get back in that dressing room!")
