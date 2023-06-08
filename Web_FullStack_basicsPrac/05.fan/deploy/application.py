from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient
client = MongoClient('mongodb+srv://wjsckdals108:ckdals108@cluster0.oxx6bv6.mongodb.net/?retryWrites=true&w=majority')
db = client.dbTable

application = app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    #sample_receive = request.form['sample_give']
    #return jsonify({'msg':"post 전송 완료"})
    nickname_receive = request.form['nickname_give']
    comment_receive = request.form['comment_give']
    
    doc = {
        'nickname':nickname_receive,
        'comment':comment_receive
    }
    
    db.fan.insert_one(doc)
    
    return jsonify({'result' : "저장완료"})
    
@app.route("/guestbook",methods=["GET"])
def guestbook_get():
    all_guestbook = list(db.fan.find({},{'_id':False}))
    return jsonify({'result':all_guestbook})
    #return jsonify({'msg':"GET 전송 완료"})

if __name__ == '__main__':
    app.run()
    