from flask import Flask
from flask import request
from flask import jsonify
import json
import statistics

app = Flask(__name__)
with open('../inventory.txt') as f:
    data = json.load(f)


@app.route('/')
def hello():
    return jsonify(data)


@app.route('/categories', methods=['POST'])
def get_categories_for_stroe():
    requestData = request.data
    dataDict = json.loads(requestData)
    for item in data:
        if item['store'] == dataDict['store']:
            return jsonify(item['category'])


@app.route('/inventory', methods=['POST'])
def get_item_inventory():
    requestData = request.data
    dataDict = json.loads(requestData)
    for item in data:
        if item['item_name'] == dataDict['item_name']:
            info = {
                "category": item['category'],
                "items": item['items']
            }

            return jsonify(info)


@app.route('/median', methods=['POST'])
def get_median_for_category():
    requestData = request.data
    dataDict = json.loads(requestData)
    median = []

    for x in data:
        if x['category'] == dataDict['category']:
            for i in range(x['items']):
                median.append(x['price'])
    med = statistics.median(median)
    return jsonify(med)


app.run(host='localhost', port=8090)
