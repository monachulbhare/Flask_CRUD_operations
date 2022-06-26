from flask import Flask,request,json
from flask_jwt_extended import JWTManager,create_access_token,create_refresh_token,jwt_required,get_jwt_identity
import time
from datetime import timedelta

app = Flask(__name__)
jwt = JWTManager(app)

app.config["JWT_SECRET_KEY"]= "@VAISHU#mona&Siddhi2001,2004"
app.config["JWT_ACCESS_TOKEN_EXPIRED"]=timedelta(minutes=3)
app.config["JWT_REFRESH_TOKEN_EXPIRED"]=timedelta(minutes=20)

@app.route('/api/access',methods = ['POST'])
def generate_access_token():
    data = request.get_json()
    if data:
        username = data.get('username')
        password = data.get('password')
        if username == "vaishu" and password == "mona123":
            user_identity=(username,password)
            access_token = create_access_token(identity=user_identity)
            refresh_token = create_refresh_token(identity=user_identity)
            return json.dumps({"ACCESS_TOKEN":access_token,"REFRESH_TOKEN":refresh_token})
        else:
            return json.dumps({"Error":"Invalid Crendentials"})
    else:
        return json.dumps({"Error":"Invalid Payload"})

@app.route('/api/refresh')
@jwt_required(refresh=True)
def generate_access_token_from_refresh():
    user_identity=get_jwt_identity()
    access_token = create_access_token(user_identity)
    return json.dumps({"ACCESS TOKEN":access_token})

@app.route('/api/welcome')
@jwt_required()
def welcome():
    return "JSON web token applied...!"

if __name__ == "__main__":
    app.run(debug=True)