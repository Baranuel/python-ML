import time
from collections import deque

# -----------------------------
# Exercise 1: Queue with fixed capacity
# -----------------------------
class FixedQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, item):
        if len(self.queue) >= self.capacity:
            print("Queue Overflow!")
        else:
            self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            print("Queue Underflow!")
            return None
        return self.queue.pop(0)


# -----------------------------
# Exercise 2: Compare list vs deque enqueue times
# -----------------------------
def compare_enqueue(n=100000):
    data = range(n)

    # Using list
    lst = []
    start = time.time()
    for item in data:
        lst.append(item)  # O(1) amortized
    list_time = time.time() - start

    # Using deque
    dq = deque()
    start = time.time()
    for item in data:
        dq.append(item)  # O(1)
    deque_time = time.time() - start

    return list_time, deque_time


# -----------------------------
# Exercise 3: Prime numbers < 200
# -----------------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(200) if is_prime(n)]


# -----------------------------
# Exercise 4: Sort + remove duplicates
# -----------------------------
def unique_sorted(x):
    return sorted(set(x))


# -----------------------------
# Example runs
# -----------------------------
if __name__ == "__main__":
    print("Exercise 1 Example:")
    q = FixedQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)  # Overflow
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())  # Underflow

    print("\nExercise 2 Example:")
    list_time, deque_time = compare_enqueue(500000)
    print(f"List enqueue time: {list_time:.4f}s")
    print(f"Deque enqueue time: {deque_time:.4f}s")

    print("\nExercise 3 Example:")
    print(primes)

    print("\nExercise 4 Example:")
    print(unique_sorted([5, 3, 1, 2, 3, 5, 4, 1]))
