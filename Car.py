class car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def carDisplay(self):
        print(f"Car name is {self.name},Model is {self.model},color is {self.color}")