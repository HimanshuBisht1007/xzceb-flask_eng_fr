'''Module Docstring'''
import os
# import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishtofrench(english_text):
    '''English to French'''
    if english_text == "":
        french_text = ""
    else:
        french_text = language_translator.translate(
    text=english_text,
    model_id="en-fr").get_result()['translations'][0]['translation']    
    return french_text

def frenchtoenglish(french_text):
    '''French to English'''
    if french_text == "":
        english_text = ""
    else:
        english_text = language_translator.translate(
    text=french_text,
    model_id="fr-en").get_result()['translations'][0]['translation']
    return english_text
    