class CircularQueue:
    """Circular queue using an array and a size counter.

    The counter `count` removes the ambiguity of front == rear:
    count == 0 -> empty, count == capacity -> full.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0      # index of first element
        self.rear = -1      # index of last element
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, x):
        if self.is_full():
            print(f"Queue Overflow: cannot enqueue {x}")
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = x
        self.count += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow: cannot dequeue from empty queue")
            return None
        x = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return x

    def get_front(self):
        if self.is_empty():
            print("Queue is empty: no front element")
            return None
        return self.data[self.front]

    def display(self):
        if self.is_empty():
            print("Queue: [] (empty)")
            return
        items = [self.data[(self.front + i) % self.capacity] for i in range(self.count)]
        print("Queue (front -> rear):", items)


if __name__ == "__main__":
    q = CircularQueue(4)
    q.dequeue()                    # underflow
    for v in (1, 2, 3, 4):
        q.enqueue(v)
    q.enqueue(5)                   # overflow
    q.display()
    print("Dequeued:", q.dequeue())
    print("Dequeued:", q.dequeue())
    q.enqueue(5)                   # reuses freed slots (wrap-around)
    q.enqueue(6)
    q.display()
    print("Front:", q.get_front())
    q.enqueue(7)                   # full again
