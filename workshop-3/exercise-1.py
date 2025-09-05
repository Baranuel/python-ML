
# Use a Python list to implement a queue with a fixed finite capacity.
# Make sure that the ENQUEUE and DEQUEUE functions signal when there
# is queue underflow and overflow.

class Queue:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.queue = []
    
    def enqueue(self, number:int):
        """ Add an element to the end of the queue """

        if len(self.queue) >= self.capacity:
            print("Capacity of the queue has been reached")
            return
        else: self.queue.append(number)
        print(self.queue)
    
    def dequeue(self, index:int = None):
        """ Remove an element from the queue """

        if len(self.queue) <= 0:
            print("There are no items in the queue")

        if index is None: self.queue.pop(0)
        else: self.queue.pop(index)

        print(self.queue)


def main():
    queue = Queue(5)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue.dequeue()
    queue.dequeue(1)

if __name__ == "__main__":
    main()