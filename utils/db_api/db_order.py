import sqlite3


class Orders:

    def __init__(self):
        self.connection = sqlite3.connect("Orders")
        self.cursor = self.connection.cursor()

    def create_order(self):

        self.cursor.execute("""
        
            create table orders (        
                id integer primary key ,
                customer varchar,
                product_id varchar            
            )
        """)

    def add_order(self, customer, product_id):
        self.cursor.execute("""
        
            insert into orders (customer, product_id) values (?, ? )

        
        """, (customer, product_id))
        self.connection.commit()


    def get_order_by_customer(self,customer):
        self.cursor.execute("""
        
            select * from orders where customer = ?
        
        
        """,  (customer, )).fetchall()

    def order_delete(self, id):
        self.cursor.execute("""
            delete from orders where id = ?
        
        """, (id, ))
        self.connection.commit()

    def create_product_list(self):
        self.cursor.execute("""
               create table if not exists products(
                   id integer primary key ,
                   title varchar ,
                   description varchar ,
                   price varchar ,
                   categories varchar ,
                   photo varchar
               )
           """)

    def add_product(self,title, description, price, categories, photo):
        self.cursor.execute("""
        
                insert into products (title, description, price, categories,photo) values 
                (?, ? , ?, ?, ?)        
        """, (title, description, price, categories, photo))

    def all_product(self):
        self.cursor.execute("""
        
            select * from products 
        
        
        
        """ ).fetchall()
        return self.connection.commit()

    def get_product(self, id):
        self.cursor.execute("""
        
            select * from products where id= ? 
        
        
        """, (id,)).fetchone()

    def delete_product(self, id):
        self.cursor.execute("""
        
        delete from products where id=?
        
        
        """, (id, ))
        return self.connection.commit()















