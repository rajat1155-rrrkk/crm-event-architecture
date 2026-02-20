class LeadConsumer:
    def handle_lead_created(self, lead_data):
        print(f"[Consumer] Processing lead: {lead_data}")
