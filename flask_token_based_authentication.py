import json
import time
from datetime import timedelta
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/novdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#db = SQLAlchemy(app)
                                                                 #private key
app.config["JWT_SECRET_KEY"] = "@*#KSH(#JFK)$#%KFS#($KDKDK@)"   # secrete key -- which always lies with server
                                                                # never share with anyone -- means anyone..
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)  #  Username/password --> to fetch /save -- any data from server
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours=8)  # Refresh Token -- to obtain-- AccessToken
from flask_jwt_extended import get_jwt_identity,JWTManager,create_access_token,create_refresh_token,jwt_required
jwt = JWTManager(app)  # json web token


#jwtextended..
from flask_jwt_extended import get_jwt_identity,JWTManager,create_access_token,create_refresh_token,jwt_required


@app.route('/api/user/',methods=['POST'])
def obtain_token():
    data = request.get_json()
    if data:
        username = data.get('username')
        password = data.get('password')
        if username=='yogesh' and password=='yogesh123':
            unique_identity = (username,password)
            accessToken = create_access_token(identity=unique_identity)
            refreshToken = create_refresh_token(identity=unique_identity)
            return json.dumps({'ACCESS_TOKEN':accessToken,'REFRESH_TOKEN':refreshToken})
        else:
            return json.dumps({'ERROR':"Invalid Credentails"})
    else:
        return json.dumps({'ERROR': "Invalid Payload"})

@app.route("/api/refresh")
@jwt_required(refresh=True)     # in order to call this method --> refresh token required -- which returns access token
def get_access_token(): #generate access token using refresh token
    current_user_id = get_jwt_identity()  # username,password
    accesstoken = create_access_token(identity=current_user_id)  #
    return jsonify({"accesstoken": accesstoken})

@app.route("/api/customer")
@jwt_required()
def get_list_of_customers():
    return "Method Is Invoked.."


if __name__ == '__main__':
    app.run(debug=True)


