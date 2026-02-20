# CRM Event Architecture

Enterprise-style event-driven CRM architecture simulation.

This repository models asynchronous CRM workflow processing using event publishing, event consumers, retry mechanisms, and dead-letter handling patterns commonly used in distributed enterprise systems.

---

## 🏗 Architecture Overview

This project simulates an event-driven CRM ecosystem where domain actions generate events that are processed asynchronously by independent consumers.

Core architectural layers:

- Event Bus Layer (Publisher–Subscriber pattern)
- Domain Event Publishers
- Event Consumers
- Retry & Backoff Handler
- Dead Letter Queue Simulation
- Unit Testing Layer

The design mirrors enterprise integration patterns used in Salesforce-led and distributed CRM ecosystems.

---

## 🔄 High-Level Event Flow


Lead Created
↓
Event Published (LeadCreated)
↓
Event Bus
↓
Consumer Processing
↓
[If Failure]
↓
Retry Handler (Controlled Attempts)
↓
Dead Letter Queue (If Retries Exhausted)


This models real-world distributed system behavior where failure handling and resiliency are first-class architectural concerns.

---

## 📦 Project Structure


crm-event-architecture/
│
├── event_bus/
│ └── event_bus.py
│
├── publishers/
│ └── lead_publisher.py
│
├── consumers/
│ └── lead_consumer.py
│
├── retry_handler/
│ └── retry_handler.py
│
├── dead_letter/
│ └── dead_letter_queue.py
│
├── tests/
│ ├── test_event_flow.py
│ └── test_resilience.py
│
├── main.py
└── README.md


---

## 🎯 Design Goals

- Simulate asynchronous event-driven processing
- Demonstrate retry and resilience patterns
- Model enterprise CRM integration logic
- Maintain modular and testable design
- Showcase distributed system thinking

---

## ⚙️ Core Components

### Event Bus

Implements a lightweight publish–subscribe pattern allowing decoupled event communication between publishers and consumers.

### Publishers

Domain-level components that emit events (e.g., `LeadCreated`) into the system.

### Consumers

Independent handlers that process domain events asynchronously.

### Retry Handler

Implements controlled retry attempts with delay to simulate enterprise-grade resilience patterns.

### Dead Letter Queue (DLQ)

Captures events that fail after exhausting retry attempts, simulating real-world fault tolerance strategies.

---

## 🧪 Resilience & Failure Handling

This architecture models enterprise-grade failure management patterns:

- Controlled retry attempts
- Backoff delay simulation
- Dead Letter Queue handling for unrecoverable events
- Separation of event publishing and failure processing logic

These patterns reflect real-world distributed CRM integration systems where fault tolerance and observability are critical.

---

## ▶ Running the Demo

To simulate the event flow:

```bash
python main.py
