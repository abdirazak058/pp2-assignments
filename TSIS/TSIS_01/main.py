from connect import connect_db

def infor_add(conn):
    cur = conn.cursor()

    Last_name_new_people = input("SurName: ")
    Name_new_poeple = input("Name: ")
    Phone_new_people = input("Phone: ")
    Operator_new_people = input("Operator: ")
    Email_new_people = input("Email: ")
    Birthday_new_people = input("Birthday (YYYY-MM-DD): ")

    cur.execute(
        "INSERT INTO contacts (last_name, name) VALUES (%s, %s) RETURNING id;",
        (Last_name_new_people, Name_new_poeple)
    )

    contact_id = cur.fetchone()[0]

    cur.execute(
        """INSERT INTO contact_info (contact_id, phone, operator, email, birthday)
           VALUES (%s, %s, %s, %s, %s);""",
        (contact_id, Phone_new_people, Operator_new_people, Email_new_people, Birthday_new_people)
    )

    conn.commit()
    print("Information ADD!")

    cur.close()


def infor_many_add(conn):
    cur = conn.cursor()

    How_many = int(input("How many people?: "))

    for i in range(How_many):
        print(f"\n{i+1}-adam:")

        Last_name_new_people = input("Surname: ")
        Name_new_poeple = input("Name: ")
        Email_new_people = input("Email: ")
        Birthday_new_people = input("Birthday (YYYY-MM-DD): ")

        cur.execute(
            "INSERT INTO contacts (last_name, name) VALUES (%s, %s) RETURNING id;",
            (Last_name_new_people, Name_new_poeple)
        )
        contact_id = cur.fetchone()[0]

        K = int(input("Qansha nomer?: "))

        for j in range(K):
            print(f"{j+1}-номер:")

            Phone_new_people = input("Phone: ")
            Operator_new_people = input("Operator: ")

            cur.execute(
                """INSERT INTO contact_info (contact_id, phone, operator, email, birthday)
                   VALUES (%s, %s, %s, %s, %s);""",
                (contact_id, Phone_new_people, Operator_new_people, Email_new_people, Birthday_new_people)
            )

    conn.commit()
    print("Information ADD!")

    cur.close()


