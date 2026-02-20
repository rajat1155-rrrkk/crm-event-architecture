class LeadConsumer:
    def handle_lead_created(self, lead_data):
        print(f"[Consumer] Processing lead: {lead_data}")

        # Simulate failure for specific condition
        if lead_data.get("industry") == "FinTech":
            raise Exception("Simulated processing failure")
