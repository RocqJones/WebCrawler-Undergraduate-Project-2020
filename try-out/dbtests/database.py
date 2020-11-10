import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, product_name text, demand INTEGER)")
        self.conn.commit()

    def insert(self, product_name, demand):
        self.cur.execute("INSERT INTO products VALUES (NULL,?,?)",(product_name,demand))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM products")
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM products WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, product_name, demand):
        self.cur.execute("UPDATE products SET product_name=?, demand=? WHERE id=?", (product_name,demand,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()