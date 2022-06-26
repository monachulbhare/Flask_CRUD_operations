from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from flask import request

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:login123@localhost/restAPIdb'
app.config["SQLALCHEMY_ECHO"] = False
app.config['....SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__='PRODUCT_INFO'
    id=db.Column("product_id",db.Integer,primary_key=True)
    name=db.Column("product_name",db.String(30))
    qty = db.Column("product_qty", db.Integer)
    price = db.Column("product_price", db.Float)
    vendor = db.Column("product_vendor", db.String(30))

db.create_all()

@app.route('/product/restAPI/V1',methods=['POST'])
def add_fresh_product_in_stock():
    form_data_req=request.get_json()
    print("form data is",form_data_req)
    if form_data_req:
        try:
            product=Product(name=form_data_req.get('name'),
                            qty=form_data_req.get('qty'),
                            price=form_data_req.get('price'),
                            vendor=form_data_req.get('vendor'))
            db.session.add(product)
            db.session.commit()
            product={'Product_id':product.id,
                     'Product_Name':product.name,
                     'Product_Quantity':product.qty,
                     'Product_Price':product.price,
                     'Product_Vendor':product.vendor}
            return json.dumps({'SUCCESS':product})
        except BaseException as bse:
            print(bse.args)
            return json.dumps({'ERROR':'Problem in save!!!'})

@app.route('/product/restAPI/V1/<int:pid>',methods=['GET'])
def search_product(pid):
    product=Product.query.filter_by(id=pid).first()
    if product:
        product = {'Product_id': product.id,
                   'Product_Name': product.name,
                   'Product_Quantity': product.qty,
                   'Product_Price': product.price,
                   'Product_Vendor': product.vendor}
        return json.dumps(product)
    else:
        return json.dumps({"ERROR":"provided ID isn't present"})

@app.route('/product/restAPI/V1',methods=['GET'])
def get_list_product():
    all_prodcts=Product.query.all()
    if all_prodcts:
        db_prod=[]
        for product in all_prodcts:
            product1 = {'Product_id': product.id,
                       'Product_Name': product.name,
                       'Product_Quantity': product.qty,
                       'Product_Price': product.price,
                       'Product_Vendor': product.vendor}
            db_prod.append(product1)
        return json.dumps(db_prod)
    else:
        return json.dumps({"ERROR":"Nothing in the DB to display"})

if __name__=='__main__':
    app.run(debug=True)