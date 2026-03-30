import psycopg2

def connect_db():
    conn = psycopg2.connect(
        dbname = "postgres",
        user = "postgres",
        password = "9495082020",
        host = "127.0.0.1",
        port = "5432"
    )
    return conn

def infor_add(conn):
    cur = conn.cursor()
    
    name = input("Atyn engiz: ")
    phone = input("Phone engiz: ")
    operator = input("Operator engiz: ")
    region = input("Region engiz: ")

    cur.execute(
        "INSERT INTO Book (name, phone, operator, region)  VALUES (%s, %s, %s, %s) ;",
        (name, phone, operator, region)
    )

    conn.commit()
    print("Information add!")
    
    cur.close()


def infor_update(conn):
    cur = conn.cursor()

    name_update_information = input("Adam aty: ")
    
    print("Ozgeretin information!")
    print("1 - Name")
    print("2 - Phone")
    print("3 - Operator")
    print("4 - Region")
    
    tanday = input("Function tanda: ")

    if tanday == "1":
        new_name = input("New name: ")
        
        cur.execute(
            "UPDATE Book SET name = %s WHERE name = %s ;", 
            (new_name, name_update_information)
        )
    

    elif tanday == "2":
        new_phone = input("New phone: ")
        
        cur.execute(
            "UPDATE Book SET phone = %s WHERE name = %s ;", 
            (new_phone, name_update_information)
        )    
    
    
    elif tanday == "3":
        new_operator = input("New operator: ")

        cur.execute(
            "UPDATE Book SET operator = %s WHERE name = %s ;",
            (new_operator, name_update_information)
        )


    elif tanday == "4":
        new_region = input("New region: ")

        cur.execute(
            "UPDATE Book SET region = %s WHERE name = %s ;",
            (new_region, name_update_information)
        )

    else:
        print("Error!")
        cur.close()
        return

    conn.commit()

    if cur.rowcount == 0:
        print("Error for NAME!")
    else:
        print("Update information!")
       
    cur.close()


def infor_delete(conn):
    cur = conn.cursor()

    name_delete_information = input("Adam aty: ")

    cur.execute(
        "DELETE FROM Book WHERE name = %s ;", 
        (name_delete_information,)
    )
    conn.commit()

    if cur.rowcount == 0:
        print("Error for NAME!")
    else:
        print("Delete information!")
    
    cur.close()


def infor_show(conn):
    cur = conn.cursor()

    cur.execute("SELECT * FROM Book ORDER BY id;")
    rows = cur.fetchall()

    print("All information!")
    print("                ")
    print(f"{'ID':<5} {'Name':<10} {'Phone':<20} {'Operator':<10} {'Region':<10}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<10} {row[2]:<20} {row[3]:<10} {row[4]:<10}")
    
    cur.close


def infor_search(conn):
    cur = conn.cursor()

    print("Search information")
    print("1 - ID")
    print("2 - Name")
    print("3 - Phone")
    print("4 - Operator")
    print("5 - Region")

    tanday = input("input information: ")
    
    
    if tanday == "1":
        search_ID = int(input("ID: "))
        cur.execute(
            "SELECT * FROM Book WHERE ID = %s",
            (search_ID, )
        )
                
    elif tanday == "2":
        search_name = input("Name: ")
        cur.execute(
            "SELECT * FROM Book WHERE name ILIKE %s",
            ('%' + search_name + '%',)
        )
        
    elif tanday == "3":
        search_phone = input("Phone: ")
        cur.execute(
            "SELECT * FROM Book WHERE phone ILIKE %s",
            ('%' + search_phone + '%',)
        )
            
    elif tanday == "4":
        search_operator = input("Operator: ")
        cur.execute(
            "SELECT * FROM Book WHERE operator ILIKE %s",
            ('%' + search_operator + '%',)
        )
        
    elif tanday == "5":
        search_region = input("Region: ")
        cur.execute(
            "SELECT * FROM Book WHERE region ILIKE %s",
            ('%' + search_region + '%',)
        )
                
    else:
        print("ERROR")
        cur.close()
        return
    
    rows = cur.fetchall()

    if not rows:
        print("Esh narse jok!")
    else:
        print(f"{'ID':<5} {'Name':<10} {'Phone':<20} {'Operator':<10} {'Region':<10}")
        print("-" * 60)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<20} {row[3]:<10} {row[4]:<10}")
    
    cur.close()



conn = connect_db()

while True:
    print("             ")
    print("----MENU----")
    print("1 - Information Add!")
    print("2 - Information Update!")
    print("3 - Information Delete!")
    print("4 - Information Show!")
    print("5 - Information Search")
    print("0 - EXIT!")

    function_number = input("Number fuction: ")

    if function_number == "1":
        infor_add(conn)
    
    elif function_number == "2":
        infor_update(conn)
    
    elif function_number == "3":
        infor_delete(conn)
    
    elif function_number == "4":
        infor_show(conn)
    
    elif function_number == "5":
        infor_search(conn)
    
    elif function_number == "0":
        print("Thank you! Function toktatyldu!")
        break
    
    else:
        print("Error for number!")

conn.close()