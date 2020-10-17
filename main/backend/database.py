import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, author text, link text)")
        self.conn.commit()

    def insert(self, author, link):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?)",(author,link))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, author, link):
        self.cur.execute("UPDATE book SET author=?, link=? WHERE id=?", (author,link,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()