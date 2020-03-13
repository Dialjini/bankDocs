from app import app
from flask import render_template, request, send_from_directory
from app import xlsx_creator



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/sendPdf')
def sendPdf():
    return xlsx_creator.create(id=int(request.args['id']))


