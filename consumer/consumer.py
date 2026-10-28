"""Welcome-email consumer: polls for new customers and 'sends' a greeting."""
import os
import time
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://demo:demo@localhost:5433/demo")


def run_once():
    with psycopg2.connect(DATABASE_URL) as conn, conn.cursor() as cur:
        cur.execute("SELECT id, customer_name, email FROM customers WHERE welcomed = FALSE")
        for cid, name, email in cur.fetchall():
            print(f"[consumer] Sending welcome email to {email}: Hello, {name}!")
            cur.execute("UPDATE customers SET welcomed = TRUE WHERE id = %s", (cid,))


if __name__ == "__main__":
    print("[consumer] started, polling every 5 seconds")
    while True:
        run_once()
        time.sleep(5)