def infor_update(conn):
    cur = conn.cursor()

    print("----MENU----")
    print("1 - Update infor People")
    print("2 - Update information of People")

    choice = input("Tanda: ")

    if choice == "1":
        cur.execute("SELECT id, last_name, name FROM contacts ORDER BY id;")
        people = cur.fetchall()

        print("\n--- CONTACTS ---")
        print(f"{'ID':<5} {'Surname':<15} {'Name':<15}")
        print("-" * 40)

        for person in people:
            print(f"{person[0]:<5} {person[1]:<15} {person[2]:<15}")

        person_id = input("\n ID: ")

        print("1 - Last name")
        print("2 - Name")
        field = input("Tanda: ")

        if field == "1":
            new_last_name = input("New Last name: ")
            cur.execute(
                "UPDATE contacts SET last_name = %s WHERE id = %s;",
                (new_last_name, person_id)
            )

        elif field == "2":
            new_name = input("New name: ")
            cur.execute(
                "UPDATE contacts SET name = %s WHERE id = %s;",
                (new_name, person_id)
            )

        else:
            print("Qate tandau!")
            cur.close()
            return

    elif choice == "2":
        cur.execute("SELECT id, last_name, name FROM contacts ORDER BY id;")
        people = cur.fetchall()

        print("\n--- CONTACTS ---")
        print(f"{'ID':<5} {'Surname':<15} {'Name':<15}")
        print("-" * 40)

        for person in people:
            print(f"{person[0]:<5} {person[1]:<15} {person[2]:<15}")

        person_id = input("\nAdam ID: ")

        cur.execute("""
            SELECT id, phone, operator, email, birthday
            FROM contact_info
            WHERE contact_id = %s
            ORDER BY id;
        """, (person_id,))

        infos = cur.fetchall()

        if not infos:
            print("Bul adamda aqparat joq!")
            cur.close()
            return

        print("\n--- CONTACT INFO ---")
        print(f"{'Info_ID':<8} {'Phone':<15} {'Operator':<12} {'Email':<25} {'Birthday'}")
        print("-" * 80)

        for info in infos:
            print(f"{info[0]:<8} {info[1]:<15} {info[2]:<12} {info[3]:<25} {info[4]}")

        info_id = input("\nOzgertetin aqparat Info_ID: ")

        print("1 - Phone")
        print("2 - Operator")
        print("3 - Email")
        print("4 - Birthday")
        field = input("Ozgertetin field: ")

        if field == "1":
            new_phone = input("New phone: ")
            cur.execute(
                "UPDATE contact_info SET phone = %s WHERE id = %s;",
                (new_phone, info_id)
            )

        elif field == "2":
            new_operator = input("New operator: ")
            cur.execute(
                "UPDATE contact_info SET operator = %s WHERE id = %s;",
                (new_operator, info_id)
            )

        elif field == "3":
            new_email = input("New email: ")
            cur.execute(
                "UPDATE contact_info SET email = %s WHERE id = %s;",
                (new_email, info_id)
            )

        elif field == "4":
            new_birthday = input("New birthday (YYYY-MM-DD): ")
            cur.execute(
                "UPDATE contact_info SET birthday = %s WHERE id = %s;",
                (new_birthday, info_id)
            )

        else:
            print("Qate tandau!")
            cur.close()
            return

    else:
        print("Qate tandau!")
        cur.close()
        return

    conn.commit()

    if cur.rowcount == 0:
        print("Bul ID boiynsha aqparat tabylmady!")
    else:
        print("Aqparat ozgertildi!")

    cur.close()

def infor_delete(conn):
    cur = conn.cursor()

    print("Ne oshiresin?")
    print("1 - Adamdy tolyq oshiru")
    print("2 - Adamnyn bir nomerin/aqparatyn oshiru")

    choice = input("Tanda: ")

    if choice == "1":
        cur.execute("SELECT id, last_name, name FROM contacts ORDER BY id;")
        people = cur.fetchall()

        print("\n--- CONTACTS ---")
        print(f"{'ID':<5} {'Surname':<12} {'Name':<12}")
        print("-" * 35)

        for person in people:
            print(f"{person[0]:<5} {person[1]:<12} {person[2]:<12}")

        person_id = input("\nOshiretin adam ID: ")

        sure = input("Rasymen adamdy tolyq oshiresinbe? (yes/no): ")

        if sure.lower() == "yes":
            cur.execute("DELETE FROM contacts WHERE id = %s;", (person_id,))
            conn.commit()

            if cur.rowcount == 0:
                print("Bul ID boiynsha adam tabylmady!")
            else:
                print("Adam tolyq oshirildi!")
        else:
            print("Oshiru toqtady.")

    elif choice == "2":
        cur.execute("SELECT id, last_name, name FROM contacts ORDER BY id;")
        people = cur.fetchall()

        print("\n--- CONTACTS ---")
        print(f"{'ID':<5} {'Surname':<12} {'Name':<12}")
        print("-" * 35)

        for person in people:
            print(f"{person[0]:<5} {person[1]:<12} {person[2]:<12}")

        person_id = input("\nAdam ID: ")

        cur.execute("""
            SELECT id, phone, operator, email, birthday
            FROM contact_info
            WHERE contact_id = %s
            ORDER BY id;
        """, (person_id,))

        infos = cur.fetchall()

        if not infos:
            print("Bul adamda aqparat/nomer joq!")
            cur.close()
            return

        print("\n--- CONTACT INFO ---")
        print(f"{'Info_ID':<8} {'Phone':<15} {'Operator':<10} {'Email':<22} {'Birthday'}")
        print("-" * 75)

        for info in infos:
            print(f"{info[0]:<8} {info[1]:<15} {info[2]:<10} {info[3]:<22} {info[4]}")

        info_id = input("\nOshiretin aqparat ID: ")

        cur.execute("DELETE FROM contact_info WHERE id = %s;", (info_id,))
        conn.commit()

        if cur.rowcount == 0:
            print("Bul Info_ID boiynsha aqparat tabylmady!")
        else:
            print("Aqparat/nomer oshirildi!")

    else:
        print("Qate tandau!")

    cur.close()


