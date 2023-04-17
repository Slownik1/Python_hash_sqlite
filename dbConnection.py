import sqlite3

def dbInsert(hash, salt):
    data = (hash, salt)
    con = sqlite3.connect("pass.db")
    cur = con.cursor()
    cur.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='pass' ")
    if cur.fetchone()[0] == 1:
        print('Table exists')
        cur.execute("INSERT INTO pass VALUES (?,?)", data)
        con.commit()
        con.close()
    else:
        cur.execute("CREATE TABLE pass(hashedPassword, passwordSalt)")
        cur.execute("INSERT INTO pass VALUES (?,?)", data)
        con.commit()
        con.close()
