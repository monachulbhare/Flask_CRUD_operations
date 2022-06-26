from config import app  # instance of flask
from flask import request,render_template
from model import *

@app.route("/save",methods=["POST","GET"])
def add_fresh_product_in_stock():
    message = ''
    if request.method == 'POST':
        formdata = request.form
        print('formdata --',formdata)

        dbprod = Product.query.filter_by(id=formdata.get('pid')).first()
        if dbprod:
            message = "Duplicate Product Id"
        else:
            try:
                product = Product(id=formdata.get('pid'),
                        name=formdata.get('pnm'),
                        qty=formdata.get('qty'),
                        price=formdata.get('prc'),
                        vendor=formdata.get('ven'),
                        barcode=formdata.get('bcode'))
                db.session.add(product) #---------->for adding item in table....this two lines are must.
                db.session.commit()
                message = "Product Successfully Added.."
            except BaseException as e:
                message = e.args[1]

    return render_template('product.html',result = message)

def modify_existing_product_details():
    pass

def check_product_availble_in_stock_or_not():
    pass

def fetch_list_of_products():
    print(Product.query.all())



if __name__ == '__main__':
    app.run(debug=True)
