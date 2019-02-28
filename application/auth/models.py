from application import db

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(80), unique= True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    blacklist = db.Column(db.Boolean, default=False)
    current_order = db.Column(db.Boolean, default=False, nullable=False)
    orders=db.relationship("Tilaus", backref='account', lazy=True)

    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.role = role
        current_order=False
  
    def get_id(self):
        return self.id

    def get_by_id(self, id):
        return self

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return [self.role]

    def has_role(self, role):
        return [self.role]

