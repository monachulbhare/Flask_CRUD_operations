from configuration import app
from student_model import *
from flask import request,render_template
#we want to perform CRUD operations on data
@app.route("/")
@app.route("/stud")
def welcome_page():
    return render_template("index_page.html", flag=True)

@app.route("/save",methods = ["GET","POST"])
def add_student():
    message = ""
    if request.method == 'POST':
        formdata = request.form
        print("---formdata---:",formdata)

        stud = Student.query.filter_by(sid = formdata.get("sid")).first()
        if stud:
           # message = "Duplicate product"
            stud.snm = formdata.get('snm'),
            stud.sage = formdata.get('sage'),
            stud.saddr = formdata.get('saddr'),
            stud.smail = formdata.get('smail'),
            stud.sphone = formdata.get('sphone')
            db.session.commit()
            message = "Product Update...!"
        else:
            try:
                student = Student(
                            sid=formdata.get('sid'),
                            snm=formdata.get('snm'),
                            sage=formdata.get('sage'),
                            saddr = formdata.get('saddr'),
                            smail = formdata.get('smail'),
                            sphone = formdata.get('sphone'))
                db.session.add(student)
                db.session.commit()
                message = "Student Added Successfully....!"
            except BaseException as e:
                message = e.args[0]
    dummy = Student(sid= 0,snm=" ",sage=0,saddr=" ",smail=" ",sphone=0)
    return render_template("student.html",message = message,d_student=dummy)




@app.route("/stud/read",methods = ["GET"])
def all_student_data():
    student_list = Student.query.all()
    return render_template("student_list.html",student_list=student_list)

@app.route("/stud/edit/<int:sid>")
def update_student_data(sid):
    database_stud = Student.query.filter_by(sid=sid).first()
    if database_stud:
        return render_template("student.html",d_student=database_stud)

@app.route("/stud/delete/<int:sid>")
def delete_student(sid):
    database_stud = Student.query.filter_by(sid=sid).first()
    if database_stud:
        db.session.delete(database_stud)
        db.session.commit()
    students = Student.query.all()
    return render_template("student_list.html",student_list= students)

@app.route("/stud/search",methods = ["GET","POST"])
def search_student():
    students = None
    if request.method == "POST":
        user_selection = request.form.get('search')
        user_input = request.form.get('inputval')
        if user_selection == "ID":
            students = Student.query.filter_by(sid=user_input).first()
        elif user_selection == "NAME":
            students = Student.query.filter(Student.snm == user_input).all()
        else:
            print("...not selected...")
    return render_template('index_page.html',flag=True, students = students)


if __name__ == '__main__':
    app.run(debug=True)