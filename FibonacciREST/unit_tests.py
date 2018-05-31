import unittest
import os
import json
import flask

from app import config_app, db

class UnitTestCase(unittest.TestCase):

    
    def setUp(self):
        self.app = config_app(config_type="testing")
        self.client = self.app.test_client
        self.fibnumber = {'fib_number_input' : 1}
        
    # Create with a valid number then delete
    def test_fibrequest_creation_deletion_case(self):
        """Test positive POST request and delete"""
        add_res = self.client().post('/FibNumberReqs/12')
    
        self.assertEqual(add_res.status_code, 201)
        json_data = json.loads(add_res.data)

        del_res = self.client().delete('/FibNumberReqs/' + str(json_data['id']))# + id) # + add_res.)
        self.assertEqual(del_res.status_code, 200)

    #No high range set but test to use a larger number
    def test_fibrequest_highvalue_creation_positive_case(self):
        """Test high number POST request and delete"""
        add_res = self.client().post('/FibNumberReqs/40', data=self.fibnumber)
        self.assertEqual(add_res.status_code, 201)

        self.assertEqual(add_res.status_code, 201)
        json_data = json.loads(add_res.data)

        del_res = self.client().delete('/FibNumberReqs/' + str(json_data['id']))# + id) # + add_res.)
        self.assertEqual(del_res.status_code, 200)

    #Test negative number   
    def test_fibrequest_creation_negative_failure_case(self):
        """Test negative number POST request"""
        res = self.client().post('/FibNumberReqs/-1')
        self.assertEqual(res.status_code, 404)
        
    #Test non numeric value
    def test_fibrequest_creation_non_number_case(self):
        """Test non number POST request"""
        res = self.client().post('/FibNumberReqs/A', data=self.fibnumber)
        self.assertEqual(res.status_code, 404)

    #Test get all
    def test_fibrequest_get_all_case(self):
        """Test get all"""
        res = self.client().get('/FibNumberReqs',data=self.fibnumber)
        self.assertEqual(res.status_code, 200)

    #Test get of nonexisting ID
    def test_fibrequest_get_by_nonexisting_id(self):
        """Test get by id"""
        res = self.client().get('/FibNumberReqs/999')
        self.assertEqual(res.status_code, 405)
        
    #Test put case
    def test_fibrequest_put_case(self):
        """Test put"""
        rv = self.client().put('/FibNumberReqs')
        self.assertEqual(rv.status_code, 405)
   
if __name__ == "__main__":
    unittest.main()