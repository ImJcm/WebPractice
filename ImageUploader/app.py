from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

client = MongoClient('mongodb+srv://wjsckdals108:ckdals108@cluster0.oxx6bv6.mongodb.net/?retryWrites=true&w=majority')
db = client.images

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/listing", methods=["GET"])
def listing():
    images = list(db.images.find({},{'_id':False}))
    return jsonify({'result':'success', 'images':images})
    
@app.route('/posting', methods=["POST"])
def posting():
    path = './static'
    os.makedirs(path, exist_ok=True)
    
    title_receive = request.form['title_give']
    comment_receive = request.form['comment_give']
    file_receive = request.files['file_give']
    
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'file-{mytime}'
    extension = file_receive.filename.split('.')[-1]
    save_to = f'static/{filename}.{extension}'
    file_receive.save(save_to)
    
    doc = {
        'title' : title_receive,
        'comment' : comment_receive,
        'file' : f'{filename}.{extension}'    
    }
    
    db.images.insert_one(doc)
    
    return jsonify({'result': '파일 업로드 성공!'})
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)