from operator import or_
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

import logging
import traceback
from test_model import Human

if os.getenv('DEBUG') == '1':
    from test_model import Person
else:
    from mysql_model import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLITE_URI') if os.getenv('DEBUG') == '1' else os.getenv('MYSQL_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PORT'] = os.getenv('PORT')
app.logger.setLevel(logging.DEBUG)
log_handler = logging.FileHandler(os.getenv('LOG_FILE'))
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s')
log_handler.setFormatter(formatter)
log_handler.setLevel(logging.DEBUG)
app.logger.addHandler(log_handler)
log = app.logger


db = SQLAlchemy(app)


@app.route('/')
def inex():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'


@app.route('/exercise request/<user_name>')
def test_sample(user_name):
    return user_name

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exercise_html')
def exercise_html():
    return render_template('exercise.html')

@app.route('/answer')
def answer_html():
    result = request.args.get("my_name")
    return render_template('answer.html',name=result)

@app.route('/try_rest',methods=['POST'])
def try_rest():
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json":request_json}
    return jsonify(response_json)

@app.route('/person_search')
def person_search():
    log.debug('person_search')
    return render_template('./person_search.html')

@app.route('/person_result')
def person_result():
    try:
        search_size = request.args.get("search_size")
        log.debug(f'search_size:{search_size}')
        search_size = int(search_size)
        persons = db.session.query(Person).filter(Person.size > search_size)
    except Exception:
        log.error(traceback.format_exec())
    return render_template('./person_result.html', persons=persons, search_size=search_size)


@app.route('/human_search')
def human_search():
    log.debug('human_search')
    return render_template('./human_search.html')

@app.route('/human_result')
def human_result():
    try:
        search_height = request.args.get("search_height")
        search_weight = request.args.get("search_weight")
        select1 = request.args.get("select1")
        select2 = request.args.get("select2")
        radio = request.args.get("radio")
        
        humans_8 = db.session.query(Human).filter(Human.height <= search_height, Human.weight >= search_weight)#身長以下and体重以上
        humans_7 = db.session.query(Human).filter(Human.height >= search_height, Human.weight <= search_weight)#身長以上and体重以下
        humans_6 = db.session.query(Human).filter(Human.height <= search_height, Human.weight <= search_weight)#身長以下and体重以下
        humans_5 = db.session.query(Human).filter(Human.height >= search_height, Human.weight >= search_weight)#身長以上and体重以上
        
        humans_4 = db.session.query(Human).filter(or_(Human.height <= search_height, Human.weight >= search_weight))#身長以下or体重以上
        humans_3 = db.session.query(Human).filter(or_(Human.height >= search_height, Human.weight <= search_weight))#身長以上or体重以下
        humans_2 = db.session.query(Human).filter(or_(Human.height <= search_height, Human.weight <= search_weight))#身長以下or体重以下
        humans_1 = db.session.query(Human).filter(or_(Human.height >= search_height, Human.weight >= search_weight))#身長以上or体重以上

    except Exception:
        log.error(traceback.format_exec())
        return render_template('./human_result.html', humans=humans_1, search_height=search_height,search_weight=search_weight,select1=select1, select2=select2, radio=radio )

@app.route('/try_html')
def try_html():
    log.debug('try_html')
    return render_template('/try_html.html')

@app.route('/show_data',methods=["GET","POST"])
def show_data():
    try:
        name = request.form.get("name")
        age = request.form.get("age")
    except Exception:
        log.error(traceback.format_exec())
        return render_template('show_data.html',name=name,age=age)