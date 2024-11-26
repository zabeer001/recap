from collections import deque

# Initialize the queue
queue = deque()

# Function to enqueue an item
def enqueue(q, item):
    q.append(item)

# Function to dequeue an item
def dequeue(q):
    if q:
        return q.popleft()
    else:
        raise IndexError("Dequeue from empty queue")

# Function to check if the queue is empty
def is_empty(q):
    return len(q) == 0

# Function to peek at the front item
def peek(q):
    if q:
        return q[0]
    else:
        raise IndexError("Peek from empty queue")

# Example usage
enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)


print("Queue after enqueues:", list(queue))  # Output: [10, 20, 30]

print("Dequeued element:", dequeue(queue))  # Output: 10
print("Queue after dequeue:", list(queue))  # Output: [20, 30]
print("Front element:", peek(queue))        # Output: 20
