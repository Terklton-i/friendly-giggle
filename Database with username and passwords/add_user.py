import sqlite3
import hashlib
import getpass
import json

# loading data from the config file
with open("table_names_config.json") as names_config_file:
    data = json.load(names_config_file)

# creating a variable for table name
table_name = data['Table names']
table_name = table_name[0]
table_name = table_name['name']


# def a function for creating login info
def ask_for_login_info():
    username_db = input("Username: ")
    # hiding password
    password_db = getpass.getpass()
    # encrypt the password
    b_password = password_db.encode('utf-8')
    hash_password = hashlib.sha256(b_password).hexdigest()
    return username_db.lower(), hash_password
username_db, hash_password = ask_for_login_info()

# calling the function for creating login info
conn = sqlite3.connect('ppab6.db')

c = conn.cursor()

# if you want to create the table from scratch - uncomment this:


# c.execute("""CREATE TABLE users (
#             username VARCHAR,
#             password_hash VARCHAR
#             )"""
#         )



with conn:
# checking if username exists
    while len(list(c.execute("SELECT username FROM {users} WHERE username = :username_db".format(users = table_name),
                            {"username_db": username_db}))) > 0:
        print("That username is already in use!")
        username_db, hash_password = ask_for_login_info()
# inserting the login info into database table
    c.execute("INSERT INTO {users} VALUES (:username, :hash_password)".format(users = table_name),
    {"username": username_db, "hash_password": hash_password})

