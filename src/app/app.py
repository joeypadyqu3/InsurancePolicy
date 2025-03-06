from flask import Flask, request, jsonify
from config.swagger import swagger_configuration

app = Flask(__name__)
swagger_configuration()


@app.post('/message')
def message():
    
    data = request.json
    
    return jsonify(data)
    
@app.get('/index')
def hello():
    
    return 'Hello, World!'
