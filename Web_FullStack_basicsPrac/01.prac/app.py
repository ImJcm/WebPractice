from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

#GET 요청 API 코드
# @app.route('/test', methods=['GET'])
# def test_get():
#    title_receive = request.args.get('title_give')
#    print(title_receive)
#    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

#POST 요청 API 코드
#post방식과 /test로 오는 request 요청 통신을 받는다 + test_post()실행
#return jsonify(~)을 통해 response 전달(반환)
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)