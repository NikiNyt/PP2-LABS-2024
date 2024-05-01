import psycopg2
from config import load_config

def create_tables():
    commands = (
         """
         create sequence phonebook_id_seq;
         """,
         """
          CREATE TABLE phonebook (
            id integer default nextval('Phonebook_id_seq'::regclass) primary key,
            user_name VARCHAR(255) NOT NULL,
            user_phone VARCHAR(11) NOT NULL
        )
         """)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()