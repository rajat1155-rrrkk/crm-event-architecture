from event_bus.event_bus import EventBus
from publishers.lead_publisher import LeadPublisher
from consumers.lead_consumer import LeadConsumer


def run_demo():
    bus = EventBus()

    consumer = LeadConsumer()
    bus.subscribe("LeadCreated", consumer.handle_lead_created)

    publisher = LeadPublisher(bus)
    publisher.create_lead({"name": "Enterprise Corp", "industry": "FinTech"})


if __name__ == "__main__":
    run_demo()
