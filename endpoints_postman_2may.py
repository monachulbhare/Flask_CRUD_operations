from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)


class Product:

    def __init__(self,prodid,prodnm,prodprc,prodqty,prodven):
        self.prod_id = int(prodid)
        self.prod_name = prodnm
        self.prod_price = float(prodprc)
        self.prod_qty = int(prodqty)
        self.prod_ven = prodven

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)



product_list = []

@app.route('/product/api/',methods=['POST'])        #http://localhost:5000/product/api/ POSt
def save_product():
    reqdata = request.get_json()
    if reqdata:
        for prod in product_list:
            if prod.prod_id== int(reqdata.get('PRODUCT_ID')):
                return jsonify({"ERROR":"Duplicate Product"}),200

        product = Product(prodid = reqdata.get('PRODUCT_ID'),
                prodnm=reqdata.get('PRODUCT_NAME'),
                prodprc=reqdata.get('PRODUCT_PRICE'),
                prodqty=reqdata.get('PRODUCT_QUANTITY'),
                prodven=reqdata.get('PRODUCT_VENDOR')
                )
        product_list.append(product)
        return jsonify(product.__dict__),201
    return jsonify({"ERROR":"Invalid Request Params..."}),200


@app.route('/product/api/<int:pid>',methods=['PUT'])
def update_product(pid):
    reqdata = request.get_json()
    if reqdata:
        for prod in product_list:
            if prod.prod_id == pid:
                prod.prod_name = reqdata.get('PRODUCT_NAME')
                prod.prod_price = reqdata.get('PRODUCT_PRICE')
                prod.prod_qty = reqdata.get('PRODUCT_QUANTITY')
                prod.prod_ven = reqdata.get('PRODUCT_VENDOR')
                return jsonify(prod.__dict__),200
    return jsonify({'Error':'Product cannot be updated..'}),200

@app.route('/product/api/<int:pid>',methods=['PATCH'])
def add_more_quntities_(pid):
    reqdata = request.get_json()
    if reqdata:
        for prod in product_list:
            if prod.prod_id == pid:
                prod.prod_qty = reqdata.get('PRODUCT_QUANTITY')
                return jsonify(prod.__dict__),200
    return jsonify({'Error':'Product cannot be updated..'}),200

@app.route('/product/api/<int:pid>',methods=['DELETE'])
def delete_product(pid):
    for prod in product_list:
        if prod.prod_id == pid:
            product_list.remove(prod)
            return jsonify({"SUCCESS": "PRODUCT REMOVED SUCCESSFULLY..."}),204
    return jsonify({'Error':'Product cannot be DELETED..'}),200


@app.route('/product/api/search/byid/<int:pid>',methods=['GET'])
def search_product_by_id(pid):
    for prod in product_list:
        if prod.prod_id == pid:
            return jsonify(prod.__dict__),200
    return jsonify({'Error': 'Product not found..'}), 200


@app.route('/product/api/search/byven/<vname>',methods=['GET'])
def search_product_by_vendor(vname):
    final_product_list = []
    for prod in product_list:
        if prod.prod_ven==vname:
            final_product_list.append(prod.__dict__)
        return jsonify(final_product_list),200
    return jsonify({'Error': 'Products with given vendor not found..'}), 200



#http://localhost:5000/product/api/v1       ---> list product
@app.route('/product/api/',methods=['GET'])  # get method --- retrieve the content from server
def get_list_products():
    final_list = []
    for prod in product_list:
        final_list.append(prod.__dict__)
    return jsonify(final_list),200



@app.route('/product/api/multi/',methods=['POST'])        #http://localhost:5000/product/api/multi/ POSt
def save_product_multimedia():
    reqdata = request.form
    prod_media = request.files
    print(reqdata)
    print(prod_media)
        # entire file name - split karo -- . [-1]--->
    ALLOWED_EXTENSION = ['PNG','JPEG','BMP']
    filename = prod_media.get('PRODUCT_PHOTO').filename
    print(filename)
    if filename and filename.split('.')[-1] in ALLOWED_EXTENSION:
        prod_media.get('PRODUCT_PHOTO').save('product_image.png')
    else:
        return jsonify({"error":'invalid file type...'})

        #return jsonify(product.__dict__),201
    return jsonify({"ERROR":"able to call..."}),200


if __name__ == '__main__':
    app.run(debug=True)