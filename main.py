import psycopg2
import pandas as pd
import sys
# Connection parameters, yours will be different
param_dic = {
    "host": "localhost",
    "database": "online_shop",
    "user": "postgres",
    "password": "i77GPf#%"
}


def connect(params_dic):
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn


def postgresql_to_dataframe(conn, select_query, column_names):
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df

# Connect to the database
conn = connect(param_dic)
column_names = ["dept_no", "dept_name"]
# Execute the "SELECT *" query
df = postgresql_to_dataframe(conn, "select * from departments", column_names)
print(df.head())