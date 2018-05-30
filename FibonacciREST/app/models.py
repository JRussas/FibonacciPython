from app import db
from sqlalchemy.dialects import postgresql as pg

class FibonacciNumbersRequest(db.Model):
    """This is the Fibonacci Number Request Model"""

    __tablename__ = 'fibonacci_number_requests'

    """Number Sequence"""
    number_sequence = db.Column(db.Text)
    

    """PrimaryKey"""
    id = db.Column(db.Integer, primary_key=True)
    
    """Fib Number"""
    fib_number_input = db.Column(db.Integer, nullable=True)

    """Date of request creation"""
    date_requested = db.Column(
        db.DateTime, 
        default = db.func.current_timestamp()
        )

    """Date of last modification"""
    date_modified = db.Column( 
        db.DateTime, 
        default=db.func.current_timestamp(), 
        onupdate=db.func)
    

def __repr__(self):
    return "<FibonacciNumbersRequest ID:{1} Number:{2} Sequence: {3}>".format(self.id, self.fib_number_input, self.number_sequence)

