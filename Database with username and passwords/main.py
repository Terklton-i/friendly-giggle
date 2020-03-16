import hashlib
import json
# ask user for input
login = int(input("Press 1 to Log in or Press 2 to Creat a new account: "))

# checking for correct input
if login != 1 and login != 2:
    login = input("Press 1 to Log in or Press 2 to Creat a new account: ")

# loading data from the config file
with open("config.json") as config_file:
    data = json.load(config_file)

# saving the login data into strings
def ask_for_login_info():
    username = input("Username: ")
    password = input("Password: ")
    # encrypt the password
    b_password = password.encode('utf-8')
    hash_password = hashlib.sha256(b_password).hexdigest()
    return username.lower(), hash_password
username, hash_password = ask_for_login_info()

# checking if the username is taken
if login == 2:
    for user in data['Users']:
        while username == user['username']:
            print("Choose a different username: ")
            username, hash_password = ask_for_login_info()

# creating a dict with the new user info
add_data = {}
add_data['username'] = username
add_data['password'] = hash_password
data['Users'].append(add_data)


# registering a new user by creating new log in info in the text file
with open("config.json", "w") as config_file:
    json.dump(data, config_file, indent = 4)

# checking for valid log in info
def is_valid_credentials(username, password):
    x = 1
    for user in data['Users']:
        if username == user['username'] and password == user['password']:
            x = 0
    if x == 0:
        return True
    else:
        return False


if is_valid_credentials(username, hash_password) is True:
    print("\nI like dogs")
else:
    print("GTFO")








