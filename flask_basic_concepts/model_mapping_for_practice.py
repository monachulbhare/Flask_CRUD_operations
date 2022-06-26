from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:login123@localhost/table_mapping"
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

def one_to_one_mapping(self):

    class Employee(db.Model):
        id = db.Column('emp_id',db.Integer,primary_key = True)
        name = db.Column('emp_name',db.String(30))
        age = db.Column('emp_age',db.Integer)
        address = db.relationship("Address",backref = "emp_ref",uselist = False)
           #db.relationship("Address",backref="emp_ref",uselist=False,lazy=False) # Address model

    class Address(db.Model):
        id = db.Column('add_id', db.Integer, primary_key=True)
        city = db.Column('city', db.String(30))
        pincode = db.Column('pincode',db.Integer)
        e_id = db.Column('em_id',db.ForeignKey('employee.emp_id'),unique = True,nullable = True)

    emp = Employee.query.filter_by(id = 101).first()
    print(emp.__dict__)
    print(emp.address.__dict__)

    addr = Address.query.filter_by(id=2).first()
    print(addr.__dict__)
    print(addr.emp_ref.__dict__)
    # e1=Employee(id=101,name='mahesh',age=28)
    # e2 = Employee(id=102, name='siddhi', age=28)
    # e3 = Employee(id=103, name='om', age=28)
    #
    # ad1 = Address(id=1,city="nashik",pincode=422501,e_id=e1.id)
    # ad2 = Address(id=2, city="pune", pincode=425601, e_id=e2.id)
    # ad3 = Address(id=3, city="nagpur", pincode=482501, e_id=e3.id)
    #
    # db.session.add_all([e1, e2, e3])
    # db.session.commit()
    # print("employee filled")
    # db.session.add_all([ad1,ad2,ad3])
    # db.session.commit()
    # print("address filled")

def one_to_many_mapping():
    class Employee(db.Model):
        def __init__(self,id,name,age,address):
            id = self.db.Column('emp_id',db.Integer,primary_key = True)
            name = db.Column('emp_name',db.String(30))
            age = db.Column('emp_age',db.Integer)
            address = db.relationship("Address",backref = "emp_ref",uselist = True, lazy = False)

    class Address(db.Model):
        id = db.Column('add_id', db.Integer, primary_key=True)
        city = db.Column('city', db.String(30))
        pincode = db.Column('pincode',db.Integer)
        e_id = db.Column('em_id',db.ForeignKey('employee.emp_id'),unique = False,nullable = True)

    emp = Employee.query.filter_by(id=101).first()
    print(emp.__dict__)
    print("---------------------------------------")
    print(emp.address.__dict__)
    # db.create_all()
    # e1 = Employee(id=101, name='mahesh', age=28)
    # e2 = Employee(id=102, name='siddhi', age=28)
    # e3 = Employee(id=103, name='om', age=28)
    #
    # ad1 = Address(id=1,city="nashik",pincode=422501,e_id=e1.id)
    # ad2 = Address(id=2, city="pune", pincode=425601, e_id=e2.id)
    # ad3 = Address(id=3, city="nagpur", pincode=482501, e_id=e1.id)
    #
    # db.session.add_all([e1, e2, e3])
    # db.session.commit()
    # print("employee filled")
    # db.session.add_all([ad1,ad2,ad3])
    # db.session.commit()
    # print("address filled")
    #

def many_to_many_mapping():
    emp_addr_mapping = db.Table("emp_addr_mapping",
                db.Column("emp_id",db.Integer,db.ForeignKey("employee.emp_id"),unique=False),
                db.Column("add_id",db.Integer,db.ForeignKey("address.add_id"),unique= False))
    class Employee(db.Model):
        id = db.Column('emp_id',db.Integer,primary_key = True)
        name = db.Column('emp_name',db.String(130))
        age = db.Column('emp_age',db.Integer)

    class Address(db.Model):
        id = db.Column('add_id', db.Integer, primary_key=True)
        city = db.Column('city', db.String(30))
        pincode = db.Column('pincode',db.Integer)
        emp_list = db.relationship("Employee",secondary = emp_addr_mapping,backref=db.backref("adr_list",lazy = True))
    db.create_all()

    e1 = Employee(1,'satish',26)
    e2 = Employee(2,"netra",34)
    e3 = Employee(3,"piyush",24)
    e4 = Employee(4, "antara",28)
    db.session.add_all([e1,e2,e3,e4])
    db.session.commit()

    ad1 = Address(11,"pune",422501)
    ad2 = Address(12,"nashik",422009)
    ad3 = Address(13,"pune",422507)
    ad4 = Address(14,"katraj",422504)
    db.session.add_all([ad1,ad2,ad3,ad4])
    db.session.commit()

    e1.adr_list.extend([ad1,ad2,ad3,ad4])
    e1.adr_list.extend([ad1, ad2, ad3, ad4])
    e2.adr_list.extend([ad1, ad2, ad3, ad4])
    e3.adr_list.extend([ad1, ad2, ad3, ad4])
    e4.adr_list.extend([ad1, ad2, ad3, ad4])
    e2.adr_list.extend([ad1, ad2, ad3, ad4])

    db.session.commit()

if __name__ == "__main__":

    print("function of mapping Executing.....!")
    #one_to_one_mapping()
    #one_to_many_mapping()
    many_to_many_mapping()
    print("============================")