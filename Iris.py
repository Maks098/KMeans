class Iris:
    def __init__(self,dataInput,speciment):
        self.inputarray=dataInput.split(",")
        self.speciment=speciment
        self.inputarray.pop()