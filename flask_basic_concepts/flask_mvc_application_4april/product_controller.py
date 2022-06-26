from config import app,db # instance of flask
from flask import request,render_template
from model import *

@app.route("/")
@app.route("/product")
def welcome_page():
    return render_template('index.html',flag = True)
#render_template is used to generate output from a

@app.route("/product/save",methods=["POST","GET"])
def add_fresh_product_in_stock():
    message = ''
    if request.method == 'POST':
        formdata = request.form
        print('formdata --',formdata)

        dbprod = Product.query.filter_by(id=formdata.get('pid')).first()
        if dbprod:
            #message = "Duplicate Product Id"
            dbprod.name = formdata.get('pnm')
            dbprod.qty = formdata.get('qty')
            dbprod.price = formdata.get('prc')
            dbprod.vendor = formdata.get('ven')
            dbprod.barcode = formdata.get('bcode')
            db.session.commit()
            message = "Product Update...!"
        else:
            try:
                product = Product(id=formdata.get('pid'),
                        name=formdata.get('pnm'),
                        qty=formdata.get('qty'),
                        price=formdata.get('prc'),
                        vendor=formdata.get('ven'),
                        barcode=formdata.get('bcode'))
                db.session.add(product)
                db.session.commit()
                message = "Product Successfully Added.."
            except BaseException as e:
                message = e.args[1]
    dummy = Product(id=0, name="", qty=0, price=0.0, vendor="", barcode="")
    return render_template('product.html',result = message,d_product = dummy)

@app.route("/product/edit/<int:prid>")
def update_product(prid):
    dbproduct = Product.query.filter_by(id=prid).first()  # id se-- retrive
    if dbproduct:
        return render_template('product.html', d_product = dbproduct)

@app.route("/product/delete/<int:prid>")
def delete_products_db(prid):
    dbproduct = Product.query.filter_by(id=prid).first()        #id se-- retrive
    if dbproduct:
        db.session.delete(dbproduct) # delete
        db.session.commit()         # db changes -final

    products = Product.query.all()  #product retrived from db --> 1 less
    return render_template('list_products.html', products_list=products) # list

@app.route("/product/list",methods=["GET"])     #http://localhost:5000/product/list
def fetch_list_of_products():
    products = Product.query.all()
    #products = sorted(products,key=lambda prod:prod.name)

    return render_template('list_products.html', products_list=products)


@app.route('/product/search',methods = ["GET","POST"])
def search_for_product():
    products = None
    if request.method == "POST":
        user_selection = request.form.get('search')
        user_input = request.form.get('inputval')
        if user_selection == "ID":
            products = Product.query.filter_by(id=user_input).first()
        elif user_selection == "NAME":
            products = Product.query.filter(Product.name==user_input).all()
        elif user_selection == "VENDOR":
            products = Product.query.filter(Product.vendor==user_input).all()

    return render_template('index.html',flag = True,products = products)


if __name__ == '__main__':
    app.run(debug=True)
    #fetch_list_of_products()