def infor_show(conn):
    cur = conn.cursor()

    cur.execute("SELECT id, last_name, name FROM contacts ORDER BY id;")
    people = cur.fetchall()

    print("\n--- CONTACTS ---")
    print(f"{'ID':<5} {'Surname':<12} {'Name':<12}")
    print("-" * 30)

    for person in people:
        print(f"{person[0]:<5} {person[1]:<12} {person[2]:<12}")

    person_id = input("\nAdam ID engiz: ")

    cur.execute("""
        SELECT c.last_name, c.name,
               i.phone, i.operator, i.email, i.birthday
        FROM contacts c
        LEFT JOIN contact_info i ON c.id = i.contact_id
        WHERE c.id = %s;
    """, (person_id,))

    rows = cur.fetchall()

    if not rows:
        print("Bul ID boiynsha adam tabylmady!")
    else:
        print("\n--- FULL INFO ---")
        print(f"Surname: {rows[0][0]}")
        print(f"Name: {rows[0][1]}")
        print(f"Email: {rows[0][4]}")
        print(f"Birthday: {rows[0][5]}")

        print("\nPhones:")
        for row in rows:
            if row[2]:
                print(f"{row[2]} ({row[3]})")

    cur.close()


def infor_search(conn):
    cur = conn.cursor()

    print("Search information")
    print("1 - Contact ID")
    print("2 - Last name")
    print("3 - Name")
    print("4 - Phone")
    print("5 - Operator")
    print("6 - Email")
    print("7 - Birthday")

    tanday = input("Input information: ")

    if tanday == "1":
        search_id = input("ID: ")
        cur.execute("""
            SELECT c.id, c.last_name, c.name,
                   i.phone, i.operator, i.email, i.birthday
            FROM contacts c
            LEFT JOIN contact_info i ON c.id = i.contact_id
            WHERE c.id = %s
            ORDER BY i.id;
        """, (search_id,))

    elif tanday == "2":
        search_last_name = input("Last name: ")
        cur.execute("""
            SELECT c.id, c.last_name, c.name,
                   i.phone, i.operator, i.email, i.birthday
            FROM contacts c
            LEFT JOIN contact_info i ON c.id = i.contact_id
            WHERE c.last_name ILIKE %s
            ORDER BY c.id, i.id;
        """, ('%' + search_last_name + '%',))

    elif tanday == "3":
        search_name = input("Name: ")
        cur.execute("""
            SELECT c.id, c.last_name, c.name,
                   i.phone, i.operator, i.email, i.birthday
            FROM contacts c
            LEFT JOIN contact_info i ON c.id = i.contact_id
            WHERE c.name ILIKE %s
            ORDER BY c.id, i.id;
        """, ('%' + search_name + '%',))

    elif tanday == "4":
        search_phone = input("Phone: ")
        cur.execute("""
            SELECT c.id, c.last_name, c.name,
                   i.phone, i.operator, i.email, i.birthday
            FROM contacts c
            LEFT JOIN contact_info i ON c.id = i.contact_id
            WHERE i.phone ILIKE %s
            ORDER BY c.id, i.id;
        """, ('%' + search_phone + '%',))

    elif tanday == "5":
        search_operator = input("Operator: ")
        cur.execute("""
            SELECT c.id, c.last_name, c.name,
                   i.phone, i.operator, i.email, i.birthday
            FROM contacts c
            LEFT JOIN contact_info i ON c.id = i.contact_id
            WHERE i.operator ILIKE %s
            ORDER BY c.id, i.id;
        """, ('%' + search_operator + '%',))

    elif tanday == "6":
        search_email = input("Email: ")
        cur.execute("""
            SELECT c.id, c.last_name, c.name,
                   i.phone, i.operator, i.email, i.birthday
            FROM contacts c
            LEFT JOIN contact_info i ON c.id = i.contact_id
            WHERE i.email ILIKE %s
            ORDER BY c.id, i.id;
        """, ('%' + search_email + '%',))

    elif tanday == "7":
        search_birthday = input("Birthday (YYYY-MM-DD): ")
        cur.execute("""
            SELECT c.id, c.last_name, c.name,
                   i.phone, i.operator, i.email, i.birthday
            FROM contacts c
            LEFT JOIN contact_info i ON c.id = i.contact_id
            WHERE i.birthday = %s
            ORDER BY c.id, i.id;
        """, (search_birthday,))

    else:
        print("ERROR")
        cur.close()
        return

    rows = cur.fetchall()

    if not rows:
        print("Esh narse jok!")
    else:
        print(f"{'ID':<5} {'Surname':<15} {'Name':<15} {'Phone':<15} {'Operator':<12} {'Email':<25} {'Birthday'}")
        print("-" * 100)

        for row in rows:
            print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15} {row[3]:<15} {row[4]:<12} {row[5]:<25} {row[6]}")

    cur.close()


