from fpdf import FPDF
import os
from app.gdocs_reader import read

def create(id):
    document = read()
    print(document)
    return str(id)
