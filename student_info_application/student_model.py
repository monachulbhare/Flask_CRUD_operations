from configuration import db

class Student(db.Model):
    __tablename__ = "student_info"
    sid = db.Column("stud_id",db.Integer,primary_key = True,nullable=False)
    snm = db.Column("stud_name",db.String(30),nullable=True)
    sage = db.Column("stud_age",db.Integer)
    saddr = db.Column("stud_address",db.String(50))
    smail = db.Column("stud_email",db.String(50))
    sphone = db.Column("stud_phone",db.BigInteger)

    def __str__(self):
        return f'''\n{self.__dict__}'''
    def __repr__(self):
        return str(self)

db.create_all()