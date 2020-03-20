from flask import send_from_directory
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import NameObject
import os
from app.gdocs_reader import read
from datetime import datetime


def spravkaFieldPicker(date):
    month = date.month
    years = []
    year = date.year

    for i in range(12):
        years.append(str(year)[2:])
        month -= 1
        if month < 1:
            month = 12
            year = year - 1
    return years


def updateCheckboxValues(page, fields):
    for j in range(0, len(page['/Annots'])):
        writer_annot = page['/Annots'][j].getObject()
        for field in fields:
            if writer_annot.get('/T') == field:
                writer_annot.update({NameObject("/V"): NameObject(fields[field]),
                                     NameObject("/AS"): NameObject(fields[field])})


def scen1(info, fields):
    iter = 0
    for i in fields.keys():
        # fields[i] = iter
        # iter += 1
        try:
            if iter == 27:
                fields[i] = info[23].split(', ')[0].split(' ')[0]
            if iter == 28:
                fields[i] = info[23].split(', ')[1].split(' ')[0]
            if iter == 29:
                fields[i] = info[23].split(', ')[2].split(' ')[0]
        except Exception:
            print('ok')

        if iter == 0 or iter == 50 or iter == 53:
            fields[i] = info[3]
        if iter == 15:
            fields[i] = info[4]
        if iter == 2:
            fields[i] = info[8]
        if iter == 4:
            fields[i] = info[11]
        if iter == 8:
            fields[i] = info[12]
        if iter == 25:
            fields[i] = info[20]
        if iter == 26:
            fields[i] = info[21]
        if iter == 30:
            fields[i] = info[25]
        if iter == 31:
            fields[i] = info[26]
        if iter == 32:
            fields[i] = info[27]
        if iter == 118:
            fields[i] = info[28]
        if iter == 117:
            fields[i] = info[29]
        if iter == 119:
            fields[i] = info[13]
        if iter == 120:
            fields[i] = info[14]
        if iter == 121:
            fields[i] = info[30]
        if iter == 122:
            fields[i] = info[31]
        if iter == 123:
            fields[i] = info[32]
        if iter == 33:
            fields[i] = info[33]
        if iter == 38:
            fields[i] = info[36]
        if iter == 39:
            fields[i] = info[38].split(', ')[0]
        if iter == 41:
            fields[i] = info[38].split(', ')[1]
        try:
            if iter == 40:
                fields[i] = info[38].split(', ')[2]
            if iter == 42:
                fields[i] = info[38].split(', ')[3]
        except Exception:
            print('ok')
        if iter == 43:
            fields[i] = info[40].split(', ')[0]
        if iter == 44:
            fields[i] = info[40].split(', ')[1]
        if iter == 45:
            fields[i] = info[40].split(', ')[2]
        if iter == 46:
            fields[i] = info[42].split(', ')[0]
        if iter == 47:
            fields[i] = info[42].split(', ')[1]
        if iter == 48:
            fields[i] = info[46]
        if iter == 49:
            fields[i] = str(datetime.today().day) + '.' + str(datetime.today().month) + '.' + str(datetime.today().year)
        if iter == 54:
            fields[i] = info[47]
        if iter == 55:
            fields[i] = info[48]
        if iter == 56:
            fields[i] = info[49]
        if iter == 115:
            fields[i] = info[53]
        if iter == 62:
            fields[i] = info[54]
        if iter == 61:
            fields[i] = info[55]
        if iter == 60:
            fields[i] = info[58]
        if iter == 11:
            fields[i] = info[67]
        iter += 1
        if fields[i] is None:
            fields[i] = ''



