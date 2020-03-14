from flask import send_from_directory
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import NameObject
import os
from app.gdocs_reader import read


def updateCheckboxValues(page, fields):
    for j in range(0, len(page['/Annots'])):
        writer_annot = page['/Annots'][j].getObject()
        for field in fields:
            if writer_annot.get('/T') == field:
                writer_annot.update({NameObject("/V"): NameObject(fields[field]),
                                     NameObject("/AS"): NameObject(fields[field])})


def create(id):
    if id == 1:
        pdf_path = os.path.dirname(__file__) + '/files/VTB_anketa.pdf'
    elif id == 2:
        pdf_path = os.path.dirname(__file__) + '/files/VTB_accept.pdf'
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
        checkboxes[list(checkboxes.keys())[0]] = '/Yes'
        # place to edit checkboxes
        # --------------------------------------------------------------------------------------------------------------
        # place to edit text
        for i in fields.keys():
            fields[i] = '1'
        # place to edit text
        pdf_writer = PdfFileWriter()

        for page in range(pdf.getNumPages()):
            pdf_writer.addPage(pdf.getPage(page))
            pdf_writer.updatePageFormFieldValues(page=pdf_writer.getPage(page), fields=fields)
            updateCheckboxValues(page=pdf_writer.getPage(page), fields=checkboxes)

        with open(os.path.dirname(__file__) + '/files/downloaded.pdf', 'wb') as out:
            pdf_writer.write(out)

    document = read(mode='data')
    print(document)
    return str(id)
