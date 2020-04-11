from xhtml2pdf import pisa
import os
from flask import render_template, Flask
import codecs
from io import StringIO



html = codecs.open(os.path.dirname(__file__) + '/files/AlphaBank/index.html', 'r', encoding='utf-8')
test = html.read().replace('{{ path }}', os.path.dirname(__file__) + '/files/AlphaBank/')
# print(test)
print(os.path.dirname(__file__))
pisa.CreatePDF(StringIO(test), dest=open('downloaded.pdf', 'w+b'), encoding='utf-8')
# with open(os.path.dirname(__file__) + '/files/downloaded.pdf', 'wb') as out:
#     pisa.CreatePDF(StringIO(test), dest=out, encoding='utf-8')

html.close()
