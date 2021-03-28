import psycopg2 as ps
import pandas as pd


def getDfFromPostgre(settings, sql):
    # create connection to postgresql
    connection = ps.connect(**settings)
    # create cursor
    cursor = connection.cursor()
    # execute sql query
    cursor.execute(sql)
    # get data from cursor
    data = cursor.fetchall()
    # set data to pandas df
    column_names = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(data, columns=column_names)
    return df


# create connection settings
options = {
    "host": "localhost",
    "database": "online_shop",
    "user": "postgres",
    "password": "i77GPf#%",
}

sql = "select * from users_data,departments;"

dataFrame = getDfFromPostgre(options, sql)
print(dataFrame.head())