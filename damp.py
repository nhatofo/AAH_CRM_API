import json, psycopg2 
from urllib.parse import urlencode
from urllib.request import Request, urlopen


# Create Table

def create_table(
    sql_query: str, 
    conn: psycopg2.extensions.connection, 
    cur: psycopg2.extensions.cursor
) -> None:
    try:
        # Execute the table creation query
        cur.execute(sql_query)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        print(f"Query: {cur.query}")
        conn.rollback()
        cur.close()
    else:
        # To take effect, changes need be committed to the database
        conn.commit()

def drop_table(
    sql_query: str, 
    conn: psycopg2.extensions.connection, 
    cur: psycopg2.extensions.cursor
) -> None:
    try:
        # Execute the table creation query
        cur.execute(sql_query)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        print(f"Query: {cur.query}")
        conn.rollback()
        cur.close()
    else:
        # To take effect, changes need be committed to the database
        conn.commit()

if __name__ == "__main__":

    # Connect to the database 
    connection = psycopg2.connect(database='postgres', user='postgres', password='docker', host='localhost', port='5432')
    cursor = connection.cursor()



    drop_sql = """
           DROP TABLE if exists trans_staging;
    """  

    trans_sql = """
        CREATE TABLE trans_staging  (
            id SERIAL PRIMARY KEY,
            first_name   varchar(45) NOT NULL,
            last_name    varchar(45) NOT NULL,
            date_of_birth date NOT NULL,
            phone varchar(20) NOT NULL,
            company_name varchar(40) NOT NULL,
            company_description varchar(80) NOT NULL,
            job varchar(50),
            email varchar(50),
            user_name varchar(50) NOT NULL,
            credit_card_number bigint NOT NULL,
            credit_card_provider varchar(40) NOT NULL,
            credit_card_expire date NOT NULL,
            address_street varchar(45) NOT NULL,
            addrss_postal varchar(45) NOT NULL,
            address_country varchar(45) NOT NULL
        );
    """
drop_table(drop_sql, connection, cursor)
create_table(trans_sql, connection, cursor)

fields = [
    'id',
    'first_name',
    'last_name',
    'date_of_birth',
    'phone',
    'company_name',
    'company_description',
    'job',
    'email',
    'user_name',
    'credit_card_number',
    'credit_card_provider',
    'credit_card_expire',
    'address_street',
    'addrss_postal',
    'address_country'
]

for apidata in fields:
    my_data = [apidata[field] for field in fields]
    insert_query = "INSERT INTO trans_staging VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s, %d, %s, %s, %s, %s, %s)" #%d for int %s for string
    connection.execute(insert_query, tuple(my_data))
    cursor.commit()

print("Done..")

    # Close all connections to the database
connection.close()
cursor.close()