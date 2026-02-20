import unittest
from retry_handler.retry_handler import RetryHandler
from dead_letter.dead_letter_queue import DeadLetterQueue


class TestResiliencePatterns(unittest.TestCase):

    def test_retry_success_after_failure(self):
        retry = RetryHandler(max_retries=3, delay=0)

        attempts = {"count": 0}

        def flaky_function():
            attempts["count"] += 1
            if attempts["count"] < 2:
                raise Exception("Temporary failure")
            return "Success"

        result = retry.execute(flaky_function)
        self.assertEqual(result, "Success")
        self.assertEqual(attempts["count"], 2)

    def test_retry_exceeds_and_moves_to_dlq(self):
        retry = RetryHandler(max_retries=2, delay=0)
        dlq = DeadLetterQueue()

        def always_fail():
            raise Exception("Permanent failure")

        try:
            retry.execute(always_fail)
        except Exception:
            dlq.add("TestEvent", {"data": "sample"})

        self.assertEqual(len(dlq.failed_events), 1)


if __name__ == "__main__":
    unittest.main()
