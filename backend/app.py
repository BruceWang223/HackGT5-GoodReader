
from flask import Flask, render_template, request, json, jsonify, abort
# from flask_sqlalchemy import SQLAlchemy
from io import BytesIO
from PyPDF2 import PdfFileReader

import NLP as nlp
import urllib2
from bs4 import BeautifulSoup

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/wangwangminheng/Desktop/hack/database.db'
# db = SQLAlchemy(app)

# class FileContents(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(300))
#     data = db.Column(db.LargeBinary)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data',methods=['POST'])
def urlOrtext():
    temp = json.loads(request.data.decode('utf-8'))

    # textContent = temp["content"] if temp["type"] == 1 else 
    textContent = ""

    if temp["type"] == 1:
        textContent = temp["content"]
    elif temp["type"] == 0:
        url = temp["content"]

        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        textContent = " ".join(ele.text for ele in soup.find_all('p'))


    # temp = json.dumps(request.data)
    # print(json.dumps(request.data))
    # print(temp["content"])
    return getResponse(textContent)

@app.route('/upload', methods = ['POST'])
def upload():
    files = request.files['fileToUpload']
    pdf = request.files.get('fileToUpload')
    
    read = PdfFileReader(pdf)
    # print read
    # info = read.getDocumentInfo()
    number_of_pages = read.getNumPages()
    print number_of_pages
    # page = read.getPage(1)
    # text = page.extractText().encode('utf-8')

    texts = " ".join([read.getPage(i).extractText().encode('utf-8') for i in range(number_of_pages)])

    # print text

    return getResponse(texts)

    # out = open(pdf)
    # print type(out)
    # newFile = FileContents(name=file.filename, data=file.read())
    # print type(newFile)
    # db.session().add(newFile)
    # db.session().commit()
    
    # file_data = FileContents.query.filter_by(id = 1).first()
    # print type(file_data)
    # print((file_data).data)
    # a = file_data.data.decode('iso-8859-1').encode('utf-8')  
    # print(a)
    # print((file_data.data))
    # return json.dumps({'status':'OK'})
    # return "asdf"

def getResponse(text):
    processor = nlp.NLP(text)
    return processor.getInsight()

if __name__=="__main__":
    app.run(host='127.0.0.1', port=3000)

