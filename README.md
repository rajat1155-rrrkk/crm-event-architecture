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

The design reflects enterprise integration patterns used in Salesforce-led and distributed CRM ecosystems.

---

## 🔄 High-Level Event Flow

Lead Created → Event Published → Event Bus → Consumer Processing  
If failure → Retry Handler → Dead Letter Queue (if max retries exceeded)

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
│ └── test_event_flow.py
│
└── README.md





---

## 🎯 Design Goals

- Simulate asynchronous event-driven processing
- Demonstrate retry and resilience patterns
- Model enterprise CRM integration logic
- Maintain modular and testable design
- Provide architectural demonstration use case

---

## 🛠 Tech Stack

- Python
- Object-Oriented Design
- Publisher–Subscriber Pattern
- Retry with Backoff Simulation
- Unit Testing (unittest)

---

## 🔮 Future Enhancements

- AsyncIO-based event bus
- Persistent event store simulation
- Circuit breaker pattern
- Logging abstraction
- Observability layer
- Webhook-style external integrations

---

## 📌 Project Purpose

This repository demonstrates enterprise event-driven CRM system design patterns for architectural modeling, system thinking, and distributed workflow simulation.










