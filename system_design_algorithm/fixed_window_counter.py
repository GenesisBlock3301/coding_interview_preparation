from time import time


class FixedWindow:

    def __init__(self, interval_time, capacity):
        self._interval_time = interval_time
        self._capacity = capacity
        self.timestamp = 1

    def access_or_dropped(self, request):
        for r in request:
            val = 0
            if r > self._capacity:
                val = r - self._capacity
                print(f"dropped {r - self._capacity} request")
            self.timestamp += self._interval_time
            print(f"Successfully added {val if val != 0 else r}")


bucket = FixedWindow(1, 3)

bucket.access_or_dropped([4, 3, 2, 3, 1, 10])
