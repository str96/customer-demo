"""Nightly customer report. Reads from a view, not the table directly."""
import csv
import os
import sys
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://demo:demo@localhost:5433/demo")


def main():
    with psycopg2.connect(DATABASE_URL) as conn, conn.cursor() as cur:
        cur.execute("SELECT id, display_name, initial, email, created_at FROM v_customer_report ORDER BY id")
        writer = csv.writer(sys.stdout)
        writer.writerow(["id", "display_name", "initial", "email", "created_at"])
        for row in cur.fetchall():
            writer.writerow(row)


if __name__ == "__main__":
    main()
