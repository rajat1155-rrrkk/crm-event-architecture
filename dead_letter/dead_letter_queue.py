class DeadLetterQueue:
    def __init__(self):
        self.failed_events = []

    def add(self, event_type, event_data):
        self.failed_events.append((event_type, event_data))
        print(f"[DLQ] Event moved to dead letter queue: {event_type} - {event_data}")
