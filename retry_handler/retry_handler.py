import time


class RetryHandler:
    def __init__(self, max_retries=3, delay=1):
        self.max_retries = max_retries
        self.delay = delay

    def execute(self, func, *args, **kwargs):
        attempt = 0

        while attempt < self.max_retries:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                attempt += 1
                print(f"[Retry] Attempt {attempt}/{self.max_retries} failed: {e}")
                time.sleep(self.delay)

        raise Exception("Max retries exceeded")
