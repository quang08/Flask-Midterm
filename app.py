# C1
# a)
from flask import Flask, render_template, request, jsonify
import sqlite3
import json

with open("./data.json") as f:
    data = json.load(f)

app = Flask(__name__, static_url_path="/static")
app = Flask(__name__)
sqlDB = "db/ShoppingDB.db"


def connect_db():
    return sqlite3.connect(sqlDB)


def insert_data_from_json():
    with connect_db() as connection:
        cursor = connection.cursor()
        with open("data.json", "r") as json_file:
            customers = json.load(json_file)
            for customer in customers:
                cursor.execute(
                    """
                    INSERT INTO Customers (customer_id, first_name, last_name, company, address, email)
                    VALUES (?, ?, ?, ?, ?, ?)
                """,
                    (
                        customer["customer_id"],
                        customer["first_name"],
                        customer["last_name"],
                        customer["company"],
                        customer["address"],
                        customer["email"],
                    ),
                )
        connection.commit()


# insert_data_from_json()


@app.route("/")
def index():
    return render_template("index.html")


# C2
# a)
@app.route("/Customers", methods=["GET"])
def get_customers():
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Customers")
        customers = cursor.fetchall()
        columns = [column[0] for column in cursor.description]  # lấy tên các cột
        customer_list = [
            dict(zip(columns, row)) for row in customers
        ]  # tạo dict từ các cột và các giá trị tương ứng
        # return jsonify(customer_list)
        return render_template("customers.html", customers=customer_list)


# b)
@app.route("/Customers", methods=["DELETE"])
def delete_customer():
    customer_id = request.args.get(
        "customer_id"
    )  # lấy giá trị của tham số customer_id. Được truyền vào qua url

    if customer_id is None:
        return jsonify({"error": "Thiếu id"}), 400

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Customers WHERE customer_id=?", (customer_id,))
        connection.commit()

        return jsonify({"message": "Customer deleted successfully"})


# C3
# a)
@app.route("/Customers/new", methods=["GET"])
def new_customer():
    return render_template("new_customer.html")


@app.route("/Customers", methods=["POST"])
def add_customer():  # form
    # get data from form
    customer_data = request.form

    if not customer_data:
        return jsonify({"error": "Thiếu thông tin của Customer"}), 400

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO Customers (first_name, last_name, company, address, email)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                customer_data.get("first_name"),
                customer_data.get("last_name"),
                customer_data.get("company"),
                customer_data.get("address"),
                customer_data.get("email"),
            ),
        )
        connection.commit()

        # Lấy id của customer vừa thêm vào
        last_row_id = cursor.lastrowid

        return render_template(
            "new_customer.html",
            message="Customer added successfully",
        )

        return jsonify(
            {"customer_id": last_row_id, "message": "Customer added successfully"}
        )


# b)
@app.route("/Customers/<int:customer_id>", methods=["GET"])
def edit_customer(customer_id):
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM Customers
            WHERE customer_id=?
            """,
            (customer_id,),
        )
        customer = cursor.fetchone()

        if customer is None:
            return jsonify({"error": f"Customer with ID {customer_id} not found"}), 404

        columns = [column[0] for column in cursor.description]
        customer_dict = dict(zip(columns, customer))

        return jsonify(customer_dict)


@app.route("/Customers", methods=["PUT"])
def update_customer():
    customer_id = request.args.get("customer_id")

    if customer_id is None:
        return jsonify({"error": "Thiếu id của Customer"}), 400

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE Customers
            SET first_name=?, last_name=?, company=?, address=?, email=?
            WHERE customer_id=?
            """,
            (
                request.json.get("first_name"),
                request.json.get("last_name"),
                request.json.get("company"),
                request.json.get("address"),
                request.json.get("email"),
                customer_id,
            ),
        )
        connection.commit()

        return jsonify({"message": "Customer updated successfully"})


# C4
# a)
@app.route("/CheckCustomer", methods=["POST"])
def check_customer():
    customer_data = request.json

    if "email" not in customer_data or "first_name" not in customer_data:
        return jsonify({"error": "Thiếu thông tin Email hoặc FirstName"}), 400

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM Customers
            WHERE email=? AND first_name=?
            """,
            (customer_data["email"], customer_data["first_name"]),
        )
        customer = cursor.fetchone()

        if customer:
            columns = [column[0] for column in cursor.description]
            return jsonify({"exists": True, "customer": dict(zip(columns, customer))})
        else:
            return jsonify({"exists": False, "message": "Customer not found"})


# b)
@app.route("/SearchCustomers", methods=["POST"])
def search_customers():
    search_string = request.json.get("search_string")

    if not search_string:
        return jsonify({"error": "Thiếu chuỗi tìm kiếm"}), 400

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM Customers
            WHERE first_name LIKE ? OR last_name LIKE ? OR company LIKE ? OR address LIKE ? OR email LIKE ?
            """,
            (
                f"%{search_string}%",
                f"%{search_string}%",
                f"%{search_string}%",
                f"%{search_string}%",
                f"%{search_string}%",
            ),
        )
        customers = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        customer_list = [dict(zip(columns, row)) for row in customers]

        return jsonify({"search_results": customer_list})


# c)
@app.route("/CustomerOrders/<int:customer_id>", methods=["GET"])
def customer_orders(customer_id):
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM Orders
            WHERE customer_id=?
            """,
            (customer_id,),
        )
        orders = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        order_list = [dict(zip(columns, row)) for row in orders]

        # return jsonify({"orders": order_list})
        return render_template(
            "customer_orders.html", customer_id=customer_id, orders=order_list
        )


# d)
@app.route("/InsertCustomers", methods=["POST"])
def insert_customers():
    customers_data = request.json.get("customers")
    # Ví dụ payload cho postman
    ""
    {
        "customers": [
            {
                "first_name": "rick",
                "last_name": "sanchez",
                "company": "ABC",
                "address": "123 ABC Street",
                "email": "test123@gmail.com",
            },
            {
                "first_name": "rick1",
                "last_name": "sanchez1",
                "company": "ABC",
                "address": "234 ABC Street",
                "email": "test123@gmail.com",
            },
            {
                "first_name": "rick2",
                "last_name": "sanchez2",
                "company": "ABC",
                "address": "345 ABC Street",
                "email": "test123@gmail.com",
            },
        ]
    }
    ""

    if not customers_data or not isinstance(customers_data, list):
        return (
            jsonify(
                {"error": "Thiếu danh sách khách hàng hoặc danh sách không hợp lệ"}
            ),
            400,
        )

    with connect_db() as connection:
        cursor = connection.cursor()

        for customer_data in customers_data:
            cursor.execute(
                """
                INSERT INTO Customers (first_name, last_name, company, address, email)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    customer_data.get("first_name"),
                    customer_data.get("last_name"),
                    customer_data.get("company"),
                    customer_data.get("address"),
                    customer_data.get("email"),
                ),
            )

        connection.commit()

        return jsonify({"message": "Customers inserted successfully"})
