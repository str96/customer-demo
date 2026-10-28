CREATE TABLE customers (
    id            SERIAL PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email         TEXT NOT NULL,
    welcomed      BOOLEAN NOT NULL DEFAULT FALSE,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE VIEW v_customer_report AS
SELECT id,
       customer_name AS display_name,
       upper(left(customer_name, 1)) AS initial,
       email,
       created_at
FROM customers;

INSERT INTO customers (customer_name, email, welcomed) VALUES
    ('Mary Ann Smith',  'maryann@example.com', TRUE),
    ('Madonna',         'madonna@example.com', TRUE),
    ('John Doe ',       'john@example.com',    TRUE),
    ('Priya Raman',     'priya@example.com',   TRUE),
    ('Arjun Kumar',     'arjun@example.com',   TRUE);