def scen3(info, fields):
    iter = 0
    date = datetime.today()
    for i in fields.keys():
        # fields[i] = iter
        if iter == 0:
            fields[i] = str(date.day)
        if iter == 1:
            fields[i] = str(['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа',
                      'сентября', 'октября', 'ноября', 'декабря'][date.month - 1])
        if iter == 2:
            fields[i] = str(date.year)[2:]
        if iter == 3:
            fields[i] = info[3]
        if iter == 4:
            fields[i] = info[71].split('.')[0]
        if iter == 5:
            fields[i] = info[71].split('.')[1]
        if iter == 6:
            fields[i] = info[71].split('.')[2][2:]
        if iter == 7:
            fields[i] = info[25]
        if iter == 8:
            fields[i] = info[13][:65]
        if iter == 9:
            fields[i] = info[13][65:]
        if iter == 10:
            fields[i] = info[14]
        if iter == 11:
            fields[i] = info[50]
        try:
            if iter == 12:
                fields[i] = info[30].split(', ')[0]
            if iter == 14:
                fields[i] = info[30].split(', ')[1]
            if iter == 15:
                fields[i] = info[30].split(', ')[2]
        except Exception:
            print('')
        try:
            if iter == 16:
                fields[i] = info[30].split(', ')[3][0]
            if iter == 73:
                fields[i] = info[30].split(', ')[3][1]
            if iter == 72:
                fields[i] = info[30].split(', ')[3][2]
            if iter == 71:
                fields[i] = info[30].split(', ')[3][3]
        except Exception:
            print('')
        try:
            if 'офис' in info[30].split(', ')[4]:
                if iter == 18:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][0]
                if iter == 67:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][1]
                if iter == 66:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][2]
                if iter == 65:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][3]
            else:
                if iter == 17:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][0]
                if iter == 70:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][1]
                if iter == 69:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][2]
                if iter == 68:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][3]
        except Exception:
            print('')
        if iter == 19:
            fields[i] = info[31]
        try:
            if iter == 20:
                fields[i] = info[30].split(', ')[0]
            if iter == 22:
                fields[i] = info[30].split(', ')[1]
            if iter == 23:
                fields[i] = info[30].split(', ')[2]
        except Exception:
            print('')
        try:
            if iter == 24:
                fields[i] = info[30].split(', ')[3][0]
            if iter == 25:
                fields[i] = info[30].split(', ')[3][1]
            if iter == 26:
                fields[i] = info[30].split(', ')[3][2]
            if iter == 27:
                fields[i] = info[30].split(', ')[3][3]
        except Exception:
            print('')
        try:
            if 'офис' in info[30].split(', ')[4]:
                if iter == 32:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][0]
                if iter == 33:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][1]
                if iter == 34:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][2]
                if iter == 35:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][3]
            else:
                if iter == 28:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][0]
                if iter == 29:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][1]
                if iter == 30:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][2]
                if iter == 31:
                    fields[i] = info[30].split(', ')[4].split(' ')[0][3]
        except Exception:
            print('')
        if iter == 36:
            fields[i] = info[31]
        years = spravkaFieldPicker(date)
        if iter == 37:
            fields[i] = years[0]
        if iter == 38:
            fields[i] = years[1]
        if iter == 39:
            fields[i] = years[2]
        if iter == 40:
            fields[i] = years[3]
        if iter == 41:
            fields[i] = years[4]
        if iter == 42:
            fields[i] = years[5]
        if iter == 43:
            fields[i] = years[6]
        if iter == 44:
            fields[i] = years[7]
        if iter == 45:
            fields[i] = years[8]
        if iter == 46:
            fields[i] = years[9]
        if iter == 47:
            fields[i] = years[10]
        if iter == 48:
            fields[i] = years[11]
        if iter == 49:
            fields[i] = years[0]
        if iter == 50:
            fields[i] = info[26]
        if iter == 51:
            fields[i] = info[26]
        if iter == 52:
            fields[i] = info[26]
        if iter == 53:
            fields[i] = info[26]
        if iter == 54:
            fields[i] = info[26]
        if iter == 55:
            fields[i] = info[26]
        if iter == 56:
            fields[i] = info[26]
        if iter == 57:
            fields[i] = info[26]
        if iter == 58:
            fields[i] = info[26]
        if iter == 59:
            fields[i] = info[26]
        if iter == 60:
            fields[i] = info[26]

        if fields[i] is None:
            fields[i] = ''
        iter += 1


def scen4(info, fields):
    iter = 0
    for i in fields.keys():

        iter += 1
    return 'scen4'



