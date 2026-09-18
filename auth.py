# auth.py - User authentication logic

users = {
    "admin": "password123",
    "doctor1": "securepass"
}

def login(username, password):
    if username in users and users[username] == password:
        return f"Login successful. Welcome, {username}!"
    else:
        return "Login failed. Invalid username or password."

# Sample usage
if __name__ == "__main__":
    print(login("admin", "password123"))
    print(login("admin", "wrongpass"))
