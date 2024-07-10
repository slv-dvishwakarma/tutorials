import unittest
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Check if 'username' cookie is set
    username = request.cookies.get('username')
    if username:
        return f'Hello, {username}!'
    else:
        return 'Welcome! Please set your username.'

@app.route('/setcookie/<username>')
def set_cookie(username):
    # Create a response
    resp = make_response(f'Cookie set for {username}')
    # Set the 'username' cookie
    resp.set_cookie('username', username)
    return resp

@app.route('/clearcookie')
def clear_cookie():
    # Create a response
    resp = make_response('Cookie cleared')
    # Clear the 'username' cookie
    resp.set_cookie('username', '', expires=0)
    return resp

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_set_cookie(self):
        response = self.app.get('/setcookie/testuser')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cookie set for testuser', response.data)

    def test_clear_cookie(self):
        response = self.app.get('/clearcookie')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cookie cleared', response.data)

if __name__ == '__main__':
    unittest.main()
