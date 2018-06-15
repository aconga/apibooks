from datetime import date
from tempfile import NamedTemporaryFile
from django.core import files
import requests


def format_datetime(f):
    return f.strftime("%d/%m/%Y %H:%M")


def fix_datetime(text):
    ''' captura una fecha como texto y la retorna en el formato de texto usado y como date '''
    if len(text) == 10:
        year = int(text[:4])
        month = int(text[5:7])
        day = int(text[8:10])
        return {
            'str': date(year, month, day).strftime('%Y-%m-%d'),
            'date': date(year, month, day)
        }
    elif len(text) == 7:
        year = int(text[:4])
        month = int(text[5:7])
        return {
            'str': date(year, month, 1).strftime('%Y-%m'),
            'date': date(year, month, 1)
        }
    elif len(text) == 4:
        return {
            'str': text,
            'date': date(int(text), 1, 1)
        }
    else:
        return {
            'str': '',
            'date': None
        }


def temp_file_from_url(url):
    ''' Crea un archivo temporal desde una url '''
    request = requests.get(url, stream=True)
    if request.status_code != requests.codes.ok:
        return None
    lf = NamedTemporaryFile()
    for block in request.iter_content(1024 * 8):
        if not block:
            break
        lf.write(block)

    return files.File(lf)
