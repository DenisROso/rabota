#Задание №2

import requests as requests

reply_dict = {}

def xml_reply_replaces(input_line=""):
    processing_text = input_line.replace("<ValCurs Date=", "")
    processing_text = processing_text.replace('<?xml version="1.0" encoding="windows-1251"?>', "")
    processing_text = processing_text.replace('" name="Foreign Currency Market">', "")
    processing_text = processing_text.replace("<Valute ID=", "#")
    processing_text = processing_text.replace("</Valute>", "")
    processing_text = processing_text.replace("><NumCode>", "--")
    processing_text = processing_text.replace("</NumCode><CharCode>", "--")
    processing_text = processing_text.replace("</CharCode><Nominal>", "--")
    processing_text = processing_text.replace("</Nominal><Name>", "--")
    processing_text = processing_text.replace("</Name><Value>", "--")
    processing_text = processing_text.replace("</Value>", "")
    processing_text = processing_text.replace("</ValCurs>", "")
    processing_text = processing_text.replace('"', "")
    for current_pair in processing_text.split("#"):
        line = current_pair.split("--")
        if len(line) > 1:
            if line[2].lower() not in reply_dict.keys():
                dcm = float(line[5].replace(",", ".")) / float(line[3].replace(",", "."))
                reply_dict[line[2].lower()] = dcm
    return reply_dict


def currency_rates(currency="USD"):
    response = xml_reply_replaces(requests.get("http://www.cbr.ru/scripts/XML_daily.asp", "").text)
    reply = {currency: response.get(currency.lower(), "None")}
    return reply


currency_array = ['uSd', 'eur', "AuD"]
for el in currency_array:
    data_info = currency_rates(el)
    print(f'Валюта {el.upper()}, курс = {data_info.get(el)}')