class Queue:
    # Stacks to be used in the operations.
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    # Enqueues 'X' into the queue. Returns true after enqueuing.
    def enqueue(self, X):
        self.stk1.append(X)
        return True

    """
      Dequeues top element from queue. Returns -1 if the queue is empty, 
      otherwise returns the popped element.
    """

    def dequeue(self):
        if self.stk2:
            return self.stk2.pop()
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        return -1 if not self.stk2 else self.stk2.pop()
