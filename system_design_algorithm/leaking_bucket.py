from time import sleep


class LeakingBucket:

    def __init__(self, capacity):
        self._capacity = capacity
        self._queue = [1, 2, 3, 4]

    def insert_queue(self, request):
        if len(self._queue) < self._capacity:
            self._queue.append(request)
            return self._queue
        else:
            return f"Dropped request {request}"

    def dequeue(self):
        sleep(2)
        self._queue.pop(0)
        print("Queue pass value..")


if __name__ == "__main__":
    bucket = LeakingBucket(5)
    print(f"insert = 20", bucket.insert_queue(20))
    print(f"insert = 30", bucket.insert_queue(30))
    print(f"insert = 40", bucket.insert_queue(40))
    bucket.dequeue()
    bucket.dequeue()
    print(f"insert = 30", bucket.insert_queue(30))
    print(f"insert = 40", bucket.insert_queue(40))
    print(f"insert = 50", bucket.insert_queue(50))