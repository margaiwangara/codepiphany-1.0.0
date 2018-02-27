from users import db

class Users(db.Model):
    __tablename__ = "user_populate"
    user_id = db.Column("user_id",db.Integer,primary_key=True,autoincrement=True)
    email = db.Column("email", db.String(50),unique=True)
    username = db.Column("username",db.String(50))
    password = db.Column("password",db.String(100))
    reg_date = db.Column("reg_date",db.DateTime)
