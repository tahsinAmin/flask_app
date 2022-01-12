import psycopg2
import psycopg2.extras
import collections
import json

# connect tom the db
conn = None

# for office
try:
    with psycopg2.connect(
        host = 'localhost',
        database = 'test',
        user = 'postgres',
        password = 'password',
        port = 5432) as conn:

        # cursor
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            objects_list = []
            cur.execute('SELECT * FROM hotels_content')
            rows = cur.fetchall()
            for record in rows:
                d = collections.OrderedDict()
                d['id']         = record['id']
                d['title']      = record['title']
                d['price']      = record['price']
                d['review']     = record['review']
                d['location']   = record['location']
                d['amenities']  = record['amenities']
                d['image_link'] = record['image_link']
                objects_list.append(d)
            
            j = json.dumps(objects_list)
            print(j)
            with open('hotel_objects.js','w') as f:
                f.write(j)

except Exception as error:
    print(error)
finally:
    # finally will execute with or wiothout any error bcz if and error occurs, the try block stops.

    if conn is not None:
        # close the connection
        conn.close()