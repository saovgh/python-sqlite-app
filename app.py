from flask import Flask, render_template, request, redirect, url_for  
from crud import create_user, read_users, update_user, delete_user  

app = Flask(__name__)  

@app.route('/')  
def index():  
    users = read_users()  
    return render_template('index.html', users=users)  

@app.route('/add', methods=['POST'])  
def add_user():  
    name = request.form['name']  
    email = request.form['email']  
    create_user(name, email)  
    return redirect(url_for('index'))  

@app.route('/update/<int:user_id>', methods=['POST'])  
def update_user_route(user_id):  
    name = request.form['name']  
    email = request.form['email']  
    update_user(user_id, name, email)  
    return redirect(url_for('index'))  

@app.route('/delete/<int:user_id>')  
def delete_user_route(user_id):  
    delete_user(user_id)  
    return redirect(url_for('index'))  

if __name__ == '__main__':  
    app.run(debug=True)  