class Stack:
    def __init__(self, limit):
        self.st = [None] * limit
        self.top = -1
        self.lim = limit

    def push(self, x):
        if self.top >= self.lim - 1:
            print("Stack is full")
            return -1
        self.top += 1
        self.st[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
            return -1
        k = self.st[self.top]
        self.top -= 1
        return k

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return -1
        return self.st[self.top]

    def find(self, x):
        found = False
        for i in range(self.top, -1, -1):
            if self.st[i] == x:
                print(f"Found {x} at index {i}")
                found = True
        if not found:
            print("Not found")

    def replace(self, x, y):
        for i in range(self.top + 1):
            if self.st[i] == x:
                self.st[i] = y
                print(f"Replaced {x} with {y} at index {i}")

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top >= self.lim - 1
