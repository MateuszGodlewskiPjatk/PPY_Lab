class Stos:

    def __init__(self, max_size):
        self.stack = list()
        self.max_size = max_size

    def put(self, element):
        if len(self.stack) < self.max_size:
            self.stack.append(element)
        else:
            print("error")

    def __str__(self):
        return "Stack: " + str(self.stack) + "\nMax size: " + str(self.max_size)