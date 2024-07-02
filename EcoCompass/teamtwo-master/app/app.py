from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from connections.amex import amex
from connections.startling_bank import star

import psycopg2
from psycopg2 import extras

from model_co2 import top10, monthly_chart, company_comp

app = Flask(__name__)

# Database connection details
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "myapp"
DB_USER = "myuser"
DB_PASSWORD = "mypassword"

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
)

# Create a cursor object
cur = conn.cursor()

# Create the credit card statement table
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS topups (
        id SERIAL PRIMARY KEY,
        merchant TEXT,
        multi NUMERIC(10,2))
"""
)
conn.commit()


@app.route("/", methods=["GET", "POST"])
def index():
    # Fetch all the data from the database

    statements = top10()


    if request.method == "POST":
        # Handle file upload
        file = request.files["file"]
        if file:
            # Read the CSV file
            spending_data = pd.read_csv(file)

            if "Notes" not in spending_data.columns:
                file_parser = amex(spending_data)
            else:
                file_parser = star(spending_data)

            cur.execute(file_parser.table_def())
            conn.commit()

            column_names = ", ".join(file_parser.file.columns)

            # Create a SQL INSERT statement
            sql = (
                f"INSERT INTO {file_parser.tbl_nm} ({column_names}) VALUES %s"
            )

            # Convert the DataFrame to a list of tuples
            values = [tuple(x) for x in file_parser.file.to_numpy()]

            # Use the execute_values function to insert the data
            cur.execute("BEGIN")
            psycopg2.extras.execute_values(
                cur, sql, values, template=None, page_size=100
            )
            cur.execute("COMMIT")

            # Redirect to the index page
            return redirect(url_for("index"))

    # return render_template('index.html')
    cur.execute("SELECT COUNT(*) FROM public.starling")
    row_count = cur.fetchone()[0]

    # Check the row count and execute a conditional statement
    if row_count > 160:
        image_filename = 'images/gauge2.png'
    else:
        image_filename = 'images/gauge.png'

    return render_template("index.html", data=statements, image_filename=image_filename)


@app.route("/detail")
def detail():
    return render_template("detail.html", plot_url=monthly_chart())


@app.route("/company")
def company():
    return render_template("company.html", plot_url=company_comp())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
