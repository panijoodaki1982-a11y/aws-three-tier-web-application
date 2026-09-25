from flask import Flask
import os
import pymysql

app = Flask(__name__)

# Database configuration is loaded from environment variables
# so credentials are not stored in the source code.
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


@app.route("/")
def home():
    return """
    <h1>Pantea's AWS Three-Tier Web Application</h1>
    <p>Application successfully deployed on Amazon EC2.</p>
    """


@app.route("/database")
def database():
    try:
        connection = get_db_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT NOW();")
            result = cursor.fetchone()

        connection.close()

        return f"Successfully connected to Amazon RDS. Database time: {result[0]}"

    except Exception as error:
        return f"Database connection error: {error}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
