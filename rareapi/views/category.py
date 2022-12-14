import sqlite3
import json
from models import Category

def get_all_category():
    """this is a docstring"""
    # Open a connection to the database
    with sqlite3.connect('./db.sqlite3') as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Category c
        ORDER BY label ASC
        """)

        category = []

        dataset = db_cursor.fetchall()

    for row in dataset:
        category_list = Category(row['id'], row['label'])

        category.append(category_list.__dict__)

    return json.dumps(category)

def get_single_category(id):
    """docstring"""
    with sqlite3.connect('./db.sqlite3') as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Category c
        WHERE c.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        category = Category(data['id'], data['label'])


    return json.dumps(category.__dict__)


def create_category(new_category):
    """docstring"""
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Category
            ( label )
        VALUES
            ( ? )
        """, (
        new_category['label'],
        ))

        id = db_cursor.lastrowid
        new_category['id'] = id


    return json.dumps(new_category)

def delete_category(id):
    """docstring
        """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM category
        WHERE id = ?
        """, (id, ))
