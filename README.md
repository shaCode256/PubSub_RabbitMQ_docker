# 🐰 RabbitMQ Pub/Sub Project (Python + Docker)

A simple demo project showing a **Publisher/Subscriber (Pub/Sub)** pattern using **RabbitMQ** and **Python**, all containerized with **Docker Compose**.

This project demonstrates:
- A `publisher` sending JSON messages
- One or more `subscribers` consuming messages from a fanout exchange
- A shared `MessageData` class for consistent message structure
- RabbitMQ running via Docker with management UI

---

## 📁 Project Structure

```
rabbitmq_docker_project/
├── docker-compose.yml
├── shared/
│   └── model.py          # MessageData class (name, index, time)
├── publisher/
│   ├── app.py            # Publishes a message every second
│   ├── Dockerfile
│   └── requirements.txt
├── subscriber/
│   ├── app.py            # Listens and prints messages
│   ├── Dockerfile
│   └── requirements.txt
```

---

## 🚀 How to Run

### 1. Make sure you have Docker & Docker Compose installed

- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

### 2. Run the project

```bash
docker compose up --build
```

All services will start:
- `rabbitmq` (with a management UI at [http://localhost:15672](http://localhost:15672), user: `guest`, pass: `guest`)
- `publisher` sending messages every 1 second
- `subscriber` receiving and printing messages

---

## 🧪 Sample Output

### In `publisher` logs:
```bash
Publisher sent: {"Name": "Publisher1", "Index": 42, "Time": "2025-04-23T14:53:02.123"}
```

### In `subscriber` logs:
```bash
Subscriber received:
Name: Publisher1
Index: 42
Time: 2025-04-23T14:53:02.123
```

---

## 🧱 RabbitMQ Configuration

- **Exchange**: `logs`  
- **Exchange Type**: `fanout` (broadcast to all bound queues)
- Each subscriber automatically gets its own anonymous queue bound to the exchange.

---

## 📦 Notes

- Multiple subscribers can be added by running more containers.
- You can modify the `MessageData` structure inside `shared/model.py`.

---

## 📜 License

MIT License

---

## ❤️ Made with focus, Docker, and a sprinkle of `"Time"` 🕐
