from flask import send_from_directory
from docx import Document, styles
from docx.shared import Pt
import os


def replace_request(words, replacements, doc):
    for j in range(0, len(words)):
        if not replacements[j]:
            replacements[j] = ' '
        for i in doc.tables[0]._cells:
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

def create():
    return 'OK'