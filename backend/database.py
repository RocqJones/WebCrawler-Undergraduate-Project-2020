import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS fruits (id INTEGER PRIMARY KEY, product_name text, demand INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS cerials (id INTEGER PRIMARY KEY, product_name text, demand INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS vegetables (id INTEGER PRIMARY KEY, product_name text, demand INTEGER)")
        self.conn.commit()

    def insert_f(self, product_name, demand):
        self.cur.execute("INSERT INTO fruits VALUES (NULL,?,?)",(product_name,demand))
        self.conn.commit()

    def insert_c(self, product_name, demand):
        self.cur.execute("INSERT INTO cerials VALUES (NULL,?,?)",(product_name,demand))
        self.conn.commit()

    def insert_v(self, product_name, demand):
        self.cur.execute("INSERT INTO vegetables VALUES (NULL,?,?)",(product_name,demand))
        self.conn.commit()

    def view_f(self):
        self.cur.execute("SELECT * FROM fruits")
        rows = self.cur.fetchall()
        return rows

    def view_c(self):
        self.cur.execute("SELECT * FROM cerials")
        rows = self.cur.fetchall()
        return rows

    def view_v(self):
        self.cur.execute("SELECT * FROM vegetables")
        rows = self.cur.fetchall()
        return rows

    def delete_f(self, id):
        self.cur.execute("DELETE FROM fruits WHERE id=?",(id,))
        self.conn.commit()

    def delete_c(self, id):
        self.cur.execute("DELETE FROM cerials WHERE id=?",(id,))
        self.conn.commit()
    
    def delete_v(self, id):
        self.cur.execute("DELETE FROM vegetables WHERE id=?",(id,))
        self.conn.commit()

    def update_f(self, id, product_name, demand):
        self.cur.execute("UPDATE fruits SET product_name=?, demand=? WHERE id=?", (product_name,demand,id))
        self.conn.commit()

    def update_c(self, id, product_name, demand):
        self.cur.execute("UPDATE cerials SET product_name=?, demand=? WHERE id=?", (product_name,demand,id))
        self.conn.commit()

    def update_v(self, id, product_name, demand):
        self.cur.execute("UPDATE vegetables SET product_name=?, demand=? WHERE id=?", (product_name,demand,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()