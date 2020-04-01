from app import app
from flask import render_template, request
from app import xlsx_creator, word_creator, gdocs_reader
import json




@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/sendPdf')
def sendPdf():
    print(request.args['userid'])
    if int(request.args['id']) < 4:
        return xlsx_creator.create(id=int(request.args['id']), userid=int(request.args['userid']))
    else:
        return word_creator.create(id=int(request.args['id']), userid=int(request.args['userid']))


@app.route('/getUsers')
def getUsers():
    return json.dumps(gdocs_reader.read(mode='users'))


@app.route('/getDoc')
def getDoc():
    print(gdocs_reader.read(mode='data'))
    return json.dumps(gdocs_reader.read(mode='data'))
