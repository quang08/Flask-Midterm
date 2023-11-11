CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product VARCHAR(255),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

INSERT INTO Orders (customer_id, product, order_date) VALUES (1, 'Product A', '2023-01-01');
INSERT INTO Orders (customer_id, product, order_date) VALUES (1, 'Product B', '2023-01-15');
INSERT INTO Orders (customer_id, product, order_date) VALUES (2, 'Product C', '2023-02-01');
