import psycopg2

conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='1234',dbname='myduka_db')

cur = conn.cursor()


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products = get_products()
print(products)


def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()

   



def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


#method 1 - f-string
def insert_sales(values):
    cur.execute(f"insert into sales(pid,quantity)values{values}")
    conn.commit()


#method 2 - using placeholders
def insert_sales_2(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",values)
    conn.commit()





