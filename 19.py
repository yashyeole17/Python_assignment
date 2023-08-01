
#Q19    Write Python Program to Perform Queue Operations



class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue.pop(0)
        print(f"Dequeued: {item}")
        return item

    def size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", self.queue)


# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()

queue.dequeue()
queue.display()

print("Queue size:", queue.size())

