import sqlite3


class Connection():
    # Initialises the connection
    def __init__(self):
        self.connection = sqlite3.connect("database.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

    # Returns profile username by the id given
    def get_profile_username_by_id(self, id: int) -> str:
        self.cursor.execute("SELECT username FROM profiles WHERE id = ?;", (id,))
        username = self.cursor.fetchone()
        return username

    # Returns all profiles
    def get_profiles(self) -> list[str]:
        self.cursor.execute("""
            SELECT * FROM profiles;
        """)

        profiles = self.cursor.fetchall()
        return profiles

    # Returns profiles column names
    def get_profiles_columns(self) -> list[str]:
        self.cursor.execute("PRAGMA table_info(profiles)")
        columns = [column[1] for column in self.cursor.fetchall()]

        return columns

    # Adds new profile
    def add_profile(self, id: int, username: str, password: str, creation_date: str):
        self.cursor.execute("""
            INSERT INTO profiles
            (id, username, password, creation_date)
            VALUES (?, ?, ?, ?);
        """, (id, username, password, creation_date))
        self.connection.commit()

    # Deletes profile
    def delete_profile(self, id: int):
        self.cursor.execute("DELETE FROM profiles WHERE id = ?", (id,))
        self.connection.commit()

    # Returns all posts
    def get_posts(self) -> list[str]:
        self.cursor.execute("""
            SELECT * FROM posts;
        """)

        posts = self.cursor.fetchall()
        return posts

    # Returns posts column names
    def get_posts_columns(self) -> list[str]:
        self.cursor.execute("PRAGMA table_info(posts)")
        columns = [column[1] for column in self.cursor.fetchall()]

        return columns

    # Adds new post
    def add_post(self, id: int, title: str, text: str, author_id: int, creation_date: str, likes: int):
        self.cursor.execute("""
            INSERT INTO posts
            (id, title, text, author_id, creation_date, likes)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (id, title, text, author_id, creation_date, likes))
        self.connection.commit()

    # Deletes post
    def delete_post(self, id: int):
        self.cursor.execute("DELETE FROM posts WHERE id = ?", (id,))
        self.connection.commit()

    # Returns all comments
    def get_comments(self) -> list[str]:
        self.cursor.execute("""
            SELECT * FROM comments;
        """)

        comments = self.cursor.fetchall()
        return comments

    # Returns comments column names
    def get_comments_columns(self) -> list[str]:
        self.cursor.execute("PRAGMA table_info(comments)")
        columns = [column[1] for column in self.cursor.fetchall()]

        return columns

    # Adds new comment
    def add_comment(self, id: int, text: str, likes: int, author_id: int, post_id: int, creation_date: str):
        self.cursor.execute("""
            INSERT INTO comments
            (id, text, likes, author_id, post_id, creation_date)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (id, text, likes, author_id, post_id, creation_date))
        self.connection.commit()

    # Deletes comment
    def delete_comment(self, id: int):
        self.cursor.execute("DELETE FROM comments WHERE id = ?", (id,))
        self.connection.commit()

    # Closes the connection
    def close(self):
        self.connection.close()
