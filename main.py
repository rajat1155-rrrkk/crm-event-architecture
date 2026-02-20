from event_bus.event_bus import EventBus
from publishers.lead_publisher import LeadPublisher
from consumers.lead_consumer import LeadConsumer
from retry_handler.retry_handler import RetryHandler
from dead_letter.dead_letter_queue import DeadLetterQueue


def run_demo():
    bus = EventBus()
    retry_handler = RetryHandler(max_retries=2, delay=1)
    dlq = DeadLetterQueue()

    consumer = LeadConsumer()

    def wrapped_handler(data):
        try:
            retry_handler.execute(consumer.handle_lead_created, data)
        except Exception:
            dlq.add("LeadCreated", data)

    bus.subscribe("LeadCreated", wrapped_handler)

    publisher = LeadPublisher(bus)
    publisher.create_lead({"name": "Enterprise Corp", "industry": "FinTech"})


if __name__ == "__main__":
    run_demo()
