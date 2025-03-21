class Divide:
    def __init__(self, a, b): 
        self.a = a
        self.b = b

    def calculate(self):
        return self.a / self.b  

if __name__ == "__main__":  
    print(Divide(10, 2).calculate())
