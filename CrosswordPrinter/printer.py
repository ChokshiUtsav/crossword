# -*- coding: utf-8 -*-
import os
import json
from template import HtmlTemplate

def eng_to_guj_numericals(number):
    if number == 0:
        return u'\u0ae6'
    elif number == 1:
        return u'\u0ae7'
    elif number == 2:
        return u'\u0ae8'
    elif number == 3:
        return u'\u0ae9'
    elif number == 4:
        return u'\u0aea'
    elif number == 5:
        return u'\u0aeb'
    elif number == 6:
        return u'\u0aec'
    elif number == 7:
        return u'\u0aed'
    elif number == 8:
        return u'\u0aee'
    elif number == 9:
        return u'\u0aef'

def number_to_months(numerical_string):
    if numerical_string == "1":
        return "January"
    elif numerical_string == "2":
        return "February"
    elif numerical_string == "3":
        return "March"
    elif numerical_string == "4":
        return "April"
    elif numerical_string == "5":
        return "May"
    elif numerical_string == "6":
        return "June"
    elif numerical_string == "7":
        return "July"
    elif numerical_string == "8":
        return "August"
    elif numerical_string == "9":
        return "September"
    elif numerical_string == "10":
        return "October"
    elif numerical_string == "11":
        return "November"
    elif numerical_string == "12":
        return "December"

def print_crossword(month, data):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    output_file = "Crossword_" + month + ".html"
    html_template = HtmlTemplate(dir_path, output_file)
    html_template.add_template_variable("month", month)
    html_template.add_template_variable("crossword", data["crossword"])
    html_template.add_template_variable("horizontal_keys", data["horizontal_keys"])
    html_template.add_template_variable("vertical_keys", data["vertical_keys"])
    html_template.render_html()

def load_and_process_json():
    with open('crossword_data.json') as f:
        data = json.load(f) 
    for key in data["data"]:
        month =  number_to_months(key)
        if data["language"] == "gu":
            row  = len(data["data"][key]["crossword"])
            col = len(data["data"][key]["crossword"][0])
            for r in range(row):
                for c in range(col):
                    val = data["data"][key]["crossword"][r][c]
                    data["data"][key]["crossword"][r][c] = eng_to_guj_numericals(val) if val > 0 else val
            
            for k in data["data"][key]["horizontal_keys"]:
                k["order"] = eng_to_guj_numericals(k["order"])
                k["length"] = eng_to_guj_numericals(k["length"])

            for k in data["data"][key]["vertical_keys"]:
                k["order"] = eng_to_guj_numericals(k["order"])
                k["length"] = eng_to_guj_numericals(k["length"])

        print_crossword(month, data["data"][key])
    
load_and_process_json()