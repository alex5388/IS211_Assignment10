import sqlite3

conn = sqlite3.connect('pets.db')

def main():
    with conn:

        c = conn.cursor()

        while True:
            id = input("Enter Pet Owner's ID number. Enter '-1' to exit. ")

            #exit program
            if int(id) < 0:
                print('Exiting...')
                exit()


            #query with security => (?)
            c.execute("SELECT first_name, last_name, person.age, name, breed,"
                        "pet.age, dead FROM person, pet, person_pet "
                        "WHERE person.id = person_pet.person_id AND "
                        "pet.id = person_pet.pet_id AND person.id=(?)", (id))

            #get query info to display later
            person = c.fetchall()

            #valid entry check
            if len(person) == 0:
                print('Invalid ID. Try again...')
                continue

            #iterate through tables
            for row in person:
                first_name = row[0]
                last_name = row[1]
                age = row[2]
                pet_name = row[3]
                pet_type = row[4]
                pet_age = row[5]
                dead = row[6]

                #conditonal output dependent on pet's life
                if dead == 1:
                    print (f'{first_name} {last_name}, age {age}, owned a {pet_type} named {pet_name}, who was {pet_age} years old.')
                else:
                    print (f'{first_name} {last_name}, age {age}, owns a {pet_type} named {pet_name}, who is {pet_age} years old.')

if __name__ == "__main__":
    main()
