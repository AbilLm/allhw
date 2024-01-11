import sqlite3
from pathlib import Path


def init_db():
    db_path = Path(__file__).parent.parent / "db.sqlite"
    global db, cursor
    db = sqlite3.connect(db_path)
    cursor = db.cursor()



def create_tables():
    cursor.execute("""
        DROP TABLE IF EXISTS catalog
    """)
    cursor.execute("""
        DROP TABLE IF EXISTS category
    
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
            )
    
    
    
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS catalog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            amount INTEGER,
            image TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category(id)
              
        )
        
    
    """)
    db.commit()
def populate_tables():
    cursor.execute("""
        INSERT INTO category(name) VALUES 
        ('быт.техника'),
        ("книги"),
        ('одежда')
    
    
    

    """)
    cursor.execute("""
        INSERT INTO catalog(name, amount, image, category_id) VALUES 
        ('Поварешка', '1', 'images/OIP(1).jpg', 1),
        ('Кастрюля', '2', 'images/OIP.jpg', 1),
        ('Война и Мир', '3', 'img.jpg', 2),
        ('Норвежский лес', '2', 'img.jpg', 2),
        ('Свитер', '2', 'img.jpg', 3),
        ('Джинсы', '3', 'img.jpg', 3)
    
    
    
    
    """)
    db.commit()

def get_catalog():
    cursor.execute("SELECT * FROM catalog ")
    return cursor.fetchall()

def get_object(cat_id:int):
    cursor.execute("""
    SELECT * FROM catalog WHERE category_id = :cat_id
    
    """, {"cat_id": cat_id})
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
    #print(get_catalog())