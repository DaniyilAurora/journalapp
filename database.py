import sqlite3


class Database():
    def __init__(self):
        self.connection = sqlite3.connect("database.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

        if self.is_first_launch():
            self.create_tables()

    def create_tables(self):
        # Create "posts" table
        self.cursor.execute("""
                CREATE TABLE posts(
                    id INTEGER PRIMARY KEY,
                    title VARCHAR(255),
                    text TEXT,
                    author_id INTEGER,
                    creation_date DATETIME,
                    likes INTEGER
                );
        """)

        self.connection.commit()

        # Create "profiles" table
        self.cursor.execute("""
                CREATE TABLE profiles(
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(255),
                    password BLOB,
                    creation_date DATETIME
                );
        """)

        self.connection.commit()

        # Create "comments" table
        self.cursor.execute("""
                CREATE TABLE comments(
                    id INTEGER PRIMARY KEY,
                    text TEXT,
                    likes INTEGER,
                    author_id INTEGER,
                    post_id INTEGER,
                    creation_date DATETIME
                );
        """)

        self.connection.commit()

    def is_first_launch(self) -> bool:
        self.cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name=?;
        """, ("profiles",))

        result = self.cursor.fetchone()

        return result is None