def infor_count_DB(conn):
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM contacts;")
    total = cur.fetchone()[0]

    print(f"Barlyq adam sany: {total}")

    cur.close()


def infor_all_delete(conn):
    cur = conn.cursor()

    sure = input("Barlyq derekterdi oshiresinbe? (yes/no): ")

    if sure.lower() == "yes":
        cur.execute("DELETE FROM contact_info;")

        cur.execute("DELETE FROM contacts;")

        conn.commit()
        print("Barlyq derekter oshirildi!")

    else:
        print("Stopped!")

    cur.close()

def infor_limit_show(conn):
    cur = conn.cursor()

    limit = int(input("Qansha adam shygarylsyn?: "))

    cur.execute("""
        SELECT id, last_name, name
        FROM contacts
        ORDER BY id
        LIMIT %s;
    """, (limit,))

    rows = cur.fetchall()

    if not rows:
        print("Derek joq!")
    else:
        print(f"{'ID':<5} {'Surname':<15} {'Name':<15}")
        print("-" * 40)

        for row in rows:
            print(f"{row[0]:<5} {row[1]:<15} {row[2]:<15}")

    cur.close()

conn = connect_db()

while True:
    print("             ")
    print("----MENU----")
    print("1 - Information Add!")
    print("2 - Information Many Add")
    print("3 - Information Update!")
    print("4 - Information Delete!")
    print("5 - Information Show!")
    print("6 - Information Search")
    print("7 - Information count all DB")
    print("8 - Infromation all delete")
    print("9 - Information limit show")
    print("0 - EXIT!")

    function_number = input("Number fuction: ")

    if function_number == "1":
        infor_add(conn)
    
    elif function_number == "2":
        infor_many_add(conn)
    
    elif function_number == "3":
        infor_update(conn)
    
    elif function_number == "4":
        infor_delete(conn)
    
    elif function_number == "5":
        infor_show(conn)
    
    elif function_number == "6":
        infor_search(conn)

    elif function_number == "7":
        infor_count_DB(conn)
    
    elif function_number == "8":
        parol = input("Password: ")

        if parol == "9495082020":
            infor_all_delete(conn)
            print("Барлық деректер кетірілді!")
        
        else:
            print("parol kate!")
            continue

    elif function_number == "0":        
        print("Thank you! Function toktatyldu!")
        break
    
    elif function_number == "9":
        infor_limit_show(conn)
        
    else:
        print("Error for number!")

conn.close()