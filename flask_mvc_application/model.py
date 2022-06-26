from config import db  # aware abt --> flask mysql sam_db

#MODEL --> a class which is aware about --> database mapping..
class Product(db.Model):        #model class --> this class is aware about -- table coumns
    __tablename__ = "PRODUCT_INFO"
    id = db.Column("product_id",db.Integer,primary_key=True)
    name = db.Column("product_name",db.String(30),nullable=False)
    qty = db.Column("product_qty",db.Integer)
    price = db.Column("product_price",db.Float)  #float ---> mysql --> sqlalchemy
    vendor = db.Column("product_vendor",db.String(30),nullable=False)
    barcode = db.Column("product_barcode",db.String(30),unique=True)

    def __str__(self):
        return f'''\n {self.__dict__}'''

    def __repr__(self):
        return str(self)

#products = Product.query.filter(Product.id.between(100,120)).all()
#print(products)
#import sys
#sys.exit(0)
#query----products whose price between .. and ....
#products = Product.query.filter(Product.price.between(100,500)).all()
#print(products)


#from sqlalchemy import or_,and_,any_
#query--->products whose name is ... and vendor is ....
# products = Product.query.filter(and_(Product.name=='Mobile', Product.vendor=="Flipkart")).all()
# print(products)



#query--->we want products whose name is .....
# product = Product.query.filter(Product.name == "cheri").all()
# print(product)
# import sys
# sys.exit(0)

#for primary key--->used filter_by().first()
#for other attributre--->we use filter().all()
#query----->product whose id is...
# product = Product.query.filter_by(id = 1041).first()
# print(product)
# import sys
# sys.exit(0)
# #select *
# all_products = Product.query.all()
# print(all_products)


"""
#create table
db.create_all() # create table -->

#insert into
p1 = Product(id=356,name="cheri",qty=23,price=283.34,vendor="Flipkart",barcode="@*(SK(##")
db.session.add(p1)
db.session.commit()

#bulk_insert
p2 = Product(id=11,name="MObile",qty=233,price=0283.34,vendor="Flipkart",barcode="2*(SK#*(##")
p3 = Product(id=12,name="MObile",qty=243,price=9283.34,vendor="Flipkart",barcode="@*4(SK#*(##")
p4 = Product(id=13,name="MObile",qty=253,price=2883.34,vendor="Flipkart",barcode="@*5SK#*(##")
p5 = Product(id=14,name="MObile",qty=263,price=2873.34,vendor="Flipkart",barcode="6@*(SK#*(##")
db.session.add_all([p2,p3,p4,p5])
db.session.commit()
"""
