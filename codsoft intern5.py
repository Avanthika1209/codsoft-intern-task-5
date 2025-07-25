contacts = {}

def add(): 
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    addr = input("Address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': addr}

def view():
    if not contacts: print("No contacts.")
    for n, d in contacts.items():
        print(f"\nName: {n}\nPhone: {d['phone']}\nEmail: {d['email']}\nAddress: {d['address']}")

def search():
    name = input("Search name: ")
    c = contacts.get(name)
    if c: print(f"\nPhone: {c['phone']}, Email: {c['email']}, Address: {c['address']}")
    else: print("Not found.")

def delete():
    name = input("Name to delete: ")
    if contacts.pop(name, None): print("Deleted.")
    else: print("Not found.")

while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    ch = input("Choice: ")
    if ch == '1': add()
    elif ch == '2': view()
    elif ch == '3': search()
    elif ch == '4': delete()
    elif ch == '5': break
    else: print("Invalid.")
