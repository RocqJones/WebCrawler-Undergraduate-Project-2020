import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS fruits (id INTEGER PRIMARY KEY, product_name text, demand INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS cerials (id INTEGER PRIMARY KEY, product_name text, demand INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS vegetables (id INTEGER PRIMARY KEY, product_name text, demand INTEGER)")
        self.conn.commit()

    def insert(self, product_name, demand):
        self.cur.execute("INSERT INTO fruits VALUES (NULL,?,?)",(product_name,demand))
        self.cur.execute("INSERT INTO cerials VALUES (NULL,?,?)",(product_name,demand))
        self.cur.execute("INSERT INTO vegetables VALUES (NULL,?,?)",(product_name,demand))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM fruits,cerials,vegetables")
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM fruits,cerials,vegetables WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, product_name, demand):
        self.cur.execute("UPDATE fruits SET product_name=?, demand=? WHERE id=?", (product_name,demand,id))
        self.cur.execute("UPDATE cerials SET product_name=?, demand=? WHERE id=?", (product_name,demand,id))
        self.cur.execute("UPDATE vegetables SET product_name=?, demand=? WHERE id=?", (product_name,demand,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()