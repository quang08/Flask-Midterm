CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    company TEXT,
    address TEXT,
    email TEXT
);

-- Insert 20 records into Customers table
INSERT INTO Customers (first_name, last_name, company, address, email)
VALUES
    ('John', 'Doe', 'ABC Inc.', '123 Main St', 'john.doe@email.com'),
    ('Jane', 'Smith', 'XYZ Corp', '456 Oak Ave', 'jane.smith@email.com'),
    ('Michael', 'Johnson', 'LMN Ltd', '789 Pine Ln', 'michael.johnson@email.com'),
    ('Emily', 'Davis', 'PQR Industries', '101 Elm Blvd', 'emily.davis@email.com'),
    ('Robert', 'White', 'JKL Co.', '202 Cedar Dr', 'robert.white@email.com'),
    ('Amanda', 'Harris', 'GHI Enterprises', '303 Birch Rd', 'amanda.harris@email.com'),
    ('Daniel', 'Miller', 'STU Ltd', '404 Maple St', 'daniel.miller@email.com'),
    ('Olivia', 'Martinez', 'VWX Corp', '505 Spruce Ave', 'olivia.martinez@email.com'),
    ('Christopher', 'Brown', 'DEF Ltd', '606 Pine Ln', 'christopher.brown@email.com'),
    ('Sophia', 'Taylor', 'NOP Inc.', '707 Oak Ave', 'sophia.taylor@email.com'),
    ('Matthew', 'Anderson', 'UVW Co.', '808 Cedar Dr', 'matthew.anderson@email.com'),
    ('Emma', 'Wilson', 'QRS Industries', '909 Elm Blvd', 'emma.wilson@email.com'),
    ('David', 'Garcia', 'ABC Inc.', '1010 Birch Rd', 'david.garcia@email.com'),
    ('Isabella', 'Smith', 'JKL Co.', '1111 Maple St', 'isabella.smith@email.com'),
    ('Ethan', 'Jackson', 'STU Ltd', '1212 Pine Ln', 'ethan.jackson@email.com'),
    ('Madison', 'Brown', 'DEF Ltd', '1313 Oak Ave', 'madison.brown@email.com'),
    ('Jacob', 'Taylor', 'NOP Inc.', '1414 Cedar Dr', 'jacob.taylor@email.com'),
    ('Ava', 'Martinez', 'UVW Co.', '1515 Elm Blvd', 'ava.martinez@email.com'),
    ('Logan', 'Davis', 'QRS Industries', '1616 Birch Rd', 'logan.davis@email.com'),
    ('Ella', 'Wilson', 'GHI Enterprises', '1717 Maple St', 'ella.wilson@email.com');


CREATE TABLE Employee (
    Employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    department TEXT,
    address TEXT,
    email TEXT
);

-- Insert 20 records into Employee table
INSERT INTO Employee (first_name, last_name, department, address, email)
VALUES
    ('John', 'Doe', 'ABC Inc.', '123 Main St', 'john.doe@email.com'),
    ('Jane', 'Smith', 'XYZ Corp', '456 Oak Ave', 'jane.smith@email.com'),
    ('Michael', 'Johnson', 'LMN Ltd', '789 Pine Ln', 'michael.johnson@email.com'),
    ('Emily', 'Davis', 'PQR Industries', '101 Elm Blvd', 'emily.davis@email.com'),
    ('Robert', 'White', 'JKL Co.', '202 Cedar Dr', 'robert.white@email.com'),
    ('Amanda', 'Harris', 'GHI Enterprises', '303 Birch Rd', 'amanda.harris@email.com'),
    ('Daniel', 'Miller', 'STU Ltd', '404 Maple St', 'daniel.miller@email.com'),
    ('Olivia', 'Martinez', 'VWX Corp', '505 Spruce Ave', 'olivia.martinez@email.com'),
    ('Christopher', 'Brown', 'DEF Ltd', '606 Pine Ln', 'christopher.brown@email.com'),
    ('Sophia', 'Taylor', 'NOP Inc.', '707 Oak Ave', 'sophia.taylor@email.com'),
    ('Matthew', 'Anderson', 'UVW Co.', '808 Cedar Dr', 'matthew.anderson@email.com'),
    ('Emma', 'Wilson', 'QRS Industries', '909 Elm Blvd', 'emma.wilson@email.com'),
    ('David', 'Garcia', 'ABC Inc.', '1010 Birch Rd', 'david.garcia@email.com'),
    ('Isabella', 'Smith', 'JKL Co.', '1111 Maple St', 'isabella.smith@email.com'),
    ('Ethan', 'Jackson', 'STU Ltd', '1212 Pine Ln', 'ethan.jackson@email.com'),
    ('Madison', 'Brown', 'DEF Ltd', '1313 Oak Ave', 'madison.brown@email.com'),
    ('Jacob', 'Taylor', 'NOP Inc.', '1414 Cedar Dr', 'jacob.taylor@email.com'),
    ('Ava', 'Martinez', 'UVW Co.', '1515 Elm Blvd', 'ava.martinez@email.com'),
    ('Logan', 'Davis', 'QRS Industries', '1616 Birch Rd', 'logan.davis@email.com'),
    ('Ella', 'Wilson', 'GHI Enterprises', '1717 Maple St', 'ella.wilson@email.com');
