class LeadPublisher:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def create_lead(self, lead_data):
        print(f"[Publisher] Lead created: {lead_data}")
        self.event_bus.publish("LeadCreated", lead_data)
