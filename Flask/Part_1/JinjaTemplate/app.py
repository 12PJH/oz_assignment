from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    title = "Users"
    users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

    # (1) rendering 할 html 파일명 입력
    # (2) htm로 넘겨줄 데이터 입력
    return render_template('index.html', users=users,title=title)

if __name__ == '__main__':
    app.run(debug=True)

    
