# Do an experiment which demonstrates the difference in running time
# for the ENQUEUE operation when you use a list or a collections.deque
# for implementing a queue with an unbounded capacity

import time
from collections import deque


def main():
    items_amount = 100000

    list = []
    queue = deque()

    list_start = time.time()
    for item in range(items_amount):
        list.append(0, item)
    list_end = time.time() - list_start;

    queue_start = time.time()
    for item in range(items_amount):
        queue.append(item)
    queue_end = time.time() - queue_start;

    print(f"List ENQUEUE time: {list_end:.6f} seconds")
    print(f"Deque ENQUEUE time: {queue_end:.6f} seconds")

if __name__ == "__main__":
    main()