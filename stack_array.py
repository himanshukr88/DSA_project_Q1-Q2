class Stack:
    """Fixed-capacity stack backed by a plain array (no built-in stack library)."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity   # pre-allocated array
        self.top = -1                   # -1 means empty

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, x):
        if self.is_full():
            print(f"Stack Overflow: cannot push {x}")
            return False
        self.top += 1
        self.data[self.top] = x
        return True

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: cannot pop from empty stack")
            return None
        x = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return x

    def peek(self):
        if self.is_empty():
            print("Stack is empty: nothing to peek")
            return None
        return self.data[self.top]

    def display(self):
        if self.is_empty():
            print("Stack: [] (empty)")
            return
        print("Stack (bottom -> top):", self.data[: self.top + 1])


if __name__ == "__main__":
    s = Stack(3)
    s.pop()            # underflow
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)         # overflow
    s.display()
    print("Peek:", s.peek())
    print("Popped:", s.pop())
    s.display()
    s.pop(); s.pop()
    s.pop()            # underflow again
    s.display()
