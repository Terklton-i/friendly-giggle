import sqlite3
import os
import sys

# if os.path.isfile("ppab6.db"):

#     decision = input("The database with this name already exists. Do you want to delete and recreate it? ")
#     while decision.lower() != "yes" and decision.lower() != "no":
#         decision = input("It's a yes/no question, idiot. Delete the database or not? ")
#     if decision.lower() == "yes":
#         os.remove("ppab6.db")
#         conn = sqlite3.connect('ppab6.db')
#     elif decision.lower() == "no":
#         sys.exit(0)
# else:
#     conn = sqlite3.connect('ppab6.db')

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE users (
            username VARCHAR
            password_hash VARCHAR
            )"""
        )






