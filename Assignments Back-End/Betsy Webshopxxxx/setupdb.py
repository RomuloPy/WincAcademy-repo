from models import (db, User, Tag, Product, OrderTransaction, UserProduct)
import os
from time import sleep


def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "database.db")
    if os.path.exists(database_path):
        os.remove(database_path)


def populate_test_data():
    db.connect()
    print("Initializing database, please wait...")
    db.create_tables([User, Tag, Product, UserProduct, OrderTransaction])

    users = [
        {'name': 'Antonio',
        'address': 'Costa',
        'payment': 1234},
        {'name': 'Rafael',
        'address': 'Gala',
        'payment': 2345},
        {'name': 'Jason',
        'address': 'Helmond',
        'payment': 3456},
        {'name': 'Romulo',
        'address': 'Leonardus',
        'payment': 4567},
    ]

    for user in users:
        User.create(
            name = user['name'],
            address = user['address'],
            payment = user['payment']
        )
    
    tags = ['strings', 'percussion', 'wind', 'electronic', 'membrane']

    for tag in tags:
        Tag.create(tag = tag)

    products = [
        {'name': 'Piano',
        'description': 'Modern-day piano ancestry is traced to various instruments such as Clavichord, Dulcimer, and Harpsichord. Cristofori, unsatisfied by the lack of control over the volume level of the Harpsichord, replaced the plucking mechanism from the old versions with a hammer to create the modern piano. A Piano player activates these hammers by pressing keys on the Keyboard, and the harder the pressure, the louder is the volume. It belongs to both the string and the percussion family and technically is one of the most complicated musical instruments, with over 2500 parts.',
        'price': 5000.00,
        'quantity': 2,
        'tags': 'strings'},

        {'name': 'Bass Guitar',
        'description': 'The bass guitar, electric bass or simply bass, is the lowest-pitched member of the guitar family. It is a plucked string instrument similar in appearance and construction to an electric or acoustic guitar, but with a longer neck and scale length, and typically four to six strings or courses. Since the mid-1950s, the bass guitar has largely replaced the double bass in popular music.',
        'price': 1000.00,
        'quantity': 8,
        'tags': 'strings'},

        {'name': 'Drum Set',
        'description': 'A Drum set or simply drums is a collection of large and small drums, cymbals, and other percussion instruments. They are arranged on stands to be played by a single person. The percussion instruments may vary for each genre and from one drummer to other. The drum sticks are held in the hands to hit the drums, and the feet operate the pedals that control the Cymbals.',
        'price': 3500.00,
        'quantity': 4,
        'tags': 'percussion'},

        {'name': 'Keyboard',
        'description': 'A musical Keyboard is a diverse instrument with a set of depressible keys or levers placed adjacent to each other. It belongs to the percussion family of the instruments, and various notes are played by pressing these keys with fingers.',
        'price': 1500.00,
        'quantity': 6,
        'tags': 'electronic'},

        {'name': 'Saxophone',
        'description': 'The saxophone is a woodwind instrument. It has a conical tube, typically made of brass, with variously sized about 20 to 24 openings controlled by padded keys. The tip of this conical tube is flared into the shape of a bell to let the air pass. A player holds the sax with their hands and uses their fingers to press on the keys to play it.',
        'price': 2500.00,
        'quantity': 3,
        'tags': 'wind'},

        {'name': 'Electric Guitar',
        'description': 'The electric guitar is a string instrument with steel strings, unlike the nylon ones found on the classical guitar. They have devices called magnetic pickups embedded into their body under the strings. When the strings vibrate, these pickups convert the vibrations into electric signals, which pass through an amplifier over a cable where they are converted into sound and played. They have a wooden body and the widest range of shapes possible, as the shape of an electric guitar doesn’t affect the sound it produces.',
        'price': 950.00,
        'quantity': 10,
        'tags': 'strings'},
    ]

    for product in products:
        Product.create(
            name = product['name'],
            description = product['description'],
            price = product['price'],
            quantity = product['quantity'],
            tags = product['tags'],
        )
    
    # User Products
    user_products = [
        {'owner': 'Jason',
        'product': 'Piano',
        'quantity': 1,
        },
        {'owner': 'Rafael',
        'product': 'Drum Set',
        'quantity': 1,
        },
        {'owner': 'Romulo',
        'product': 'Bass Guitar',
        'quantity': 2,
        }

    ]

    for user_product in user_products:
        UserProduct.create(
            owner = user_product['owner'],
            product = user_product['product'],
            quantity = user_product['quantity'],
        )
    

    db.close()
    sleep(5)
    print("Database Successfully Created!")

if __name__ == "__main__":
    delete_database()
    populate_test_data()