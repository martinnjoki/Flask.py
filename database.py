import psycopg2
conn = psycopg2.connect(host='localhost', user='postgres', password = '1234', dbname = 'myduka_db')
cur = conn.cursor()
cur.execute("SELECT * FROM products")
products = cur.fetchall()
print(products)

cur.execute("insert into products(name,buying_price,selling_price)values('samsung', 15000,20000)")
conn.commit()
print(products)

cur.execute("SELECT * FROM sales")
sales = cur.fetchall()
print(sales)

def insert_sales(values):
    cur.execute(f"insert into sales(pid, quantity)values{values}")
    conn.commit()
sales1 = (10, 2)
sales2 = (9,  3)
insert_sales(sales1)
insert_sales(sales2)    
    

def get_sales():
    cur.execute("SELECT * FROM sales")
    sales = cur.fetchall()
    get_sales()
      