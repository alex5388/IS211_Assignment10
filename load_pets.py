import sqlite3

conn = sqlite3.connect('pets.db')
c = conn.cursor()

def main():
    #insert people
    c.execute("INSERT INTO person(first_name, last_name, age) VALUES ('James', 'Smith', 41)")
    c.execute("INSERT INTO person(first_name, last_name, age) VALUES ('Diana', 'Greene', 23)")
    c.execute("INSERT INTO person(first_name, last_name, age) VALUES ('Sara', 'White', 27)")
    c.execute("INSERT INTO person(first_name, last_name, age) VALUES ('William', 'Gibson', 23)")

    #insert pets
    c.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Rusty', 'Dalmation', 4, 1)")
    c.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Bella', 'Alaskan Malamute', 3, 0)")
    c.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Max', 'Cocker Spaniel', 1, 0)")
    c.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Rocky', 'Beagle', 7, 0)")
    c.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Rufus', 'Cocker Spaniel', 1, 0)")
    c.execute("INSERT INTO pet(name, breed, age, dead) VALUES ('Spot', 'Bloodhound', 2, 1)")

    #insert person_pet relationship
    c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES (1,1)")
    c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES (1,2)")
    c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES (2,3)")
    c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES (2,4)")
    c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES (3,5)")
    c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES (4,6)")


    #c.execute('DELETE FROM person WHERE rowid = 8')
    c.execute('select * from person')
    print(c.fetchall())
    conn.commit()
    conn.close()

if __name__=="__main__":
    main()