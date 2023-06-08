import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb+srv://wjsckdals108:ckdals108@cluster0.oxx6bv6.mongodb.net/?retryWrites=true&w=majority')
db = client.dbTable

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    star_receive = request.form['star_give']
    
    URL = url_receive
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(URL, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    
    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    ogimage = soup.select_one('meta[property="og:image"]')['content']
    ogdesc = soup.select_one('meta[property="og:description"]')['content']
    
    doc = {
        'title':ogtitle,
        'image':ogimage,
        'description':ogdesc,
        'comment':comment_receive,
        'star':star_receive
    }   #'url':url_receive,
    db.movies.insert_one(doc)
    
    return jsonify({'result' : '데이터 저장완료'})
    #print(sample_receive)
    #return jsonify({'msg':'POST 연결 완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    all_movies = list(db.movies.find({},{'_id':False}))
    return jsonify({'result':all_movies})
    #return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)