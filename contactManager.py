contacts = []

with open("contacts.txt", "r") as file:
    for line in file:
        eline = line.strip().split(", ")
        contacts.append({"name": eline[0], "number": eline[1]})

print("Contacts loaded successfully.")

while True:
    mode = input("Enter command:\na - Add contact\ny - Your contacts\ns - Search contact\ne - Exit\n")
    
    if mode == 'e':
        print("Exiting program.")
        break

    elif mode == 'a':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        duplicate = False
        for c in contacts:
            if c["number"] == number:
                duplicate = True
                break

        if duplicate:
            print("This phone number already exists. Contact not added.")
            continue
        contacts.append({"name": name, "number": number})
        with open("contacts.txt", "a") as file:
            file.write(f"{name}, {number}\n")
        print("Contact added successfully.")

    elif mode == 's':
        seekname = input("Enter name to search: ").strip().lower()
        matches = []

        for c in contacts:
            if seekname in c["name"].lower():  # ігноруємо регістр, шукаємо часткове співпадіння
                matches.append(c)

        if matches:
            print(f"Found {len(matches)} match(es):")
            for c in matches:
                print(f"{c['name']}, {c['number']}")
        else:
            print("Contact not found.")
    elif mode == 'y':
        print("Your contacts:")
        for contact in contacts:
            print(f"{contact['name']}, {contact['number']}")