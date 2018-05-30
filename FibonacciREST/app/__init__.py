
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from math import sqrt

from flask import request, jsonify, abort
from math import sqrt

#local import
from instance.config import app_config


db = SQLAlchemy()
#using wolfram algorithm to compute value
def ComputeFib(number):
    return int(((1+sqrt(5))**number-(1-sqrt(5))**number)/(2**number*sqrt(5)))

#Compute values for sequence and add to list
def get_fib_sequence(num_arg):
    results = []
    
    for x in range(0, num_arg):
        
        obj = ComputeFib(x) 
        results.append(obj)
    return results

def config_app(config_type):

    from app.models import FibonacciNumbersRequest

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_type])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
       
       
    @app.route('/FibNumberReqs/<int:id>', methods=['DELETE'])
    def parse_delete_request(id, **kwargs):
        if request.method == 'DELETE':
            cur_rec = FibonacciNumbersRequest.query.get(id)
            db.session.delete(cur_rec)
            db.session.commit()
            return ('', 200)
    
    @app.route('/FibNumberReqs/<int:number>', methods=['POST'])
    def parse_post_request(number, **kwargs):
        if request.method == 'POST':

            if number is not None:
                if number < 0 :
                    #error the number can't be less than 0
                    return('Bad Request number is less than 0', 400)
                #the value is good
                else: 
                    
                    num_sq = get_fib_sequence(number)
                    #return(str(num_sq))
                    new_req = FibonacciNumbersRequest(fib_number_input = number)
                    
                    new_req.number_sequence = str(num_sq)
                    db.session.add(new_req)
                    db.session.commit()
                    obj = {
                        'id' : new_req.id,
                        'fib_number_input' : new_req.fib_number_input,
                        'date_requested' : new_req.date_requested,
                        'date_modified' : new_req.date_modified,
                        'number_sequence' : new_req.number_sequence
                    }
                    response = jsonify(obj)
                    response.status_code = 201
                    return response

    @app.route('/FibNumberReqs/<int:id>', methods=[ 'PUT' ])
    def parse_put_request(id, **kwargs):
        if request.method == 'PUT':
            return('', 405)
            

    #All get logic     
    @app.route('/FibNumberReqs')
    def parse_noparam_request(**kwargs):

        req_id = -1
        verb = str(request.method)
        if None is not request.args.get('id'):
            req_id = request.args.get('id')
        elif None is not request.data.get('id'):
            req_id = request.data.get('id')
        if -1 is not req_id:
            try:
                cur_rec = FibonacciNumbersRequest.query.get(req_id)
                if None is not cur_rec:
                    obj = {
                        'id' : cur_rec.id,
                        'fib_number_input' : cur_rec.fib_number_input,
                        'date_requested' : cur_rec.date_requested,
                        'date_modified' : cur_rec.date_modified,
                        'number_sequence' : cur_rec.number_sequence
                    }
                    response = jsonify(cur_rec)
                    response.status_code = 200
                    return response
                    #if verb == 'GET':
                    #    return jsonify(obj)  
                else:
                    #No record for this id
                    return ('', 204)
                
            except :
                #error getting the record should be from a malformed id value.  Doesn't get hit though because type makes mapping not match
                return('', 400) 
       
        else:
            reqlist = FibonacciNumbersRequest.query.all()
            if 0 == len(reqlist):
                #No id passed in and no items found
                return ('', 204)
            else:
                #No id so return the list
                results = []
                for item in reqlist:
                    obj = {
                        'id' : item.id,
                        'fib_number_input' : item.fib_number_input,
                        'date_requested' : item.date_requested,
                        'date_modified' : item.date_modified,
                        'number_sequence' : item.number_sequence
                    }
                    results.append(obj)
            
                response = jsonify(results)
                response.status_code = 200
                return response

    return app