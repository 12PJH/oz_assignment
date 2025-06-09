from flask import Flask, render_template, request, redirect, session, flash
from datetime import timedelta

app  = Flask(__name__)

app.secret_key = 'flask-secret-key' 
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  

users = {
    'jun':'pw123',
    'kim':'pw123'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # 인증성공 시
    if username in users and users[username] == password: 
        session['username'] = username
        session.permanent = True # 
        return redirect('/secret')
    
    # 인증 실패 시
    else:
        flash('Invalid username or password')
        return redirect('/')
    

@app.route('/secret')
def secret():
    if 'username' in session:
        return render_template('secret.html')
    else:
        return redirect('/')
    
# 로그아웃
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)