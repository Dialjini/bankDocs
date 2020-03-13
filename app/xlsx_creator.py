from fpdf import FPDF
import os
from gdocs_reader import read

def create(id):
    document = read()
    print(document)
    return str(id)