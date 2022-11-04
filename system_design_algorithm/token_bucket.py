from time import time, sleep


class TokenBucket:

    def __init__(self, tokens, fill_rate):
        """
        tokens:  is the total number of token in bucket.
        fill_rate: is the rate in token/sec that bucket
        will be refilled.
        """
        self.capacity = float(tokens)
        self._tokens = float(tokens)
        self.fill_rate = fill_rate
        self.timestamp = time()

    def consume(self, tokens):
        """
        consume tokens from the bucket. Returns true if there were
        sufficient tokens otherwise false.
        """

        if tokens <= self._tokens:
            self._tokens -= tokens
        else:
            return False
        return True

    def get_tokens(self):
        if self._tokens < self.capacity:
            now = time()
            delta = self.fill_rate * (now - self.timestamp)
            self._tokens = min(self.capacity, self._tokens + delta)
            self.timestamp = now
        return self._tokens


if __name__ == "__main__":
    bucket = TokenBucket(80, 1)
    print(f"tokens = {bucket.get_tokens()}")
    print(f"consume(10)={bucket.consume(10)}")
    print(f"consume(10)={bucket.consume(10)}")
    sleep(1)
    print(f"tokens = {bucket.get_tokens()}")
    sleep(1)
    print(f"tokens = {bucket.get_tokens()}")
    print(f"consume(90)={bucket.consume(90)}")
    print(f"tokens = {bucket.get_tokens()}")