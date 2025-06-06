import sqlite3


class Connection():
    def __init__(self):
        self.connection = sqlite3.connect("database.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_profiles(self) -> list[str]:
        self.cursor.execute("""
            SELECT * FROM profiles;
        """)

        profiles = self.cursor.fetchall()
        return profiles
    
    def get_posts(self) -> list[str]:
        self.cursor.execute("""
            SELECT * FROM posts;
        """)

        posts = self.cursor.fetchall()
        return posts
    
    def get_comments(self) -> list[str]:
        self.cursor.execute("""
            SELECT * FROM comments;
        """)

        comments = self.cursor.fetchall()
        return comments

    def close(self):
        self.connection.close()