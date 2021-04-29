from flask import Flask, jsonify, request
from classifier import Classifier
app=Flask(__name__)

classifier = Classifier()

@app.route('/', methods=['GET'])
def hello():
    resp = {
        "message" : "API is running :)"
    }
    return jsonify(resp)

@app.route('/classify', methods=['POST'])
def classify() :
    url = request.json['url']
    try :
        resp = {
            "status" : "success", 
            "url" : url,
            "message" : "The number is : " + str(classifier.classify(url)) 
        }
    except :
        resp = {
            "status" : "error", 
            "url" : url,
            "message" : "Some error occurred"
        }
    
    return jsonify(resp)