import os
import psycopg2
import psycopg2.extras
from flask import Flask, jsonify, request

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://demo:demo@localhost:5433/demo")
app = Flask(__name__)


def get_conn():
    return psycopg2.connect(DATABASE_URL)


@app.post("/customers")
def create_customer():
    body = request.get_json(force=True)
    name = body.get("customer_name")
    email = body.get("email")
    if not name or not email:
        return jsonify(error="customer_name and email are required"), 400
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO customers (customer_name, email) VALUES (%s, %s) RETURNING id",
            (name, email),
        )
        new_id = cur.fetchone()[0]
    return jsonify(id=new_id, customer_name=name, email=email), 201


@app.get("/customers")
def list_customers():
    with get_conn() as conn, conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("SELECT id, customer_name, email FROM customers ORDER BY id")
        return jsonify(cur.fetchall())


@app.get("/customers/<int:cid>")
def get_customer(cid):
    with get_conn() as conn, conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("SELECT id, customer_name, email FROM customers WHERE id = %s", (cid,))
        row = cur.fetchone()
    if not row:
        return jsonify(error="not found"), 404
    return jsonify(row)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
