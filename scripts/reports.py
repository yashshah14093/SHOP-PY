import os
import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet



def create_dict(path):
    data = {"name" : "weight"}
    for file in os.listdir(path):
    	with open(path+file) as f:
    		input = f.readline
    		name = input()
    		weight = input()
    		data[name] = weight
    return data



def generate_report(path):

    data_report = create_dict(path)

    date = datetime.datetime.now()


    path_to_report = "/mnt/c/Users/91894/Desktop/SHOP-PY/supplier-data/report.pdf"
    report = SimpleDocTemplate(path_to_report)
    styles = getSampleStyleSheet()

    title = "Processed Update on " + date.strftime("%B %d,%Y")
    report_title = Paragraph(title, styles["h1"])


    table_data = []
    for key,value in data_report.items():
    	table_data.append([key,value])
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
    report_table = Table(data = table_data, style = table_style, hAlign = "CENTER")

    report.build([report_title,report_table])

    return path_to_report
