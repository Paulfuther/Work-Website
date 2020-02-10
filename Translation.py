import os
from google.cloud import translate


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"FLASKWEBSITE\Files\My First Project-31fbd17fbc9c.json"



translate_client = translate.Client()

text = 'Hello World'
target = 'ja'

output = translate_client.translate(
    text,
    target_language = target
)

print (output)

