from PyPDF2 import PdfFileMerger, PdfFileReader
from urllib.request import urlopen

from io import BytesIO
import base64
import json

def handler(event, context):
    body = json.loads(event.get('body'))
    pdf_urls = body.get('pdf_urls')
    if not pdf_urls:
        return {
            'statusCode': 400,
            'body': 'Malformed body. Body must consist of a json object containing a key "pdf_urls" with value as an array of strings'
        }

    pdf_merged = PdfFileMerger()

    for url in pdf_urls:
        pdf_file = urlopen(url).read()
        memory_file = BytesIO(pdf_file)
        pdf_merged.append(PdfFileReader(memory_file))

    pdf_merged.write('/tmp/merged.pdf')

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/pdf',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://tools.thegreenmanatee.com'
        },
        'body': base64.b64encode(open('/tmp/merged.pdf', 'rb').read()).decode('utf-8'),
        'isBase64Encoded': True
    }
