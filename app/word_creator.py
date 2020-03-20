from flask import send_from_directory
from docx import Document, styles
from docx.shared import Pt
import os
from datetime import datetime
from app.gdocs_reader import read

def spravkaFieldPicker(date):
    month = date.month
    years = []
    year = date.year
    months = []
    for i in range(6):
        years.append(str(year))
        months.append(str(month))
        month -= 1
        if month < 1:
            month = 12
            year = year - 1
    return [years, months]


def replace_request(words, replacements, doc):
    for j in range(0, len(words)):
        if not replacements[j]:
            replacements[j] = ' '
        for i in doc.tables[0]._cells:
            if words[j] in i.text:
                i.text = i.text.replace(str(words[j]), str(replacements[j]))
        for i in doc.tables[1]._cells:
            if words[j] in i.text:
                i.text = i.text.replace(str(words[j]), str(replacements[j]))
    return doc


def replace_doc(words, replacements, doc):
    style = doc.styles['Normal']
    style.font.size = Pt(11)
    style.font.name = "Times New Roman"
    for j in range(0, len(words)):
        if not replacements[j]:
            replacements[j] = ' '

        for i in doc.paragraphs:
            if words[j] in i.text:
                i.style = style
                i.text = i.text.replace(str(words[j]), str(replacements[j]))
        try:
            if words[j] in doc.tables[0].cell(0, 1).text:
                doc.tables[0].cell(0, 1).text = doc.tables[0].cell(0, 1).text.replace(str(words[j]), str(replacements[j]))
        except Exception:
            continue
    return doc

def create(userid):
    doc = Document(os.path.dirname(__file__) + '/files/spravka.docx')
    date = datetime.today()
    info = read(mode='data')[userid]
    doc = replace_doc(doc=doc, words=['{{число}}', '{{месяц}}', '{{год}}', '{{ФИО}}', '{{ИНН}}', '{{число работы}}', '{{м.работы}}',
                                      '{{г.работы}}', '{{должность}}'],
                      replacements=[str(date.day), str(['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа',
                      'сентября', 'октября', 'ноября', 'декабря'][date.month - 1]), str(date.year)[2:], info[3], info[14],
                                    info[71].split('.')[0], info[71].split('.')[1], info[71].split('.')[2], info[25]])
    years = spravkaFieldPicker(date)
    doc = replace_request(words=['{{наимен орги}}', '{{ИНН}}', '{{реквизиты банка}}', '{{адрес}}', '{{сайт}}', '{{email}}',
                                 '{{телефон}}', '{{м1}}', '{{м2}}', '{{м3}}', '{{м4}}', '{{м5}}', '{{м6}}', '{{г1}}',
                                 '{{г2}}', '{{г3}}', '{{г4}}', '{{г5}}', '{{г6}}', '{{сумма денег}}'],
                          replacements=[info[13], info[14], info[65], info[30], info[33], '', info[31],
                                        years[1][0], years[1][1], years[1][2], years[1][3], years[1][4],
                                        years[1][5], years[0][0], years[0][1], years[0][2], years[0][3],
                                        years[0][4], years[0][5], info[26]], doc=doc)
    doc.save(os.path.dirname(__file__) + '/files/downloaded.xlsx')
    return send_from_directory(directory=os.path.abspath(os.path.dirname(__file__) + '/files'),
                                   filename='downloaded.xlsx')