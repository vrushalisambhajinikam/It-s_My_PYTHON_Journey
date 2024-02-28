class animal:
    multicellular=True
    eukaryotic=True
    def breadthe(self):
        print("i breadthe oxygen")
    def feed(self):
        print("i eat food")
class herbivorous(animal):
    def feed(self):
        
        print("i eat only plants .i am vegetarian")
herbi=herbivorous()
herbi.feed()
herbi.breadthe()
