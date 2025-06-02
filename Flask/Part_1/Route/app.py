from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is main page!"


@app.route("/about")
def about():
    return "This is the about page!"

# 동적으로 URL 파라미터 값을 받아서 처리해준다.
# http://127.0.0.1:5000/user/Jun
@app.route("/user/<username>")
def user_profile(username):
    return f"UserName : {username}"

# post 요청 날리느 법
# (1) postman 
# (2) requests

import requests 
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = ' test data'
    response = requests.post(url=url, data = data)

    return Response(response.text, status=response.status_code, content_type=response.headers.get('Content-Type', 'text/plain'))

@app.route('/submit', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("****POST method****", request.data)

    return Response("Successfully submitted", status = 200)


if __name__ == "__main__":
    app.run()