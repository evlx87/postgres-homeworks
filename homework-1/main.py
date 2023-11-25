"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

from config import USER, PASSWORD

with psycopg2.connect(host='localhost', database='north', user=USER, password=PASSWORD) as conn:

    with open('../homework-1/north_data/employees_data.csv', newline='', encoding='Windows-1251') as f:
        employees = csv.DictReader(f)
        with conn.cursor() as cur:
            for employer in employees:
                cur.execute(
                    "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                    [
                        (employer['employee_id']),
                        employer['first_name'],
                        employer['last_name'],
                        employer['title'],
                        employer['birth_date'],
                        employer['notes']])
                cur.execute("SELECT * FROM employees")
                rows = cur.fetchall()

    with open('../homework-1/north_data/customers_data.csv', newline='', encoding='Windows-1251') as f:
        customers = csv.DictReader(f)
        with conn.cursor() as cur:
            for customer in customers:
                cur.execute(
                    "INSERT INTO customers VALUES (%s, %s, %s)",
                    [
                        (customer['customer_id']),
                        customer['company_name'],
                        customer['contact_name']])
                cur.execute("SELECT * FROM customers")
                rows = cur.fetchall()

    with open('../homework-1/north_data/orders_data.csv', newline='', encoding='Windows-1251') as f:
        orders = csv.DictReader(f)
        with conn.cursor() as cur:
            for order in orders:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                            [
                                (order['order_id']),
                                order['customer_id'],
                                order['employee_id'],
                                order['order_date'],
                                order['ship_city']])
                cur.execute("SELECT * FROM orders")
                rows = cur.fetchall()
conn.close()
