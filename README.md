# customer-demo

Tiny multi-service app used as a test bed. Services: API, consumer, nightly report, all backed by Postgres.

## Run it
1. docker compose up -d
2. python -m venv .venv && source .venv/bin/activate   (Windows: .venv\Scripts\activate)
3. pip install -r api/requirements.txt
4. Terminal A: python api/app.py
5. Terminal B: python consumer/consumer.py
6. Terminal C: python report/nightly_report.py
7. Add a customer:
   curl -X POST localhost:5000/customers -H "Content-Type: application/json" -d '{"customer_name":"Test User","email":"t@example.com"}'
