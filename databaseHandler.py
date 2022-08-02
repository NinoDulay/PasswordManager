import sqlite3

def open_db():
    # Create a connection to the database
    global conn
    conn = sqlite3.connect('passwords.db')

    # Create a connection to the database
    global c
    c = conn.cursor()

def close_db():
    c.close()
    conn.close()

def create_table():
    open_db()

    c.execute('''
        CREATE TABLE IF NOT EXISTS passwords(
            application TEXT,
            password TEXT
        )
    ''')

    close_db()

def add_password(app, password):
    open_db()

    c.execute('''
        INSERT INTO passwords VALUES (?,?)
    ''', (app, password))

    conn.commit()

    close_db()

def show_database():
    open_db()

    c.execute('''
        SELECT * FROM passwords
    ''')

    data = c.fetchall()
    print("-"*50)
    print(f"|{'Saved Passwords':^48}|")
    print("-"*50)
    for row in data:
        print(f"|{row[0]+':':<18}|{row[1]:<29}|")
        print("-"*50)

    close_db()

def delete_password(app, password):
    open_db()

    c.execute('''
        DELETE FROM passwords 
        WHERE application = (?) AND
        password = (?)
    ''', (app, password))

    conn.commit()

    close_db()

create_table()

if __name__ == '__main__':
    pass
    #add_password('Youtube', 'dwaeryer3d')
    #show_database()
    #delete_password('Youtube', 'dwaeryer3d')


