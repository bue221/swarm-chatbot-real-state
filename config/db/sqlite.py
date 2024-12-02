import sqlite3
from datetime import datetime

# global connection
conn = None


def get_connection():
    global conn
    if conn is None:
        conn = sqlite3.connect("application.db")
    return conn


def create_database():
    # Connect to a single SQLite database
    conn = get_connection()
    cursor = conn.cursor()

    # Create Users table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            phone TEXT
        )
    """
    )

    # Create Requirements table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Requeriments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            spot_type TEXT,
            square_metters INTEGER,
            price INTEGER,
            location INTEGER,
            created_at TIMESTAMP,
            updated_at TIMESTAMP
        )
    """
    )

    # Save (commit) the changes
    conn.commit()


def add_user(user_id, first_name, last_name, email, phone):
    conn = get_connection()
    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check if the user already exists
    cursor.execute("SELECT * FROM Users WHERE user_id = ?", (user_id,))
    if cursor.fetchone():
        return

    try:
        cursor.execute(
            """
            INSERT INTO Users (user_id, first_name, last_name, email, phone)
            VALUES (?, ?, ?, ?, ?)
        """,
            (user_id, first_name, last_name, email, phone),
        )

        conn.commit()
    except sqlite3.Error as e:
        print(f"Database Error: {e}")


def update_or_create_requirements(user_id, spot_type, square_metters, price, location):
    conn = get_connection()
    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check if the requirements already exist for the user
    cursor.execute("SELECT * FROM Requeriments WHERE user_id =?", (user_id,))
    requirements = cursor.fetchone()
    if requirements:
        cursor.execute(
            """
            UPDATE Requeriments SET spot_type =?, square_metters =?, price =?, location =?, updated_at =?
            WHERE user_id =?
        """,
            (spot_type, square_metters, price, location, date, user_id),
        )
    else:
        cursor.execute(
            """
            INSERT INTO Requeriments (user_id, spot_type, square_metters, price, location)
            VALUES (?,?,?,?,?)
        """,
            (user_id, spot_type, square_metters, price, location),
        )
        conn.commit()
        print(f"Requirements updated/created for user_id: {user_id}")


def get_user_by_phone(phone):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE phone =?", (phone,))
    user = cursor.fetchone()
    return user


def get_user_requirements(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Requeriments WHERE user_id =?", (user_id,))
    requirements = cursor.fetchone()
    return requirements


# Initialize and load database
def initialize_database():
    global conn

    # Initialize the database tables
    create_database()

    # Add some initial users
    initial_users = [
        (1, "Alice", "Smith", "alice@test.com", "123-456-7890"),
        (2, "Bob", "Johnson", "bob@test.com", "234-567-8901"),
        (3, "Sarah", "Brown", "sarah@test.com", "555-567-8901"),
        # Add more initial users here
    ]

    for user in initial_users:
        add_user(*user)

    update_or_create_requirements(1, "Apartment", 100, 2000, "San Francisco")
