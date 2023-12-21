# The eshop has:
# Customers -> Set order, View their orders
# Employees -> View all incomplete orders, Send order
# Manager -> View orders per customer, all customers

users = {}
users['tom'] = {'role': 'customer', 'password': '1111'}
users['mary'] = {'role': 'employee', 'password': '1111'}
users['john'] = {'role': 'manager', 'password': '1111'}


# Login
print("Login")
username = input("Username: ")
password = input("Password: ")

# Check if user is ok
valid = False
role = None
if username in users:
    if users[username]['password'] == password:
        valid = True
        role = users[username]['role']

if valid: 
    while True:
        if role == 'customer':
            print("1. Add order")
            print("2. View my orders")
            print("0. Exit")
            choice = input("Choose: ")
            if choice == '1':
                pass
            elif choice == '2':
                pass
            elif choice == '0':
                break
        elif role == 'employee':
            print("1. View Incomplete Orders")
            print("2. Send Order")
            print("0. Exit")
            choice = input("Choose: ")
            if choice == '1':
                pass
            elif choice == '2':
                pass
            elif choice == '0':
                break
        elif role == 'manager':
            print("1. Orders per customer")
            print("2. Customers")
            print("0. Exit")
            choice = input("Choose: ")
            if choice == '1':
                pass
            elif choice == '2':
                pass
            elif choice == '0':
                break

