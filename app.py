from flask import Flask, jsonify, request, render_template, json
import json
# from cutting_algo import generate_cut_list, result, wood_cutting
cut_dict = {'125': 10, '120': 40, '108': 26, '99': 5, '60': 10, '49': 10, '43': 24, '34': 12, '30': 5, '12': 26}
app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        message = {'cut_list': [300,200,100], 
        'cut_dict': cut_dict ,
        'max_sheets': 3}
        return jsonify(message)  # serialize and use JSON headers

@app.route('/test')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')

@app.route("/")
def home():
    return render_template('site.html')