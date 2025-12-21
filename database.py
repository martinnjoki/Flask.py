import psycopg2

conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='1234',dbname='myduka')

cur = conn.cursor()


def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products = get_products()
print(products)



def get_stock():
    cur.execute("SELECT * FROM stock")
    stock = cur.fetchall()
    return stock


def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()

   
def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

def get_users():
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return users


#method 1 - f-string
def insert_sales(values):
    cur.execute(f"insert into sales(pid,quantity)values{values}")
    conn.commit()


#method 2 - using placeholders
def insert_sales_2(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",values)
    conn.commit()
    
     

def available_stock(pid):
    cur.execute(f'SELECT sum(stock_quantity) FROM stock WHERE pid = {pid}')
    total_stock = cur.fetchone()[0] or 0

    cur.execute(f'SELECT sum (quantity) FROM sales WHERE pid = {pid}')
    total_sales = cur.fetchone()[0] or 0

    return total_stock - total_sales 

def insert_stock(values):
    cur.execute(f"insert into stock (pid, stock_quantity) values{values}")
    conn.commit() 

def insert_users(values):
    cur.execute(f"insert into users (full_name, email, phone_number, password) values{values}") 
    conn.commit()  

def check_user_exists(email):
    cur.execute("SELECT * FROM users WHERE email = %s ", (email,)) 
    user = cur.fetchone()
    return user
#sales_per_product
def sales_per_product():
    cur.execute("""select products.name as p_name, sum(products.selling_price * sales.quantity)
             as total_sales from products join sales on products.id = sales.pid group by(p_name)
                """)
    product_sales = cur.fetchall()
    return product_sales 

#sales per day

def sales_per_day():
    cur.execute("""select sales.created_at as date, sum(products.selling_price * sales.quantity)
             as total_sales from products join sales on products.id = sales.pid group by(date)
    """)
    daily_sales = cur.fetchall()
    return daily_sales

#profit per day

def profit_per_day():
    cur.execute(""" 
    select sales.created_at as date , sum((products.selling_price - products.buying_price) * sales.quantity)
    as profit from products join sales on sales.pid = products.id group by(date)
    """)
    daily_profit = cur.fetchall()
    return daily_profit

#profit_per_product

def profit_per_product():
    cur.execute(""" 
        select products.name as p_name , sum((products.selling_price - products.buying_price) * sales.quantity)
            as profit from products join sales on sales.pid = products.id group by(p_name)
    """)
    product_profit = cur.fetchall()
    return product_profit
#
x = profit_per_product()
print(x)

# [('LED Desk Lamp', Decimal('200.00')), ('Maize', Decimal('2000.00'))]









