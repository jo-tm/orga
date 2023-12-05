import sqlite3
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

DB_FILE = config['database']['filename']

def connect():
    return sqlite3.connect(DB_FILE)

def create_tables():
    conn = connect()
    c = conn.cursor()

    c.execute('''CREATE TABLE members 
                 (telegram_id integer primary key, name text, address text)''')
    
    c.execute('''CREATE TABLE polls
                (id integer primary key, title text, options text, 
                 created_at text, deadline text)''')
                
    c.execute('''CREATE TABLE donations 
                (tx_hash text primary key, member_id integer, 
                 amount real, completed boolean)''')

    conn.commit()
    conn.close()

# functions connect and create_tables

def add_member(telegram_id, name, address):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO members VALUES (?, ?, ?)", (telegram_id, name, address))
    conn.commit() 
    conn.close()

def remove_member(telegram_id):
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM members WHERE telegram_id=?", (telegram_id,))
    conn.commit()
    conn.close()
    
def get_member(telegram_id):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM members WHERE telegram_id=?", (telegram_id,))
    row = c.fetchone() 
    conn.close()
    return row

def add_poll(title, options, created_at, deadline):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO polls VALUES (NULL, ?, ?, ?, ?)", 
              (title, options, created_at, deadline))
    poll_id = c.lastrowid
    conn.commit()
    conn.close()
    return poll_id
    
def get_poll(poll_id):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM polls WHERE id=?", (poll_id,))
    row = c.fetchone()
    conn.close()
    return row

def update_poll(poll_id, title, options, deadline):
    conn = connect()
    c = conn.cursor()
    c.execute("UPDATE polls SET title=?, options=?, deadline=? WHERE id=?", 
              (title, options, deadline, poll_id))
    conn.commit()
    conn.close()
    
def add_donation(tx_hash, member_id, amount):
    conn = connect()
    c = conn.cursor() 
    c.execute("INSERT INTO donations VALUES (?, ?, ?, ?)", 
              (tx_hash, member_id, amount, False)) 
    conn.commit()
    conn.close()

def get_donation(tx_hash):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM donations WHERE tx_hash=?", (tx_hash,))
    row = c.fetchone()
    conn.close() 
    return row

def update_donation(tx_hash, completed):
    conn = connect()
    c = conn.cursor()
    c.execute("UPDATE donations SET completed=? WHERE tx_hash=?", 
              (completed, tx_hash))
    conn.commit()
    conn.close()
