from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request,jsonify

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:login123@localhost/Student"
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

#db = SQLAlchemy(app)

# class Student(db.Model):
#     __tablename__ = "student_table"
#     sid = db.Column("student_id",db.Integer,Primary_key = True)
#     sname = db.Column("student_name",db.String)
#     saddress = db.Column("student_address",db.String)
#     sphone = db.Column("student_phone",db.String)
#     spercentage = db.Column("student_percentage",db.Float)

class Student():
    def __init__(self,sid,sname,sadd,sphone,smail,sper):
        self.student_id = sid
        self.student_name = sname
        self.student_address = sadd
        self.student_phone = sphone
        self.student_mail = smail
        self.student_percentage = sper

    def __str__(self):
        return f'''{str.__dict__}'''
    def __repr__(self):
        return str(self)


stud_list =[]

@app.route("/student/restAPI/v1",methods = ['POST'])
def add_student():
    reqdata = request.get_json()
    if reqdata:
        for stud in stud_list:
            if stud.student_id == int(reqdata.get('STUD_ID')):
                return jsonify({'ERROR':'Duplicate Element'}),200

        student = Student(sid = reqdata.get('STUD_ID'),
                          sname = reqdata.get('STUD_NAME'),
                          sadd =reqdata.get('STUD_ADD'),
                        sphone = reqdata.get('STUD_PHONE'),
                        smail = reqdata.get('STUD_MAIL'),
                        sper =reqdata.get('STUD_PER'))
        stud_list.append(student)
        return jsonify(student.__dict__),201
    return jsonify({'ERROR':'Invalid Request parameter'}),200


@app.route("/student/restAPI/v1",methods = ['GET'])
def read_students():
    student_list = []
    for stud in stud_list:
        student_list.append(stud.__dict__)
    return jsonify(student_list)

@app.route("/student/restAPI/v1/<sid>",methods = ['GET'])
def search_by_id(sid):
    for stud in stud_list:
        if stud.student_id == sid:
            return jsonify(stud.__dict__),200
    return jsonify({'Error':'Student not found'})

@app.route("/student/restAPI/v1/<sname>",methods = ['GET'])
def search_by_name(sname):
    for stud in stud_list:
        if stud.student_name == sname:
            student_info = stud.__dict__
            return jsonify(student_info),200
    return jsonify({'Error':'Student not found'})

@app.route("/student/restAPI/v1/<sid>",methods = ['PUT'])
def update_product(sid):
    reqdata = request.get_json()
    if reqdata:
        for stud in stud_list:
            if stud.student_id == sid:
                stud.student_name = reqdata.get('STUD_NAME')
                stud.student_address = reqdata.get('STUD_ADD'),
                stud.student_phone = reqdata.get('STUD_PHONE'),
                stud.student_mail = reqdata.get('STUD_MAIL'),
                stud.student_percentage = reqdata.get('STUD_PER')
                return jsonify(stud.__dict__),200
    return jsonify({"Error":"Student Cannot be updated!"}),201

@app.route("/student/restAPI/v1/<int:sid>",methods = ['PATCH'])
def update_product_attribute(sid):
    reqdata = request.get_json()
    if reqdata:
        for stud in stud_list:
            if stud.student_id == sid:
                stud.student_percentage = reqdata.get('STUD_PER')
                return jsonify(stud.__dict__),200
            return jsonify({"Success":"Student Updated"}),200
    return jsonify({"Error": "Student Cannot be updated!"}), 201


@app.route("/student/restAPI/v1/<sid>",methods = ['DELETE'])
def delete_student(sid):
    for stud in stud_list:
        if stud.student_id == sid:
            stud_list.remove(stud)
            return jsonify({"SUCCESS":"Student data Remove Successfully."}),201
    return jsonify({"ERROR":"Student not found"}),200
if __name__ == '__main__':
    app.run(debug=True)





