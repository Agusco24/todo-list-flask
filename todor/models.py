from todor import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(20), unique = True, nullable = False )
    password = db.Column(db.Text, nullable = False )
    
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        
    def __repr__(self):
        return f"<User: {self.userName} >"
    
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    createdBy = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False )
    title = db.Column(db.String(100), nullable = False )
    desc = db.Column(db.Text)
    state = db.Column(db.Boolean, default = False )
    
    def __init__(self, cratedBy, title, desc, state = False):
        self.createdBy = cratedBy
        self.title = title
        self.desc = desc 
        self.state = state
        
    def __repr__(self):
        return f"<Todo: {self.title} >"