def scen5(info, fields):
    iter = 0
    for i in fields.keys():
        iter += 1
    return 'scen5'


def scen6(info, fields):
    iter = 0
    for i in fields.keys():

        iter += 1
    return 'scen6'


def docWriter(fields, id, userid):
    info = read(mode='data')[userid]
    if id == 1:
        scen1(info=info, fields=fields)
    if id == 3:
        scen3(info=info, fields=fields)
    if id == 4:
        scen4(info=info, fields=fields)
    if id == 5:
        scen5(info=info, fields=fields)
    if id == 6:
        scen6(info=info, fields=fields)


def cscen1(info, fields):
    iter = 0
    for i in fields.keys():
        print(i, iter, fields[i])
        if iter == 13:
            fields[i] = '/Yes'
        if iter == 81:
            fields[i] = '/Yes'
        if iter == 82:
            fields[i] = '/Yes'
        if iter == 91:
            fields[i] = '/Yes'
        if iter == 6:
            fields[i] = '/Yes'
        if info[1] == 'Заемщик':
            if iter == 0:
                fields[i] = '/Yes'
        if info[17] == 'Рекомендация строительной/риелторской компании':
            if iter == 3:
                fields[i] = '/Yes'
        elif info[17] == 'Реклама (уточните)':
            if iter == 2:
                fields[i] = '/Yes'
        elif info[17] == 'Рекомендации друзей, знакомых':
            if iter == 4:
                fields[i] = '/Yes'
        elif info[17] == 'Просто обратился в банк за консультацией':
            if iter == 26:
                fields[i] = '/Yes'
        elif info[17] == 'Иное':
            if iter == 27:
                fields[i] = '/Yes'
        elif info[17] == 'Уже являюсь клиентом Группы ВТБ':
            if iter == 5:
                fields[i] = '/Yes'
        if info[65] == 'У родственников':
            if iter == 45:
                fields[i] = '/Yes'
        elif info[65] == 'Социальный наём':
            if iter == 42:
                fields[i] = '/Yes'
        elif info[65] == 'Коммерческий наём':
            if iter == 43:
                fields[i] = '/Yes'
        elif info[65] == 'Собственность':
            if iter == 44:
                fields[i] = '/Yes'
        elif info[65] == 'Иное':
            if iter == 46:
                fields[i] = '/Yes'
        if info[18] == 'Женат/ замужем ':
            if iter == 7:
                fields[i] = '/Yes'
        elif info[18] == 'В разводе':
            if iter == 8:
                fields[i] = '/Yes'
        elif info[18] == 'Вдовец/ вдова':
            if iter == 9:
                fields[i] = '/Yes'
        elif info[18] == 'Холост/ не замужем':
            if iter == 10:
                fields[i] = '/Yes'
        if info[19] == 'Да':
            if iter == 14:
                fields[i] = '/Yes'
        elif info[19] == 'Нет':
            if iter == 15:
                fields[i] = '/Yes'
        try:
            if info[23].split(', ')[0].split(' ')[1] == '(да)':
                if iter == 36:
                    fields[i] = '/Yes'
            elif info[23].split(', ')[0].split(' ')[1] == '(нет)':
                if iter == 37:
                    fields[i] = '/Yes'
            if info[23].split(', ')[1].split(' ')[1] == '(да)':
                if iter == 36:
                    fields[i] = '/Yes'
            elif info[23].split(', ')[1].split(' ')[1] == '(нет)':
                if iter == 37:
                    fields[i] = '/Yes'
            if info[23].split(', ')[2].split(' ')[1] == '(да)':
                if iter == 36:
                    fields[i] = '/Yes'
            elif info[23].split(', ')[2].split(' ')[1] == '(нет)':
                if iter == 37:
                    fields[i] = '/Yes'
        except Exception:
            print('')
        if info[22] == 'Ниже среднего':
            if iter == 16:
                fields[i] = '/Yes'
        elif info[22] == 'Среднее':
            if iter == 17:
                fields[i] = '/Yes'
        elif info[22] == 'Среднее-специальное':
            if iter == 18:
                fields[i] = '/Yes'
        elif info[22] == 'Неоконченное высшее':
            if iter == 19:
                fields[i] = '/Yes'
        elif info[22] == 'Высшее':
            if iter == 20:
                fields[i] = '/Yes'
        elif info[22] == 'Ученая степень':
            if iter == 23:
                fields[i] = '/Yes'
        if info[67] == 'По найму. Срочный договор':
            if iter == 33:
                fields[i] = '/Yes'
        elif info[67] == 'По найму. Бессрочно':
            if iter == 32:
                fields[i] = '/Yes'
        elif info[67] == 'ИП':
            if iter == 34:
                fields[i] = '/Yes'
        elif info[67] == 'Собственник бизнеса':
            if iter == 35:
                fields[i] = '/Yes'
        if info[34] == 'Армия':
            if iter == 47:
                fields[i] = '/Yes'
        elif info[34] == 'Информационные технологии/ телекоммуникации':
            if iter == 48:
                fields[i] = '/Yes'
        elif info[34] == 'Консалтинговые услуги':
            if iter == 49:
                fields[i] = '/Yes'
        elif info[34] == 'Медицина':
            if iter == 50:
                fields[i] = '/Yes'
        elif info[34] == 'Наука':
            if iter == 51:
                fields[i] = '/Yes'
        elif info[34] == 'Образование':
            if iter == 52:
                fields[i] = '/Yes'
        elif info[34] == 'Строительство':
            if iter == 53:
                fields[i] = '/Yes'
        elif info[34] == 'Оптовая/ розничная торговля':
            if iter == 59:
                fields[i] = '/Yes'
        elif info[34] == 'Органы власти и управления':
            if iter == 60:
                fields[i] = '/Yes'
        elif info[34] == 'Охранная деятельность':
            if iter == 61:
                fields[i] = '/Yes'
        elif info[34] == 'Предприятия ТЭК':
            if iter == 62:
                fields[i] = '/Yes'
        elif info[34] == 'Промышленность и машиностроение':
            if iter == 63:
                fields[i] = '/Yes'
        elif info[34] == 'Социальная сфера':
            if iter == 64:
                fields[i] = '/Yes'
        elif info[34] == 'Транспорт':
            if iter == 54:
                fields[i] = '/Yes'
        elif info[34] == 'Туризм':
            if iter == 55:
                fields[i] = '/Yes'
        elif info[34] == 'Услуги':
            if iter == 56:
                fields[i] = '/Yes'
        elif info[34] == 'Финансы, банки, страхование':
            if iter == 57:
                fields[i] = '/Yes'
        elif info[34] == 'Другие отрасли':
            if iter == 58:
                fields[i] = '/Yes'
        if info[63] == 'До 10':
            if iter == 65:
                fields[i] = '/Yes'
        elif info[63] == '10-50':
            if iter == 66:
                fields[i] = '/Yes'
        elif info[63] == '51-100':
            if iter == 67:
                fields[i] = '/Yes'
        elif info[63] == '101-500':
            if iter == 68:
                fields[i] = '/Yes'
        elif info[63] == '501-1000':
            if iter == 69:
                fields[i] = '/Yes'
        elif info[63] == 'более 1000':
            if iter == 70:
                fields[i] = '/Yes'
        if info[69] == 'Да':
            if iter == 30:
                fields[i] = '/Yes'
        elif info[69] == 'Нет':
            if iter == 31:
                fields[i] = '/Yes'
        if info[70] == 'До 2 лет':
            if iter == 71:
                fields[i] = '/Yes'
        elif info[70] == 'от 2 до 5 лет':
            if iter == 72:
                fields[i] = '/Yes'
        elif info[70] == 'свыше 5 лет':
            if iter == 73:
                fields[i] = '/Yes'
        if info[33] == 'Имею':
            if iter == 177:
                fields[i] = '/Yes'
        elif info[33] == 'Не имею':
            if iter == 74:
                fields[i] = '/Yes'
        if info[39] == 'Имею':
            if iter == 75:
                fields[i] = '/Yes'
        elif info[39] == 'Не имею':
            if iter == 76:
                fields[i] = '/Yes'
        if info[41] == 'Имею':
            if iter == 178:
                fields[i] = '/Yes'
        elif info[41] == 'Не имею':
            if iter == 176:
                fields[i] = '/Yes'
        if info[43] == 'Покупка':
            if iter == 84:
                fields[i] = '/Yes'
        elif info[43] == 'Приватизация':
            if iter == 85:
                fields[i] = '/Yes'
        elif info[43] == 'Наследство':
            if iter == 86:
                fields[i] = '/Yes'
        elif info[43] == 'Дарение':
            if iter == 87:
                fields[i] = '/Yes'
        elif info[43] == 'Иное':
            if iter == 88:
                fields[i] = '/Yes'
        if info[44] == 'Да':
            if iter == 77:
                fields[i] = '/Yes'
        elif info[44] == 'Нет':
            if iter == 78:
                fields[i] = '/Yes'
        if info[45] == 'Да':
            if iter == 79:
                fields[i] = '/Yes'
        elif info[45] == 'Нет':
            if iter == 80:
                fields[i] = '/Yes'
        if info[46] != '':
            if iter == 83:
                fields[i] = '/Yes'
        iter += 1


