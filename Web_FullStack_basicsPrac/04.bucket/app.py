from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient
client = MongoClient('mongodb+srv://wjsckdals108:ckdals108@cluster0.oxx6bv6.mongodb.net/?retryWrites=true&w=majority')
db = client.dbTable

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    #sample_receive = request.form['sample_give']
    #print(sample_receive)
    
    bucket_receive = request.form['bucket_give']
    doc = {
        'bucket':bucket_receive
    }
    
    db.bucket.insert_one(doc)
    
    return jsonify({'result': '저장 완료!'})
    
@app.route("/bucket", methods=["GET"])
def bucket_get():
    all_bucket = list(db.bucket.find({},{'_id':False}))
    return jsonify({'result': all_bucket})
    #return jsonify({'result': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)