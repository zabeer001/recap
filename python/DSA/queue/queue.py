class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Add item to the end of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove item from the front of the queue
        raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]  # Peek at the front item
        raise IndexError("Peek from empty queue")

    def size(self):
        return len(self.items)  # Get the size of the queue

    # Make the Queue iterable by defining __iter__
    def __iter__(self):
        return iter(self.items)  # Return an iterator for the list of items

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Convert queue to list using the iterable interface
li = list(queue) # Output: [10, 20, 30]

sum = li[0] * li[1]
print(sum)