def cscen3(info, fields):
    return 'scen3'


def cscen4(info, fields):
    iter = 0
    for i in fields.keys():

        iter += 1
    return 'scen4'



def cscen5(info, fields):
    iter = 0
    for i in fields.keys():
        iter += 1
    return 'scen5'


def cscen6(info, fields):
    iter = 0
    for i in fields.keys():

        iter += 1
    return 'scen6'


def docChecker(fields, id, userid):
    info = read(mode='data')[userid]
    print(fields)
    if id == 1:
        cscen1(info=info, fields=fields)
    if id == 3:
        cscen3(info=info, fields=fields)
    if id == 4:
        cscen4(info=info, fields=fields)
    if id == 5:
        cscen5(info=info, fields=fields)
    if id == 6:
        cscen6(info=info, fields=fields)


def create(id, userid):
    print('id = ' + str(id))
    if id == 1:
        pdf_path = os.path.dirname(__file__) + '/files/VTB_anketa.pdf'
    elif id == 2:
        return send_from_directory(directory=os.path.abspath(os.path.dirname(__file__) + '/files'),
                                   filename='VTB_accept.pdf')
    elif id == 3:
        pdf_path = os.path.dirname(__file__) + '/files/VTB_spravka.pdf'
    elif id == 4:
        pdf_path = os.path.dirname(__file__) + '/files/alpha.pdf'
    elif id == 5:
        pdf_path = os.path.dirname(__file__) + '/files/dom_rf_anketa.pdf'
    elif id == 6:
        pdf_path = os.path.dirname(__file__) + '/files/dow_rf_accept.pdf'
    else:
        return 'BAD ID'

    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        fields = pdf.getFormTextFields()
        checkboxes = {}
        for i in pdf.getFields().keys():
            if 'Check Box' in i:
                checkboxes[i] = pdf.getFields()[i]
        # place to edit checkboxes
        docChecker(id=id, userid=userid, fields=checkboxes)
        # place to edit checkboxes
        # --------------------------------------------------------------------------------------------------------------
        # place to edit text--------------------------------------------------------------------------------------------
        docWriter(id=id, userid=userid, fields=fields)
        # place to edit text--------------------------------------------------------------------------------------------
        pdf_writer = PdfFileWriter()

        for page in range(pdf.getNumPages()):
            pdf_writer.addPage(pdf.getPage(page))
            pdf_writer.updatePageFormFieldValues(page=pdf_writer.getPage(page), fields=fields)
            updateCheckboxValues(page=pdf_writer.getPage(page), fields=checkboxes)

        with open(os.path.dirname(__file__) + '/files/downloaded.pdf', 'wb') as out:
            pdf_writer.write(out)

    return send_from_directory(directory=os.path.abspath(os.path.dirname(__file__) + '/files'),
                                   filename='downloaded.pdf')
