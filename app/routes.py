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
    if int(request.args['id']) != 7:
        return xlsx_creator.create(id=int(request.args['id']))
    else:
        return word_creator.create()


@app.route('/getUsers')
def getUsers():
    return json.dumps(gdocs_reader.read(mode='users'))
