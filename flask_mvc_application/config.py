from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:login123@localhost/sam_db'  #conn -- mysql
app.config["SQLALCHEMY_ECHO"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.template_folder = "pages/"

#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/cars_api"
db = SQLAlchemy(app)  # Flask app instance --> sqlalchemy --> db configuration.
#db--> type ?? --> SQLAlChemy --> what that object is aware --> app --> Flask instance
    #---> configuration de kr rh hai..


#db -->
