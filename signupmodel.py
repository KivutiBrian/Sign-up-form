from app import db

class Signupmodel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    fullName = db.Column(db.String(45),nullable=False)
    dob = db.Column(db.String(45),nullable=False)
    gender = db.Column(db.String(45),nullable=False)
    email = db.Column(db.String(45),nullable=False)
    phone = db.Column(db.String(45),nullable=False)
    

    # create
    def create_user(self):
        db.session.add(self)
        db.session.commit()  

    #check if email exists
    @classmethod
    def check_email_exists(cls,email):
        record = Signupmodel.query.filter_by(email=email)
        if record.first():
            return True
        else:
            return False    