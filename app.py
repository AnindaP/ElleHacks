from flask import Flask, render_template, request, url_for

import re
import sys
#from google.cloud import vision
#from google.cloud.vision import types
import os, io
from google.cloud import language
import argparse
from google.cloud.language import enums
from google.cloud.language import types
#sys.path.append(os.path.abspath('./model'))

from apiclient.discovery import build
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube' , 'https://www.googleapis.com/auth/youtube.force-ssl']

app = Flask(__name__)

sendId = ''
api_key = "AIzaSyCkSLcHWRGkQo1wnC4x5zUBKbHXnKGRuJo"
youtube = build('youtube','v3', developerKey=api_key)
def start_here():
	flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
	credentials = flow.run_local_server()
	youtube = build('youtube', 'v3', credentials=credentials)
	print('start')
	requestComment()

def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    if score < 0 and magnitude > 0:
        return 1
    else:
        return 0
		
def analyze(text):
	document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ellehacks2020_katie.json'
	client = language.LanguageServiceClient()
    #doc = client.document_from_text(text)
	annotations = client.analyze_sentiment(document = document)    
	if(print_result(annotations)):
		print("neg")
		deleteComment(sendId)

	
def requestComment():
	request = youtube.commentThreads().list(
		part="snippet,replies",
		maxResults=20,
		videoId="m-IUcQrJYCo"
	)
	response = request.execute()
	
	for item in response["items"]:
		comment = item["snippet"]["topLevelComment"]
		sendId = comment["id"]
		author = comment["snippet"]["authorDisplayName"]
		text = comment ["snippet"]["textDisplay"]
		analyze(text)
	print('requestComment')

def deleteComment(sendId):
	request = youtube.comments().setModerationStatus(id=sendId,moderationStatus="rejected")
	request.execute()
	
def call_html():
	return '<a href="https://www.youtube.com/watch?v=tsfV0NQUpVU">here</a>'

#init flask app
@app.route('/')
def index():
    #return '<h1>Hello!</h1>'
	#return render_template('home.html')
	call_html();
	#return '<a href="https://www.youtube.com/watch?v=tsfV0NQUpVU">here</a>'
	start_here()
	
	return '<h1>Hello!</h1>'
	
	

#@app.route('/predict', methods = ['POST'])
#def predict():
	#return '<a href="https://www.youtube.com/watch?v=tsfV0NQUpVU">here</a>'
	#requestComment()
	
	
	
if __name__ == '__main__':
	port = int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0',port=port)